"""Posts de 13/11/2026: C1 calendário, F1 pra resolver, C2 cento de docinhos, F2 gastos, C3 perdas.
Uso: python3 d1113.py local|canvas  (local = prévias com arquivos; canvas = .dc.html com /_blob/)"""
import json, os, sys
exec(open('/home/claude/receitech-social/gerador/assets/gen.py').read().split("files = {")[0])

MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1113"
os.makedirs(OUT, exist_ok=True)
BANK = "/home/claude/receitech-social/banco-imagens/"
IMGS = {
    "PAN": "natal_panetone_1.jpg", "EMP": "salg_empada_2.jpg", "TOR": "doce_torta_2.jpg",
    "BOLO": "doce_bolo_2.jpg", "BRIG": "doce_brig_1.jpg", "COX": "salg_coxinha_1.jpg",
    "POTE": "doce_bolopote_2.jpg",
}
LOGOS = {"LOGOB": "/home/claude/receitech-social/gerador/posts/logo_dark.png",
         "LOGOW": "/home/claude/receitech-social/gerador/posts/logo_white.png"}
BLOBS = {"LOGOB": "/_blob/f2996fe4c9fb0951e6c5b11ec42e37da", "LOGOW": "/_blob/c900d55a8870af975f0e491905355cb1"}
bf = os.path.join(OUT, "blobs.json")
if os.path.exists(bf):
    BLOBS.update(json.load(open(bf)))


def U(k):
    if MODE == "canvas":
        return BLOBS[k]
    return "file://" + (LOGOS[k] if k in LOGOS else BANK + IMGS[k])


NAVY, CREAM, SKY, RED = "#101828", "#F3EDE3", "#CFE2FF", "#D92D20"
POP = "font-family: 'Poppins', sans-serif"
SER = "font-family: 'Libre Caslon Text', Georgia, serif"
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Libre+Caslon+Text:wght@400;700&display=swap"


def chev(color, size):
    return (f'<svg width="{size*0.62:.0f}" height="{size}" viewBox="0 0 14 22" aria-hidden="true" style="display: inline-block; vertical-align: -0.12em; margin-left: 0.18em">'
            f'<path d="M3 2l9 9-9 9" fill="none" stroke="{color}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"></path></svg>')


def box(bg, inner):
    return f'<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {bg}; {POP}">{inner}</div>'


def status_bar():
    return '<div style="height: 54px"></div>'


def home_ind():
    return f'<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>'


def thumb(k, size=48, r=12):
    if k is None:
        cake = svg('<path d="M4 20h16M5 20v-7h14v7M8 13V9M12 13V9M16 13V9"></path>', 22, "#98A2B3", 1.8)
        return f'<div style="flex: none; width: {size}px; height: {size}px; border-radius: {r}px; background: #F2F4F7; display: flex; align-items: center; justify-content: center">{cake}</div>'
    return f'<img src="{U(k)}" alt="" style="flex: none; width: {size}px; height: {size}px; border-radius: {r}px; object-fit: cover">'


def chip(t, bg="#F2F4F7", fg=SEC):
    return f'<span style="background: {bg}; color: {fg}; font-size: 11px; font-weight: 600; padding: 3px 9px; border-radius: 20px">{t}</span>'


def delivery_card(k, hora, cliente, item, tipo):
    return f'''<div style="display: flex; gap: 12px; align-items: center; padding: 10px 0; border-bottom: 1px solid {DIV}">
{thumb(k)}
<div style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 600">{hora} · {cliente}</span><span style="font-size: 13px; color: {SEC}">{item}</span></div>
{chip(tipo)}</div>'''


