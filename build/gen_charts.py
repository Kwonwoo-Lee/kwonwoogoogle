"""
gen_charts.py - 강의 본문에 들어가는 설명용 SVG 다이어그램을 생성합니다 (한국어 + 영어).
실제 시세 데이터가 아니라 개념 설명용으로 손으로 좌표를 잡은 예시 그림입니다.
실행: python build/gen_charts.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

OUT_ROOT = ROOT / "static" / "img" / "charts"

FONT_KO = "'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif"
FONT_EN = "-apple-system, 'Segoe UI', sans-serif"
INK = "#20201a"
MUTED = "#767568"
GRID = "#e1e0d9"
CARD = "#fdfdfb"
ACCENT = "#1a5fb4"
UP = "#1f9d55"
DOWN = "#d0453b"
UP_FILL = "#dcf3e4"
DOWN_FILL = "#fbe1df"

TEXT = {
    "ko": {
        "candle_anatomy_title": "상승(양봉) 캔들의 구조",
        "high": "고가", "close": "종가", "open": "시가", "low": "저가",
        "body_label": "몸통", "upper_wick": "위꼬리",
        "patterns_title": "자주 나오는 캔들 패턴",
        "doji": "도지", "hammer": "망치형", "inverted_hammer": "역망치형(슈팅스타)", "long_bull": "장대양봉",
        "golden_cross_title": "골든크로스 (단기 이평선이 장기 이평선을 상향 돌파)",
        "golden_cross_point": "골든크로스 지점", "short_ma": "단기 이평선", "long_ma": "장기 이평선",
        "bollinger_title": "볼린저밴드: 상단/하단 근접 시 과열·과매도로 해석",
        "oversold": "과매도(하단밴드)", "overbought": "과열(상단밴드)",
        "breakout_title": "저항선 돌파 후 지지선으로 역할 전환 + 재테스트",
        "resistance": "저항선", "becomes_support": "→ 지지선으로 전환",
        "breakout": "돌파", "retest": "재테스트(지지 확인)",
        "sweep_title": "유동성 스윕: 직전 저점을 살짝 뚫고 빠르게 반전",
        "prior_low": "직전 저점", "sweep_reversal": "스윕(가짜 이탈) 후 반전",
        "fvg_title": "FVG(페어밸류갭): 3개 캔들 사이의 가격 공백",
        "candle1": "캔들1", "candle2": "캔들2 (강한 상승)", "candle3": "캔들3", "fvg_area": "FVG (가격 공백)",
        "rr_title": "손익비 1:3 예시 (리스크 1 감수, 보상 3 기대)",
        "entry": "진입가", "stop": "손절가", "target": "목표가",
    },
    "en": {
        "candle_anatomy_title": "Anatomy of a bullish candle",
        "high": "High", "close": "Close", "open": "Open", "low": "Low",
        "body_label": "Body", "upper_wick": "Upper wick",
        "patterns_title": "Common candlestick patterns",
        "doji": "Doji", "hammer": "Hammer", "inverted_hammer": "Inverted Hammer (Shooting Star)",
        "long_bull": "Long bullish candle",
        "golden_cross_title": "Golden Cross (short-term MA crosses above long-term MA)",
        "golden_cross_point": "Golden Cross point", "short_ma": "Short-term MA", "long_ma": "Long-term MA",
        "bollinger_title": "Bollinger Bands: touching the bands signals overbought/oversold",
        "oversold": "Oversold (lower band)", "overbought": "Overbought (upper band)",
        "breakout_title": "Resistance breaks, flips into support, then gets retested",
        "resistance": "Resistance", "becomes_support": "→ becomes support",
        "breakout": "Breakout", "retest": "Retest (support confirmed)",
        "sweep_title": "Liquidity sweep: price dips just below a prior low, then reverses",
        "prior_low": "Prior low", "sweep_reversal": "Sweep (false breakdown), then reversal",
        "fvg_title": "FVG (Fair Value Gap): a price gap across 3 candles",
        "candle1": "Candle 1", "candle2": "Candle 2 (strong move)", "candle3": "Candle 3",
        "fvg_area": "FVG (price gap)",
        "rr_title": "1:3 risk/reward example (risk 1 to make 3)",
        "entry": "Entry", "stop": "Stop", "target": "Target",
    },
}


def _svg(width, height, body, font):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'font-family="{font}">\n'
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


def candle_anatomy(lang):
    t = TEXT[lang]
    body = []
    cx = 260
    body.append(_candle(cx, 50, 300, 110, 250, up=True, width=64))
    body.append(_dashed(cx + 32, 50, 420, 50))
    body.append(_text(430, 55, t["high"], 16, MUTED, "start"))
    body.append(_dashed(cx + 32, 110, 420, 110))
    body.append(_text(430, 115, t["close"], 16, UP, "start"))
    body.append(_dashed(cx + 32, 250, 420, 250))
    body.append(_text(430, 255, t["open"], 16, MUTED, "start"))
    body.append(_dashed(cx + 32, 300, 420, 300))
    body.append(_text(430, 305, t["low"], 16, MUTED, "start"))
    body.append(_dashed(cx - 32, 180, 90, 180))
    body.append(_text(80, 185, t["body_label"], 16, INK, "end"))
    body.append(_dashed(cx, 75, 90, 75))
    body.append(_text(80, 80, t["upper_wick"], 16, INK, "end"))
    body.append(_text(260, 30, t["candle_anatomy_title"], 17, INK, "middle", "700"))
    return _svg(520, 340, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def candle_patterns(lang):
    t = TEXT[lang]
    labels = [t["doji"], t["hammer"], t["inverted_hammer"], t["long_bull"]]
    body = [_text(360, 28, t["patterns_title"], 17, INK, "middle", "700")]
    xs = [110, 250, 390, 530]

    cx = xs[0]
    body.append(_candle(cx, 70, 230, 148, 152, up=True, width=54))
    cx = xs[1]
    body.append(_candle(cx, 90, 230, 90, 130, up=True, width=54))
    cx = xs[2]
    body.append(_candle(cx, 70, 210, 170, 210, up=False, width=54))
    cx = xs[3]
    body.append(_candle(cx, 65, 235, 75, 225, up=True, width=54))

    for x, label in zip(xs, labels):
        body.append(_text(x, 265, label, 15, MUTED, "middle"))
    return _svg(640, 300, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def golden_cross(lang):
    t = TEXT[lang]
    short_pts = [(40, 230), (110, 245), (180, 220), (250, 190), (300, 165),
                 (360, 120), (430, 90), (500, 75), (580, 65)]
    long_pts = [(40, 150), (110, 165), (180, 178), (250, 185), (300, 188),
                (360, 185), (430, 178), (500, 172), (580, 168)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body = [_text(310, 28, t["golden_cross_title"], 16, INK, "middle", "700")]
    body.append(f'<path d="{path(long_pts)}" fill="none" stroke="{MUTED}" stroke-width="3"/>')
    body.append(f'<path d="{path(short_pts)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')

    body.append(f'<circle cx="322" cy="176" r="7" fill="{UP}"/>')
    body.append(_dashed(322, 176, 322, 260, UP))
    body.append(_text(322, 278, t["golden_cross_point"], 14, UP, "middle", "700"))

    body.append(f'<line x1="420" y1="245" x2="450" y2="245" stroke="{ACCENT}" stroke-width="3"/>')
    body.append(_text(458, 250, t["short_ma"], 14, INK, "start"))
    body.append(f'<line x1="420" y1="265" x2="450" y2="265" stroke="{MUTED}" stroke-width="3"/>')
    body.append(_text(458, 270, t["long_ma"], 14, INK, "start"))
    return _svg(620, 300, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def bollinger_bands(lang):
    t = TEXT[lang]
    upper = [(40, 90), (110, 85), (180, 95), (250, 80), (320, 70), (390, 90), (460, 100), (540, 95)]
    mid = [(40, 150), (110, 150), (180, 152), (250, 150), (320, 148), (390, 150), (460, 152), (540, 150)]
    lower = [(40, 210), (110, 215), (180, 208), (250, 220), (320, 225), (390, 210), (460, 200), (540, 205)]
    price = [(40, 145), (80, 120), (110, 88), (150, 105), (180, 98), (215, 145),
             (250, 205), (285, 222), (320, 228), (355, 200), (390, 155),
             (425, 105), (460, 102), (500, 130), (540, 150)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body = [_text(300, 28, t["bollinger_title"], 15, INK, "middle", "700")]
    body.append(f'<path d="{path(upper)}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6,4"/>')
    body.append(f'<path d="{path(mid)}" fill="none" stroke="{MUTED}" stroke-width="1.5"/>')
    body.append(f'<path d="{path(lower)}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6,4"/>')
    body.append(f'<path d="{path(price)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')

    body.append(f'<circle cx="320" cy="228" r="7" fill="{DOWN}"/>')
    body.append(_text(320, 255, t["oversold"], 13, DOWN, "middle", "700"))
    body.append(f'<circle cx="320" cy="70" r="7" fill="{UP}"/>')
    body.append(_text(320, 60, t["overbought"], 13, UP, "middle", "700"))
    return _svg(600, 280, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def support_resistance_breakout(lang):
    t = TEXT[lang]
    price = [(30, 230), (70, 150), (110, 155), (150, 90), (190, 95), (230, 150),
             (270, 155), (310, 90), (350, 95), (390, 40), (430, 70),
             (470, 55), (510, 30), (550, 60)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body = [_text(300, 26, t["breakout_title"], 15, INK, "middle", "700")]
    body.append(_dashed(30, 92, 380, 92, MUTED, 2))
    body.append(f'<line x1="380" y1="92" x2="550" y2="92" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6,4"/>')
    body.append(_text(40, 82, t["resistance"], 13, MUTED, "start"))
    body.append(_text(470, 82, t["becomes_support"], 13, ACCENT, "start"))

    body.append(f'<path d="{path(price)}" fill="none" stroke="{INK}" stroke-width="3"/>')

    body.append(f'<circle cx="390" cy="40" r="6" fill="{UP}"/>')
    body.append(_text(390, 285, t["breakout"], 13, UP, "middle", "700"))
    body.append(_dashed(390, 40, 390, 270, UP))

    body.append(f'<circle cx="430" cy="70" r="6" fill="{ACCENT}"/>')
    body.append(_text(430, 300, t["retest"], 13, ACCENT, "middle", "700"))
    body.append(_dashed(430, 70, 430, 288, ACCENT))
    return _svg(600, 320, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def liquidity_sweep(lang):
    t = TEXT[lang]
    body = [_text(280, 26, t["sweep_title"], 15, INK, "middle", "700")]
    prior_low_y = 220
    body.append(_dashed(30, prior_low_y, 530, prior_low_y, MUTED, 2))
    body.append(_text(45, prior_low_y - 10, t["prior_low"], 13, MUTED, "start"))

    price = [(40, 120), (90, 160), (140, 150), (190, 190), (230, 210),
             (260, 236), (290, 205), (330, 140), (380, 90), (430, 70), (490, 55)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body.append(f'<path d="{path(price)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    body.append(f'<circle cx="260" cy="236" r="7" fill="{DOWN}"/>')
    body.append(_dashed(260, 236, 260, 290, DOWN))
    body.append(_text(260, 308, t["sweep_reversal"], 13, DOWN, "middle", "700"))
    return _svg(560, 330, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def fvg_diagram(lang):
    t = TEXT[lang]
    body = [_text(280, 26, t["fvg_title"], 15, INK, "middle", "700")]
    body.append(_candle(110, 200, 260, 200, 240, up=True, width=50))
    body.append(_text(110, 290, t["candle1"], 14, MUTED, "middle"))
    body.append(_candle(280, 60, 220, 65, 210, up=True, width=50))
    body.append(_text(280, 290, t["candle2"], 14, MUTED, "middle"))
    body.append(_candle(450, 70, 190, 75, 150, up=True, width=50))
    body.append(_text(450, 290, t["candle3"], 14, MUTED, "middle"))

    body.append(f'<rect x="135" y="150" width="290" height="50" fill="{ACCENT}" opacity="0.16" '
                f'stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="5,4"/>')
    body.append(_text(280, 145, t["fvg_area"], 14, ACCENT, "middle", "700"))
    return _svg(560, 320, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


def risk_reward(lang):
    t = TEXT[lang]
    body = [_text(300, 26, t["rr_title"], 15, INK, "middle", "700")]
    entry_y, stop_y, target_y = 190, 240, 60
    x0, x1 = 60, 540

    body.append(f'<line x1="{x0}" y1="{entry_y}" x2="{x1}" y2="{entry_y}" stroke="{INK}" stroke-width="2"/>')
    body.append(_text(x1 + 8, entry_y + 5, t["entry"], 14, INK, "start", "700"))

    body.append(_dashed(x0, stop_y, x1, stop_y, DOWN, 2))
    body.append(_text(x1 + 8, stop_y + 5, t["stop"], 14, DOWN, "start", "700"))

    body.append(_dashed(x0, target_y, x1, target_y, UP, 2))
    body.append(_text(x1 + 8, target_y + 5, t["target"], 14, UP, "start", "700"))

    price = [(90, entry_y), (140, entry_y + 20), (190, entry_y - 10),
             (260, entry_y - 60), (330, 110), (400, 85), (470, target_y)]

    def path(pts):
        return "M " + " L ".join(f"{x},{y}" for x, y in pts)

    body.append(f'<path d="{path(price)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')

    bx = 40
    body.append(f'<line x1="{bx}" y1="{entry_y}" x2="{bx}" y2="{stop_y}" stroke="{DOWN}" stroke-width="3"/>')
    body.append(_text(bx - 8, (entry_y + stop_y) // 2 + 5, "1R", 13, DOWN, "end", "700"))
    body.append(f'<line x1="{bx}" y1="{entry_y}" x2="{bx}" y2="{target_y}" stroke="{UP}" stroke-width="3"/>')
    body.append(_text(bx - 8, (entry_y + target_y) // 2 - 60, "3R", 13, UP, "end", "700"))
    return _svg(660, 300, "\n".join(body), FONT_KO if lang == "ko" else FONT_EN)


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
    for lang in ("ko", "en"):
        out_dir = OUT_ROOT / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        for filename, fn in DIAGRAMS.items():
            (out_dir / filename).write_text(fn(lang), encoding="utf-8")
            print(f"생성: {out_dir / filename}")
