"""
gen_charts.py - 강의 본문에 들어가는 설명용 SVG 다이어그램을 생성합니다.
실제 시세 데이터가 아니라 개념 설명용으로 손으로 좌표를 잡은 예시 그림입니다.
실행: python build/gen_charts.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

OUT_DIR = ROOT / "static" / "img" / "charts"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT = "'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif"
INK = "#20201a"
MUTED = "#767568"
GRID = "#e1e0d9"
CARD = "#fdfdfb"
ACCENT = "#1a5fb4"
UP = "#1f9d55"
DOWN = "#d0453b"
UP_FILL = "#dcf3e4"
DOWN_FILL = "#fbe1df"


def _svg(width, height, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'font-family="{FONT}">\n'
        f'<rect x="0" y="0" width="{width}" height="{height}" rx="12" fill="{CARD}" stroke="{GRID}"/>\n'
        f"{body}\n</svg>\n"
    )


def _text(x, y, s, size=15, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def _dashed(x1, y1, x2, y2, color=MUTED, width=1.5):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{width}" stroke-dasharray="5,4"/>')


def _candle(cx, top, bottom, body_top, body_bottom, up=True, width=34):
    color = UP if up else DOWN
    fill = UP_FILL if up else DOWN_FILL
    x = cx - width / 2
    return (
        f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{bottom}" stroke="{color}" stroke-width="2.5"/>\n'
        f'<rect x="{x}" y="{body_top}" width="{width}" height="{max(body_bottom - body_top, 3)}" '
        f'fill="{fill}" stroke="{color}" stroke-width="2.5"/>'
    )


def candle_anatomy():
    body = []
    cx = 260
    body.append(_candle(cx, 50, 300, 110, 250, up=True, width=64))
    # 가이드 라인 + 라벨
    body.append(_dashed(cx + 32, 50, 420, 50))
    body.append(_text(430, 55, "고가", 16, MUTED, "start"))
    body.append(_dashed(cx + 32, 110, 420, 110))
    body.append(_text(430, 115, "종가", 16, UP, "start"))
    body.append(_dashed(cx + 32, 250, 420, 250))
    body.append(_text(430, 255, "시가", 16, MUTED, "start"))
    body.append(_dashed(cx + 32, 300, 420, 300))
    body.append(_text(430, 305, "저가", 16, MUTED, "start"))
    # 몸통/꼬리 라벨 (왼쪽)
    body.append(_dashed(cx - 32, 180, 90, 180))
    body.append(_text(80, 185, "몸통", 16, INK, "end"))
    body.append(_dashed(cx, 75, 90, 75))
    body.append(_text(80, 80, "위꼬리", 16, INK, "end"))
    body.append(_text(260, 30, "상승(양봉) 캔들의 구조", 17, INK, "middle", "700"))
    return _svg(520, 340, "\n".join(body))


def candle_patterns():
    labels = ["도지", "망치형", "역망치형(슈팅스타)", "장대양봉"]
    body = [_text(360, 28, "자주 나오는 캔들 패턴", 17, INK, "middle", "700")]
    xs = [110, 250, 390, 530]

    # 도지: 몸통 거의 없음, 위아래 꼬리 비슷
    cx = xs[0]
    body.append(_candle(cx, 70, 230, 148, 152, up=True, width=54))

    # 망치형: 몸통 위쪽, 아래꼬리 김
    cx = xs[1]
    body.append(_candle(cx, 90, 230, 90, 130, up=True, width=54))

    # 역망치형: 몸통 아래쪽, 위꼬리 김
    cx = xs[2]
    body.append(_candle(cx, 70, 210, 170, 210, up=False, width=54))

    # 장대양봉: 몸통 매우 큼, 꼬리 짧음
    cx = xs[3]
    body.append(_candle(cx, 65, 235, 75, 225, up=True, width=54))

    for x, label in zip(xs, labels):
        body.append(_text(x, 265, label, 15, MUTED, "middle"))
    return _svg(640, 300, "\n".join(body))


def golden_cross():
    # 단기 이평선: 아래에서 시작해 장기선을 뚫고 올라감
    short_pts = [(40, 230), (110, 245), (180, 220), (250, 190), (300, 165),
                 (360, 120), (430, 90), (500, 75), (580, 65)]
    # 장기 이평선: 완만하게 하락하다 평평해짐
    long_pts = [(40, 150), (110, 165), (180, 178), (250, 185), (300, 188),
                (360, 185), (430, 178), (500, 172), (580, 168)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body = [_text(310, 28, "골든크로스 (단기 이평선이 장기 이평선을 상향 돌파)", 16, INK, "middle", "700")]
    body.append(f'<path d="{path(long_pts)}" fill="none" stroke="{MUTED}" stroke-width="3"/>')
    body.append(f'<path d="{path(short_pts)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')

    # 교차점 근처 마커 (약 x=300~330)
    body.append(f'<circle cx="322" cy="176" r="7" fill="{UP}"/>')
    body.append(_dashed(322, 176, 322, 260, UP))
    body.append(_text(322, 278, "골든크로스 지점", 14, UP, "middle", "700"))

    # 범례
    body.append(f'<line x1="420" y1="245" x2="450" y2="245" stroke="{ACCENT}" stroke-width="3"/>')
    body.append(_text(458, 250, "단기 이평선", 14, INK, "start"))
    body.append(f'<line x1="420" y1="265" x2="450" y2="265" stroke="{MUTED}" stroke-width="3"/>')
    body.append(_text(458, 270, "장기 이평선", 14, INK, "start"))
    return _svg(620, 300, "\n".join(body))


def bollinger_bands():
    upper = [(40, 90), (110, 85), (180, 95), (250, 80), (320, 70), (390, 90), (460, 100), (540, 95)]
    mid = [(40, 150), (110, 150), (180, 152), (250, 150), (320, 148), (390, 150), (460, 152), (540, 150)]
    lower = [(40, 210), (110, 215), (180, 208), (250, 220), (320, 225), (390, 210), (460, 200), (540, 205)]
    price = [(40, 145), (80, 120), (110, 88), (150, 105), (180, 98), (215, 145),
             (250, 205), (285, 222), (320, 228), (355, 200), (390, 155),
             (425, 105), (460, 102), (500, 130), (540, 150)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body = [_text(300, 28, "볼린저밴드: 상단/하단 근접 시 과열·과매도로 해석", 15, INK, "middle", "700")]
    body.append(f'<path d="{path(upper)}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6,4"/>')
    body.append(f'<path d="{path(mid)}" fill="none" stroke="{MUTED}" stroke-width="1.5"/>')
    body.append(f'<path d="{path(lower)}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6,4"/>')
    body.append(f'<path d="{path(price)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')

    body.append(f'<circle cx="320" cy="228" r="7" fill="{DOWN}"/>')
    body.append(_text(320, 255, "과매도(하단밴드)", 13, DOWN, "middle", "700"))
    body.append(f'<circle cx="320" cy="70" r="7" fill="{UP}"/>')
    body.append(_text(320, 60, "과열(상단밴드)", 13, UP, "middle", "700"))
    return _svg(600, 280, "\n".join(body))


def support_resistance_breakout():
    price = [(30, 230), (70, 150), (110, 155), (150, 90), (190, 95), (230, 150),
             (270, 155), (310, 90), (350, 95), (390, 40), (430, 70),
             (470, 55), (510, 30), (550, 60)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body = [_text(300, 26, "저항선 돌파 후 지지선으로 역할 전환 + 재테스트", 15, INK, "middle", "700")]
    # 저항선이었다가 돌파 후 지지선 역할
    body.append(_dashed(30, 92, 380, 92, MUTED, 2))
    body.append(f'<line x1="380" y1="92" x2="550" y2="92" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6,4"/>')
    body.append(_text(40, 82, "저항선", 13, MUTED, "start"))
    body.append(_text(470, 82, "→ 지지선으로 전환", 13, ACCENT, "start"))

    body.append(f'<path d="{path(price)}" fill="none" stroke="{INK}" stroke-width="3"/>')

    body.append(f'<circle cx="390" cy="40" r="6" fill="{UP}"/>')
    body.append(_text(390, 285, "돌파", 13, UP, "middle", "700"))
    body.append(_dashed(390, 40, 390, 270, UP))

    body.append(f'<circle cx="430" cy="70" r="6" fill="{ACCENT}"/>')
    body.append(_text(430, 300, "재테스트(지지 확인)", 13, ACCENT, "middle", "700"))
    body.append(_dashed(430, 70, 430, 288, ACCENT))
    return _svg(600, 320, "\n".join(body))


def liquidity_sweep():
    body = [_text(280, 26, "유동성 스윕: 직전 저점을 살짝 뚫고 빠르게 반전", 15, INK, "middle", "700")]
    prior_low_y = 220
    body.append(_dashed(30, prior_low_y, 530, prior_low_y, MUTED, 2))
    body.append(_text(45, prior_low_y - 10, "직전 저점", 13, MUTED, "start"))

    # 가격 흐름: 저점 근처까지 하락 → 살짝 뚫음(스윕) → 급반전 상승
    price = [(40, 120), (90, 160), (140, 150), (190, 190), (230, 210),
             (260, 236), (290, 205), (330, 140), (380, 90), (430, 70), (490, 55)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body.append(f'<path d="{path(price)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    body.append(f'<circle cx="260" cy="236" r="7" fill="{DOWN}"/>')
    body.append(_dashed(260, 236, 260, 290, DOWN))
    body.append(_text(260, 308, "스윕(가짜 이탈) 후 반전", 13, DOWN, "middle", "700"))
    return _svg(560, 330, "\n".join(body))


def fvg_diagram():
    body = [_text(280, 26, "FVG(페어밸류갭): 3개 캔들 사이의 가격 공백", 15, INK, "middle", "700")]
    # 캔들1 (완만 상승)
    body.append(_candle(110, 200, 260, 200, 240, up=True, width=50))
    body.append(_text(110, 290, "캔들1", 14, MUTED, "middle"))
    # 캔들2 (강한 상승, 임펄스)
    body.append(_candle(280, 60, 220, 65, 210, up=True, width=50))
    body.append(_text(280, 290, "캔들2 (강한 상승)", 14, MUTED, "middle"))
    # 캔들3 (완만 상승, 캔들1 고가보다 훨씬 위에서 시작)
    body.append(_candle(450, 70, 190, 75, 150, up=True, width=50))
    body.append(_text(450, 290, "캔들3", 14, MUTED, "middle"))

    # FVG 영역: 캔들1의 고가(=200)와 캔들3의 저가(=150) 사이
    body.append(f'<rect x="135" y="150" width="290" height="50" fill="{ACCENT}" opacity="0.16" '
                f'stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="5,4"/>')
    body.append(_text(280, 145, "FVG (가격 공백)", 14, ACCENT, "middle", "700"))
    return _svg(560, 320, "\n".join(body))


def risk_reward():
    body = [_text(300, 26, "손익비 1:3 예시 (리스크 1 감수, 보상 3 기대)", 15, INK, "middle", "700")]
    entry_y, stop_y, target_y = 190, 240, 60
    x0, x1 = 60, 540

    body.append(f'<line x1="{x0}" y1="{entry_y}" x2="{x1}" y2="{entry_y}" stroke="{INK}" stroke-width="2"/>')
    body.append(_text(x1 + 8, entry_y + 5, "진입가", 14, INK, "start", "700"))

    body.append(_dashed(x0, stop_y, x1, stop_y, DOWN, 2))
    body.append(_text(x1 + 8, stop_y + 5, "손절가", 14, DOWN, "start", "700"))

    body.append(_dashed(x0, target_y, x1, target_y, UP, 2))
    body.append(_text(x1 + 8, target_y + 5, "목표가", 14, UP, "start", "700"))

    # 가격 경로: 진입 -> 살짝 눌림 -> 목표가로 상승
    price = [(90, entry_y), (140, entry_y + 20), (190, entry_y - 10),
             (260, entry_y - 60), (330, 110), (400, 85), (470, target_y)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body.append(f'<path d="{path(price)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')

    # 리스크/보상 구간 표시 (왼쪽에 브래킷 느낌의 세로선)
    bx = 40
    body.append(f'<line x1="{bx}" y1="{entry_y}" x2="{bx}" y2="{stop_y}" stroke="{DOWN}" stroke-width="3"/>')
    body.append(_text(bx - 8, (entry_y + stop_y) // 2 + 5, "1R", 13, DOWN, "end", "700"))
    body.append(f'<line x1="{bx}" y1="{entry_y}" x2="{bx}" y2="{target_y}" stroke="{UP}" stroke-width="3"/>')
    body.append(_text(bx - 8, (entry_y + target_y) // 2 - 60, "3R", 13, UP, "end", "700"))
    return _svg(660, 300, "\n".join(body))


DIAGRAMS = {
    "candle-anatomy.svg": candle_anatomy,
    "candle-patterns.svg": candle_patterns,
    "golden-cross.svg": golden_cross,
    "bollinger-bands.svg": bollinger_bands,
    "support-resistance-breakout.svg": support_resistance_breakout,
    "liquidity-sweep.svg": liquidity_sweep,
    "fvg-diagram.svg": fvg_diagram,
    "risk-reward.svg": risk_reward,
}

if __name__ == "__main__":
    for filename, fn in DIAGRAMS.items():
        (OUT_DIR / filename).write_text(fn(), encoding="utf-8")
        print(f"생성: {OUT_DIR / filename}")
