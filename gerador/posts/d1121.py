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


# Luana (21/11): tela 1 = frase c no N1. Tela 2 precisa dizer que o custo e o preço saem sozinhos.
# Tela do app: caixa R$ 9,20 pra custo fechar R$ 70,00; preço por produto com margem padrão 65% = 70 / 0,35 = R$ 200,00.
S2_OPTS = {
    "a": "Você cadastra as receitas. O custo e o preço do bolo saem sozinhos.",
    "b": "O custo do bolo sai sozinho, até a caixa. E o preço já vem junto.",
    "c": "Nada de calculadora: o Receitech soma as três receitas e já te dá o preço.",
}


def receitas_screen2():
    h = receitas_screen()
    h = h.replace("R$ 7,20", "R$ 9,20").replace("R$ 68,00", "R$ 70,00")
    a = h.index('<div style="display: flex; justify-content: space-between; padding: 14px 2px 4px')
    b = h.index('<div style="position: absolute; left: 0; right: 0; bottom: 8px')
    mini = lambda l, v, c=DARK: f'<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {SEC}">{l}</span><span style="font-size: 18px; font-weight: 600; color: {c}">{v}</span></div>'
    new = (f'<div style="margin-top: 12px; padding: 0 2px; display: flex; justify-content: space-between; align-items: baseline">'
           f'<span style="font-size: 15px; font-weight: 500">Preço por produto</span><span style="font-size: 22px; font-weight: 700">R$ 200,00</span></div>'
           f'<div style="margin-top: 10px; padding: 0 2px; display: flex; justify-content: space-between">'
           f'{mini("Lucro por produto", "R$ 130,00", "#067647")}{mini("Margem", "65%")}</div>\n</div>\n')
    return h[:a] + new + h[b:]


def s2_opt(k):
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{S2_OPTS[k]}</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(receitas_screen2(), 500)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(SKY, inner)


SLIDES21 = [
    ("D21_P1_opC", "21/11 · P1 · tela 1 (N1, frase c) · escolhida", lambda: p2_n1("c")),
    ("D21_P1_S2a", "21/11 · P1 · tela 2 · frase 1", lambda: s2_opt("a")),
    ("D21_P1_S2b", "21/11 · P1 · tela 2 · frase 2", lambda: s2_opt("b")),
    ("D21_P1_S2c", "21/11 · P1 · tela 2 · frase 3", lambda: s2_opt("c")),
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
