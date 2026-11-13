import json, os

ROOT = "/mnt/user-data/outputs/artifacts/8fbb8213-28ad-4781-b078-38258a667157/project"
BRIG = "/_blob/dec215cfbdbfd09ab202c7670b2cc7b6"
AVATAR = "/_blob/a81ef0a98b4093fac9d3dbb0aaf19b75"
MARK_W = "/_blob/bdeaa92c95f99e4db2eac302cfecb005"
MARK_B = "/_blob/67bc2f98bb3a9fe4041f403b2754fc6d"

BLUE = "#3D86F7"; DARK = "#101828"; SEC = "#475467"; GREEN = "#039855"
LBLUE = "#EBF5FF"; DIV = "#EAECF0"; ORANGE = "#F79009"

PW, PH = 540, 720  # post 3:4
FONT = "font-family: 'Poppins', sans-serif"


def brand_row(color, mark):
    return f'''<div style="display: flex; align-items: center; gap: 10px">
<img src="{mark}" alt="" style="width: 34px; height: 34px">
<span style="font-size: 22px; font-weight: 600; color: {color}; letter-spacing: -0.3px">Receitech</span>
</div>'''


# ---------- pinned posts ----------
def post_oque():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {BLUE}; box-sizing: border-box; padding: 44px 44px 0; {FONT}; display: flex; flex-direction: column; gap: 26px">
{brand_row("#FFFFFF", MARK_W)}
<h1 style="margin: 0; font-size: 46px; line-height: 1.08; font-weight: 700; color: #FFFFFF; letter-spacing: -1.2px">Você faz e vende doces, bolos e salgados?</h1>
<p style="margin: 0; font-size: 20px; line-height: 1.4; color: #FFFFFF; opacity: 0.9">O app mostra quanto custa, quanto cobrar e quanto sobra pra você.</p>
<div style="position: absolute; left: 44px; right: 44px; bottom: -36px; height: 300px; background: #FFFFFF; border-radius: 28px; box-sizing: border-box; padding: 26px 26px 0; display: flex; flex-direction: column; gap: 18px; box-shadow: 0 24px 48px rgba(16,24,40,0.25)">
<div style="display: flex; align-items: center; gap: 14px">
<img src="{BRIG}" alt="Brigadeiro gourmet" style="width: 56px; height: 56px; border-radius: 14px; object-fit: cover">
<div style="display: flex; flex-direction: column; gap: 2px">
<span style="font-size: 18px; font-weight: 600; color: {DARK}">Brigadeiro gourmet</span>
<span style="font-size: 13px; color: {SEC}">Doces · 1 brigadeiro</span>
</div>
</div>
<div style="display: flex; flex-direction: column; gap: 4px">
<span style="font-size: 13px; font-weight: 500; color: {SEC}">Preço</span>
<span style="font-size: 40px; font-weight: 700; color: {DARK}; letter-spacing: -1px">R$ 2,25</span>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; border-top: 1px solid {DIV}; padding-top: 14px">
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: {SEC}">Custo</span><span style="font-size: 18px; font-weight: 600; color: {DARK}">R$ 0,79</span></div>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: {SEC}">Lucro</span><span style="font-size: 18px; font-weight: 600; color: {GREEN}">R$ 1,46</span></div>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: {SEC}">Margem</span><span style="font-size: 18px; font-weight: 600; color: {DARK}">65%</span></div>
</div>
</div>
</div>'''


def post_lucro():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: #FFFFFF; box-sizing: border-box; padding: 44px; {FONT}; display: flex; flex-direction: column; gap: 22px">
{brand_row(DARK, MARK_B)}
<h1 style="margin: 0; font-size: 46px; line-height: 1.08; font-weight: 700; color: {DARK}; letter-spacing: -1.2px">Quanto sobrou pra você esse mês?</h1>
<p style="margin: 0; font-size: 20px; line-height: 1.4; color: {SEC}">Cada venda que você registra já mostra o lucro. Sem planilha.</p>
<div style="margin-top: auto; display: flex; flex-direction: column; gap: 18px; border-top: 1px solid {DIV}; padding-top: 26px">
<div style="display: flex; flex-direction: column; gap: 2px">
<span style="font-size: 15px; font-weight: 500; color: {SEC}">Lucro no mês</span>
<span style="font-size: 64px; font-weight: 700; color: {GREEN}; letter-spacing: -2px; line-height: 1.05">R$ 97,89</span>
<span style="font-size: 15px; color: {SEC}">67 brigadeiros vendidos</span>
</div>
<div style="display: flex; height: 18px; border-radius: 9px; overflow: hidden">
<div style="width: 35%; background: {ORANGE}"></div>
<div style="width: 65%; background: {GREEN}"></div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px">
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {SEC}">Vendido</span><span style="font-size: 19px; font-weight: 600; color: {DARK}">R$ 150,75</span></div>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {SEC}">Custo</span><span style="font-size: 19px; font-weight: 600; color: #B54708">R$ 52,86</span></div>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {SEC}">Lucro</span><span style="font-size: 19px; font-weight: 600; color: {GREEN}">R$ 97,89</span></div>
</div>
</div>
</div>'''


