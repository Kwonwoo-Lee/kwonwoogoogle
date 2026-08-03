"""
news_source.py - 빌드 시점에 실제 금융 뉴스 RSS를 가져옵니다.
================================================================
이 사이트는 서버가 없는 정적 사이트라서, 뉴스도 "실시간"이 아니라
"빌드할 때마다 그 시점의 최신 헤드라인으로 갱신"되는 방식입니다.
실제 언론사 RSS를 그대로 가져와 헤드라인·발행일·원문 링크만 보여주고,
본문은 절대 긁어와 재게시하지 않습니다(항상 원문으로 연결).

RSS를 못 가져오거나 파싱에 실패해도 빌드 자체가 멈추면 안 되므로,
실패 시 빈 목록을 반환하고 콘솔에 경고만 남깁니다.
"""
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

NEWS_SOURCES = {
    "ko": {"url": "https://www.hankyung.com/feed/finance", "source_name": "한국경제"},
    "en": {"url": "https://finance.yahoo.com/news/rssindex", "source_name": "Yahoo Finance"},
}

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; stock-academy-build/1.0)"}


def fetch_news(lang: str, limit: int = 20):
    cfg = NEWS_SOURCES.get(lang)
    if not cfg:
        return []

    try:
        req = urllib.request.Request(cfg["url"], headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
    except Exception as e:
        print(f"  [뉴스] {lang} RSS를 가져오지 못했습니다 (건너뜀): {e}")
        return []

    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        print(f"  [뉴스] {lang} RSS 파싱 실패 (건너뜀): {e}")
        return []

    items = []
    for item in root.findall(".//item")[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not title or not link:
            continue

        pub_date_raw = item.findtext("pubDate")
        pub_date = ""
        if pub_date_raw:
            try:
                pub_date = parsedate_to_datetime(pub_date_raw).strftime("%Y-%m-%d %H:%M")
            except Exception:
                pub_date = pub_date_raw

        source_el = item.find("source")
        source = (source_el.text or "").strip() if source_el is not None and source_el.text else cfg["source_name"]

        items.append({"title": title, "link": link, "pub_date": pub_date, "source": source})
    return items
