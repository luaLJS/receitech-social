"""Posts de 26/11/2026.
Post 1 (carrossel, 11h): Caixa (entradas e saídas de dinheiro), foto natal_cupcake_1 (caixa de cupcakes de Natal).
Uso: python3 d1126.py local|canvas [OUT]   (env P1V=1 rodada 1 do Post 1)"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1126"
_argv = sys.argv
sys.argv = ["d1125.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1125.py').read().split('\nif __name__ == "__main__"', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

IMGS["CUP"] = "natal_cupcake_1.jpg"
BLOBS["CUP"] = os.environ.get("BLOB_CUP", "/_blob/PENDENTE")
ALT_CUP = "Caixa aberta com quatro cupcakes de Natal decorados: Papai Noel, Feliz Natal, árvore e roupa do Papai Noel"
RED = "#D92D20"

# ---------- tela do app: Finanças > Caixa ----------
# Novembro: entrou 5.480 − saiu 2.315 = sobrou 3.165
assert 5480 - 2315 == 3165


def caixa_screen():
    chevl = svg('<path d="M15 5l-7 7 7 7"></path>', 18, DARK, 2.4)
    chevr = svg('<path d="M9 5l7 7-7 7"></path>', 18, DARK, 2.4)
    chev = svg('<path d="M9 5l7 7-7 7"></path>', 16, "#98A2B3", 2.2)
    card_ic = svg('<rect x="2" y="5" width="20" height="14" rx="2"></rect><path d="M2 10h20"></path>', 13, SEC, 2)

    def row(icon_html, title, sub, val, neg, extra=""):
        col = RED if neg else GREEN
        sign = "−" if neg else "+"
        return f'''<div style="display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 1px solid {DIV}">
{icon_html}
<div style="flex: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0"><span style="font-size: 15px; font-weight: 600">{title}</span>
<span style="font-size: 12px; color: {SEC}">{sub}</span>{extra}</div>
<span style="font-size: 15px; font-weight: 700; color: {col}; white-space: nowrap">{sign} R$ {val}</span></div>'''

    def ic(bg, fg, path):
        return f'<div style="width: 40px; height: 40px; border-radius: 12px; background: {bg}; display: flex; align-items: center; justify-content: center; flex: none">{svg(path, 20, fg, 2)}</div>'
    cup = f'<img src="{U("CUP")}" alt="Cupcakes de Natal" style="width: 40px; height: 40px; border-radius: 12px; object-fit: cover; flex: none">'
    cart = ic("#FEF3F2", RED, '<circle cx="9" cy="20" r="1.5"></circle><circle cx="18" cy="20" r="1.5"></circle><path d="M2 3h3l2.6 12.4a2 2 0 0 0 2 1.6h8.8a2 2 0 0 0 2-1.6L22 7H6"></path>')
    box_ = ic("#FEF3F2", RED, '<path d="M21 8l-9-5-9 5 9 5 9-5z"></path><path d="M3 8v8l9 5 9-5V8"></path><path d="M12 13v8"></path>')
    wifi = ic("#FEF3F2", RED, '<path d="M5 12.5a10 10 0 0 1 14 0"></path><path d="M8.5 16a5 5 0 0 1 7 0"></path><path d="M12 19.5h.01"></path>')
    cake = ic("#ECFDF3", GREEN, '<path d="M4 21h16"></path><path d="M5 21v-8h14v8"></path><path d="M5 13c2 1.5 4 1.5 7 0s5-1.5 7 0"></path><path d="M12 9V5"></path>')
    tag = lambda t: f'<span style="margin-top: 2px; align-self: flex-start; display: flex; align-items: center; gap: 5px; padding: 3px 8px; border-radius: 8px; background: #F2F4F7; font-size: 11px; font-weight: 500; color: {SEC}">{card_ic}{t}</span>'
    items = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == "Finanças" else 500}; color: {BLUE if n == "Finanças" else "#98A2B3"}">{n}</span>' for n in ["Vendas", "Rotina", "Finanças", "Produtos", "Perfil"])
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="padding: 4px 20px 0; display: flex; align-items: center; justify-content: space-between"><div style="display: flex; gap: 22px; font-size: 17px"><span style="color: #98A2B3; font-weight: 500">Resumo</span><span style="color: #98A2B3; font-weight: 500">Lucro</span><span style="font-weight: 700; border-bottom: 2px solid {DARK}; padding-bottom: 6px">Caixa</span></div><span style="height: 34px; padding: 0 14px; border-radius: 17px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600">{svg('<path d="M12 5v14M5 12h14"></path>', 15, "#FFFFFF", 2.6)}Criar</span></div>
<div style="padding: 18px 20px 0">
<div style="display: flex; align-items: center; justify-content: center; gap: 14px; font-size: 15px; font-weight: 600">{chevl}<span>Novembro</span>{chevr}</div>
<div style="margin-top: 16px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px">
<div style="padding: 10px 10px; border-radius: 12px; background: #ECFDF3"><div style="font-size: 12px; color: {SEC}">Entrou</div><div style="margin-top: 2px; font-size: 17px; font-weight: 700; color: {GREEN}">R$ 5.480</div></div>
<div style="padding: 10px 10px; border-radius: 12px; background: #FEF3F2"><div style="font-size: 12px; color: {SEC}">Saiu</div><div style="margin-top: 2px; font-size: 17px; font-weight: 700; color: {RED}">R$ 2.315</div></div>
<div style="padding: 10px 10px; border-radius: 12px; background: {LBLUE}"><div style="font-size: 12px; color: {SEC}">Sobrou</div><div style="margin-top: 2px; font-size: 17px; font-weight: 700; color: {DARK}">R$ 3.165</div></div></div>
<div style="margin-top: 12px; display: flex; align-items: center; justify-content: space-between; padding: 11px 12px; border-radius: 12px; border: 1px solid {DIV}; font-size: 14px"><span>Ainda vai sair em novembro</span><span style="display: flex; align-items: center; gap: 6px; font-weight: 700">R$ 640 {chev}</span></div>
<div style="margin-top: 18px; font-size: 13px; font-weight: 600; color: {SEC}">Hoje, 26 de novembro</div>
{row(cup, "6 cupcakes de Natal", "Venda · Pix", "90,00", False)}
{row(cart, "Mercado", "Ingredientes e embalagens", "214,60", True, tag("Cartão · fatura de 10 de dezembro"))}
{row(box_, "Caixinhas de cupcake", "Ingredientes e embalagens", "156,00", True, tag("3x de R$ 52 · a 1ª em 10 de dezembro"))}
<div style="margin-top: 14px; font-size: 13px; font-weight: 600; color: {SEC}">Ontem, 25 de novembro</div>
{row(cake, "Bolo de festa", "Venda · cartão de débito", "160,00", False)}
{row(wifi, "Internet do negócio", "Contas do negócio", "99,90", True)}
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; background: #FFFFFF; border-top: 1px solid {DIV}; display: flex; justify-content: space-around; padding-top: 14px; box-sizing: border-box">{items}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


P1T = {
    "a": "Todo dinheiro que entra e sai do seu negócio, anotado no Receitech.",
    "b": "Quanto sobrou de dinheiro no seu negócio em novembro? O Receitech mostra.",
    "c": "Comprou caixinha no cartão em 3x? O Receitech lança cada parcela no mês certo.",
}
P1SUB = "No Caixa do Receitech, a venda entra sozinha e o gasto você anota em segundos, até no cartão parcelado."
P1S2 = "A venda entra sozinha. O gasto você anota. E vê quanto sobrou no mês."


def p1_n6(k, size=None):
    size = size or {"a": 31, "b": 33, "c": 33}[k]
    """N6: caixa alta em bloco, justificada, sobre a foto escurecida."""
    inner = f'''<img src="{U("CUP")}" alt="{ALT_CUP}" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover; object-position: 50% 50%">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.58)"></div>
<div style="position: absolute; left: 0; right: 0; top: 46px; text-align: center; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 4px; color: #FFF4D2">RECEITECH</div>
<div style="position: absolute; left: 50px; right: 50px; top: 0; bottom: 20px; display: flex; align-items: center">
<div style="width: 100%; text-align: justify; text-align-last: left; {POP}; font-weight: 600; color: #FFF4D2; font-size: {size}px; line-height: 1.12; letter-spacing: 0.3px; word-spacing: 2px; text-shadow: 0 1px 10px rgba(0,0,0,0.3); text-transform: uppercase">{P1T[k]}</div></div>
<div style="position: absolute; left: 56px; right: 56px; bottom: 44px; text-align: center; {POP}; font-size: 14px; font-weight: 500; line-height: 1.4; color: #FFFFFF">{P1SUB}</div>'''
    return box(NAVY, inner)


def p1_n4(k):
    """N4: foto levemente desfocada + caixa alta justificada, logo embaixo."""
    inner = f'''<img src="{U("CUP")}" alt="{ALT_CUP}" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover; filter: blur(3px); transform: scale(1.04)">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.28)"></div>
<div style="position: absolute; left: 34px; right: 34px; top: 0; bottom: 60px; display: flex; align-items: center">
<div style="width: 100%; text-align: justify; text-align-last: left; {POP}; font-weight: 600; color: #FFFFFF; font-size: 28px; line-height: 1.14; letter-spacing: 0.3px; word-spacing: 2px; text-transform: uppercase; text-shadow: 0 1px 12px rgba(0,0,0,0.35)">{P1T[k]}</div></div>
<div style="position: absolute; left: 50px; right: 50px; bottom: 82px; text-align: center; {POP}; font-size: 14px; font-weight: 500; line-height: 1.4; color: #FFFFFF; text-shadow: 0 1px 8px rgba(0,0,0,0.4)">{P1SUB}</div>
<img src="{U("LOGOW")}" alt="receitech" style="position: absolute; left: 50%; margin-left: -45px; bottom: 34px; width: 90px; height: auto">'''
    return box(NAVY, inner)


def p1_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 46px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{P1S2}</div>
<div style="position: absolute; left: 50%; top: 168px; transform: translateX(-50%)">{phone(caixa_screen(), 510)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 26px; height: 20px; width: auto">'''
    return box(LBLUE, inner)


SLIDES26P1 = [
    ("D26_P1_T1a", "26/11 · P1 · tela 1 · 1.1 (N6)", lambda: p1_n6("a")),
    ("D26_P1_T1b", "26/11 · P1 · tela 1 · 1.2 (N6)", lambda: p1_n6("b")),
    ("D26_P1_T1c", "26/11 · P1 · tela 1 · 1.3 (N6)", lambda: p1_n6("c")),
    ("D26_P1_T1n4", "26/11 · P1 · tela 1 · layout N4 (frase 1.1)", lambda: p1_n4("a")),
    ("D26_P1_S2", "26/11 · P1 · tela 2 (Caixa)", p1_s2),
]


def emit(slides):
    for code, title, fn in slides:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc, code
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")


if __name__ == "__main__":
    if os.environ.get("P1V"):
        emit(SLIDES26P1)
    print("ok", MODE, OUT)


# ================= Post 2 · Resumo: saúde financeira do negócio (carrossel, 18h) =================
IMGS["ESF"] = "salg_esfiha_1.jpg"
BLOBS["ESF"] = os.environ.get("BLOB_ESF", "/_blob/PENDENTE")
ALT_ESF = "Três esfihas abertas de carne sobre uma tábua de madeira"
SERIF = "font-family: 'Instrument Serif', Georgia, serif"
# novembro: ganhos do negócio 4.220 = contas 400 + salário 3.000 + lucro final 820
assert 400 + 3000 + 820 == 4220


def gauge():
    # arco de 90° (raio 184), três faixas, ponteiro curto apontando pra dentro na faixa verde
    import math
    R, cx, cy = 184, 130, 196
    def pt(a, r=R):
        return cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))
    def arc(a0, a1, col):
        x0, y0 = pt(a0); x1, y1 = pt(a1)
        return f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{col}" stroke-width="16" stroke-linecap="butt"></path>'
    a = 61  # posição do ponteiro (135° = esquerda, 45° = direita)
    p0 = pt(a, R + 12); p1 = pt(a, R - 22)
    return f'''<svg width="320" height="86" viewBox="0 0 260 70" aria-hidden="true">
<g transform="translate(0,-2)">{arc(135, 106, "#F97066")}{arc(105, 76, "#FDB022")}{arc(75, 45, "#32D583")}
<path d="M{p0[0]:.1f} {p0[1]:.1f} L{p1[0]:.1f} {p1[1]:.1f}" stroke="{DARK}" stroke-width="5" stroke-linecap="round"></path></g></svg>'''


def resumo_screen():
    chevl = svg('<path d="M15 5l-7 7 7 7"></path>', 18, DARK, 2.4)
    chevr = svg('<path d="M9 5l7 7-7 7"></path>', 18, DARK, 2.4)
    chev = svg('<path d="M9 5l7 7-7 7"></path>', 16, "#98A2B3", 2.2)
    check = svg('<path d="M5 12l5 5 9-10"></path>', 14, GREEN, 3)

    def sq(title, line, val=None):
        v = f'<div style="margin-top: 6px; font-size: 18px; font-weight: 700">{val}</div>' if val else f'<div style="margin-top: 8px; display: flex; align-items: center; gap: 5px; font-size: 12px; font-weight: 600; color: {GREEN}">{check}{line}</div>'
        return f'<div style="padding: 12px 10px; border-radius: 12px; border: 1px solid {DIV}"><div style="font-size: 12px; line-height: 1.3; color: {SEC}">{title}</div>{v}</div>'
    items = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == "Finanças" else 500}; color: {BLUE if n == "Finanças" else "#98A2B3"}">{n}</span>' for n in ["Vendas", "Rotina", "Finanças", "Produtos", "Perfil"])
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="padding: 4px 20px 0; display: flex; gap: 22px; font-size: 17px"><span style="font-weight: 700; border-bottom: 2px solid {DARK}; padding-bottom: 6px">Resumo</span><span style="color: #98A2B3; font-weight: 500">Lucro</span><span style="color: #98A2B3; font-weight: 500">Caixa</span></div>
<div style="padding: 18px 20px 0">
<div style="display: flex; align-items: center; justify-content: center; gap: 14px; font-size: 15px; font-weight: 600">{chevl}<span>Novembro</span>{chevr}</div>
<div style="margin-top: 26px; font-size: 18px; font-weight: 700">Saúde financeira do seu negócio</div>
<div style="margin-top: 30px; display: flex; flex-direction: column; align-items: center">{gauge()}
<div style="margin-top: 8px; font-size: 13px; color: {SEC}">Ganhos do negócio</div>
<div style="font-size: 36px; font-weight: 700; letter-spacing: -0.8px">R$ 4.220</div>
<span style="margin-top: 6px; padding: 4px 12px; border-radius: 14px; background: #ECFDF3; color: {GREEN}; font-size: 13px; font-weight: 600">Saudável</span>
<div style="margin-top: 10px; text-align: center; font-size: 14px; line-height: 1.4; color: {SEC}; padding: 0 10px">As vendas de novembro pagaram as contas e o seu salário, e ainda sobrou lucro.</div></div>
<div style="margin-top: 28px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px">
{sq("Contas do negócio", "Pagas pelas vendas")}{sq("Seu salário", "Pago pelas vendas")}{sq("Lucro final", "", "R$ 820")}</div>
<div style="margin-top: 22px; display: flex; align-items: center; justify-content: space-between; padding: 14px 12px; border-radius: 12px; background: #F9FAFB; font-size: 14px; font-weight: 500"><span>Do lucro ao dinheiro na conta</span>{chev}</div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; background: #FFFFFF; border-top: 1px solid {DIV}; display: flex; justify-content: space-around; padding-top: 14px; box-sizing: border-box">{items}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


P2T = {
    "d": ("Seu negócio está saudável?", "O Receitech responde todo mês."),
    "e": ("Contas pagas, salário pago e lucro?", "O Receitech mostra se o seu mês fechou assim."),
    "f": ("A saúde financeira do seu negócio", "num ponteiro só, no Receitech."),
}
P2SUB = "No Resumo do Receitech, você vê se as vendas do mês pagaram as contas, o seu salário e ainda deram lucro."
P2S2 = "As vendas pagaram as contas e o seu salário. E ainda sobraram R$ 820 de lucro."


def p2_t9(k):
    """T9 (ref. according to my calculations): pergunta grande em serifa itálica + resposta + objeto embaixo; azul."""
    a, b = P2T[k]
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 58px; text-align: center; color: #FFFFFF">
<div style="{SERIF}; font-style: italic; font-size: 56px; line-height: 1.0; letter-spacing: -0.6px; text-wrap: balance">{a}</div>
<div style="margin-top: 16px; {POP}; font-size: 21px; font-weight: 600; letter-spacing: -0.3px; text-wrap: balance">{b}</div>
<div style="margin-top: 12px; {POP}; font-size: 14px; font-weight: 500; line-height: 1.4; color: rgba(255,255,255,0.9); padding: 0 14px">{P2SUB}</div></div>
<img src="{U("ESF")}" alt="{ALT_ESF}" style="position: absolute; left: 60px; bottom: 48px; width: 420px; height: 262px; object-fit: cover; border-radius: 16px">'''
    return box(BLUE, inner)


def p2_t7(k):
    """T7 (ref. Do I really need a website?): título grande em cima à esquerda + objeto no canto de baixo; creme."""
    a, b = P2T[k]
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">RECEITECH</div>
<div style="position: absolute; left: 44px; right: 44px; top: 70px; {POP}; color: {NAVY}; font-size: 40px; font-weight: 700; line-height: 1.08; letter-spacing: -1.4px">{a} <span style="{SERIF}; font-style: italic; font-weight: 400; font-size: 46px; letter-spacing: -0.4px; color: {BLUE}">{b}</span></div>
<div style="position: absolute; left: 44px; width: 210px; bottom: 50px; {POP}; font-size: 15px; font-weight: 500; line-height: 1.4; color: {NAVY}">{P2SUB}</div>
<img src="{U("ESF")}" alt="{ALT_ESF}" style="position: absolute; right: 40px; bottom: 44px; width: 236px; height: 236px; object-fit: cover; border-radius: 16px">'''
    return box(CREAM, inner)


def p2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 46px; color: #FFFFFF; font-size: 27px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{P2S2}</div>
<div style="position: absolute; left: 50%; top: 178px; transform: translateX(-50%)">{phone(resumo_screen(), 510)}</div>
<img src="{U("LOGOW")}" alt="receitech" style="position: absolute; right: 44px; bottom: 26px; height: 20px; width: auto">'''
    return box(NAVY, inner)


SLIDES26P2 = [
    ("D26_P2_T1d", "26/11 · P2 · tela 1 · 6.1 (T9)", lambda: p2_t9("d")),
    ("D26_P2_T1e", "26/11 · P2 · tela 1 · 6.2 (T9)", lambda: p2_t9("e")),
    ("D26_P2_T1f", "26/11 · P2 · tela 1 · 6.3 (T9)", lambda: p2_t9("f")),
    ("D26_P2_T1t7", "26/11 · P2 · tela 1 · 6.4 layout T7 (frase 6.1)", lambda: p2_t7("d")),
    ("D26_P2_S2", "26/11 · P2 · tela 2 (Resumo)", p2_s2),
]
if __name__ == "__main__" and os.environ.get("P2V"):
    emit(SLIDES26P2)


# ================= Post 2 refeito como FOTO ÚNICA (Luana 26/11: o dia é 1 carrossel + 1 foto única) =================
def p2_single(k):
    """T9 azul: pergunta grande em serifa itálica + resposta; celular à esquerda e foto à direita
    (invertido em relação ao P1 de 25/11, que fica logo abaixo no grid: foto à esquerda, celular à direita)."""
    a, b = P2T[k]
    inner = f'''<div style="position: absolute; left: 36px; right: 36px; top: 40px; text-align: center; color: #FFFFFF">
<div style="{SERIF}; font-style: italic; font-size: {48 if k != "e" else 44}px; line-height: 1.0; letter-spacing: -0.5px; text-wrap: balance">{a}</div>
<div style="margin-top: 12px; {POP}; font-size: 19px; font-weight: 600; letter-spacing: -0.3px; text-wrap: balance">{b}</div></div>
<div style="position: absolute; left: 40px; top: {222 if k != "e" else 236}px">{phone(resumo_screen(), 452)}</div>
<img src="{U("ESF")}" alt="{ALT_ESF}" style="position: absolute; right: 36px; bottom: 150px; width: 238px; height: 238px; object-fit: cover; border-radius: 16px">
<div style="position: absolute; right: 36px; width: 238px; bottom: 44px; {POP}; font-size: 13px; font-weight: 500; line-height: 1.4; color: #FFFFFF">{P2SUB}</div>'''
    return box(BLUE, inner)


SLIDES26P2F = [
    ("D26_P2_F1", "26/11 · P2 · foto única · 7.1", lambda: p2_single("d")),
    ("D26_P2_F2", "26/11 · P2 · foto única · 7.2", lambda: p2_single("e")),
    ("D26_P2_F3", "26/11 · P2 · foto única · 7.3", lambda: p2_single("f")),
]
if __name__ == "__main__" and os.environ.get("P2F"):
    emit(SLIDES26P2F)


# ================= Post 2 · rodada 3 (Luana 26/11: frase 7.1; celular no meio, grande, cortado embaixo;
# foto do banco ainda não usada, nada de esfiha; nada de "lado a lado", seguir as referências) =================
IMGS["CESTA"] = "natal_cesta_1.jpg"
IMGS["BROW"] = "doce_brownie_1.jpg"
BLOBS["CESTA"] = os.environ.get("BLOB_CESTA", "/_blob/PENDENTE")
BLOBS["BROW"] = os.environ.get("BLOB_BROW", "/_blob/PENDENTE")
ALT_CESTA = "Cesta de Natal com laço vermelho, panetone, biscoitos de Natal, doce de leite e castanhas embalados"
ALT_BROW = "Brownie recheado com cobertura de chocolate, creme branco e morango"
A71, B71 = P2T["d"]


def p2_t9b(photo="CESTA", alt=ALT_CESTA, pos="50% 55%"):
    """T9 (ref. according to my calculations): pergunta grande em itálico, linha menor, celular grande no meio
    cortado embaixo; a foto entra reta por cima do canto de baixo do celular, como alguém colaria."""
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 52px; text-align: center; color: #FFFFFF">
<div style="{SERIF}; font-style: italic; font-size: 58px; line-height: 0.98; letter-spacing: -0.6px">{A71}</div>
<div style="margin-top: 14px; {POP}; font-size: 19px; font-weight: 600; letter-spacing: -0.3px">{B71}</div></div>
<div style="position: absolute; left: 50%; margin-left: -140px; top: 252px">{phone(resumo_screen(), 600)}</div>
'''
    return box(BLUE, inner)


def p2_t9c(photo="CESTA", alt=ALT_CESTA, pos="50% 82%"):
    """T9 com a foto atrás: a foto entra reta, larga, atrás do celular; o celular grande no meio, cortado embaixo."""
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 46px; text-align: center; color: #FFFFFF">
<div style="{SERIF}; font-style: italic; font-size: 54px; line-height: 0.98; letter-spacing: -0.6px">{A71}</div>
<div style="margin-top: 12px; {POP}; font-size: 18px; font-weight: 600; letter-spacing: -0.3px">{B71}</div></div>
<img src="{U(photo)}" alt="{alt}" style="position: absolute; left: 40px; right: 40px; top: 232px; width: 460px; height: 300px; object-fit: cover; object-position: {pos}; border-radius: 18px">
<div style="position: absolute; left: 50%; margin-left: -131px; top: 342px">{phone(resumo_screen(), 560)}</div>'''
    return box(BLUE, inner)


def p2_n12(photo="CESTA", alt=ALT_CESTA, pos="50% 50%"):
    """N12 (ref. my summer non-negotiables): foto de fundo escurecida, texto em cima, celular no centro cortado embaixo."""
    inner = f'''<img src="{U(photo)}" alt="{alt}" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover; object-position: {pos}">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.42)"></div>
<div style="position: absolute; left: 30px; right: 30px; top: 50px; text-align: center; color: #FFFFFF; line-height: 1.02">
<div style="{POP}; font-size: 34px; font-weight: 600; letter-spacing: -1.2px">Seu negócio está</div>
<div style="{SERIF}; font-style: italic; font-size: 60px">saudável?</div>
<div style="margin-top: 10px; {POP}; font-size: 17px; font-weight: 600">{B71}</div></div>
<div style="position: absolute; left: 50%; margin-left: -127px; top: 262px">{phone(resumo_screen(), 550)}</div>'''
    return box(NAVY, inner)


SLIDES26P2R3 = [
    ("D26_P2_G1", "26/11 · P2 · 8.1 (T9, foto atrás do celular)", lambda: p2_t9c()),
    ("D26_P2_G2", "26/11 · P2 · 8.2 (N12, cesta de Natal no fundo)", lambda: p2_n12()),
    ("D26_P2_G3", "26/11 · P2 · 8.3 (N12, brownie recheado no fundo)", lambda: p2_n12("BROW", ALT_BROW, "30% 50%")),
]
if __name__ == "__main__" and os.environ.get("P2R3"):
    emit(SLIDES26P2R3)


# ================= Post 2 · rodada 4 (Luana 26/11: "parece que um computador fez"; 3 fotos redondas,
# meio giradas, em volta do celular, tipo scrapbook) =================
for _k, _f, _alt in [("NAKED", "doce_nakedcake_1.jpg", "Naked cake com morangos, uvas e mirtilos"),
                     ("TRONCO", "natal_tronco_1.jpg", "Tronco de Natal de chocolate com folhinhas verdes"),
                     ("CHEESE", "doce_cheesecake_1.jpg", "Fatia de cheesecake com calda de frutas vermelhas")]:
    IMGS[_k] = _f
    BLOBS[_k] = os.environ.get("BLOB_" + _k, "/_blob/PENDENTE")
ALTS4 = {"NAKED": "Naked cake com morangos, uvas e mirtilos", "TRONCO": "Tronco de Natal de chocolate com folhinhas verdes",
         "CHEESE": "Fatia de cheesecake com calda de frutas vermelhas"}


def scrap(k, x, y, d, rot, shape, pos="50% 50%"):
    rad = "50%" if shape == "circle" else "26px"
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {d}px; height: {d}px; transform: rotate({rot}deg); '
            f'border-radius: {rad}; background: #FFFFFF; padding: 6px; box-sizing: border-box; box-shadow: 0 8px 18px rgba(16,24,40,0.22)">'
            f'<img src="{U(k)}" alt="{ALTS4[k]}" style="width: 100%; height: 100%; object-fit: cover; object-position: {pos}; border-radius: {rad}; display: block"></div>')


def p2_scrap(shape="circle", bg=None, fg="#FFFFFF"):
    bg = bg or BLUE
    photos = (scrap("NAKED", 352, 236, 168, 9, shape) +
              scrap("TRONCO", 14, 372, 158, -10, shape, "45% 50%") +
              scrap("CHEESE", 368, 520, 150, -6, shape, "45% 62%"))
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 46px; text-align: center; color: {fg}">
<div style="{SERIF}; font-style: italic; font-size: 56px; line-height: 0.98; letter-spacing: -0.6px">{A71}</div>
<div style="margin-top: 12px; {POP}; font-size: 18px; font-weight: 600; letter-spacing: -0.3px">{B71}</div></div>
<div style="position: absolute; left: 50%; margin-left: -140px; top: 236px">{phone(resumo_screen(), 600)}</div>
{photos}'''
    return box(bg, inner)


SLIDES26P2R4 = [
    ("D26_P2_H1", "26/11 · P2 · 9.1 (scrapbook, fotos redondas, azul)", lambda: p2_scrap("circle")),
    ("D26_P2_H2", "26/11 · P2 · 9.2 (scrapbook, cantos arredondados, azul)", lambda: p2_scrap("rounded")),
    ("D26_P2_H3", "26/11 · P2 · 9.3 (scrapbook, fotos redondas, creme)", lambda: p2_scrap("circle", CREAM, NAVY)),
]
if __name__ == "__main__" and os.environ.get("P2R4"):
    emit(SLIDES26P2R4)


# ================= Post 2 · rodada 5 (Luana 26/11: "scrapbook não tem borda branca nas fotos") =================
def scrap2(k, x, y, d, rot, shape, pos="50% 50%"):
    rad = "50%" if shape == "circle" else "24px"
    return (f'<img src="{U(k)}" alt="{ALTS4[k]}" style="position: absolute; left: {x}px; top: {y}px; width: {d}px; height: {d}px; '
            f'object-fit: cover; object-position: {pos}; border-radius: {rad}; transform: rotate({rot}deg); '
            f'box-shadow: 0 8px 18px rgba(16,24,40,0.22)">')


def p2_scrap2(shape="rounded", bg=None, fg="#FFFFFF"):
    bg = bg or BLUE
    photos = (scrap2("NAKED", 356, 240, 160, 9, shape) +
              scrap2("TRONCO", 20, 376, 150, -10, shape, "45% 50%") +
              scrap2("CHEESE", 372, 526, 142, -6, shape, "45% 62%"))
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 46px; text-align: center; color: {fg}">
<div style="{SERIF}; font-style: italic; font-size: 56px; line-height: 0.98; letter-spacing: -0.6px">{A71}</div>
<div style="margin-top: 12px; {POP}; font-size: 18px; font-weight: 600; letter-spacing: -0.3px">{B71}</div></div>
<div style="position: absolute; left: 50%; margin-left: -140px; top: 236px">{phone(resumo_screen(), 600)}</div>
{photos}'''
    return box(bg, inner)


SLIDES26P2R5 = [
    ("D26_P2_J1", "26/11 · P2 · 10.1 (scrapbook sem borda, cantos arredondados)", lambda: p2_scrap2("rounded")),
    ("D26_P2_J2", "26/11 · P2 · 10.2 (scrapbook sem borda, redondas)", lambda: p2_scrap2("circle")),
]
if __name__ == "__main__" and os.environ.get("P2R5"):
    emit(SLIDES26P2R5)


# ================= Post 2 · rodada 6 (Luana 26/11: fotos FORA do celular, celular um pouco menor;
# trocar a foto da esquerda, o tronco de Natal não dá pra ver o que é) =================
IMGS["PALHA"] = "doce_palha_1.jpg"
BLOBS["PALHA"] = os.environ.get("BLOB_PALHA", "/_blob/PENDENTE")
ALTS4["PALHA"] = "Pedaços de palha italiana de chocolate com biscoito, passados no açúcar"


def p2_scrap3(shape="rounded"):
    photos = (scrap2("NAKED", 406, 262, 120, 9, shape) +
              scrap2("PALHA", 14, 400, 122, -10, shape, "40% 45%") +
              scrap2("CHEESE", 408, 540, 116, -7, shape, "45% 62%"))
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 46px; text-align: center; color: #FFFFFF">
<div style="{SERIF}; font-style: italic; font-size: 56px; line-height: 0.98; letter-spacing: -0.6px">{A71}</div>
<div style="margin-top: 12px; {POP}; font-size: 18px; font-weight: 600; letter-spacing: -0.3px">{B71}</div></div>
<div style="position: absolute; left: 50%; margin-left: -118.6px; top: 254px">{phone(resumo_screen(), 500)}</div>
{photos}'''
    return box(BLUE, inner)


SLIDES26P2R6 = [
    ("D26_P2_K1", "26/11 · P2 · 11.1 (scrapbook, fotos fora do celular, cantos arredondados)", lambda: p2_scrap3("rounded")),
    ("D26_P2_K2", "26/11 · P2 · 11.2 (scrapbook, fotos fora do celular, redondas)", lambda: p2_scrap3("circle")),
]
if __name__ == "__main__" and os.environ.get("P2R6"):
    emit(SLIDES26P2R6)
