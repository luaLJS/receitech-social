"""Posts de 19/11/2026. Post 1: prazo de encomenda no cardápio (retomado do P2 de 18/11).
Uso: python3 d1119.py local|canvas [OUT]"""
import json, os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1119"
_argv = sys.argv
sys.argv = ["d1118.py", MODE, OUT]
_src = open('/home/claude/receitech-social/gerador/posts/d1118.py').read().split('if __name__ == "__main__":')[0]
exec(_src)
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

# ================= Post 1 · prazo de encomenda no cardápio =================
P1_A = "Seu cliente sabe com quanto tempo tem que encomendar?"
P1_B = "No cardápio do Receitech, o prazo aparece em cada produto."


def d19_p1_s1():
    """T3: foto inteira + serifa itálica, texto no alto sobre o fundo claro da foto."""
    inner = f'''{rena_bg()}
<div style="position: absolute; left: 36px; right: 36px; top: 40px; display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center">
<div style="{ITA}; color: {NAVY}; font-size: 44px; line-height: 1.0; letter-spacing: -0.5px; text-wrap: balance">{P1_A}</div>
<div style="max-width: 420px; color: {NAVY}; font-size: 16px; font-weight: 600; line-height: 1.35">{P1_B}</div></div>'''
    return box("#EDEDF0", inner)


def d19_p1_s2():
    return p2_s2().replace("A cliente vê antes de pedir.", "Quem compra vê antes de pedir.")


SLIDES19 = [
    ("D19_P1_S1", "19/11 · P1 · tela 1 (T3)", d19_p1_s1),
    ("D19_P1_S2", "19/11 · P1 · tela 2 (cardápio: prazo)", d19_p1_s2),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES19:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