def step(n, title, text):
    return f'''<div style="display: flex; gap: 18px; align-items: flex-start">
<div style="flex: none; width: 52px; height: 52px; border-radius: 26px; background: {BLUE}; color: #FFFFFF; font-size: 24px; font-weight: 700; display: flex; align-items: center; justify-content: center">{n}</div>
<div style="display: flex; flex-direction: column; gap: 2px; padding-top: 2px">
<span style="font-size: 22px; font-weight: 600; color: {DARK}">{title}</span>
<span style="font-size: 17px; line-height: 1.35; color: {SEC}">{text}</span>
</div>
</div>'''


def post_comecar():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {LBLUE}; box-sizing: border-box; padding: 44px; {FONT}; display: flex; flex-direction: column; gap: 30px">
{brand_row(DARK, MARK_B)}
<h1 style="margin: 0; font-size: 46px; line-height: 1.08; font-weight: 700; color: {DARK}; letter-spacing: -1.2px">Como começar</h1>
<div style="display: flex; flex-direction: column; gap: 26px">
{step(1, "Tire foto da receita", "O app lê os ingredientes sozinho.")}
{step(2, "Veja custo e preço", "Quanto custa cada unidade e quanto cobrar.")}
{step(3, "Registre as vendas", "E veja quanto sobra pra você.")}
</div>
<div style="margin-top: auto; display: flex; flex-direction: column; align-items: flex-start; gap: 10px">
<div style="background: {BLUE}; color: #FFFFFF; font-size: 20px; font-weight: 600; padding: 16px 28px; border-radius: 999px">Comece grátis · link na bio</div>
<span style="font-size: 15px; color: {SEC}">App Store e Google Play</span>
</div>
</div>'''


# ---------- regular posts (grid only) ----------
def post_foto():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; {FONT}">
<img src="{BRIG}" alt="Brigadeiros" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 60%; background: linear-gradient(rgba(16,24,40,0), rgba(16,24,40,0.85))"></div>
<div style="position: absolute; left: 44px; right: 44px; bottom: 48px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 44px; font-weight: 700; line-height: 1.1; color: #FFFFFF; letter-spacing: -1px">Esse brigadeiro custa R$ 0,79.</span>
<span style="font-size: 26px; font-weight: 500; color: #FFFFFF">Quanto você cobra?</span>
</div>
</div>'''


def post_serie(n, nome, dark_bg):
    bg = BLUE if dark_bg else "#FFFFFF"
    c1 = "#FFFFFF" if dark_bg else BLUE
    c2 = "#FFFFFF" if dark_bg else DARK
    c3 = "rgba(255,255,255,0.85)" if dark_bg else SEC
    mark = MARK_W if dark_bg else MARK_B
    border = "" if dark_bg else f"border: 1px solid {DIV};"
    return f'''<div style="width: {PW}px; height: {PH}px; overflow: hidden; background: {bg}; {border} box-sizing: border-box; padding: 44px; {FONT}; display: flex; flex-direction: column; justify-content: space-between">
{brand_row(c2, mark)}
<div style="display: flex; flex-direction: column; gap: 8px">
<span style="font-size: 96px; font-weight: 700; color: {c1}; letter-spacing: -3px; line-height: 1">{n} de 100</span>
<span style="font-size: 44px; font-weight: 600; color: {c2}; letter-spacing: -1px; line-height: 1.1">{nome}</span>
</div>
<span style="font-size: 18px; color: {c3}">Tudo que o app faz, um por vídeo.</span>
</div>'''


def post_texto(frase, apoio, bg, c_frase, c_apoio):
    return f'''<div style="width: {PW}px; height: {PH}px; overflow: hidden; background: {bg}; box-sizing: border-box; padding: 52px 44px; {FONT}; display: flex; flex-direction: column; justify-content: center; gap: 20px">
<span style="font-size: 46px; font-weight: 700; line-height: 1.12; color: {c_frase}; letter-spacing: -1.2px">{frase}</span>
<span style="font-size: 20px; line-height: 1.4; color: {c_apoio}">{apoio}</span>
</div>'''


