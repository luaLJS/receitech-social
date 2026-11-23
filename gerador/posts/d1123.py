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

# ================= Post 2 · taxa do cartão repassada ao cliente =================
IMGS["PUDIM"] = "doce_pudim_1.jpg"
BLOBS["PUDIM"] = "/_blob/aef6ba8e07d968c0e0df6c93c628e639"
ALT_PUD = "Pudim de leite com calda de caramelo e uma fatia servida num prato"
P2_T1 = {
    "a": ("Vendeu no crédito?", "A taxa da maquininha pode ir pro total do cliente.", "No Receitech, você liga “Repassar taxa” na venda e o total já sai com a taxa somada."),
    "b": ("Pudim de R$ 90 no crédito.", "Quem paga a taxa?", "No Receitech, você liga “Repassar taxa” na venda e o total do cliente já sai com a taxa somada."),
    "c": ("A taxa do cartão", "não precisa sair do seu lucro.", "No Receitech, você liga “Repassar taxa” na venda e o total do cliente já sai com a taxa somada."),
}
P2_T2 = "Ligou “Repassar taxa”, o total do cliente já vem com a taxa. Você recebe os R$ 90 inteiros."


def p2_n6(k):
    t1, t2, sub = P2_T1[k]
    txt = t1.upper() + "<br>" + t2.upper()
    top = {"a": 250, "b": 190, "c": 222}[k]
    inner = f'''<img src="{U("PUDIM")}" alt="{ALT_PUD}" style="position: absolute; left: 0; top: {top}px; width: {PW}px; height: {PH - top}px; object-fit: cover; object-position: 22% 50%">
<div style="position: absolute; left: 0; right: 0; top: {top}px; height: 90px; background: linear-gradient({NAVY}, rgba(16,24,40,0))"></div>
<div style="position: absolute; left: 40px; right: 40px; top: 40px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; font-weight: 600; color: #FFF4D2; font-size: 31px; line-height: 1.1; letter-spacing: 0.3px">{txt}</div>
<div style="{POP}; font-weight: 500; color: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 440px">{sub}</div></div>'''
    return box(NAVY, inner)


def pagamento_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)

    def chip(t, on=False):
        st = f"background: {BLUE}; color: #FFFFFF; border: 1px solid {BLUE}" if on else f"background: #FFFFFF; color: {DARK}; border: 1px solid #D0D5DD"
        return f'<span style="padding: 8px 14px; border-radius: 20px; font-size: 15px; font-weight: 500; {st}">{t}</span>'

    def head(t):
        return f'<div style="padding: 18px 0 8px; font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">{t}</div>'

    def line(l, v, bold=False, color=None):
        w = 700 if bold else 500
        c = color or DARK
        return f'<div style="display: flex; justify-content: space-between; padding: 5px 0; font-size: {17 if bold else 15}px"><span style="font-weight: {w}">{l}</span><span style="font-weight: {w}; color: {c}">{v}</span></div>'
    switch = f'<span style="width: 46px; height: 28px; border-radius: 14px; background: {BLUE}; position: relative; flex: none"><span style="position: absolute; right: 3px; top: 3px; width: 22px; height: 22px; border-radius: 11px; background: #FFFFFF"></span></span>'
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="height: 48px; display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; padding: 0 6px">
<div style="display: flex; justify-content: center">{back}</div><span style="text-align: center; font-size: 18px; font-weight: 700">Pagamento</span><span></span></div>
<div style="padding: 0 20px">
{head("PRODUTOS")}
<div style="display: flex; align-items: center; gap: 12px; padding: 4px 0 12px; border-bottom: 1px solid {DIV}">
<img src="{U("PUDIM")}" alt="Pudim de leite" style="width: 52px; height: 52px; border-radius: 12px; object-fit: cover; object-position: 20% 40%">
<div style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Pudim de leite grande</span><span style="font-size: 13px; color: {SEC}">1 unidade</span></div>
<span style="font-size: 16px; font-weight: 600">R$ 90,00</span></div>
{head("FORMA DE PAGAMENTO")}
<div style="display: flex; gap: 8px; flex-wrap: wrap">{chip("Pix")}{chip("Débito")}{chip("Crédito", True)}{chip("Dinheiro")}</div>
<div style="margin-top: 16px; padding: 14px 16px; border-radius: 16px; border: 1px solid {DIV}; display: flex; align-items: center; justify-content: space-between; gap: 12px">
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Repassar taxa ao cliente</span><span style="font-size: 13px; color: {SEC}">Taxa do crédito: 4,99%</span></div>{switch}</div>
<div style="margin-top: 16px; border-radius: 16px; background: {LBLUE}; padding: 12px 16px">
{line("Total dos produtos", "R$ 90,00")}
{line("Taxa do cartão", "+ R$ 4,73")}
<div style="height: 1px; background: #C7D7EE; margin: 6px 0"></div>
{line("Total a pagar", "R$ 94,73", True, BLUE)}</div>
<div style="position: absolute; left: 20px; right: 20px; bottom: 34px; height: 52px; border-radius: 14px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Salvar encomenda</div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


