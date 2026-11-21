"""Posts de 21/11/2026. Post 1: mais de uma receita no mesmo produto (retomado do P2 de 20/11).
Uso: [P2=1] python3 d1121.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1121"
_argv = sys.argv
sys.argv = ["d1120.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1120.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)


def p1_n6(k):
    """N6: caixa alta em bloco, justificada, no alto; foto inteira do bolo (sem desfoque) com véu escuro só em cima."""
    t1, t2, sub = P2_OPTS[k]
    txt = t1.upper() + "<br>" + t2.upper()
    inner = f'''<img src="{U("MORANGO")}" alt="{ALT_MOR}" style="position: absolute; left: 0; top: 226px; width: {PW}px; height: 610px; object-fit: cover; object-position: 50% 0%">
<div style="position: absolute; left: 0; right: 0; top: 226px; height: 110px; background: linear-gradient({NAVY}, rgba(16,24,40,0))"></div>
<div style="position: absolute; left: 40px; right: 40px; top: 38px; display: flex; flex-direction: column; gap: 12px">
<div style="{POP}; font-weight: 600; color: #FFF4D2; font-size: 31px; line-height: 1.1; letter-spacing: 0.3px">{txt}</div>
<div style="{POP}; font-weight: 500; color: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 420px">{sub}</div></div>'''
    return box(NAVY, inner)


SLIDES21 = [
    ("D21_P1_opA", "21/11 · P1 · opção a (N1)", lambda: p2_n1("a")),
    ("D21_P1_opB", "21/11 · P1 · opção b (N1)", lambda: p2_n1("b")),
    ("D21_P1_opC", "21/11 · P1 · opção c (N1)", lambda: p2_n1("c")),
    ("D21_P1_N6", "21/11 · P1 · layout alternativo (N6, frase a)", lambda: p1_n6("a")),
    ("D21_P1_S2", "21/11 · P1 · tela 2 (receitas do produto)", p2_s2),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES21:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
