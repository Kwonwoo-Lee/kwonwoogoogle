"""
build.py - 정적 사이트 빌더
=============================
content/<course>/*.md (frontmatter + 마크다운)를 읽어서 templates/*.html로
렌더링한 뒤 dist/ 아래에 순수 정적 HTML로 출력합니다. Node.js 없이 파이썬만
으로 동작하고, 결과물은 어떤 정적 호스팅(Vercel/Netlify/Cloudflare Pages/
GitHub Pages)에도 그대로 올릴 수 있습니다.

실행: python build.py
결과: dist/ 폴더가 곧 배포할 사이트 전체입니다.
"""
import re
import shutil
from datetime import date, datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import markdown as md
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

import site_config as cfg

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
DIST_DIR = ROOT / "dist"

COURSES = {
    "basics": {
        "slug": "basics",
        "title": "주식 기초",
        "short_title": "기초",
        "description": "주식이 무엇인지부터 호가창, 캔들차트, 재무제표, 리스크 관리까지 "
                       "투자를 시작하기 전 반드시 알아야 할 기본기를 순서대로 배웁니다.",
        "icon": "📘",
    },
    "strategies": {
        "slug": "strategies",
        "title": "매매기법",
        "short_title": "매매기법",
        "description": "이동평균선 크로스, 모멘텀, 평균회귀, ICT 스마트머니 기법 등 "
                       "실제로 많이 쓰이는 매매 전략을 원리부터 단계별로 설명합니다.",
        "icon": "📈",
    },
}

MD_EXT = ["extra", "tables", "sane_lists", "toc"]


def _parse_frontmatter(text: str):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("frontmatter(---로 시작하는 메타데이터 블록)가 없습니다.")
    meta = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)
    return meta, body


