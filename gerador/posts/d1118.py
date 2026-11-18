"""Posts de 18/11/2026. Post 1: gás e energia no custo da receita (equipamentos).
Uso: python3 d1118.py local|canvas [OUT]"""
import json, os, sys
exec(open('/home/claude/receitech-social/gerador/assets/gen.py').read().split("files = {")[0])

MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1118"
os.makedirs(OUT, exist_ok=True)
BANK = "/home/claude/receitech-social/banco-imagens/"
IMGS = {"CENOURA": "doce_bolocenoura_1.jpg", "RENA": "natal_bolorena_1.jpg"}
BLOBS = {"LOGOB": "/_blob/f2996fe4c9fb0951e6c5b11ec42e37da", "LOGOW": "/_blob/c900d55a8870af975f0e491905355cb1"}
bf = "/home/claude/receitech-social/gerador/posts/d1118_blobs.json"
if os.path.exists(bf):
    BLOBS.update(json.load(open(bf)))


def U(k):
    if MODE == "canvas":
        return BLOBS[k]
    if k == "LOGOB":
        return "file:///home/claude/receitech-social/gerador/posts/logo_dark.png"
    if k == "LOGOW":
        return "file:///home/claude/receitech-social/gerador/posts/logo_white.png"
    return "file://" + BANK + IMGS[k]


NAVY, CREAM, SKY, CREAMT = "#101828", "#F3EDE3", "#CFE2FF", "#FFF4D2"
POP = "font-family: 'Poppins', sans-serif"
HVY = "font-family: 'Inter Tight', 'Poppins', sans-serif"
CND = "font-family: 'Anton', 'Inter Tight', sans-serif"
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Libre+Caslon+Text:wght@400;700&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@800;900&family=Anton&display=swap"
ALT_CEN = "Bolo de cenoura com cobertura de chocolate, cortado"


def box(bg, inner):
    return f'<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {bg}; {POP}">{inner}</div>'


# ================= Post 1 · gás e energia no custo =================
P1_SUB = "No Receitech, ele entra no custo de cada receita automaticamente."


def p1_n2():
    """N2: texto enorme + sublinhado, fundo céu, foto simples embaixo à direita."""
    inner = f'''<div style="position: absolute; left: 30px; right: 26px; top: 76px; {HVY}; font-weight: 900; color: {NAVY}; font-size: 84px; line-height: 0.92; letter-spacing: -4px">o gás do <span style="text-decoration: underline; text-decoration-thickness: 7px; text-underline-offset: 8px">forno</span> também é custo 🔥</div>
<div style="position: absolute; left: 34px; top: 486px; width: 222px; font-size: 18px; font-weight: 600; line-height: 1.3; color: {NAVY}">{P1_SUB}</div>
<img src="{U("CENOURA")}" alt="{ALT_CEN}" style="position: absolute; right: 34px; top: 444px; width: 230px; height: 230px; object-fit: cover; object-position: 50% 50%">'''
    return box(SKY, inner)


def p1_n5():
    """N5: pôster com moldura azul, foto no meio."""
    inner = f'''<div style="position: absolute; left: 22px; right: 22px; top: 22px; bottom: 22px; border-radius: 28px; background: {BLUE}"></div>
<div style="position: absolute; left: 50px; top: 50px; {CND}; color: #FFFFFF; font-size: 50px; line-height: 1">GÁS</div>
<div style="position: absolute; left: 150px; right: 50px; top: 50px; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; color: {SKY}">RECEITECH MOSTRA</div>
<div style="position: absolute; left: 150px; right: 46px; top: 66px; {CND}; color: #FFFFFF; font-size: 31px; line-height: 1.02">O FORNO TAMBÉM ENTRA NO CUSTO DO BOLO</div>
<img src="{U("CENOURA")}" alt="{ALT_CEN}" style="position: absolute; left: 50px; right: 50px; top: 168px; width: 440px; height: 430px; object-fit: cover; object-position: 50% 50%; border-radius: 16px">
<div style="position: absolute; left: 0; right: 0; bottom: 56px; text-align: center; font-size: 15px; font-weight: 600; color: #FFFFFF">{P1_SUB}</div>'''
    return box("#FFFFFF", inner)