PINNED = [post_oque(), post_lucro(), post_comecar()]
LUCRO_POST = PINNED[1]


# ---------- full phone post ----------
def channel_card(title, bg, price, profit, margin, fee=None, cost="0,79"):
    fee_html = ""
    if fee:
        fee_html = f"""<div style="display: flex; flex-direction: column; margin-top: 14px">
<span style="font-size: 13px; color: #B42318">Taxa do aplicativo</span>
<span style="font-size: 22px; font-weight: 500; color: #B42318">{fee[0]} <span style="font-size: 14px">({fee[1]})</span></span>
</div>"""
    chev = svg('<path d="M9 6l6 6-6 6"></path>', 24, SEC, 2.4)
    return f"""<div style="background: {bg}; border-radius: 18px; padding: 12px 14px 16px 18px; display: flex; flex-direction: column">
<div style="display: flex; align-items: center; justify-content: space-between">
<span style="font-size: 13px; font-weight: 800; letter-spacing: 0.6px; color: #373F47">{title}</span>{chev}
</div>
<span style="margin-top: 2px; font-size: 13px; font-weight: 500; color: #707070">Preço por produto</span>
<span style="margin-top: 2px; color: #373F47; line-height: 1.1"><span style="font-size: 30px; font-weight: 600; opacity: 0.9">R$ </span><span style="font-size: 40px; font-weight: 800">{price}</span></span>
<div style="margin-top: 12px; display: grid; grid-template-columns: 1fr 1fr 1fr">
<div style="display: flex; flex-direction: column"><span style="font-size: 13px; color: #707070">Custo</span><span style="font-size: 22px; font-weight: 500; color: #373F47">R$ {cost}</span></div>
<div style="display: flex; flex-direction: column"><span style="font-size: 13px; color: #707070">Lucro</span><span style="font-size: 22px; font-weight: 500; color: #373F47">R$ {profit}</span></div>
<div style="display: flex; flex-direction: column"><span style="font-size: 13px; color: #707070">Margem</span><span style="font-size: 22px; font-weight: 500; color: #373F47">{margin}</span></div>
</div>
{fee_html}
</div>"""


def product_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    share = svg('<path d="M12 3v12M7 8l5-5 5 5"></path><path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"></path>', 22, DARK, 2)
    t_edit = svg('<path d="M4 6h10M4 11h10M4 16h6"></path><path d="M14 18l6-6-2-2-6 6v2z"></path>', 18, SEC, 2)
    t_ficha = svg('<path d="M7 3h7l5 5v13H7z"></path><path d="M14 3v5h5M10 13h6M10 17h6"></path>', 18, BLUE, 2)
    t_sim = svg('<path d="M3 17l6-6 4 4 8-8"></path><path d="M15 7h6v6"></path>', 18, SEC, 2)
    bakery = svg('<path d="M4 15c0-4 3.5-7 8-7s8 3 8 7z"></path><path d="M3 15h18v3H3z"></path>', 13, "#3C4043", 2)
    return f"""<div style="width: 390px; height: 844px; background: #FFFFFF; {FONT}; color: {DARK}; overflow: hidden; display: flex; flex-direction: column">
<div style="height: 54px"></div>
<div style="height: 48px; display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; padding: 0 6px">
<div style="display: flex; justify-content: center">{back}</div>
<span style="text-align: center; font-size: 18px; font-weight: 700">Produto</span>
<div style="display: flex; justify-content: center">{share}</div>
</div>
<div style="height: 48px; display: grid; grid-template-columns: 1fr 1fr 1fr; border-bottom: 1px solid {DIV}">
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px">{t_edit}<span style="font-size: 10px; font-weight: 600; letter-spacing: 0.2px; color: {SEC}">EDITAR</span></div>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; position: relative">{t_ficha}<span style="font-size: 10px; font-weight: 700; letter-spacing: 0.2px; color: {BLUE}">FICHA</span><div style="position: absolute; bottom: -1px; width: 44px; height: 2px; background: {BLUE}"></div></div>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px">{t_sim}<span style="font-size: 10px; font-weight: 600; letter-spacing: 0.2px; color: {SEC}">SIMULAÇÃO</span></div>
</div>
<div style="padding: 18px 20px 0; display: flex; flex-direction: column">
<div style="display: flex; gap: 14px; align-items: center">
<img src="{BRIG}" alt="Brigadeiro gourmet" style="width: 76px; height: 76px; border-radius: 16px; object-fit: cover">
<div style="display: flex; flex-direction: column; gap: 6px">
<div style="display: flex; gap: 8px">
<span style="display: flex; align-items: center; gap: 5px; background: #F1F3F4; color: #3C4043; font-size: 11px; font-weight: 600; padding: 4px 9px; border-radius: 20px">{bakery}Preparado</span>
<span style="background: #F0EBFB; color: #7F56D9; font-size: 11px; font-weight: 600; padding: 4px 9px; border-radius: 20px">Doces</span>
</div>
<span style="font-size: 25px; font-weight: 700; letter-spacing: -0.8px; line-height: 1.15">Brigadeiro gourmet</span>
</div>
</div>
<div style="margin-top: 22px; display: flex; flex-direction: column; gap: 18px">
{channel_card("DIRETA", "#EBF4FF", "2,25", "1,46", "65%")}
{channel_card("IFOOD", "#F0F0F0", "3,20", "1,45", "45%", ("R$ 0,96", "30%"))}
</div>
</div>
<div style="margin-top: auto; height: 30px; display: flex; align-items: center; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>"""