# ---------------- C1 ----------------
def c1_s1():
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 60px; text-align: center; font-size: 12px; font-weight: 600; letter-spacing: 4px; color: {BLUE}">RECEITECH</div>
<div style="position: absolute; left: 44px; right: 44px; top: 128px; display: flex; flex-direction: column; align-items: center; gap: 26px; text-align: center; {SER}; color: {NAVY}; font-size: 31px; line-height: 1.24; letter-spacing: -0.5px">
<span>Dezembro tem um dia que dá prejuízo pra quem vende encomenda.</span>
<span>E ele está chegando{chev(NAVY, 30)}</span>
</div>
<img src="{U("PAN")}" alt="Panetone trufado" style="position: absolute; left: 135px; top: 446px; width: 270px; height: 200px; object-fit: cover; border-radius: 12px">'''
    return box(CREAM, inner)


def cal_screen():
    # dezembro 2026: dia 1 = terça. Grade começa no domingo.
    ev = {5: ["Bolo Lia"], 8: ["Torta Bia"], 11: ["Cento Rosa"], 12: ["Bolo Ana", "Kit festa"],
          17: ["Panetone"], 18: ["Bolo Mel", "Cento Iara"], 19: ["Panetone", "Torta Gil", "Kit Natal"],
          20: ["Rabanada"], 21: ["Panetone", "Bolo Edu", "Cento", "Torta"], 22: ["Panetone", "Kit Natal", "Bolo Cris", "Cento", "Torta"],
          23: ["Panetone", "Empadas", "Torta Rita", "Bolo Nina", "Cento"], 24: ["Panetone", "Bolo Teo", "Kit Natal", "Torta"],
          30: ["Bolo Bia"]}
    days = [(29, False), (30, False)] + [(d, True) for d in range(1, 32)] + [(d, False) for d in (1, 2)]
    cells = ""
    for d, cur in days:
        evs = ev.get(d, []) if cur else []
        sel = cur and d == 23
        num_style = (f"background: {BLUE}; color: #FFFFFF;" if sel else (f"color: {DARK};" if cur else "color: #C0C5CF;"))
        chips = "".join(f'<div style="font-size: 8.5px; line-height: 1; padding: 2px 3px; margin-top: 2px; border-radius: 3px; background: {LBLUE}; color: #1D4ED8; white-space: nowrap; overflow: hidden">{e}</div>' for e in evs[:4])
        cells += f'''<div style="height: 82px; border-top: 1px solid {DIV}; padding: 3px 2px 0; box-sizing: border-box; overflow: hidden; display: flex; flex-direction: column">
<span style="align-self: center; width: 20px; height: 20px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 600; {num_style}">{d}</span>{chips}</div>'''
    wk = "".join(f'<span style="text-align: center; font-size: 11px; font-weight: 600; color: {SEC}">{x}</span>' for x in "DSTQQSS")
    left = svg('<path d="M15 5l-7 7 7 7"></path>', 18, DARK, 2.4)
    right = svg('<path d="M9 5l7 7-7 7"></path>', 18, DARK, 2.4)
    close = svg('<path d="M6 6l12 12M18 6L6 18"></path>', 20, DARK, 2.2)
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
{status_bar()}
<div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 18px 0"><span style="font-size: 20px; font-weight: 700">Calendário</span>{close}</div>
<div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 18px 10px">{left}<div style="display: flex; flex-direction: column; align-items: center"><span style="font-size: 14px; font-weight: 600">Dezembro 2026</span></div>{right}</div>
<div style="display: grid; grid-template-columns: repeat(7, 1fr); padding: 0 8px 6px">{wk}</div>
<div style="display: grid; grid-template-columns: repeat(7, 1fr); padding: 0 8px">{cells}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 300px; background: #FFFFFF; border-radius: 22px 22px 0 0; box-shadow: 0 -10px 30px rgba(16,24,40,0.16); padding: 10px 20px 0; box-sizing: border-box">
<div style="width: 40px; height: 4px; border-radius: 2px; background: #D0D5DD; margin: 0 auto 12px"></div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 16px; font-weight: 700">Quarta, 23 de dezembro</span>{chip("9 ENTREGAS", LBLUE, BLUE)}</div>
{delivery_card("PAN", "9h", "Ana", "Panetone trufado 500 g", "Retirada")}
{delivery_card("EMP", "10h30", "Carla", "50 empadinhas", "Delivery")}
{delivery_card("TOR", "11h", "Rita", "Torta de limão", "Retirada")}
</div>
</div>'''


