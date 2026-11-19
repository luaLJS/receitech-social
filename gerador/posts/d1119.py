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


# ================= Post 2 · orçamento de encomenda =================
IMGS["PAVE"] = "natal_pave_1.jpg"
BLOBS["PAVE"] = "/_blob/a9d0ef52e82f1936bcea5cb8b70e4b38"
ALT_PAVE = "Pavê de chocolate na travessa, sobre fundo vermelho"
P2_OPTS = {
    "a": ("CEIA", "PEDIRAM ORÇAMENTO DE 3 PAVÊS?", "No Receitech, o orçamento sai com os seus preços e vira encomenda com um toque."),
    "b": ("NATAL", "O ORÇAMENTO JÁ SAI COM OS SEUS PREÇOS", "No Receitech, você escolhe os produtos, manda o orçamento e confirma a encomenda com um toque."),
    "c": ("SIM?", "ORÇAMENTO ACEITO JÁ VIRA ENCOMENDA", "No Receitech, um toque leva cliente, data e valor pra encomenda."),
}
P2_PICK = "a"


def p2_n5(k=None):
    big, head, sub = P2_OPTS[k or P2_PICK]
    inner = f'''<div style="position: absolute; left: 22px; right: 22px; top: 22px; bottom: 22px; border-radius: 28px; background: {BLUE}"></div>
<div style="position: absolute; left: 50px; top: 50px; width: 150px; {CND}; color: #FFFFFF; font-size: 50px; line-height: 1">{big}</div>
<div style="position: absolute; left: 196px; right: 50px; top: 50px; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; color: {SKY}">RECEITECH MOSTRA</div>
<div style="position: absolute; left: 196px; right: 46px; top: 66px; {CND}; color: #FFFFFF; font-size: 31px; line-height: 1.02">{head}</div>
<img src="{U("PAVE")}" alt="{ALT_PAVE}" style="position: absolute; left: 50px; right: 50px; top: 168px; width: 440px; height: 430px; object-fit: cover; object-position: 50% 50%; border-radius: 16px">
<div style="position: absolute; left: 60px; right: 60px; bottom: 50px; text-align: center; font-size: 15px; font-weight: 600; line-height: 1.35; color: #FFFFFF">{sub}</div>'''
    return box("#FFFFFF", inner)


def orcamento_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    pen = svg('<path d="M4 20h4L19 9l-4-4L4 16v4z"></path>', 16, SEC, 2)

    def line(a, b, bold=False):
        w = 700 if bold else 500
        return f'<div style="display: flex; justify-content: space-between; padding: 6px 0; font-size: 15px; font-weight: {w}"><span>{a}</span><span>{b}</span></div>'

    def sec(t):
        return f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 18px 0 6px"><span style="font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">{t}</span>{pen}</div>'
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="height: 48px; display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; padding: 0 6px">
<div style="display: flex; justify-content: center">{back}</div><span style="text-align: center; font-size: 18px; font-weight: 700">Orçamento</span><span></span></div>
<div style="padding: 6px 20px 0">
<span style="display: inline-block; padding: 4px 12px; border-radius: 20px; background: #FFFAEB; color: #B54708; font-size: 13px; font-weight: 600">Orçamento enviado</span>
{sec("CLIENTE")}
<div style="font-size: 16px; font-weight: 600">Juliana Prado</div>
{sec("ENTREGA")}
<div style="font-size: 16px; font-weight: 600">23 de dezembro · Retirada</div>
{sec("ITENS")}
<div style="display: flex; align-items: center; gap: 12px; padding: 6px 0">
<img src="{U("PAVE")}" alt="Pavê de chocolate" style="width: 48px; height: 48px; border-radius: 10px; object-fit: cover">
<div style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">3 × Pavê de Natal</span><span style="font-size: 13px; color: {SEC}">R$ 120,00 cada</span></div>
<span style="font-size: 15px; font-weight: 600">R$ 360,00</span></div>
<div style="border-top: 1px solid {DIV}; margin-top: 8px; padding-top: 6px">{line("Total", "R$ 360,00", True)}</div>
<div style="font-size: 13px; color: {SEC}; padding-top: 2px">Válido até 10 de dezembro</div>
<div style="margin-top: 22px; height: 50px; border-radius: 14px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Confirmar encomenda</div>
<div style="margin-top: 10px; height: 50px; border-radius: 14px; border: 1px solid {DIV}; color: {DARK}; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Reenviar orçamento</div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


def d19_p2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">Os preços já vêm dos seus produtos. Aceitaram? Um toque e vira encomenda.</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(orcamento_screen(), 500)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; left: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(CREAM, inner)


SLIDES19 += [
    ("D19_P2_opA", "19/11 · P2 · opção a (N5)", lambda: p2_n5("a")),
    ("D19_P2_opB", "19/11 · P2 · opção b (N5)", lambda: p2_n5("b")),
    ("D19_P2_opC", "19/11 · P2 · opção c (N5)", lambda: p2_n5("c")),
    ("D19_P2_S2", "19/11 · P2 · tela 2 (orçamento)", d19_p2_s2),
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