def phone(screen_html, frame_h):
    inner_h = frame_h - 20
    sc = inner_h / 844
    inner_w = 390 * sc
    frame_w = inner_w + 20
    return f"""<div style="position: relative; width: {frame_w:.1f}px; height: {frame_h}px; border-radius: {46*frame_h/600:.1f}px; background: #0B0F19; box-sizing: border-box; padding: 10px; box-shadow: 0 30px 60px rgba(16,24,40,0.35)">
<div style="width: {inner_w:.1f}px; height: {inner_h}px; border-radius: {38*frame_h/600:.1f}px; overflow: hidden; position: relative; background: #FFFFFF">
<div style="width: 390px; height: 844px; transform: scale({sc:.5f}); transform-origin: 0 0">
{screen_html}
</div>
<div style="position: absolute; top: {10*sc/0.66:.1f}px; left: 50%; margin-left: {-60*sc:.1f}px; width: {120*sc:.1f}px; height: {34*sc:.1f}px; border-radius: 20px; background: #0B0F19"></div>
</div>
</div>"""


def post_celular():
    return f"""<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {BLUE}; box-sizing: border-box; padding: 36px 40px 0; {FONT}; display: flex; flex-direction: column; align-items: center; gap: 22px">
<h1 style="margin: 0; align-self: stretch; text-align: center; font-size: 34px; line-height: 1.12; font-weight: 700; color: #FFFFFF; letter-spacing: -1px">Quanto cobrar no iFood sem perder lucro?</h1>
<div style="position: relative">
{phone(product_screen(), 560)}
<div style="position: absolute; right: -78px; bottom: 96px; background: #FFFFFF; border-radius: 14px; padding: 10px 14px; box-shadow: 0 12px 28px rgba(16,24,40,0.28); display: flex; flex-direction: column">
<span style="font-size: 12px; color: {SEC}">Taxa de 30%</span>
<span style="font-size: 15px; font-weight: 700; color: {DARK}">já na conta</span>
</div>
</div>
</div>"""




REGULAR = [
    post_serie(3, "Encomendas", False),
    post_foto(),
    post_texto("Lucro não é o que vai pro seu bolso.", "Uma parte fica no negócio. O app mostra quanto dá pra tirar.", "#ECFDF3", DARK, SEC),
    post_serie(2, "Controle de estoque", True),
    post_texto("Mudou um preço e lá vai refazer o cardápio no Canva?", "Com o cardápio online do app, você muda o preço uma vez e pronto.", "#F9FAFB", DARK, SEC),
    post_serie(1, "Cardápio online", False),
]

# ---------- icons ----------
def svg(path, size=24, color=DARK, sw=2, label=None):
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg {aria} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