def c1_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 54px; color: {NAVY}; font-size: 30px; font-weight: 600; line-height: 1.18; letter-spacing: -0.8px">Olha o calendário do app como fica.</div>
<div style="position: absolute; left: 92px; top: 172px">{phone(cal_screen(), 600)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 30px; bottom: 26px; height: 22px; width: auto">'''
    return box("#FFFFFF", inner)


# ---------------- F1 ----------------
def rotina_screen():
    nav = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == "Rotina" else 500}; color: {BLUE if n == "Rotina" else SEC}">{n}</span>' for n in ["Rotina", "Vendas", "Lucro", "Produtos", "Perfil"])
    arrow = svg('<path d="M5 12h14M13 6l6 6-6 6"></path>', 15, BLUE, 2.4)
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
{status_bar()}
<div style="padding: 4px 20px 0"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.5px">Minha rotina</span></div>
<div style="padding: 20px 20px 0">
<span style="font-size: 18px; font-weight: 600">Pra resolver</span>
<div style="margin-top: 12px; border: 1px solid {DIV}; border-radius: 16px; padding: 14px">
<div style="display: flex; gap: 12px; align-items: center">{thumb("BOLO", 52)}<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Você entregou o bolo da Ana?</span><span style="font-size: 12px; color: {SEC}">Entrega marcada pra sábado, 12 de dezembro, 15h</span></div></div>
<div style="margin-top: 14px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px">
<span style="height: 42px; border-radius: 12px; background: {BLUE}; color: #FFFFFF; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center">Entreguei</span>
<span style="height: 42px; border-radius: 12px; border: 1px solid #D0D5DD; color: {DARK}; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center">Mudar a data</span>
</div></div></div>
<div style="padding: 32px 20px 0">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 18px; font-weight: 600">Entregas</span><span style="display: flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 600; color: {BLUE}">Ver calendário {arrow}</span></div>
<div style="display: flex; align-items: center; gap: 8px; margin-top: 6px"><span style="font-size: 13px; color: {SEC}">Hoje</span>{chip("2 ENTREGAS", LBLUE, BLUE)}</div>
<div style="margin-top: 6px">
{delivery_card(None, "14h", "Camila", "Torta de frango", "Retirada")}
{delivery_card(None, "17h", "Joana", "20 brigadeiros", "Delivery")}
</div></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; border-top: 1px solid {DIV}; background: #FFFFFF; display: flex; justify-content: space-around; align-items: flex-start; padding-top: 14px; box-sizing: border-box">{nav}</div>
{home_ind()}
</div>'''


def f1():
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 50px; text-align: center; color: {NAVY}; font-size: 32px; font-weight: 600; line-height: 1.16; letter-spacing: -0.9px">Nenhuma encomenda de Natal fica esquecida. 🎄</div>
<img src="{U("BOLO")}" alt="Bolo de morango" style="position: absolute; left: 30px; top: 330px; width: 190px; height: 190px; object-fit: cover; border-radius: 14px">
<div style="position: absolute; left: 236px; top: 196px">{phone(rotina_screen(), 560)}</div>'''
    return box(SKY, inner)


# ---------------- C2 ----------------
def c2_s1():
    inner = f'''<div style="position: absolute; left: 44px; right: 60px; top: 66px; color: #FFFFFF; font-size: 33px; font-weight: 600; line-height: 1.18; letter-spacing: -1px">Antes de montar o próximo cento de docinhos, veja isso{chev("#FFFFFF", 31)}</div>
<img src="{U("BRIG")}" alt="Brigadeiros e beijinhos na caixa" style="position: absolute; left: 44px; right: 44px; top: 330px; width: 452px; height: 300px; object-fit: cover; border-radius: 16px">'''
    return box(NAVY, inner)


def cost_line(name, sub, val, bold=False, top=False):
    bt = f"border-top: 1px solid {DIV}; margin-top: 4px;" if top else ""
    return f'''<div style="display: flex; justify-content: space-between; align-items: center; padding: 7px 0; {bt}">
<div style="display: flex; flex-direction: column"><span style="font-size: 14px; font-weight: {600 if bold else 500}">{name}</span>{f'<span style="font-size: 12px; color: {SEC}">{sub}</span>' if sub else ''}</div>
<span style="font-size: 14px; font-weight: {700 if bold else 500}">{val}</span></div>'''


