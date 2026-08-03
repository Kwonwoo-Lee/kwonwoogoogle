"""
build.py - 정적 사이트 빌더 (한국어 + 영어)
=============================================
content/<lang>/<course>/*.md (frontmatter + 마크다운)를 읽어서
templates/*.html로 렌더링한 뒤 dist/ 아래에 순수 정적 HTML로 출력합니다.
한국어는 기존 URL 그대로(/basics/...), 영어는 /en/ 접두어를 붙입니다
(/en/basics/...). 같은 강의는 두 언어에서 slug가 동일하다는 전제로
hreflang 대응 URL을 자동 계산합니다.

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

LANGUAGES = ["ko", "en"]
DEFAULT_LANG = "ko"  # 기본 언어는 URL 접두어 없음 (/basics/...), 그 외는 /en/basics/... 처럼 접두어 붙음
NATIVE_NAME = {"ko": "한국어", "en": "English"}
OG_LOCALE = {"ko": "ko_KR", "en": "en_US"}
READING_WPM = {"ko": 350, "en": 220}  # ko는 어절/분, en은 단어/분 기준 추정치

COURSES = {
    "basics": {
        "slug": "basics",
        "icon": "📘",
        "ko": {
            "title": "주식 기초",
            "short_title": "기초",
            "description": "주식이 무엇인지부터 호가창, 캔들차트, 재무제표, 리스크 관리까지 "
                           "투자를 시작하기 전 반드시 알아야 할 기본기를 순서대로 배웁니다.",
        },
        "en": {
            "title": "Stock Basics",
            "short_title": "Basics",
            "description": "From what a stock actually is to reading order books, candlestick "
                           "charts, financial statements, and risk management — the fundamentals "
                           "every beginner needs before investing a single dollar.",
        },
    },
    "strategies": {
        "slug": "strategies",
        "icon": "📈",
        "ko": {
            "title": "매매기법",
            "short_title": "매매기법",
            "description": "이동평균선 크로스, 모멘텀, 평균회귀, ICT 스마트머니 기법 등 "
                           "실제로 많이 쓰이는 매매 전략을 원리부터 단계별로 설명합니다.",
        },
        "en": {
            "title": "Trading Strategies",
            "short_title": "Strategies",
            "description": "Moving average crossovers, momentum, mean reversion, support/resistance "
                           "breakouts, and ICT smart money concepts — widely used trading strategies "
                           "explained step by step, from first principles.",
        },
    },
}

SITE_TEXT = {
    "ko": {
        "name": cfg.SITE_NAME,
        "tagline": cfg.SITE_TAGLINE,
        "description": cfg.SITE_DESCRIPTION,
        "keywords": cfg.SITE_KEYWORDS,
    },
    "en": {
        "name": "TradeSmrt",
        "tagline": "Learn stock investing, one step at a time",
        "description": "A free, step-by-step stock trading course covering everything from market "
                        "basics to moving averages and ICT smart money concepts.",
        "keywords": "learn stocks, stock trading for beginners, stock market basics, trading strategies, "
                     "moving average crossover, candlestick patterns, ICT smart money concepts, "
                     "risk reward ratio, technical analysis",
    },
}

UI = {
    "ko": {
        "home": "홈", "privacy": "개인정보처리방침", "contact": "문의",
        "about": "소개", "terms": "이용약관",
        "free_all": "전부 무료", "auto_update": "이 사이트의 모든 콘텐츠는 정보 제공 목적이며 "
            "투자 권유가 아닙니다. 투자 판단과 책임은 본인에게 있습니다.",
        "prev_lesson": "← 이전 강의", "next_lesson": "다음 강의 →",
    },
    "en": {
        "home": "Home", "privacy": "Privacy Policy", "contact": "Contact",
        "about": "About", "terms": "Terms of Use",
        "free_all": "All free", "auto_update": "All content on this site is for informational "
            "purposes only and is not investment advice. You are solely responsible for your own "
            "investment decisions.",
        "prev_lesson": "← Previous lesson", "next_lesson": "Next lesson →",
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


def estimate_reading_minutes(markdown_text: str, lang: str) -> int:
    words = len(re.findall(r"\S+", markdown_text))
    return max(1, round(words / READING_WPM[lang]))


def _lesson_badge(lang: str, index: int) -> str:
    return f"{index}강" if lang == "ko" else f"Lesson {index}"


def _reading_label(lang: str, minutes: int) -> str:
    return f"{minutes}분 읽기" if lang == "ko" else f"{minutes} min read"


def load_lessons(lang: str):
    """course_slug -> 정렬된 lesson dict 리스트 (해당 언어)"""
    lessons_by_course = {}
    for course_slug in COURSES:
        course_dir = CONTENT_DIR / lang / course_slug
        lessons = []
        for path in sorted(course_dir.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            meta, body = _parse_frontmatter(raw)
            html_body = md.markdown(body, extensions=MD_EXT)
            keywords = meta.get("keywords", [])
            reading_min = meta.get("reading_min", estimate_reading_minutes(body, lang))
            lessons.append({
                "course": course_slug,
                "slug": meta["slug"],
                "title": meta["title"],
                "description": meta["description"],
                "order": int(meta["order"]),
                "updated": str(meta.get("updated", date.today().isoformat())),
                "reading_min": reading_min,
                "reading_label": _reading_label(lang, reading_min),
                "html": html_body,
                "keywords": ", ".join(keywords) if keywords else COURSES[course_slug][lang]["title"],
            })
        lessons.sort(key=lambda x: x["order"])
        for i, lesson in enumerate(lessons):
            lesson["badge"] = _lesson_badge(lang, i + 1)
        lessons_by_course[course_slug] = lessons
    return lessons_by_course


def make_env():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["cfg"] = cfg
    env.globals["courses"] = COURSES
    env.globals["languages"] = LANGUAGES
    env.globals["default_lang"] = DEFAULT_LANG
    env.globals["native_name"] = NATIVE_NAME
    env.globals["og_locale"] = OG_LOCALE
    return env


def url_for(lang: str, *parts) -> str:
    clean = "/".join(p.strip("/") for p in parts if p)
    prefix = "" if lang == DEFAULT_LANG else f"/{lang}"
    if clean:
        return f"{prefix}/{clean}/"
    return f"{prefix}/" if prefix else "/"


def alternates_for(*parts) -> dict:
    """같은 페이지의 언어별 URL 대응표 (hreflang / 언어 전환 링크용)"""
    return {lang: url_for(lang, *parts) for lang in LANGUAGES}


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    env = make_env()
    env.globals["url_for"] = url_for

    all_pages = []  # sitemap용 (path, updated)
    rss_items = []  # rss.xml용 (한국어만 - 네이버 서치어드바이저 수집용)

    for lang in LANGUAGES:
        ui = UI[lang]
        site = SITE_TEXT[lang]
        lessons_by_course = load_lessons(lang)
        base_dir = DIST_DIR if lang == DEFAULT_LANG else DIST_DIR / lang

        # 홈
        home_tpl = env.get_template("home.html")
        home_path = url_for(lang)
        write(base_dir / "index.html", home_tpl.render(
            lang=lang, ui=ui, site=site,
            lessons_by_course=lessons_by_course,
            canonical=home_path, alternates=alternates_for(),
        ))
        all_pages.append((home_path, date.today().isoformat()))

        # 코스별 인덱스 + 레슨
        for course_slug, course_meta in COURSES.items():
            lessons = lessons_by_course[course_slug]
            course = {"slug": course_slug, "icon": course_meta["icon"], **course_meta[lang]}

            idx_tpl = env.get_template("course_index.html")
            course_url = url_for(lang, course_slug)
            write(base_dir / course_slug / "index.html", idx_tpl.render(
                lang=lang, ui=ui, site=site,
                course=course, lessons=lessons, canonical=course_url,
                alternates=alternates_for(course_slug),
            ))
            all_pages.append((course_url, date.today().isoformat()))

            lesson_tpl = env.get_template("lesson.html")
            for i, lesson in enumerate(lessons):
                prev_lesson = lessons[i - 1] if i > 0 else None
                next_lesson = lessons[i + 1] if i < len(lessons) - 1 else None
                lesson_url = url_for(lang, course_slug, lesson["slug"])
                progress_label = (
                    f"{course['title']} · {i + 1}/{len(lessons)}강 · {lesson['reading_label']}"
                    if lang == "ko" else
                    f"{course['title']} · Lesson {i + 1}/{len(lessons)} · {lesson['reading_label']}"
                )
                write(base_dir / course_slug / lesson["slug"] / "index.html", lesson_tpl.render(
                    lang=lang, ui=ui, site=site,
                    course=course, lesson=lesson, lessons=lessons,
                    prev_lesson=prev_lesson, next_lesson=next_lesson,
                    lesson_index=i + 1, progress_label=progress_label, canonical=lesson_url,
                    alternates=alternates_for(course_slug, lesson["slug"]),
                ))
                all_pages.append((lesson_url, lesson["updated"]))
                if lang == "ko":
                    rss_items.append({
                        "title": f"[{course['title']}] {lesson['title']}",
                        "description": lesson["description"],
                        "url": lesson_url,
                        "updated": lesson["updated"],
                    })

        # 개인정보처리방침 / 소개 / 이용약관 (강의가 아닌 정적 정책·소개 페이지)
        for page_slug, template_name in (("privacy", "privacy.html"), ("about", "about.html"), ("terms", "terms.html")):
            page_tpl = env.get_template(template_name)
            page_url = url_for(lang, page_slug)
            write(base_dir / page_slug / "index.html", page_tpl.render(
                lang=lang, ui=ui, site=site,
                canonical=page_url, alternates=alternates_for(page_slug),
            ))
            all_pages.append((page_url, date.today().isoformat()))

    # 404 페이지 (Cloudflare Pages가 dist/404.html을 자동으로 인식해서 서빙)
    not_found_tpl = env.get_template("404.html")
    write(DIST_DIR / "404.html", not_found_tpl.render(site_name=SITE_TEXT["ko"]["name"]))

    # 정적 파일 복사
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, DIST_DIR / "static")

    # sitemap.xml (모든 언어 페이지 포함)
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

    # rss.xml - 네이버 서치어드바이저 제출용 (한국어 콘텐츠만)
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

    total_lessons = sum(
        len(load_lessons(DEFAULT_LANG)[c]) for c in COURSES
    )
    print(f"빌드 완료 -> {DIST_DIR}")
    print(f"  언어 {len(LANGUAGES)}개({', '.join(LANGUAGES)}), 페이지 {len(all_pages)}개 (언어당 강의 {total_lessons}개)")
    print(f"  SITE_URL = {cfg.SITE_URL}  (실제 도메인으로 site_config.py에서 변경하세요)")


if __name__ == "__main__":
    build()