I_CHEV = '<path d="M6 9l6 6 6-6"></path>'
I_PLUS = '<rect x="3" y="3" width="18" height="18" rx="5"></rect><path d="M12 8v8M8 12h8"></path>'
I_MENU = '<path d="M4 7h16M4 12h16M4 17h16"></path>'
I_LINK = '<path d="M10 14a4 4 0 0 0 5.66 0l3-3a4 4 0 0 0-5.66-5.66l-1 1"></path><path d="M14 10a4 4 0 0 0-5.66 0l-3 3a4 4 0 0 0 5.66 5.66l1-1"></path>'
I_ADDP = '<circle cx="9" cy="8" r="4"></circle><path d="M2 21c0-4 3-6 7-6s7 2 7 6"></path><path d="M19 8v6M16 11h6"></path>'
I_GRID = '<rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M9 3v18M15 3v18M3 9h18M3 15h18"></path>'
I_REEL = '<rect x="3" y="3" width="18" height="18" rx="5"></rect><path d="M3 8h18M8 3l3 5M14 3l3 5"></path><path d="M10 11.5v5l4.5-2.5z"></path>'
I_TAG = '<rect x="3" y="3" width="18" height="18" rx="4"></rect><circle cx="12" cy="10" r="3"></circle><path d="M6.5 19c1-2.5 3-3.5 5.5-3.5s4.5 1 5.5 3.5"></path>'
I_PIN = '<path d="M9 3h6l-1 6 3 3v2H7v-2l3-3z"></path><path d="M12 14v7"></path>'
HL = [
    ("Começar", '<path d="M8 5v14l11-7z"></path>'),
    ("Preço", '<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"></path><circle cx="8" cy="8" r="1.5"></circle>'),
    ("Cardápio", '<path d="M5 3h14v18H5z"></path><path d="M9 8h6M9 12h6M9 16h4"></path>'),
    ("Lucro", '<path d="M3 17l6-6 4 4 8-8"></path><path d="M15 7h6v6"></path>'),
    ("Dúvidas", '<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14"></path><path d="M12 17.5v.01"></path>'),
]

HEAD = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#00376B}}a:hover{{color:#002850}}
</style>
</helmet>
'''
TAIL = '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''


def page(title, body, w, h):
    return HEAD.format(title=title) + body + TAIL.format(w=w, h=h)


TILE_W = (390 - 4) / 3
SCALE = TILE_W / PW
TILE_H = PH * SCALE


def tile(inner, pinned):
    pin = ""
    if pinned:
        pin = f'<div style="position: absolute; top: 6px; right: 6px; filter: drop-shadow(0 1px 2px rgba(0,0,0,0.5))">{svg(I_PIN, 16, "#FFFFFF", 2, "Fixado")}</div>'
    return f'''<div style="position: relative; width: {TILE_W:.3f}px; height: {TILE_H:.3f}px; overflow: hidden; background: #F2F4F7">