# conta: total a pagar = 90 / (1 - 0,0499) = 94,73; taxa = 94,73 x 4,99% = 4,73; 94,73 - 4,73 = 90,00
assert abs(90 / (1 - 0.0499) - 94.73) < 0.005 and abs(94.73 * 0.0499 - 4.73) < 0.005


def p2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 46px; color: {NAVY}; font-size: 27px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{P2_T2}</div>
<div style="position: absolute; left: 50%; top: 188px; transform: translateX(-50%)">{phone(pagamento_screen(), 490)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 26px; height: 20px; width: auto">'''
    return box(CREAM, inner)


P2_SLIDES = [
    ("D23_P2_T1a", "23/11 · P2 · tela 1 · 1a (N6)", lambda: p2_n6("a")),
    ("D23_P2_T1b", "23/11 · P2 · tela 1 · 1b (N6)", lambda: p2_n6("b")),
    ("D23_P2_T1c", "23/11 · P2 · tela 1 · 1c (N6)", lambda: p2_n6("c")),
    ("D23_P2_S2", "23/11 · P2 · tela 2 (pagamento)", p2_s2),
]


# Luana (23/11): a partir de hoje, 1 carrossel (2 telas) + 1 foto única por dia. Post 2 vira foto única.
def p2_single(k):
    t1, t2, sub = P2_T1[k]
    txt = t1.upper() + "<br>" + t2.upper()
    top = TOPS[k]
    inner = f"""<img src="{U("PUDIM")}" alt="{ALT_PUD}" style="position: absolute; left: 0; top: {top}px; width: {PW}px; height: {PH - top}px; object-fit: cover; object-position: 0% 50%">
<div style="position: absolute; left: 0; right: 0; top: {top}px; height: 80px; background: linear-gradient({NAVY}, rgba(16,24,40,0))"></div>
<div style="position: absolute; left: 40px; right: 40px; top: 40px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; font-weight: 600; color: #FFF4D2; font-size: 31px; line-height: 1.1; letter-spacing: 0.3px">{txt}</div>
<div style="{POP}; font-weight: 500; color: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 440px">{sub}</div></div>
<div style="position: absolute; right: 26px; top: {top + 34}px">{phone(pagamento_screen(), 560)}</div>"""
    return box(NAVY, inner)


SINGLE_SLIDES = [
    ("D23_P2_F1a", "23/11 · P2 · foto única · 1a", lambda: p2_single("a")),
    ("D23_P2_F1b", "23/11 · P2 · foto única · 1b", lambda: p2_single("b")),
    ("D23_P2_F1c", "23/11 · P2 · foto única · 1c", lambda: p2_single("c")),
]


# Luana (23/11): "odiei os textos" da foto única. Textos novos: situação real (cliente paga no cartão) + o que o app faz.
SUB_P2 = "No Receitech, quando a venda é no cartão, a taxa da maquininha já entra no valor que o cliente paga."
P2_T1.update({
    "d": ("Cliente pagou no cartão?", "A taxa entra no valor dele, não no seu.", SUB_P2),
    "e": ("Quanto cobrar a mais", "no cartão? A conta já sai pronta.", SUB_P2),
    "f": ("A maquininha desconta.", "Você recebe o valor inteiro.", SUB_P2),
})
TOPS = {"a": 250, "b": 190, "c": 222, "d": 222, "e": 222, "f": 222}
NEW_SINGLE = [
    ("D23_P2_F2a", "23/11 · P2 · foto única · 2a", lambda: p2_single("d")),
    ("D23_P2_F2b", "23/11 · P2 · foto única · 2b", lambda: p2_single("e")),
    ("D23_P2_F2c", "23/11 · P2 · foto única · 2c", lambda: p2_single("f")),
]

if __name__ == "__main__":
    for code, title, fn in (FINAL23 if os.environ.get("FINAL") else P2_SLIDES if os.environ.get("P2") else SINGLE_SLIDES if os.environ.get("SINGLE") else NEW_SINGLE if os.environ.get("NEW") else SLIDES23):
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
