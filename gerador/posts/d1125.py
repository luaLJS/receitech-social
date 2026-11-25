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

SLIDES25 = [
    ("D25_P1_F1", "25/11 · P1 · foto única · 1.1", lambda: p2_single("g")),
    ("D25_P1_F2", "25/11 · P1 · foto única · 1.2", lambda: p2_single("h")),
    ("D25_P1_F3", "25/11 · P1 · foto única · 1.3", lambda: p2_single("i")),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES25:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
