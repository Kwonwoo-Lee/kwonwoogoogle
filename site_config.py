"""
site_config.py - 사이트 전역 설정
====================================
도메인을 정하시면 SITE_URL만 바꾸면 사이트 전체(sitemap, canonical,
OG 태그 등)에 반영됩니다. 애드센스 승인을 받으면 ADSENSE_CLIENT_ID만
채우면 모든 광고 슬롯에 자동으로 반영됩니다.
"""

SITE_NAME = "주식아카데미"
SITE_TAGLINE = "누구나 쉽게 배우는 주식 투자 강의"
SITE_DESCRIPTION = (
    "주식 기초 용어부터 이동평균선, ICT 스마트머니 기법까지 "
    "단계별로 쉽게 설명하는 무료 주식 투자 강의 사이트."
)

# 홈페이지 등 개별 키워드가 없는 페이지에서 쓰는 기본 키워드 (콤마 구분).
# 구글은 이 태그를 사실상 무시하지만, 네이버는 아직 참고하는 편이라 넣어둡니다.
SITE_KEYWORDS = (
    "주식 공부, 주식 기초, 주식 초보, 주식 강의, 주식 용어, 주식 매매기법, "
    "이동평균선, 캔들차트 보는법, ICT 스마트머니, 손익비, 리스크 관리"
)

# 배포 전에는 임시 도메인으로 두고, 실제 도메인을 사면 여기만 바꾸면 됩니다.
SITE_URL = "https://example-stock-academy.com"

# 애드센스 승인 전에는 비워두세요 - 비어있으면 광고 슬롯이 렌더링되지 않습니다.
ADSENSE_CLIENT_ID = ""  # 예: "ca-pub-1234567890123456"

# 검색엔진 소유권 확인용 (Google Search Console에서 발급받으면 채워넣으세요)
GOOGLE_SITE_VERIFICATION = ""

# 네이버 서치어드바이저(https://searchadvisor.naver.com)에서 사이트 등록 후 발급받는 값
NAVER_SITE_VERIFICATION = ""

# OG 이미지 기본값 (static/img/og-default.png)
DEFAULT_OG_IMAGE = "/static/img/og-default.png"

TWITTER_HANDLE = ""  # 예: "@your_handle" (없으면 빈 문자열)

CONTACT_EMAIL = "kwonwoo4056@gmail.com"