def custo_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    flame = svg('<path d="M12 3c1 3 4 4.5 4 8.5A4 4 0 0 1 8 12c0-1.5.6-2.6 1.4-3.4C9.6 10 10.5 11 11.5 11 11 8 11 5.5 12 3z"></path>', 18, "#B54708", 2)
    bolt = svg('<path d="M13 3L5 13h6l-1 8 8-10h-6z"></path>', 18, "#B54708", 2)

    def row(n, sub, v, icon=""):
        return (f'<div style="display: flex; align-items: center; justify-content: space-between; padding: 13px 0; border-bottom: 1px solid {DIV}">'
                f'<div style="display: flex; align-items: center; gap: 10px">{icon}<div style="display: flex; flex-direction: column; gap: 2px">'
                f'<span style="font-size: 16px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {SEC}">{sub}</span></div></div>'
                f'<span style="font-size: 16px; font-weight: 600; white-space: nowrap">R$ {v}</span></div>')

    def ic(svgh):
        return f'<span style="width: 34px; height: 34px; border-radius: 10px; background: #FFFAEB; display: flex; align-items: center; justify-content: center">{svgh}</span>'
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="height: 48px; display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; padding: 0 6px">
<div style="display: flex; justify-content: center">{back}</div><span style="text-align: center; font-size: 18px; font-weight: 700">Custo da receita</span><span></span></div>
<div style="padding: 14px 20px 0; display: flex; gap: 14px; align-items: center">
<img src="{U("CENOURA")}" alt="Bolo de cenoura" style="width: 64px; height: 64px; border-radius: 14px; object-fit: cover">
<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 22px; font-weight: 700; letter-spacing: -0.5px">Bolo de cenoura</span>
<span style="font-size: 14px; color: {SEC}">Rende 16 fatias</span></div></div>
<div style="padding: 10px 20px 0">
{row("Ingredientes", "9 ingredientes", "14,20")}
<div style="padding: 16px 0 2px; font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">GÁS E ENERGIA</div>
{row("Forno a gás", "40 minutos", "1,60", ic(flame))}
{row("Batedeira", "6 minutos", "0,05", ic(bolt))}
<div style="display: flex; justify-content: space-between; padding: 16px 0 6px; font-size: 17px; font-weight: 700"><span>Custo da receita</span><span>R$ 15,85</span></div>
<div style="margin-top: 10px; border-radius: 16px; background: {LBLUE}; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center">
<span style="font-size: 15px; font-weight: 500">Custo de 1 fatia</span><span style="font-size: 22px; font-weight: 700; color: {BLUE}">R$ 0,99</span></div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


def p1_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">Você diz quanto tempo vai no forno. O gás entra na conta sozinho.</div>
<div style="position: absolute; right: 44px; top: 176px">{phone(custo_screen(), 500)}</div>
<img src="{U("CENOURA")}" alt="Bolo de cenoura com cobertura de chocolate" style="position: absolute; left: 40px; top: 470px; width: 160px; height: 160px; object-fit: cover; border-radius: 12px">
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; left: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(CREAM, inner)


# ================= Post 2 · prazo de encomenda no cardápio =================
ITA = "font-family: 'Instrument Serif', Georgia, serif; font-style: italic"
ALT_RENA = "Bolo de Natal decorado com chantilly, árvore de Natal e rena"
P2_A = "Bolo de Natal pra amanhã?"
P2_B = "No cardápio do Receitech, cada produto mostra com quantos dias a cliente precisa encomendar."


def rena_bg():
    return (f'<img src="{U("RENA")}" alt="" style="position: absolute; left: -20px; top: -20px; width: 580px; height: 760px; object-fit: cover; filter: blur(18px)">'
            f'<img src="{U("RENA")}" alt="{ALT_RENA}" style="position: absolute; left: 0; top: 160px; width: 540px; height: 640px; object-fit: cover; object-position: 50% 0%; '
            f'-webkit-mask-image: linear-gradient(to bottom, transparent 0, #000 70px); mask-image: linear-gradient(to bottom, transparent 0, #000 70px)">')


def p2_t3():
    """T3: foto inteira + serifa itálica (texto no alto, sobre o fundo claro da foto)."""
    inner = f'''{rena_bg()}
<div style="position: absolute; left: 36px; right: 36px; top: 40px; text-align: center; {ITA}; color: {NAVY}; font-size: 52px; line-height: 1.0; letter-spacing: -0.5px">{P2_A}</div>
<div style="position: absolute; left: 60px; right: 60px; top: 160px; text-align: center; color: {NAVY}; font-size: 16px; font-weight: 600; line-height: 1.35">{P2_B}</div>'''
    return box("#EDEDF0", inner)


