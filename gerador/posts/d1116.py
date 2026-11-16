"""Posts de 16/11/2026. Post 1 formas de uso (bolo de pote).
Mockups da tela 1: N8 adaptado x N10.
Uso: python3 d1116.py local|canvas [OUT]"""
import json, os, sys
exec(open('/home/claude/receitech-social/gerador/assets/gen.py').read().split("files = {")[0])

MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1116"
os.makedirs(OUT, exist_ok=True)
BANK = "/home/claude/receitech-social/banco-imagens/"
IMGS = {"POTE": "doce_bolopote_3.jpg"}
BLOBS = {}
bf = "/home/claude/receitech-social/gerador/posts/d1116_blobs.json"
if os.path.exists(bf):
    BLOBS.update(json.load(open(bf)))


def U(k):
    return BLOBS[k] if MODE == "canvas" else "file://" + BANK + IMGS[k]


NAVY, CREAM, SKY, CREAMT = "#101828", "#F3EDE3", "#CFE2FF", "#FFF4D2"
POP = "font-family: 'Poppins', sans-serif"
SER = "font-family: 'Libre Caslon Text', Georgia, serif"
ITA = "font-family: 'Instrument Serif', Georgia, serif; font-style: italic"
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Libre+Caslon+Text:wght@400;700&family=Instrument+Serif:ital@0;1&display=swap"


def box(bg, inner):
    return f'<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {bg}; {POP}">{inner}</div>'


def word(t, x, y, anchor="left"):
    side = f"left: {x}px" if anchor == "left" else f"right: {x}px"
    return f'<span style="position: absolute; {side}; top: {y}px; color: #FFFFFF; font-size: 14px; font-weight: 500">{t}</span>'


# ---------- opção a: N8 adaptado ----------
def p1_n8():
    words = (word("massa de chocolate", 44, 58) + word("rende 2 kg", 46, 58, "right")
             + word("bolo inteiro", 26, 200) + word("fatia", 34, 310, "right")
             + word("bolo de pote", 26, 420) + word("1 receita", 30, 150, "right"))
    inner = f'''{words}
<img src="{U("POTE")}" alt="Bolo de pote de chocolate com granulado" style="position: absolute; left: 120px; top: 96px; width: 300px; height: 380px; object-fit: cover; object-position: 50% 50%">
<div style="position: absolute; left: 44px; right: 44px; top: 512px; {ITA}; color: #FFFFFF; font-size: 44px; line-height: 1.02; letter-spacing: -0.5px; text-align: center">A mesma massa vira bolo, fatia e bolo de pote.</div>
<div style="position: absolute; left: 44px; right: 44px; top: 628px; color: #FFFFFF; font-size: 18px; font-weight: 500; line-height: 1.35; text-align: center">O Receitech calcula o custo de cada um.</div>'''
    return box(BLUE, inner)


# ---------- opção b: N10 ----------
def p1_n10():
    inner = f'''<div style="position: absolute; left: 44px; top: 84px; {SER}; color: {CREAMT}; font-size: 44px; letter-spacing: -1px">A mesma massa</div>
<div style="position: absolute; right: 44px; top: 176px; width: 340px; text-align: right; color: {CREAMT}; font-size: 30px; line-height: 1.14; letter-spacing: -1px">vira bolo, fatia e bolo de pote. O Receitech calcula o custo de cada um.</div>
<img src="{U("POTE")}" alt="Bolo de pote de chocolate com granulado" style="position: absolute; left: 44px; top: 400px; width: 250px; height: 230px; object-fit: cover; object-position: 50% 50%">
<div style="position: absolute; right: 44px; bottom: 34px; color: {CREAMT}; font-size: 11px; letter-spacing: 1px">@receitech_</div>'''
    return box(NAVY, inner)


SLIDES = [
    ("D16_P1_S1_a", "16/11 · P1 · tela 1 · opção a (N8 adaptado)", p1_n8),
    ("D16_P1_S1_b", "16/11 · P1 · tela 1 · opção b (N10)", p1_n10),
]


def page_f(title, body, w, h):
    return page(title, body, w, h).replace(
        "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap", FONTS.replace("&", "&amp;"))


if __name__ == "__main__":
    for code, title, fn in SLIDES:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "Libre+Caslon" in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
