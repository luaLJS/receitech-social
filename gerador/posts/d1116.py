"""Posts de 16/11/2026. Post 1 formas de uso (bolo de pote).
Mockups da tela 1: N8 adaptado x N10.
Uso: python3 d1116.py local|canvas [OUT]"""
import json, os, sys
exec(open('/home/claude/receitech-social/gerador/assets/gen.py').read().split("files = {")[0])

MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1116"
os.makedirs(OUT, exist_ok=True)
BANK = "/home/claude/receitech-social/banco-imagens/"
IMGS = {"POTE": "doce_bolopote_3.jpg", "BOLO": "doce_bolo_3.jpg", "FATIA": "doce_bolofatia_1.jpg"}
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
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Libre+Caslon+Text:wght@400;700&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@800;900&family=Anton&display=swap"


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


# ---------- opção c: T1 (título + 3 fotos) ----------
def p1_t1():
    def cell(k, label, pos):
        return f'''<div style="display: flex; flex-direction: column; gap: 8px">
<img src="{U(k)}" alt="{label}" style="width: 146px; height: 230px; object-fit: cover; object-position: {pos}">
<span style="{POP}; font-size: 16px; color: {NAVY}; font-weight: 500">{label}</span></div>'''
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 104px; text-align: center; {POP}; font-weight: 700; color: {NAVY}; font-size: 38px; line-height: 1.06; letter-spacing: -1.6px; text-wrap: balance">A mesma massa vira bolo, fatia e bolo de pote.</div>
<div style="position: absolute; left: 40px; right: 40px; top: 236px; display: flex; justify-content: space-between">
{cell("BOLO", "bolo", "50% 60%")}{cell("FATIA", "fatia", "68% 50%")}{cell("POTE", "pote", "50% 50%")}</div>
<div style="position: absolute; left: 0; right: 0; top: 560px; text-align: center; {POP}; font-weight: 700; color: {NAVY}; font-size: 22px; letter-spacing: -0.8px">O Receitech calcula o custo de cada um. <span style="color: {BLUE}">›</span></div>'''
    return box("#FFFFFF", inner)


# ---------- opção d: frase em cima + uma foto simples ----------
def p1_simples():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 56px; color: {NAVY}; font-size: 31px; font-weight: 600; line-height: 1.16; letter-spacing: -0.9px">A mesma massa vira bolo, fatia e bolo de pote.<br><span style="color: {BLUE}">O Receitech calcula o custo de cada um.</span></div>
<img src="{U("POTE")}" alt="Bolo de pote de chocolate com granulado" style="position: absolute; left: 110px; top: 290px; width: 320px; height: 360px; object-fit: cover; object-position: 50% 50%">'''
    return box(SKY, inner)


# ---------- opção e: N3 (caixa alta condensada na foto) ----------
def p1_n3():
    inner = f'''<img src="{U("FATIA")}" alt="Bolo de chocolate com cobertura e uma fatia sendo servida" style="position: absolute; left: 0; top: 0; width: 540px; height: 720px; object-fit: cover; object-position: 62% 50%">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.45)"></div>
<div style="position: absolute; left: 0; right: 0; top: 120px; text-align: center; color: #FFFFFF; font-size: 14px; font-weight: 500">receitech</div>
<div style="position: absolute; left: 40px; right: 40px; top: 0; bottom: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 26px; text-align: center">
<div style="font-family: 'Anton', 'Inter Tight', sans-serif; color: {SKY}; font-size: 64px; line-height: 0.98; letter-spacing: 0.5px">A MESMA MASSA VIRA BOLO, FATIA E BOLO DE POTE.</div>
<div style="color: #FFFFFF; font-size: 19px; font-weight: 500">O Receitech calcula o custo de cada um.</div></div>'''
    return box(NAVY, inner)


# ---------- opção f: N6 (caixa alta em bloco na foto) ----------
def p1_n6():
    inner = f'''<img src="{U("BOLO")}" alt="Bolo de chocolate com brigadeiros em cima" style="position: absolute; left: 0; top: 0; width: 540px; height: 720px; object-fit: cover; object-position: 50% 50%">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.42)"></div>
<div style="position: absolute; left: 60px; right: 60px; top: 0; bottom: 0; display: flex; align-items: center">
<div style="width: 100%; text-align: justify; text-align-last: justify; font-weight: 600; color: {CREAMT}; font-size: 38px; line-height: 1.04; word-spacing: 10px">A MESMA MASSA VIRA BOLO, FATIA E BOLO DE POTE.</div></div>
<div style="position: absolute; left: 60px; right: 60px; bottom: 70px; color: #FFFFFF; font-size: 17px; font-weight: 500">O Receitech calcula o custo de cada um.</div>'''
    return box(NAVY, inner)


SLIDES = [
    ("D16_P1_S1_b", "16/11 · P1 · tela 1 · opção b (N10)", p1_n10),
    ("D16_P1_S1_c", "16/11 · P1 · tela 1 · opção c (T1, três fotos)", p1_t1),
    ("D16_P1_S1_d", "16/11 · P1 · tela 1 · opção d (frase + uma foto)", p1_simples),
    ("D16_P1_S1_e", "16/11 · P1 · tela 1 · opção e (N3, caixa alta na foto)", p1_n3),
    ("D16_P1_S1_f", "16/11 · P1 · tela 1 · opção f (N6, bloco na foto)", p1_n6),
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
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><link href='file:///tmp/claude-0/-home-claude-receitech-social/d7960c7d-3200-51d5-bbb4-0ad4048a92d9/scratchpad/fonts/local.css' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