def load_lessons():
    """course_slug -> 정렬된 lesson dict 리스트"""
    lessons_by_course = {}
    for course_slug in COURSES:
        course_dir = CONTENT_DIR / course_slug
        lessons = []
        for path in sorted(course_dir.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            meta, body = _parse_frontmatter(raw)
            html_body = md.markdown(body, extensions=MD_EXT)
            keywords = meta.get("keywords", [])
            lessons.append({
                "course": course_slug,
                "slug": meta["slug"],
                "title": meta["title"],
                "description": meta["description"],
                "order": int(meta["order"]),
                "updated": str(meta.get("updated", date.today().isoformat())),
                "reading_min": meta.get("reading_min", estimate_reading_minutes(body)),
                "html": html_body,
                "keywords": ", ".join(keywords) if keywords else COURSES[course_slug]["title"],
            })
        lessons.sort(key=lambda x: x["order"])
        lessons_by_course[course_slug] = lessons
    return lessons_by_course


def estimate_reading_minutes(markdown_text: str) -> int:
    words = len(re.findall(r"\S+", markdown_text))
    # 한글은 어절 기준이라 평균 분당 350단어 정도로 추정
    return max(1, round(words / 350))


def make_env():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["cfg"] = cfg
    env.globals["courses"] = COURSES
    return env


def url_for(*parts) -> str:
    clean = "/".join(p.strip("/") for p in parts if p)
    return f"/{clean}/" if clean else "/"


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    env = make_env()
    env.globals["url_for"] = url_for
    lessons_by_course = load_lessons()

    all_pages = []  # sitemap용 (path, updated)
    rss_items = []  # rss.xml용 (title, description, url, updated) - 네이버 서치어드바이저 수집용

    # 홈
    home_tpl = env.get_template("home.html")
    write(DIST_DIR / "index.html", home_tpl.render(
        lessons_by_course=lessons_by_course,
        canonical=url_for(),
    ))
    all_pages.append((url_for(), date.today().isoformat()))

    # 코스별 인덱스 + 레슨
    for course_slug, course in COURSES.items():
        lessons = lessons_by_course[course_slug]

        idx_tpl = env.get_template("course_index.html")
        course_url = url_for(course_slug)
        write(DIST_DIR / course_slug / "index.html", idx_tpl.render(
            course=course, lessons=lessons, canonical=course_url,
        ))
        all_pages.append((course_url, date.today().isoformat()))

        lesson_tpl = env.get_template("lesson.html")
        for i, lesson in enumerate(lessons):
            prev_lesson = lessons[i - 1] if i > 0 else None
            next_lesson = lessons[i + 1] if i < len(lessons) - 1 else None
            lesson_url = url_for(course_slug, lesson["slug"])
            write(DIST_DIR / course_slug / lesson["slug"] / "index.html", lesson_tpl.render(
                course=course, lesson=lesson, lessons=lessons,
                prev_lesson=prev_lesson, next_lesson=next_lesson,
                lesson_index=i + 1, canonical=lesson_url,
            ))
            all_pages.append((lesson_url, lesson["updated"]))
            rss_items.append({
                "title": f"[{course['title']}] {lesson['title']}",
                "description": lesson["description"],
                "url": lesson_url,
                "updated": lesson["updated"],
            })

    # 개인정보처리방침
    privacy_tpl = env.get_template("privacy.html")
    write(DIST_DIR / "privacy" / "index.html", privacy_tpl.render(canonical=url_for("privacy")))
    all_pages.append((url_for("privacy"), date.today().isoformat()))

    # 정적 파일 복사
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, DIST_DIR / "static")

    # sitemap.xml
    sitemap_entries = "\n".join(
        f"  <url><loc>{cfg.SITE_URL}{path}</loc><lastmod>{updated}</lastmod></url>"
        for path, updated in all_pages
    )
    sitemap_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{sitemap_entries}\n"
        "</urlset>\n"
    )
    write(DIST_DIR / "sitemap.xml", sitemap_xml)

    # rss.xml - 네이버 서치어드바이저에 제출하면 새 강의를 훨씬 빨리 수집해갑니다
    rss_items.sort(key=lambda x: x["updated"], reverse=True)
    rss_entries = "\n".join(
        "  <item>\n"
        f"    <title>{xml_escape(item['title'])}</title>\n"
        f"    <link>{cfg.SITE_URL}{item['url']}</link>\n"
        f"    <guid>{cfg.SITE_URL}{item['url']}</guid>\n"
        f"    <description>{xml_escape(item['description'])}</description>\n"
        f"    <pubDate>{format_datetime(datetime.fromisoformat(item['updated']).replace(tzinfo=timezone.utc))}</pubDate>\n"
        "  </item>"
        for item in rss_items
    )
    rss_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n'
        "<channel>\n"
        f"  <title>{xml_escape(cfg.SITE_NAME)}</title>\n"
        f"  <link>{cfg.SITE_URL}</link>\n"
        f"  <description>{xml_escape(cfg.SITE_DESCRIPTION)}</description>\n"
        "  <language>ko</language>\n"
        f"{rss_entries}\n"
        "</channel>\n"
        "</rss>\n"
    )
    write(DIST_DIR / "rss.xml", rss_xml)

    # robots.txt
    robots_txt = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {cfg.SITE_URL}/sitemap.xml\n"
    )
    write(DIST_DIR / "robots.txt", robots_txt)

    # ads.txt (애드센스 승인 후 퍼블리셔 ID가 채워지면 실제 내용 생성)
    if cfg.ADSENSE_CLIENT_ID:
        pub_id = cfg.ADSENSE_CLIENT_ID.replace("ca-pub-", "pub-")
        ads_txt = f"google.com, {pub_id}, DIRECT, f08c47fec0942fa0\n"
    else:
        ads_txt = (
            "# 애드센스 승인 후 site_config.py의 ADSENSE_CLIENT_ID를 채우면\n"
            "# 이 파일이 자동으로 올바른 내용으로 채워집니다.\n"
        )
    write(DIST_DIR / "ads.txt", ads_txt)

    total_lessons = sum(len(v) for v in lessons_by_course.values())
    print(f"빌드 완료 -> {DIST_DIR}")
    print(f"  페이지 {len(all_pages)}개 (강의 {total_lessons}개 포함)")
    print(f"  SITE_URL = {cfg.SITE_URL}  (실제 도메인으로 site_config.py에서 변경하세요)")


if __name__ == "__main__":
    build()