<div style="width: {PW}px; height: {PH}px; transform: scale({SCALE:.5f}); transform-origin: 0 0">
{inner}
</div>
{pin}
</div>'''


def profile():
    tiles = "\n".join([tile(p, True) for p in PINNED] + [tile(p, False) for p in REGULAR])
    hls = "\n".join(f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 6px; width: 66px">
<div style="width: 64px; height: 64px; border-radius: 32px; border: 1px solid #DBDBDB; box-sizing: border-box; padding: 3px">
<div style="width: 100%; height: 100%; border-radius: 50%; background: {LBLUE}; display: flex; align-items: center; justify-content: center">{svg(p, 24, BLUE, 2)}</div>
</div>
<span style="font-size: 12px; color: {DARK}">{n}</span>
</div>''' for n, p in HL)
    body = f'''<div style="width: 390px; height: 1080px; background: #FFFFFF; {FONT}; color: {DARK}; overflow: hidden">
<div style="height: 52px; box-sizing: border-box; padding: 0 16px; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 4px"><span style="font-size: 20px; font-weight: 700">receitech</span>{svg(I_CHEV, 18, DARK, 2.2)}</div>
<div style="display: flex; align-items: center; gap: 20px">{svg(I_PLUS, 24, DARK, 1.8, "Criar")}{svg(I_MENU, 24, DARK, 1.8, "Menu")}</div>
</div>
<div style="padding: 6px 16px 0; display: flex; align-items: center; gap: 22px">
<img src="{AVATAR}" alt="Logo do Receitech" style="width: 86px; height: 86px; border-radius: 43px; border: 1px solid {DIV}">
<div style="display: flex; flex-direction: column; gap: 8px; flex: 1">
<span style="font-size: 15px; font-weight: 600">Receitech</span>
<div style="display: flex; gap: 28px">
<div style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600">9</span><span style="font-size: 13px">posts</span></div>
<div style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600">—</span><span style="font-size: 13px">seguidores</span></div>
<div style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600">—</span><span style="font-size: 13px">seguindo</span></div>
</div>
</div>
</div>
<div style="padding: 12px 16px 0; display: flex; flex-direction: column; gap: 3px; font-size: 14px; line-height: 1.4">
<span style="color: #737373; font-size: 13px">Aplicativo</span>
<span>App pra quem faz e vende doces, bolos e salgados por conta própria.</span>
<span>Preço, encomendas, estoque e quanto sobra pro seu bolso.</span>
<a href="https://receitech.com" style="display: flex; align-items: center; gap: 6px; font-weight: 600; text-decoration: none">{svg(I_LINK, 15, "#00376B", 2.2)}<span>receitech.com</span></a>
</div>
<div style="padding: 14px 16px 0; display: flex; gap: 6px">
<button style="flex: 1; height: 34px; border: 0; border-radius: 8px; background: {BLUE}; color: #FFFFFF; font: 600 14px 'Poppins', sans-serif">Seguir</button>
<button style="flex: 1; height: 34px; border: 0; border-radius: 8px; background: #EFEFEF; color: {DARK}; font: 600 14px 'Poppins', sans-serif">Mensagem</button>
<button aria-label="Sugestões de contas" style="width: 34px; height: 34px; border: 0; border-radius: 8px; background: #EFEFEF; display: flex; align-items: center; justify-content: center">{svg(I_ADDP, 16, DARK, 2)}</button>
</div>
<div style="padding: 18px 12px 0; display: flex; gap: 10px">
{hls}
</div>
<div style="margin-top: 16px; display: grid; grid-template-columns: 1fr 1fr 1fr; border-top: 1px solid {DIV}">
<div style="height: 44px; display: flex; align-items: center; justify-content: center; border-bottom: 1.5px solid {DARK}">{svg(I_GRID, 22, DARK, 1.8, "Posts")}</div>
<div style="height: 44px; display: flex; align-items: center; justify-content: center">{svg(I_REEL, 22, "#737373", 1.8, "Reels")}</div>
<div style="height: 44px; display: flex; align-items: center; justify-content: center">{svg(I_TAG, 22, "#737373", 1.8, "Marcados")}</div>
</div>
<div style="display: grid; grid-template-columns: repeat(3, {TILE_W:.3f}px); gap: 2px">
{tiles}
</div>
</div>'''
    return page("IG1 Perfil", body, 390, 1080)


def post_page(title, inner):
    return page(title, inner, PW, PH)


PINNED = [PINNED[0], post_celular(), PINNED[2]]

files = {
    "Main.dc.html": profile(),
    "IG2_Fixado1.dc.html": post_page("IG2 Fixado 1 · O que é", PINNED[0]),
    "IG3_Fixado2.dc.html": post_page("IG3 Fixado 2 · Lucro", LUCRO_POST),
    "IG5_Fixado_celular.dc.html": post_page("IG5 Fixado 2 (nova) · Preço direta x iFood", PINNED[1]),
    "IG4_Fixado3.dc.html": post_page("IG4 Fixado 3 · Como começar", PINNED[2]),
}
for k, v in files.items():
    with open(os.path.join(ROOT, k), "w") as f:
        f.write(v)

x0 = 470
boards = {
    "Main.dc.html": {"x": 0, "y": 0, "w": 390, "h": 1080, "title": "IG1 Perfil no Instagram"},
    "IG2_Fixado1.dc.html": {"x": x0, "y": 0, "w": PW, "h": PH, "title": "IG2 Fixado 1 · O que é"},
    "IG3_Fixado2.dc.html": {"x": x0 + PW + 80, "y": 0, "w": PW, "h": PH, "title": "IG3 Fixado 2 · Lucro"},
    "IG4_Fixado3.dc.html": {"x": x0 + 2 * (PW + 80), "y": 0, "w": PW, "h": PH, "title": "IG4 Fixado 3 · Como começar"},
    "IG5_Fixado_celular.dc.html": {"x": x0, "y": PH + 160, "w": PW, "h": PH, "title": "IG5 Fixado 2 (nova) · Preço direta x iFood"},
}
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-11-06T16:10:00Z"},
          "title": "Instagram do Receitech — perfil com fixados",
          "launch": {"view": "canvas"}, "pages": [], "boards": boards,
          "order": list(boards.keys()), "notes": {}, "designSystems": []}
with open(os.path.join(ROOT, "canvas.json"), "w") as f:
    json.dump(canvas, f, ensure_ascii=False, indent=1)
print("ok", SCALE, TILE_H)