def p2_n6():
    """N6: caixa alta em bloco justificada, no alto da foto."""
    inner = f'''{rena_bg()}
<div style="position: absolute; left: 56px; right: 56px; top: 48px; text-align: justify; text-align-last: justify; font-weight: 700; color: {NAVY}; font-size: 40px; line-height: 1.02; word-spacing: 6px">BOLO DE NATAL PRA AMANHÃ?</div>
<div style="position: absolute; left: 56px; right: 56px; top: 138px; color: {NAVY}; font-size: 15px; font-weight: 600; line-height: 1.35">{P2_B}</div>'''
    return box("#EDEDF0", inner)


def cardapio_screen():
    close = svg('<path d="M6 6l12 12M18 6L6 18"></path>', 18, DARK, 2.4)
    cal = svg('<rect x="4" y="5" width="16" height="15" rx="3"></rect><path d="M4 10h16M9 3v4M15 3v4"></path>', 18, BLUE, 2)
    return f'''<div style="width: 390px; height: 844px; background: #98A2B3; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="position: absolute; left: 0; right: 0; top: 70px; bottom: 0; background: #FFFFFF; border-radius: 22px 22px 0 0; overflow: hidden">
<div style="position: relative"><img src="{U("RENA")}" alt="Bolo de Natal decorado" style="width: 390px; height: 300px; object-fit: cover; object-position: 50% 70%">
<span style="position: absolute; right: 14px; top: 14px; width: 36px; height: 36px; border-radius: 18px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{close}</span>
<span style="position: absolute; left: 14px; bottom: 14px; padding: 5px 12px; border-radius: 20px; background: #FFFFFF; font-size: 13px; font-weight: 600; color: {BLUE}">Encomenda</span></div>
<div style="padding: 18px 20px 0">
<div style="font-size: 22px; font-weight: 600; letter-spacing: -0.4px">Bolo de Natal rena</div>
<div style="margin-top: 6px; font-size: 14px; color: {SEC}; line-height: 1.4">Massa branca com recheio de brigadeiro branco e frutas vermelhas. 1,5 kg, serve 15 pessoas.</div>
<div style="margin-top: 14px; display: flex; align-items: center; gap: 10px; padding: 12px 14px; border-radius: 14px; background: {LBLUE}">{cal}<span style="font-size: 15px; font-weight: 500">Peça com <b style="font-weight: 700">3 dias</b> de antecedência</span></div>
<div style="margin-top: 18px; display: flex; align-items: center; justify-content: space-between">
<span style="font-size: 20px; font-weight: 600">R$ 180,00</span>
<div style="display: flex; align-items: center; gap: 16px; border: 1px solid {DIV}; border-radius: 12px; padding: 6px 14px; font-size: 18px; font-weight: 600"><span style="color: #98A2B3">−</span><span>1</span><span style="color: {BLUE}">+</span></div></div>
<div style="margin-top: 20px; height: 52px; border-radius: 14px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Adicionar · R$ 180,00</div>
</div></div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


def p2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: #FFFFFF; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">Você define o prazo de cada produto. A cliente vê antes de pedir.</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(cardapio_screen(), 500)}</div>
<img src="{U("LOGOW")}" alt="receitech" style="position: absolute; left: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(NAVY, inner)


SLIDES = [
    ("D18_P1_opA", "18/11 · P1 · tela 1 · 11h (N2)", p1_n2),
    ("D18_P1_opB", "Reserva · N5 azul (guardar pra usar depois)", p1_n5),
    ("D18_P1_S2", "18/11 · P1 · tela 2 (custo da receita)", p1_s2),
    ("D18_P2_opA", "18/11 · P2 · opção A (T3)", p2_t3),
    ("D18_P2_opB", "18/11 · P2 · opção B (N6)", p2_n6),
    ("D18_P2_S2", "18/11 · P2 · tela 2 (cardápio: prazo)", p2_s2),
]


def page_f(title, body, w, h):
    return page(title, body, w, h).replace(
        "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap", FONTS.replace("&", "&amp;"))


if __name__ == "__main__":
    only = sys.argv[3].split(",") if len(sys.argv) > 3 else None
    for code, title, fn in SLIDES:
        if only and code not in only:
            continue
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
