"""
gen_assets.py - OG 공유 이미지 등 정적 이미지 자산을 생성합니다.
실행: python build/gen_assets.py  (site_config.py 변경 후 다시 실행하면 갱신됩니다)
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import site_config as cfg

OUT_DIR = ROOT / "static" / "img"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_BOLD = r"C:\Windows\Fonts\malgunbd.ttf"
FONT_REG = r"C:\Windows\Fonts\malgun.ttf"


def _font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def make_og_image():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), "#1a5fb4")
    draw = ImageDraw.Draw(img)

    # 우상단에 은은한 캔들스틱 장식
    import random
    random.seed(7)
    x = 760
    prev = 300
    for i in range(14):
        val = prev + random.randint(-40, 45)
        val = max(120, min(480, val))
        top, bottom = sorted([prev, val])
        color = "#8fd19e" if val >= prev else "#e2685f"
        draw.rectangle([x, top, x + 22, bottom], fill=color)
        draw.line([x + 11, top - 18, x + 11, bottom + 18], fill=color, width=3)
        x += 32
        prev = val

    title_font = _font(FONT_BOLD, 64)
    sub_font = _font(FONT_REG, 30)
    draw.text((80, 220), cfg.SITE_NAME, font=title_font, fill="white")
    draw.text((80, 310), cfg.SITE_TAGLINE, font=sub_font, fill="#eaf1fb")

    img.save(OUT_DIR / "og-default.png")
    print(f"OG 이미지 생성: {OUT_DIR / 'og-default.png'}")


def make_favicon():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" rx="7" fill="#1a5fb4"/>
<rect x="7" y="14" width="4" height="11" fill="#8fd19e"/>
<rect x="14" y="8" width="4" height="17" fill="#eaf1fb"/>
<rect x="21" y="17" width="4" height="8" fill="#e2685f"/>
</svg>"""
    (OUT_DIR / "favicon.svg").write_text(svg, encoding="utf-8")
    print(f"favicon 생성: {OUT_DIR / 'favicon.svg'}")


if __name__ == "__main__":
    make_og_image()
    make_favicon()
