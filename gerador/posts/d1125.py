"""Posts de 25/11/2026.
Post 1 (foto única, 11h): taxa do cartão repassada ao cliente (retomado de 23 e 24/11, N6, pudim), frases novas.
Uso: python3 d1125.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1125"
_argv = sys.argv
sys.argv = ["d1123.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1123.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

SUB25 = "No Receitech, você liga “Repassar taxa” na venda e o total do cliente já sai com a taxa da maquininha."
P2_T1.update({
    "g": ("A maquininha desconta.", "Você recebe o valor inteiro.", SUB25),
    "h": ("Vender no crédito", "sem perder 5% de cada venda.", SUB25),
    "i": ("Pagou no crédito?", "A taxa vai pro total do cliente.", SUB25),
})
TOPS.update({"g": 222, "h": 222, "i": 222})

IMGS["PUD2"] = "doce_pudim_2.jpg"
BLOBS["PUD2"] = "/_blob/b4d6858d13932caf186dfef02fe3fbb8"
# miniatura do app também usa a foto nova
IMGS["PUDIM"], BLOBS["PUDIM"] = IMGS["PUD2"], BLOBS["PUD2"]
ALT_PUD2 = "Pudim de leite com calda de caramelo num prato branco, com uma fatia sendo servida"


# Luana (25/11): "tá péssimo esse fundo do pudim" -> foto nova, fundo branco (doce_pudim_2)
def p1_v2(k, side="R"):
    t1, t2, sub = P2_T1[k]
    txt = t1.upper() + "<br>" + t2.upper()
    top = TOPS[k]
    pos = "8% 50%" if side == "R" else "100% 50%"
    ph = f'right: 26px' if side == "R" else 'left: 26px'
    inner = f"""<img src="{U("PUD2")}" alt="{ALT_PUD2}" style="position: absolute; left: 0; top: {top}px; width: {PW}px; height: {PH - top}px; object-fit: cover; object-position: {pos}">