def cento_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    share = svg('<path d="M12 3v12M7 8l5-5 5 5"></path><path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"></path>', 22, DARK, 2)
    t_edit = svg('<path d="M4 6h10M4 11h10M4 16h6"></path><path d="M14 18l6-6-2-2-6 6v2z"></path>', 18, SEC, 2)
    t_ficha = svg('<path d="M7 3h7l5 5v13H7z"></path><path d="M14 3v5h5M10 13h6M10 17h6"></path>', 18, BLUE, 2)
    t_sim = svg('<path d="M3 17l6-6 4 4 8-8"></path><path d="M15 7h6v6"></path>', 18, SEC, 2)
    card = channel_card("DIRETA", "#EBF4FF", "172,00", "111,80", "65%", None, "60,20")
    return f"""<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; display: flex; flex-direction: column; position: relative">
{status_bar()}
<div style="height: 48px; display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; padding: 0 6px">
<div style="display: flex; justify-content: center">{back}</div><span style="text-align: center; font-size: 18px; font-weight: 700">Produto</span><div style="display: flex; justify-content: center">{share}</div></div>
<div style="height: 48px; display: grid; grid-template-columns: 1fr 1fr 1fr; border-bottom: 1px solid {DIV}">
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px">{t_edit}<span style="font-size: 10px; font-weight: 600; color: {SEC}">EDITAR</span></div>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; position: relative">{t_ficha}<span style="font-size: 10px; font-weight: 700; color: {BLUE}">FICHA</span><div style="position: absolute; bottom: -1px; width: 44px; height: 2px; background: {BLUE}"></div></div>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px">{t_sim}<span style="font-size: 10px; font-weight: 600; color: {SEC}">SIMULAÇÃO</span></div></div>
<div style="padding: 16px 20px 0">
<div style="display: flex; gap: 14px; align-items: center">{thumb("BRIG", 68, 16)}<div style="display: flex; flex-direction: column; gap: 6px">
<div style="display: flex; gap: 8px">{chip("Preparado", "#F1F3F4", "#3C4043")}{chip("Doces", "#F0EBFB", "#7F56D9")}</div>
<span style="font-size: 23px; font-weight: 700; letter-spacing: -0.7px; line-height: 1.15">Cento de docinhos</span></div></div>
<div style="margin-top: 12px">{card}</div>
<div style="margin-top: 14px; font-size: 15px; font-weight: 700">Custo do produto</div>
<div style="margin-top: 2px">
{cost_line("Brigadeiro", "Receita · 50 un.", "R$ 24,30")}
{cost_line("Beijinho", "Receita · 50 un.", "R$ 23,50")}
<div style="background: #FFF6E5; border-radius: 10px; padding: 0 10px; margin: 2px -10px">
{cost_line("Forminhas nº 4", "Embalagem · 100 un.", "R$ 6,50")}
{cost_line("Caixa para cento", "Embalagem · 1 un.", "R$ 5,90")}
</div>
{cost_line("Custo total", "", "R$ 60,20", True, True)}
</div></div>
{home_ind()}
</div>"""


