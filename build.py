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
                     "how to get rich investing in stocks, make money trading stocks, become a millionaire investing, "
                     "how to become a successful trader, moving average crossover, ICT smart money concepts, "
                     "risk reward ratio",
    },
}

UI = {
    "ko": {
        "home": "홈", "privacy": "개인정보처리방침", "contact": "문의",
        "about": "소개", "terms": "이용약관",
        "free_all": "전부 무료", "auto_update": "이 사이트의 모든 콘텐츠는 정보 제공 목적이며 "
            "투자 권유가 아닙니다. 투자 판단과 책임은 본인에게 있습니다.",
        "prev_lesson": "← 이전 강의", "next_lesson": "다음 강의 →",
        "practice_trading": "실전 모의투자",
        "practice_trading_desc": "배운 내용을 실제 시세로 바로 연습해보세요. 가상 자금 1천만원으로 시작합니다.",
        "practice_trading_tag": "실시간 시세 · 무료",
        "market_news": "시장 뉴스",
        "market_news_desc": "실제 보도를 근거로 직접 정리·분석한 시황 글입니다. 각 글 하단에서 참고한 원문 기사를 확인할 수 있습니다.",
        "market_news_tag": "직접 분석 · 무료",
        "market_news_empty": "아직 등록된 뉴스 분석이 없습니다.",
        "reviewed_by": "TradeSmrt 편집팀 작성·검수",
        "share": "공유하기", "copy_link": "링크 복사", "link_copied": "복사됨!",
        "related_lessons": "관련 강의", "related_news": "관련 뉴스",
        "toc": "이 글의 목차",
        "tools": "투자 계산기", "tools_nav": "계산기",
        "continue_reading": "이어보기",
        "quizzes": "주식 퀴즈", "quizzes_nav": "퀴즈",
        "quizzes_desc": "실전에서 진짜 헷갈리는 상황을 짧은 문제로 풀어보며 감각을 익히세요.",
        "quizzes_empty": "아직 등록된 퀴즈가 없습니다.",
        "quiz_question_label": "Question",
        "quiz_correct_badge": "정답!",
        "quiz_correct": "정답입니다!",
        "quiz_wrong": "아쉽지만 오답이에요",
        "quiz_explanation": "해설",
        "quiz_next": "다음 문제로 이동",
        "quiz_restart": "처음부터 다시 풀기",
        "quiz_done_title": "퀴즈를 모두 풀었어요!",
        "quiz_student_label": "학습자",
        "nav_home": "홈", "nav_courses": "강의", "nav_quizzes": "퀴즈", "nav_profile": "프로필",
    },
    "en": {
        "home": "Home", "privacy": "Privacy Policy", "contact": "Contact",
        "about": "About", "terms": "Terms of Use",
        "free_all": "All free", "auto_update": "All content on this site is for informational "
            "purposes only and is not investment advice. You are solely responsible for your own "
            "investment decisions.",
        "prev_lesson": "← Previous lesson", "next_lesson": "Next lesson →",
        "practice_trading": "Paper Trading",
        "practice_trading_desc": "Put what you learned into practice with real-time prices — start with a virtual ₩10,000,000.",
        "practice_trading_tag": "Real-time prices · Free",
        "market_news": "Market News",
        "market_news_desc": "Original market analysis written from real reporting. Each article links its sources at the bottom.",
        "market_news_tag": "Original analysis · Free",
        "market_news_empty": "No news analysis has been published yet.",
        "reviewed_by": "Written & reviewed by the TradeSmrt editorial team",
        "share": "Share", "copy_link": "Copy link", "link_copied": "Copied!",
        "related_lessons": "Related lessons", "related_news": "Related news",
        "toc": "In this article",
        "tools": "Investing Calculators", "tools_nav": "Calculators",
        "continue_reading": "Continue reading",
        "quizzes": "Stock Quizzes", "quizzes_nav": "Quizzes",
        "quizzes_desc": "Sharpen your instincts on the situations that actually trip up investors, one short question at a time.",
        "quizzes_empty": "No quizzes have been published yet.",
        "quiz_question_label": "Question",
        "quiz_correct_badge": "Correct!",
        "quiz_correct": "That's correct!",
        "quiz_wrong": "Not quite — here's why",
        "quiz_explanation": "Explanation",
        "quiz_next": "Next question",
        "quiz_restart": "Restart from question 1",
        "quiz_done_title": "You've finished every quiz!",
        "quiz_student_label": "Student",
        "nav_home": "Home", "nav_courses": "Courses", "nav_quizzes": "Quizzes", "nav_profile": "Profile",
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


BASICS_LEVEL_THRESHOLDS = {
    "ko": [(15, "기초"), (25, "중급")],
    "en": [(15, "Beginner"), (25, "Intermediate")],
}


def _basics_level(lang: str, order: int) -> str:
    """주식기초 코스 전용: 15강까지 기초, 16~25강 중급, 26강부터 고급으로 자동 분류."""
    for max_order, label in BASICS_LEVEL_THRESHOLDS[lang]:
        if order <= max_order:
            return label
    return "고급" if lang == "ko" else "Advanced"


FAQ_HEADING = {"ko": "자주 묻는 질문", "en": "FAQ"}


def _faq_plain_text(lines) -> str:
    """FAQ 답변 본문(마크다운)을 JSON-LD용 평문으로 변환"""
    text = "\n".join(lines).strip()
    if not text:
        return ""
    html_fragment = md.markdown(text)
    plain = re.sub(r"<[^>]+>", "", html_fragment)
    return re.sub(r"\s+", " ", plain).strip()


def _extract_faq(body: str, lang: str):
    """본문에 '## 자주 묻는 질문'/'## FAQ' 섹션이 있으면 그 아래 '### 질문' 단위로 Q&A를 추출.
    글쓴이(자동화 루틴 포함)가 자연스러운 경우에만 넣는 선택적 섹션으로, FAQPage 구조화 데이터에 쓰인다."""
    heading = FAQ_HEADING[lang]
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == f"## {heading}":
            start = i + 1
            break
    if start is None:
        return []
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    faqs = []
    question, answer_lines = None, []
    for line in lines[start:end]:
        if line.startswith("### "):
            if question:
                faqs.append({"question": question, "answer": _faq_plain_text(answer_lines)})
            question, answer_lines = line[4:].strip(), []
        elif question is not None:
            answer_lines.append(line)
    if question:
        faqs.append({"question": question, "answer": _faq_plain_text(answer_lines)})
    return [f for f in faqs if f["answer"]]


def _render_markdown(body: str, lang: str):
    """마크다운 본문을 HTML로 변환하면서, 목차(H2 3개 이상일 때)와 FAQ 섹션을 함께 추출."""
    converter = md.Markdown(extensions=MD_EXT)
    html_body = converter.convert(body)
    toc = [{"title": t["name"], "id": t["id"]} for t in converter.toc_tokens if t["level"] == 2]
    if len(toc) < 3:
        toc = []
    faq = _extract_faq(body, lang)
    return html_body, toc, faq


def _check_missing_alt(html_body: str, label: str):
    """이미지에 alt 텍스트가 비어있으면 빌드를 막지 않고 콘솔에 경고만 띄웁니다.
    (alt는 접근성뿐 아니라 구글 이미지 검색 유입에도 쓰이는데, 마크다운 작성자가
    빼먹기 쉬운 항목이라 여기서 놓치지 않게 잡아줍니다.)"""
    for match in re.finditer(r"<img\b[^>]*>", html_body):
        tag = match.group(0)
        alt_match = re.search(r'alt="([^"]*)"', tag)
        if alt_match is None or not alt_match.group(1).strip():
            print(f"  ⚠️  alt 텍스트 없는 이미지: {label}")


def load_lessons(lang: str):
    """course_slug -> 정렬된 lesson dict 리스트 (해당 언어)"""
    lessons_by_course = {}
    for course_slug in COURSES:
        course_dir = CONTENT_DIR / lang / course_slug
        lessons = []
        for path in sorted(course_dir.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            meta, body = _parse_frontmatter(raw)
            html_body, toc, faq = _render_markdown(body, lang)
            _check_missing_alt(html_body, f"{lang}/{course_slug}/{path.name}")
            keywords = meta.get("keywords") or []
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
                "toc": toc,
                "faq": faq,
                "image": meta.get("image"),
                "keywords": ", ".join(keywords) if keywords else COURSES[course_slug][lang]["title"],
                "keywords_list": keywords,
            })
        lessons.sort(key=lambda x: x["order"])
        for i, lesson in enumerate(lessons):
            lesson["badge"] = _lesson_badge(lang, i + 1)
            if course_slug == "basics":
                lesson["level"] = _basics_level(lang, lesson["order"])
        lessons_by_course[course_slug] = lessons
    return lessons_by_course


def load_quizzes(lang: str):
    """quizzes 목록 (order순). 각 퀴즈는 객관식 4지선다 + 해설로 구성됩니다."""
    quiz_dir = CONTENT_DIR / lang / "quizzes"
    if not quiz_dir.exists():
        return []
    quizzes = []
    for path in sorted(quiz_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        meta, body = _parse_frontmatter(raw)
        html_body, _, _ = _render_markdown(body, lang)
        keywords = meta.get("keywords", [])
        quizzes.append({
            "slug": meta["slug"],
            "title": meta["title"],
            "category": meta["category"],
            "difficulty": int(meta.get("difficulty", 1)),
            "order": int(meta["order"]),
            "updated": str(meta.get("updated", date.today().isoformat())),
            "question_html": html_body,
            "options": meta["options"],
            "answer": int(meta["answer"]),
            "explanation": meta["explanation"],
            "keywords": ", ".join(keywords) if keywords else meta["category"],
        })
    quizzes.sort(key=lambda x: x["order"])
    return quizzes


def load_news(lang: str):
    """news 글 목록 (최신순). 각 글은 실제 보도를 자체적으로 종합·분석해 쓴 것으로,
    강의(lesson)와 달리 course/order 개념이 없고 published 날짜로만 정렬합니다."""
    news_dir = CONTENT_DIR / lang / "news"
    if not news_dir.exists():
        return []
    posts = []
    for path in sorted(news_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        meta, body = _parse_frontmatter(raw)
        html_body, toc, faq = _render_markdown(body, lang)
        _check_missing_alt(html_body, f"{lang}/news/{path.name}")
        keywords = meta.get("keywords") or []
        posts.append({
            "slug": meta["slug"],
            "title": meta["title"],
            "description": meta["description"],
            "published": str(meta["published"]),
            "html": html_body,
            "toc": toc,
            "faq": faq,
            "image": meta.get("image"),
            "keywords": ", ".join(keywords) if keywords else "",
            "keywords_list": keywords,
            "_filename": path.stem,
        })
    # published 날짜가 같은 글끼리는 파일명(번호) 역순으로 정렬해 최근에 추가된 글이 위로 오도록 함
    posts.sort(key=lambda x: (x["published"], x["_filename"]), reverse=True)
    for post in posts:
        del post["_filename"]
    return posts


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


def _pick_related(current: dict, candidates: list, limit: int = 3) -> list:
    """연관 콘텐츠를 프런트매터 keywords가 겹치는 순으로 고릅니다.
    겹치는 키워드가 없거나 모자라면 candidates 순서(기존처럼 다음 글/다음 강의부터)로
    채워서, 키워드를 안 채운 글도 연관 추천이 비어버리지 않게 합니다."""
    current_kw = set(current.get("keywords_list") or [])
    scored = sorted(
        candidates,
        key=lambda c: len(current_kw & set(c.get("keywords_list") or [])),
        reverse=True,
    )
    picked = [c for c in scored if current_kw & set(c.get("keywords_list") or [])][:limit]
    if len(picked) < limit:
        picked_slugs = {c["slug"] for c in picked}
        for c in candidates:
            if len(picked) >= limit:
                break
            if c["slug"] not in picked_slugs:
                picked.append(c)
                picked_slugs.add(c["slug"])
    return picked


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
        quizzes = load_quizzes(lang)
        base_dir = DIST_DIR if lang == DEFAULT_LANG else DIST_DIR / lang

        # 홈
        home_tpl = env.get_template("home.html")
        home_path = url_for(lang)
        write(base_dir / "index.html", home_tpl.render(
            lang=lang, ui=ui, site=site,
            lessons_by_course=lessons_by_course, quiz_count=len(quizzes),
            canonical=home_path, alternates=alternates_for(),
        ))
        all_pages.append((home_path, date.today().isoformat()))

        # 주식 퀴즈
        quizzes_tpl = env.get_template("quizzes.html")
        quizzes_path = url_for(lang, "quizzes")
        write(base_dir / "quizzes" / "index.html", quizzes_tpl.render(
            lang=lang, ui=ui, site=site, quizzes=quizzes,
            canonical=quizzes_path, alternates=alternates_for("quizzes"),
        ))
        all_pages.append((quizzes_path, date.today().isoformat()))

        quiz_tpl = env.get_template("quiz.html")
        for i, quiz in enumerate(quizzes):
            quiz_url = url_for(lang, "quizzes", quiz["slug"])
            write(base_dir / "quizzes" / quiz["slug"] / "index.html", quiz_tpl.render(
                lang=lang, ui=ui, site=site,
                quiz=quiz, quizzes=quizzes, quiz_index=i,
                canonical=quiz_url, alternates=alternates_for("quizzes", quiz["slug"]),
                hide_chrome=True,
            ))
            all_pages.append((quiz_url, quiz["updated"]))

        # 시장 뉴스 (RSS를 그대로 긁어오지 않고, 실제 보도를 근거로 직접 종합·분석해서 씁니다)
        news_posts = load_news(lang)
        news_tpl = env.get_template("news.html")
        news_path = url_for(lang, "news")
        write(base_dir / "news" / "index.html", news_tpl.render(
            lang=lang, ui=ui, site=site, news_items=news_posts,
            canonical=news_path, alternates=alternates_for("news"),
        ))
        all_pages.append((news_path, date.today().isoformat()))

        news_post_tpl = env.get_template("news_post.html")
        for i, post in enumerate(news_posts):
            prev_post = news_posts[i + 1] if i + 1 < len(news_posts) else None  # 최신순 정렬이므로 다음 인덱스가 "이전 글"
            next_post = news_posts[i - 1] if i > 0 else None
            related_news = _pick_related(post, [p for p in news_posts if p["slug"] != post["slug"]])
            post_url = url_for(lang, "news", post["slug"])
            write(base_dir / "news" / post["slug"] / "index.html", news_post_tpl.render(
                lang=lang, ui=ui, site=site, post=post,
                prev_post=prev_post, next_post=next_post, related_news=related_news,
                canonical=post_url,
                alternates=alternates_for("news", post["slug"]),
            ))
            all_pages.append((post_url, post["published"]))
            if lang == "ko":
                rss_items.append({
                    "title": f"[{ui['market_news']}] {post['title']}",
                    "description": post["description"],
                    "url": post_url,
                    "updated": post["published"],
                })

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
                related_lessons = _pick_related(lesson, lessons[i + 1:] + lessons[:i])
                lesson_url = url_for(lang, course_slug, lesson["slug"])
                level_part = f" · {lesson['level']}" if lesson.get("level") else ""
                progress_label = (
                    f"{course['title']} · {i + 1}/{len(lessons)}강{level_part} · {lesson['reading_label']}"
                    if lang == "ko" else
                    f"{course['title']} · Lesson {i + 1}/{len(lessons)}{level_part} · {lesson['reading_label']}"
                )
                write(base_dir / course_slug / lesson["slug"] / "index.html", lesson_tpl.render(
                    lang=lang, ui=ui, site=site,
                    course=course, lesson=lesson, lessons=lessons,
                    prev_lesson=prev_lesson, next_lesson=next_lesson, related_lessons=related_lessons,
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
        for page_slug, template_name in (("privacy", "privacy.html"), ("about", "about.html"), ("terms", "terms.html"), ("tools", "tools.html")):
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
