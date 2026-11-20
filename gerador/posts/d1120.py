"""Posts de 20/11/2026. Post 1: orçamento de encomenda (retomado do P2 de 19/11), opção 2 (b).
Uso: python3 d1120.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1120"
_argv = sys.argv
sys.argv = ["d1119.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1119.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

P2_PICK = "b"
S2_OLD = "Os preços já vêm dos seus produtos. Aceitaram? Um toque e vira encomenda."
S2_NEW = "Aceitaram? Toque em “Confirmar encomenda” e ela já entra com cliente, data e valor."


def d20_p1_s2(new=True):
    h = d19_p2_s2()
    return h.replace(S2_OLD, S2_NEW) if new else h


SLIDES20 = [
    ("D20_P1_S1", "20/11 · P1 · tela 1 (N5)", lambda: p2_n5("b")),
    ("D20_P1_S2", "20/11 · P1 · tela 2 (orçamento)", d20_p1_s2),
    ("D20_P1_S2_old", "20/11 · P1 · tela 2 (texto de ontem)", lambda: d20_p1_s2(False)),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES20:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
