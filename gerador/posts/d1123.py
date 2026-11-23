"""Posts de 23/11/2026. Post 1: mais de uma receita no mesmo produto (retomado de 21-22/11).
Luana (23/11) gostou do layout N1 e não das frases: textos novos pra tela 1 e tela 2; etiquetas em cima das camadas.
Uso: python3 d1123.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1123"
_argv = sys.argv
sys.argv = ["d1122.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1122.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

SUB23 = "No Receitech, você junta as receitas no mesmo bolo e vê quanto ele custa e por quanto vender."
T1_OPTS = {
    "a": ("Bolo recheado são 3 receitas.", "E 3 custos."),
    "b": ("Massa, recheio e cobertura.", "Quanto custa o bolo inteiro?"),
    "c": ("Bolo de 3 receitas,", "preço de 3 receitas."),
}
T2_OPTS = {
    "x": "Escolha as receitas do bolo e a caixa. O custo e o preço saem na hora.",
    "y": "Cada receita com o seu custo, até a caixa. O preço do bolo sai sozinho.",
    "f": "Selecione as receitas do bolo. A precificação sai na hora.",
}


def p1_t1(k):
    t1, t2 = T1_OPTS[k]

    def pill(t, bg, fg, x, y):
        return f'<span style="position: absolute; left: {x}px; top: {y}px; transform: translate(-50%, -50%); padding: 6px 15px; border-radius: 30px; background: {bg}; color: {fg}; {POP}; font-size: 15px; font-weight: 600; box-shadow: 0 2px 8px rgba(16,24,40,0.18)">{t}</span>'
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 34px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 4px; color: {NAVY}">RECEITECH</div>
<div style="position: absolute; left: 34px; right: 34px; top: 62px; text-align: center; {HVY}; font-weight: 900; color: {NAVY}; font-size: 46px; line-height: 0.98; letter-spacing: -2px; text-wrap: balance">{t1} <span style="color: {BLUE}">{t2}</span></div>
<img src="{U("RV")}" alt="{ALT_RV}" style="position: absolute; left: 50px; top: 236px; width: 440px; height: 330px; object-fit: cover; object-position: 50% 50%; border-radius: 14px">
{pill("massa", BLUE, "#FFFFFF", 178, 338)}{pill("recheio", "#B8F5C9", NAVY, 338, 372)}{pill("cobertura", "#FFE58F", NAVY, 300, 520)}
<div style="position: absolute; left: 50px; right: 50px; bottom: 34px; text-align: center; font-size: 15px; font-weight: 600; line-height: 1.35; color: {NAVY}">{SUB23}</div>'''
    return box("#FFFFFF", inner)


def p1_t2(k):
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{T2_OPTS[k]}</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(rv_screen(), 500)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(SKY, inner)


# Luana (23/11): tela 1 = 1b; tela 2 = frase dela, sem mudar ("Selecione as receitas do bolo. A precificação sai na hora.")
FINAL23 = [
    ("D23_P1_S1", "23/11 · P1 · tela 1 (N1, escolhida)", lambda: p1_t1("b")),
    ("D23_P1_S2", "23/11 · P1 · tela 2 (escolhida)", lambda: p1_t2("f")),
]

SLIDES23 = [
    ("D23_P1_T1a", "23/11 · P1 · tela 1 · 1a", lambda: p1_t1("a")),
    ("D23_P1_T1b", "23/11 · P1 · tela 1 · 1b", lambda: p1_t1("b")),
    ("D23_P1_T1c", "23/11 · P1 · tela 1 · 1c", lambda: p1_t1("c")),
    ("D23_P1_T2x", "23/11 · P1 · tela 2 · 2a", lambda: p1_t2("x")),
    ("D23_P1_T2y", "23/11 · P1 · tela 2 · 2b", lambda: p1_t2("y")),
]

if __name__ == "__main__":
    for code, title, fn in (FINAL23 if os.environ.get("FINAL") else SLIDES23):
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