def c2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 44px; right: 80px; display: flex; flex-direction: column; gap: 8px">
<span style="color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px">Só as forminhas e a caixa custam R$ 12,40.</span>
<span style="color: {SEC}; font-size: 16px; line-height: 1.4">O Receitech põe a embalagem no custo e sugere o preço do cento.</span></div>
<div style="position: absolute; left: 92px; top: 196px">{phone(cento_screen(), 600)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 30px; top: 30px; height: 20px; width: auto">'''
    return box(LBLUE, inner)


# ---------------- F2 ----------------
def gasto_row(name, freq, val, pend=False):
    v = f'<span style="font-size: 14px; font-weight: 600; color: {BLUE}">Informar valor</span>' if pend else f'<span style="font-size: 14px; font-weight: 600">{val}</span>'
    return f'''<div style="display: flex; justify-content: space-between; align-items: center; padding: 13px 0; border-bottom: 1px solid {DIV}">
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 500">{name}</span><span style="font-size: 12px; color: {SEC}">{freq}</span></div>{v}</div>'''


def gastos_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    dn = svg('<path d="M6 9l6 6 6-6"></path>', 16, DARK, 2.2)
    alert = svg('<circle cx="12" cy="12" r="9"></circle><path d="M12 7v6M12 16.5v.5"></path>', 16, "#B54708", 2.2)
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
{status_bar()}
<div style="display: flex; align-items: center; gap: 10px; padding: 6px 16px 0">{back}<span style="font-size: 19px; font-weight: 700">Gastos do negócio</span></div>
<div style="padding: 16px 20px 0">
<span style="display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 500; padding: 8px 12px; border: 1px solid {DIV}; border-radius: 10px">Dezembro 2026 {dn}</span>
<div style="margin-top: 14px; display: flex; align-items: center; gap: 8px; background: #FFFAEB; color: #B54708; font-size: 13px; font-weight: 500; padding: 10px 12px; border-radius: 10px">{alert}Falta informar 1 gasto deste mês</div>
<div style="margin-top: 8px">
{gasto_row("Gás de cozinha", "Todo mês", "R$ 140,00")}
{gasto_row("Internet", "Todo mês", "R$ 99,90")}
{gasto_row("Energia", "Todo mês · valor muda", "", True)}
{gasto_row("Anúncio no Instagram", "Somente neste mês", "R$ 150,00")}
</div>
<div style="display: flex; justify-content: space-between; padding: 14px 0"><span style="font-size: 14px; color: {SEC}">Total informado</span><span style="font-size: 16px; font-weight: 700">R$ 389,90</span></div>
<div style="margin-top: 6px; height: 48px; border-radius: 12px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600">+ Adicionar gasto</div>
</div>
{home_ind()}
</div>'''


def f2():
    inner = f'''<img src="{U("COX")}" alt="Coxinhas" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover">
<div style="position: absolute; inset: 0; background: linear-gradient(rgba(16,24,40,0.72), rgba(16,24,40,0.35) 46%, rgba(16,24,40,0.1))"></div>
<div style="position: absolute; left: 40px; right: 40px; top: 46px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">
<span style="color: #FFFFFF; font-size: 33px; font-weight: 600; line-height: 1.14; letter-spacing: -0.9px">Tem certeza de que sabe quanto lucra?</span>
<span style="color: rgba(255,255,255,0.88); font-size: 15px; line-height: 1.4; max-width: 400px">Gás, internet e anúncio também saem do lucro. No Receitech, eles entram na conta.</span></div>
<div style="position: absolute; left: 135px; top: 236px">{phone(gastos_screen(), 540)}</div>'''
    return box(NAVY, inner)


# ---------------- C3 ----------------
def c3_s1():
    inner = f'''<div style="position: absolute; left: 44px; right: 120px; top: 70px; {SER}; color: #FFFFFF; font-size: 31px; line-height: 1.24; letter-spacing: -0.5px">5 bolos de pote sobraram no domingo.</div>
<div style="position: absolute; left: 190px; right: 44px; top: 268px; text-align: right; {SER}; color: #FFFFFF; font-size: 31px; line-height: 1.24; letter-spacing: -0.5px">O que ninguém fala sobre isso{chev("#FFFFFF", 30)}</div>
<img src="{U("POTE")}" alt="Bolos de pote" style="position: absolute; left: 44px; top: 430px; width: 230px; height: 230px; object-fit: cover; border-radius: 12px">
<div style="position: absolute; right: 44px; bottom: 44px; font-size: 12px; color: rgba(255,255,255,0.85)">@receitech_</div>'''
    return box(BLUE, inner)


def mov_row(icon, name, qty, color, sub=None):
    return f'''<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0">
<div style="width: 34px; height: 34px; border-radius: 17px; background: #F2F4F7; display: flex; align-items: center; justify-content: center">{icon}</div>
<div style="flex: 1; display: flex; flex-direction: column"><span style="font-size: 14px; font-weight: 500">{name}</span>{f'<span style="font-size: 12px; color: {SEC}">{sub}</span>' if sub else ''}</div>
<span style="font-size: 15px; font-weight: 700; color: {color}">{qty}</span></div>'''


def estoque_screen():
    def act(icon, t, hl=False):
        st = f"border: 2px solid {RED}; background: #FEF3F2;" if hl else f"border: 1px solid {DIV};"
        return f'<div style="{st} border-radius: 14px; padding: 12px; display: flex; flex-direction: column; gap: 8px">{icon}<span style="font-size: 13px; font-weight: 600">{t}</span></div>'
    i_plus = svg('<path d="M12 5v14M5 12h14"></path>', 20, GREEN, 2.4)
    i_sale = svg('<path d="M4 7h16l-2 11H6z"></path><path d="M9 7a3 3 0 0 1 6 0"></path>', 20, BLUE, 2)
    i_trash = svg('<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"></path>', 20, RED, 2)
    i_edit = svg('<path d="M4 20h4L19 9l-4-4L4 16z"></path>', 20, SEC, 2)
    return f'''<div style="width: 390px; height: 844px; background: rgba(16,24,40,0.45); {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="position: absolute; left: 0; right: 0; bottom: 0; top: 120px; background: #FFFFFF; border-radius: 24px 24px 0 0; padding: 10px 20px 0; box-sizing: border-box">
<div style="width: 40px; height: 4px; border-radius: 2px; background: #D0D5DD; margin: 0 auto 16px"></div>
<div style="display: flex; gap: 14px; align-items: center">{thumb("POTE", 56, 14)}<div style="display: flex; flex-direction: column"><span style="font-size: 20px; font-weight: 700">Bolo de pote</span><span style="font-size: 13px; color: {SEC}">Em estoque: <b style="color: {BLUE}">0</b></span></div></div>
<div style="margin-top: 18px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px">
{act(i_plus, "Produzi mais")}{act(i_sale, "Vendi")}{act(i_trash, "Perdi ou descartei", True)}{act(i_edit, "Corrigir quantidade")}
</div>
<div style="margin-top: 20px; display: flex; justify-content: space-between; align-items: center"><span style="font-size: 16px; font-weight: 700">Últimas movimentações</span><span style="font-size: 13px; font-weight: 600; color: {BLUE}">Ver todas</span></div>
<div style="margin-top: 10px; font-size: 12px; font-weight: 600; color: {SEC}">Domingo, 13 de dezembro</div>
{mov_row(svg('<path d="M4 7h16M6 7l1 13h10l1-13"></path>', 16, RED, 2), "Perdi ou descartei", "−5", RED, "Perda de R$ 20,50")}
<div style="margin-top: 4px; font-size: 12px; font-weight: 600; color: {SEC}">Sábado, 12 de dezembro</div>
{mov_row(svg('<path d="M4 7h16l-2 11H6z"></path>', 16, BLUE, 2), "Vendi", "−7", DARK)}
<div style="margin-top: 4px; font-size: 12px; font-weight: 600; color: {SEC}">Sexta, 11 de dezembro</div>
{mov_row(svg('<path d="M12 5v14M5 12h14"></path>', 16, GREEN, 2.4), "Produzi mais", "+12", GREEN)}
</div>
{home_ind()}
</div>'''


def c3_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 48px; display: flex; flex-direction: column; gap: 10px">
<span style="color: {NAVY}; font-size: 29px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px">Esses 5 bolos de pote tiraram R$ 20,50 do seu lucro.</span>
<span style="color: {SEC}; font-size: 16px; line-height: 1.4">Em Perdi ou descartei, o Receitech registra a perda e desconta do mês.</span></div>
<div style="position: absolute; left: 92px; top: 240px">{phone(estoque_screen(), 600)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 30px; bottom: 26px; height: 22px; width: auto">'''
    return box("#FFFFFF", inner)


SLIDES = [
    ("D13_C1_S1", "13/11 · C1 · tela 1 (gancho) · 12h", c1_s1),
    ("D13_C1_S2", "13/11 · C1 · tela 2 (calendário)", c1_s2),
    ("D13_F1", "13/11 · F1 · foto única (pra resolver) · 14h30", f1),
    ("D13_C2_S1", "13/11 · C2 · tela 1 (gancho) · 17h", c2_s1),
    ("D13_C2_S2", "13/11 · C2 · tela 2 (custo do cento)", c2_s2),
    ("D13_F2", "13/11 · F2 · foto única (gastos) · 19h", f2),
    ("D13_C3_S1", "13/11 · C3 · tela 1 (gancho) · 21h", c3_s1),
    ("D13_C3_S2", "13/11 · C3 · tela 2 (perda no estoque)", c3_s2),
]

if __name__ == "__main__":
    only = sys.argv[3].split(",") if len(sys.argv) > 3 else None
    for code, title, fn in SLIDES:
        if only and code not in only:
            continue
        html = fn()
        if MODE == "canvas":
            doc = page(title, html, PW, PH).replace(
                "family=Poppins:wght@400;500;600;700&amp;display=swap",
                "family=Poppins:wght@400;500;600;700&amp;family=Libre+Caslon+Text:wght@400;700&amp;display=swap")
            assert "Libre+Caslon" in doc and "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