<div style="position: absolute; left: 40px; right: 40px; top: 40px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; font-weight: 600; color: #FFF4D2; font-size: 31px; line-height: 1.1; letter-spacing: 0.3px">{txt}</div>
<div style="{POP}; font-weight: 500; color: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 440px">{sub}</div></div>
<div style="position: absolute; {ph}; top: {top + 34}px">{phone(pagamento_screen(), 560)}</div>"""
    return box(NAVY, inner)


SLIDES25B = [
    ("D25_P1_F1", "25/11 · P1 · foto única · 1.1 (pudim novo)", lambda: p1_v2("g", "L")),
    ("D25_P1_F2", "25/11 · P1 · foto única · 1.2 (pudim novo)", lambda: p1_v2("h", "L")),
    ("D25_P1_F3", "25/11 · P1 · foto única · 1.3 (pudim novo)", lambda: p1_v2("i", "L")),
]

SLIDES25 = [
    ("D25_P1_F1", "25/11 · P1 · foto única · 1.1", lambda: p2_single("g")),
    ("D25_P1_F2", "25/11 · P1 · foto única · 1.2", lambda: p2_single("h")),
    ("D25_P1_F3", "25/11 · P1 · foto única · 1.3", lambda: p2_single("i")),
]

if __name__ == "__main__":
    for code, title, fn in ([] if (os.environ.get('V3') or os.environ.get('V4')) else SLIDES25B if os.environ.get('V2') else SLIDES25):
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)


# ================= Rodada 3 (Luana 25/11: "péssimo essas sugestões, troca de ideia de texto e layout") =================
T3OPTS = {
    "j": ("Crédito ou Pix? Pro seu lucro,", "tanto faz."),
    "k": ("A maquininha come", "5% do pudim."),
    "l": ("O cliente escolheu o crédito.", "A taxa vai junto."),
}
SUB3 = "No Receitech, você liga “Repassar taxa” na venda e a taxa entra no total do cliente."


SER = "font-family: 'Libre Caslon Text', Georgia, serif"
CREAM = "#F3EDE3"


def p1_t4(k):
    a, b = T3OPTS[k]
    inner = f'''<div style="position: absolute; left: 44px; right: 40px; top: 44px; {POP}; color: {NAVY}; font-size: 46px; font-weight: 800; line-height: 1.04; letter-spacing: -2px">{a} <span style="color: {BLUE}">{b}</span></div>
<img src="{U("PUD2")}" alt="{ALT_PUD2}" style="position: absolute; left: 44px; top: 262px; width: 236px; height: 340px; object-fit: cover; object-position: 80% 50%; border-radius: 18px">
<div style="position: absolute; left: 300px; top: 236px">{phone(pagamento_screen(), 396)}</div>
<div style="position: absolute; left: 44px; right: 44px; bottom: 40px; {POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB3}</div>'''
    return box("#F2F2F0", inner)


def p1_t2(k):
    a, b = T3OPTS[k]
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 40px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 4px; color: {BLUE}">RECEITECH</div>
<div style="position: absolute; left: 50px; right: 50px; top: 70px; text-align: center; {SER}; color: {NAVY}; font-size: 40px; line-height: 1.15; letter-spacing: -0.8px; text-wrap: balance">{a} <i>{b}</i></div>
<img src="{U("PUD2")}" alt="{ALT_PUD2}" style="position: absolute; left: 40px; top: 290px; width: 250px; height: 290px; object-fit: cover; object-position: 88% 50%; border-radius: 14px">
<div style="position: absolute; left: 306px; top: 236px">{phone(pagamento_screen(), 396)}</div>
<div style="position: absolute; left: 50px; right: 50px; bottom: 38px; text-align: center; {POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB3}</div>'''
    return box(CREAM, inner)


SLIDES25C = [
    ("D25_P1_R1", "25/11 · P1 · 2.1 (T4)", lambda: p1_t4("j")),
    ("D25_P1_R2", "25/11 · P1 · 2.2 (T4)", lambda: p1_t4("k")),
    ("D25_P1_R3", "25/11 · P1 · 2.3 (T4)", lambda: p1_t4("l")),
    ("D25_P1_R4", "25/11 · P1 · 2.4 (layout T2, frase 2.2)", lambda: p1_t2("k")),
]
if __name__ == "__main__" and os.environ.get("V3") and not os.environ.get("V4"):
    for code, title, fn in SLIDES25C:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")


# ================= Rodada 4 (Luana 25/11: funcionalidade mais gritante; foto do pudim horrível) =================
IMGS["PUD3"] = "doce_pudim_3.jpg"
BLOBS["PUD3"] = "/_blob/62ad94c4649c463ae6c60e4466a1c5bf"
ALT_PUD3 = "Pudim de leite inteiro com calda de caramelo num prato branco"
IMGS["PUDIM"], BLOBS["PUDIM"] = IMGS["PUD3"], BLOBS["PUD3"]
T4OPTS = {
    "m": ("Repasse a taxa do cartão", "pro cliente.", "Um toque na venda e o total do cliente já sai com a taxa somada. Você recebe o valor inteiro."),
    "n": ("Taxa do cartão?", "Quem paga é o cliente.", "Você liga “Repassar taxa” na venda e o total já sai com a taxa somada."),
    "o": ("O Receitech soma a taxa do cartão", "no total do cliente.", "Você liga “Repassar taxa” na venda e recebe o valor inteiro do pudim."),
}


def p1_r4(k):
    a, b, sub = T4OPTS[k]
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">NO RECEITECH</div>
<div style="position: absolute; left: 44px; right: 40px; top: 64px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; color: {NAVY}; font-size: {44 if k == "m" else 38}px; font-weight: 800; line-height: 1.04; letter-spacing: -1.8px">{a} <span style="color: {BLUE}">{b}</span></div>
<div style="{POP}; color: {NAVY}; font-size: 15px; font-weight: 500; line-height: 1.4">{sub}</div></div>
<img src="{U("PUD3")}" alt="{ALT_PUD3}" style="position: absolute; left: 44px; top: 300px; width: 250px; height: 300px; object-fit: cover; object-position: 72% 50%; border-radius: 18px">
<div style="position: absolute; left: 310px; top: 262px">{phone(pagamento_screen(), 420)}</div>'''
    return box("#F2F2F0", inner)


SLIDES25D = [
    ("D25_P1_S1", "25/11 · P1 · 3.1", lambda: p1_r4("m")),
    ("D25_P1_S2", "25/11 · P1 · 3.2", lambda: p1_r4("n")),
    ("D25_P1_S3", "25/11 · P1 · 3.3", lambda: p1_r4("o")),
]
if __name__ == "__main__" and os.environ.get("V4"):
    for code, title, fn in SLIDES25D:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
