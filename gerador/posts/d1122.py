"""Posts de 22/11/2026. Post 1: mais de uma receita no mesmo produto (retomado do P1 de 21/11),
com foto nova (red velvet), porque o bolo de morango repetia o produto do 13/11 F1.
Uso: python3 d1122.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1122"
_argv = sys.argv
sys.argv = ["d1121.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1121.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

IMGS["RV"] = "doce_redvelvet_1.jpg"
BLOBS["RV"] = "/_blob/7ec30e4d30a7ffafa413cf6df34bf7cf"
ALT_RV = "Fatia de bolo red velvet com três camadas de massa vermelha, recheio e cobertura brancos"


def p1_n1():
    """N1 (frase c escolhida em 21/11) com a foto do red velvet."""
    t1, t2, sub = P2_OPTS["c"]

    def pill(t, bg, fg, css):
        return f'<span style="position: absolute; {css}; padding: 6px 15px; border-radius: 30px; background: {bg}; color: {fg}; {POP}; font-size: 15px; font-weight: 600; box-shadow: 0 2px 8px rgba(16,24,40,0.14)">{t}</span>'
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 34px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 4px; color: {NAVY}">RECEITECH</div>
<div style="position: absolute; left: 34px; right: 34px; top: 62px; text-align: center; {HVY}; font-weight: 900; color: {NAVY}; font-size: 46px; line-height: 0.98; letter-spacing: -2px; text-wrap: balance">{t1} <span style="color: {BLUE}">{t2}</span></div>
<img src="{U("RV")}" alt="{ALT_RV}" style="position: absolute; left: 50px; top: 236px; width: 440px; height: 330px; object-fit: cover; object-position: 50% 50%; border-radius: 14px">
{pill("cobertura", "#FFE58F", NAVY, "right: 30px; top: 470px")}{pill("recheio", "#B8F5C9", NAVY, "left: 262px; top: 268px")}{pill("massa", BLUE, "#FFFFFF", "left: 32px; top: 318px")}
<div style="position: absolute; left: 50px; right: 50px; bottom: 34px; text-align: center; font-size: 15px; font-weight: 600; line-height: 1.35; color: {NAVY}">{sub}</div>'''
    return box("#FFFFFF", inner)


S2_OPTS["d"] = "Cada parte com o seu custo. O custo e o preço do bolo saem sozinhos."


def rv_screen():
    h = receitas_screen2()
    for a, b in [("Bolo de morango", "Bolo red velvet"), (U("MORANGO"), U("RV")),
                 ("Massa branca", "Massa red velvet"), ("16,40", "18,40"),
                 ("Recheio de creme com geleia", "Recheio de cream cheese"), ("19,80", "22,60"),
                 ("Chantilly com morangos", "Ganache branca"), ("24,60", "19,80")]:
        h = h.replace(a, b)
    return h


def s2(k):
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{S2_OPTS[k]}</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(rv_screen(), 500)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(SKY, inner)


# conta: 18,40 + 22,60 + 19,80 + 9,20 = 70,00; preço com margem 65%: 70 / 0,35 = 200,00; lucro 130,00
assert abs(18.40 + 22.60 + 19.80 + 9.20 - 70.00) < 0.001 and abs(70 / 0.35 - 200) < 0.001

SLIDES22 = [
    ("D22_P1_S1", "22/11 · P1 · tela 1 (N1, frase c, red velvet)", p1_n1),
    ("D22_P1_S2a", "22/11 · P1 · tela 2 · a", lambda: s2("a")),
    ("D22_P1_S2b", "22/11 · P1 · tela 2 · b", lambda: s2("b")),
    ("D22_P1_S2c", "22/11 · P1 · tela 2 · c", lambda: s2("c")),
    ("D22_P1_S2d", "22/11 · P1 · tela 2 · d", lambda: s2("d")),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES22:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
