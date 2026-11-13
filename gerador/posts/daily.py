"""Gerador dos posts diários (canvas 'Criador de redes sociais')."""
import json, os, sys
sys.path.insert(0, "/home/claude/assets")
_g = open('/home/claude/assets/gen.py').read().split("files = {")[0]
exec(_g)  # page(), svg(), product_screen(), phone(), PW, PH, cores

ROOT2 = "/mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project"
os.makedirs(ROOT2, exist_ok=True)
LD = "/_blob/f2996fe4c9fb0951e6c5b11ec42e37da"
LW = "/_blob/c900d55a8870af975f0e491905355cb1"
IL = "/_blob/7317a8d827cf8e22cb95c802fcbec908"
BRIG2 = "/_blob/7068e370f6c081e526f0cec5880a68b5"
F = "font-family: 'Poppins', sans-serif"


def slide_hook(text, illu=True):
    img = f'<img src="{IL}" alt="Brigadeiro" style="position: absolute; right: 56px; bottom: 60px; width: 64px; height: auto; transform: rotate(10deg)">' if illu else ""
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: #FFFFFF; box-sizing: border-box; padding: 48px 52px; {F}; display: flex; flex-direction: column; justify-content: space-between">
<img src="{LD}" alt="receitech" style="height: 30px; width: auto; align-self: flex-start">
<span style="font-size: 44px; font-weight: 700; line-height: 1.15; color: {DARK}; letter-spacing: -1.2px; text-wrap: balance; padding-bottom: 60px">{text}</span>
<div style="display: flex; align-items: center; gap: 10px; color: {SEC}; font-size: 15px; font-weight: 500">
{svg('<path d="M9 6l6 6-6 6"></path>', 18, SEC, 2.4)}<span>Passe pro lado</span>
</div>
{img}
</div>'''


def slide_app(title, sub, screen_html):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: #FFFFFF; box-sizing: border-box; padding: 48px 52px 0; {F}; display: flex; flex-direction: column; gap: 10px">
<img src="{LD}" alt="receitech" style="height: 30px; width: auto; align-self: flex-start">
<span style="margin-top: 10px; font-size: 34px; font-weight: 700; line-height: 1.12; color: {DARK}; letter-spacing: -1px; text-wrap: balance">{title}</span>
<span style="font-size: 18px; line-height: 1.4; color: {SEC}; text-wrap: balance">{sub}</span>
<div style="margin-top: 14px; align-self: center; position: relative; top: 0">
{phone(screen_html.replace("/_blob/dec215cfbdbfd09ab202c7670b2cc7b6", BRIG2), 520)}
</div>
</div>'''


C1 = [
    ("C1_S1.dc.html", "C1 · tela 1 (gancho)", slide_hook("Antes de vender o próximo brigadeiro, veja isso.")),
    ("C1_S2.dc.html", "C1 · tela 2 (app)", slide_app(
        "Esse brigadeiro custa R$ 0,79.",
        "O app calcula o custo de cada doce e mostra o preço certo pra sua margem.",
        product_screen())),
]

canvas_path = os.path.join(ROOT2, "canvas.json")
if os.path.exists(canvas_path):
    canvas = json.load(open(canvas_path))
else:
    canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-11-12T12:40:00Z"},
              "title": "Criador de redes sociais — posts diários", "launch": {"view": "canvas"},
              "pages": [], "boards": {}, "order": [], "notes": {}, "designSystems": []}
canvas["notes"]["t_c1"] = {"x": 0, "y": -230, "text": "C1 · Preço do produto: custo e preço sugerido", "kind": "title1", "maxW": 1160}
for i, (fn, title, html) in enumerate(C1):
    open(os.path.join(ROOT2, fn), "w").write(page(title, html, PW, PH))
    canvas["boards"][fn] = {"x": i * (PW + 80), "y": 0, "w": PW, "h": PH, "title": title}
    if fn not in canvas["order"]:
        canvas["order"].append(fn)
# Main.dc.html must exist as the entry: make it the first slide copy
open(os.path.join(ROOT2, "Main.dc.html"), "w").write(page("C1 · tela 1 (gancho)", C1[0][2], PW, PH))
canvas["boards"].pop("C1_S1.dc.html", None)
canvas["order"] = [f for f in canvas["order"] if f != "C1_S1.dc.html"]
canvas["boards"]["Main.dc.html"] = {"x": 0, "y": 0, "w": PW, "h": PH, "title": "C1 · tela 1 (gancho)"}
if "Main.dc.html" not in canvas["order"]:
    canvas["order"].insert(0, "Main.dc.html")
if os.path.exists(os.path.join(ROOT2, "C1_S1.dc.html")):
    os.remove(os.path.join(ROOT2, "C1_S1.dc.html"))
json.dump(canvas, open(canvas_path, "w"), ensure_ascii=False, indent=1)

# local preview
for fn, _, html in [("Main.dc.html", None, C1[0][2]), ("C1_S2.dc.html", None, C1[1][2])]:
    loc = html.replace(LD, "logo_dark.png").replace(IL, "brig_vermelho.png").replace(BRIG2, "/home/claude/assets/brigadeiro.jpg")
    open("/home/claude/posts/prev_" + fn.replace(".dc.html", ".html"), "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{loc}</body></html>")
print(canvas["order"])

# ---------- F1: foto única (sem gancho) ----------
def slide_single(title, sub, screen_html):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {BLUE}; box-sizing: border-box; padding: 44px 48px 0; {F}; display: flex; flex-direction: column; gap: 10px">
<img src="{LW}" alt="receitech" style="height: 30px; width: auto; align-self: flex-start">
<span style="margin-top: 8px; font-size: 34px; font-weight: 700; line-height: 1.12; color: #FFFFFF; letter-spacing: -1px; text-wrap: balance">{title}</span>
<span style="font-size: 18px; line-height: 1.4; color: rgba(255,255,255,0.9); text-wrap: balance">{sub}</span>
<div style="margin-top: 12px; align-self: center">
{phone(screen_html.replace("/_blob/dec215cfbdbfd09ab202c7670b2cc7b6", BRIG2), 520)}
</div>
</div>'''

F1 = ("F1_foto.dc.html", "F1 · foto única (sem gancho)", slide_single(
    "Quanto custa cada doce que você vende? O app responde.",
    "Custo, lucro e margem de cada produto, na venda direta e no iFood.",
    product_screen()))
canvas = json.load(open(canvas_path))
canvas["notes"]["t_f1"] = {"x": 0, "y": PH + 160 - 230, "text": "F1 · Foto única: tela do app + frase direta", "kind": "title1", "maxW": 1160}
open(os.path.join(ROOT2, F1[0]), "w").write(page(F1[1], F1[2], PW, PH))
canvas["boards"][F1[0]] = {"x": 0, "y": PH + 160, "w": PW, "h": PH, "title": F1[1]}
if F1[0] not in canvas["order"]: canvas["order"].append(F1[0])
json.dump(canvas, open(canvas_path, "w"), ensure_ascii=False, indent=1)
loc = F1[2].replace(LW, "logo_white.png").replace(BRIG2, "/home/claude/assets/brigadeiro.jpg")
open("/home/claude/posts/prev_F1.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{loc}</body></html>")

# ---------- C2: cardápio online, Natal ----------
PAN = "/_blob/ef5af87b17eb8727fe144b04fa3048ea"
def slide_hook_img(text, img_url, w=96, rot=-8):
    return slide_hook(text, illu=False).replace("</div>\n</div>'''", "") if False else f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: #FFFFFF; box-sizing: border-box; padding: 48px 52px; {F}; display: flex; flex-direction: column; justify-content: space-between">
<img src="{LD}" alt="receitech" style="height: 30px; width: auto; align-self: flex-start">
<span style="font-size: 42px; font-weight: 700; line-height: 1.15; color: {DARK}; letter-spacing: -1.2px; padding-bottom: 60px; padding-right: 20px">{text}</span>
<div style="display: flex; align-items: center; gap: 10px; color: {SEC}; font-size: 15px; font-weight: 500">
{svg('<path d="M9 6l6 6-6 6"></path>', 18, SEC, 2.4)}<span>Passe pro lado</span>
</div>
<img src="{img_url}" alt="" style="position: absolute; right: 52px; bottom: 56px; width: {w}px; height: auto; transform: rotate({rot}deg)">
</div>'''
C2S1 = ("C2_S1.dc.html", "C2 · tela 1 (gancho)", slide_hook_img("Receber encomenda de Natal pelo WhatsApp tem um problema. E tem como evitar.", PAN))
canvas = json.load(open(canvas_path))
canvas["notes"]["t_c2"] = {"x": 0, "y": 2 * (PH + 160) - 230, "text": "C2 · Cardápio online: encomendas de Natal", "kind": "title1", "maxW": 1160}
open(os.path.join(ROOT2, C2S1[0]), "w").write(page(C2S1[1], C2S1[2], PW, PH))
canvas["boards"][C2S1[0]] = {"x": 0, "y": 2 * (PH + 160), "w": PW, "h": PH, "title": C2S1[1]}
if C2S1[0] not in canvas["order"]: canvas["order"].append(C2S1[0])
json.dump(canvas, open(canvas_path, "w"), ensure_ascii=False, indent=1)
open("/home/claude/posts/prev_C2_S1.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{C2S1[2].replace(LD,'logo_dark.png').replace(PAN,'panetone.svg')}</body></html>")

# ---------- C2 tela 2: cardápio online de Natal ----------
PH_PAN = "/_blob/77809cf9a885b697802b94567ac4f507"; PH_RAB = "/_blob/997a0515a870786496af57aabbe58054"
PH_CHO = "/_blob/6b05e364e59b0893f68b2f2a0b92b2b1"; PH_BIS = "/_blob/dad992cc142ec001e3af9c1bd589853a"

def menu_card(img, name, desc, price, tag):
    return f'''<div style="display: flex; gap: 12px; padding: 12px 0; border-bottom: 1px solid {DIV}">
<div style="position: relative; flex: none; width: 104px; height: 104px; border-radius: 14px; overflow: hidden"><img src="{img}" alt="{name}" style="width: 100%; height: 100%; object-fit: cover">
<span style="position: absolute; left: 6px; top: 6px; background: rgba(16,24,40,0.78); color: #FFFFFF; font-size: 9px; font-weight: 600; padding: 3px 7px; border-radius: 20px">{tag}</span></div>
<div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between">
<div style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 15px; font-weight: 500; color: {DARK}">{name}</span><span style="font-size: 12px; line-height: 1.3; color: {SEC}">{desc}</span></div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 14px; font-weight: 500; color: {DARK}">R$ {price}</span><span style="width: 30px; height: 30px; border-radius: 15px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 500; line-height: 1">+</span></div>
</div></div>'''

def menu_screen():
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {F}; color: {DARK}; overflow: hidden; display: flex; flex-direction: column">
<div style="height: 54px"></div>
<div style="background: {LBLUE}; padding: 8px 0; text-align: center; font-size: 11px; font-weight: 600; color: {BLUE}; letter-spacing: 0.3px">Feito com Receitech</div>
<div style="padding: 18px 20px 0; display: flex; gap: 14px; align-items: center">
<div style="width: 54px; height: 54px; border-radius: 27px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 700">A</div>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 700; letter-spacing: -0.4px">Doces da Amanda</span><span style="font-size: 12px; color: {SEC}">Retirada em Santo André · entrega por CEP</span></div>
</div>
<div style="padding: 16px 20px 0; display: flex; gap: 8px">
<span style="background: {DARK}; color: #FFFFFF; font-size: 12px; font-weight: 600; padding: 7px 14px; border-radius: 20px">Natal</span>
<span style="background: #F2F4F7; color: {SEC}; font-size: 12px; font-weight: 500; padding: 7px 14px; border-radius: 20px">Bolos</span>
<span style="background: #F2F4F7; color: {SEC}; font-size: 12px; font-weight: 500; padding: 7px 14px; border-radius: 20px">Doces</span>
</div>
<div style="padding: 10px 20px 0; display: flex; flex-direction: column">
{menu_card(PH_PAN, "Panetone caseiro 500 g", "Frutas cristalizadas e massa fermentada por 24 h.", "48,00", "Encomenda")}
{menu_card(PH_CHO, "Chocotone 500 g", "Gotas de chocolate meio amargo, sem frutas.", "52,00", "Encomenda")}
{menu_card(PH_RAB, "Rabanada (6 un.)", "Pão francês, leite condensado e canela.", "24,00", "Encomenda")}
{menu_card(PH_BIS, "Kit biscoitos de Natal", "12 biscoitos decorados, embalados um a um.", "39,00", "Encomenda")}
</div>
</div>'''

def slide_app_dark(title, sub, screen_html):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {DARK}; box-sizing: border-box; {F}">
<div style="position: absolute; left: 118px; top: -30px; transform: rotate(-5deg); transform-origin: center">{phone(screen_html, 640)}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 330px; background: linear-gradient(rgba(16,24,40,0), rgba(16,24,40,0.96) 45%)"></div>
<div style="position: absolute; left: 44px; right: 44px; bottom: 44px; display: flex; flex-direction: column; gap: 14px">
<img src="{LW}" alt="receitech" style="height: 28px; width: auto; align-self: flex-start">
<span style="font-size: 32px; font-weight: 700; line-height: 1.12; color: #FFFFFF; letter-spacing: -1px">{title}</span>
<span style="font-size: 17px; line-height: 1.4; color: rgba(255,255,255,0.82)">{sub}</span>
</div>
</div>'''

C2S2 = ("C2_S2.dc.html", "C2 · tela 2 (app)", slide_app_dark(
    "O pedido entra sozinho no app, com data de entrega.",
    "Cardápio online com prazo de encomenda. O cliente escolhe, manda o pedido e você só confirma.",
    menu_screen()))
canvas = json.load(open(canvas_path))
open(os.path.join(ROOT2, C2S2[0]), "w").write(page(C2S2[1], C2S2[2], PW, PH))
canvas["boards"][C2S2[0]] = {"x": PW + 80, "y": 2 * (PH + 160), "w": PW, "h": PH, "title": C2S2[1]}
if C2S2[0] not in canvas["order"]: canvas["order"].append(C2S2[0])
json.dump(canvas, open(canvas_path, "w"), ensure_ascii=False, indent=1)
loc = C2S2[2].replace(LW, "logo_white.png")
for b_, f_ in [(PH_PAN, "/home/claude/fotos/panetone_400.jpg"), (PH_RAB, "/home/claude/fotos/rabanada_400.jpg"), (PH_CHO, "/home/claude/fotos/chocotone_400.jpg"), (PH_BIS, "/home/claude/fotos/biscoitos_400.jpg")]:
    loc = loc.replace(b_, f_)
open("/home/claude/posts/prev_C2_S2.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{loc}</body></html>")

# ---------- C2 S1 refeita (estilo diferente do C1) ----------
def slide_hook_v2(text):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {LBLUE}; box-sizing: border-box; padding: 44px 48px; {F}; display: flex; flex-direction: column">
<div style="display: flex; justify-content: flex-end; align-items: center; gap: 8px; color: {BLUE}; font-size: 14px; font-weight: 600">
<span>Passe pro lado</span>{svg('<path d="M9 6l6 6-6 6"></path>', 16, BLUE, 2.6)}
</div>
<span style="margin-top: 36px; font-size: 46px; font-weight: 700; line-height: 1.12; color: {BLUE}; letter-spacing: -1.4px; padding-right: 10px">{text}</span>
<img src="{PAN}" alt="" style="position: absolute; left: -30px; bottom: -40px; width: 300px; height: auto; transform: rotate(8deg)">
<img src="{LD}" alt="receitech" style="position: absolute; right: 48px; bottom: 44px; height: 28px; width: auto">
</div>'''
C2S1b = slide_hook_v2("Receber encomenda de Natal pelo WhatsApp tem um problema. E tem como evitar.")
open(os.path.join(ROOT2, "C2_S1.dc.html"), "w").write(page("C2 · tela 1 (gancho)", C2S1b, PW, PH))
open("/home/claude/posts/prev_C2_S1.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{C2S1b.replace(LD,'logo_dark.png').replace(PAN,'panetone.svg')}</body></html>")

# S2: logo sai do bloco de texto e vai pro canto superior direito
def slide_app_dark2(title, sub, screen_html):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {DARK}; box-sizing: border-box; {F}">
<div style="position: absolute; left: 118px; top: -30px; transform: rotate(-5deg); transform-origin: center">{phone(screen_html, 640)}</div>
<img src="{LW}" alt="receitech" style="position: absolute; right: 40px; top: 40px; height: 26px; width: auto">
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 330px; background: linear-gradient(rgba(16,24,40,0), rgba(16,24,40,0.96) 45%)"></div>
<div style="position: absolute; left: 44px; right: 44px; bottom: 48px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 32px; font-weight: 700; line-height: 1.12; color: #FFFFFF; letter-spacing: -1px">{title}</span>
<span style="font-size: 17px; line-height: 1.4; color: rgba(255,255,255,0.82)">{sub}</span>
</div>
</div>'''
C2S2b = slide_app_dark2("O pedido entra sozinho no app, com data de entrega.", "Cardápio online com prazo de encomenda. O cliente escolhe, manda o pedido e você só confirma.", menu_screen())
open(os.path.join(ROOT2, "C2_S2.dc.html"), "w").write(page("C2 · tela 2 (app)", C2S2b, PW, PH))
loc = C2S2b.replace(LW, "logo_white.png")
for b_, f_ in [(PH_PAN, "/home/claude/fotos/panetone_400.jpg"), (PH_RAB, "/home/claude/fotos/rabanada_400.jpg"), (PH_CHO, "/home/claude/fotos/chocotone_400.jpg"), (PH_BIS, "/home/claude/fotos/biscoitos_400.jpg")]:
    loc = loc.replace(b_, f_)
open("/home/claude/posts/prev_C2_S2.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{loc}</body></html>")

# ---------- C2 S1 v3 ----------
def slide_hook_v3():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {LBLUE}; box-sizing: border-box; padding: 56px 52px; {F}; display: flex; flex-direction: column; justify-content: center; gap: 28px">
<span style="font-size: 34px; font-weight: 600; line-height: 1.22; color: {DARK}; letter-spacing: -0.8px; padding-right: 30px">Receber encomenda de Natal pelo WhatsApp tem um problema.</span>
<span style="display: flex; align-items: center; gap: 12px; font-size: 34px; font-weight: 700; line-height: 1.2; color: {BLUE}; letter-spacing: -0.8px">E tem como evitar {svg('<path d="M5 12h14M13 6l6 6-6 6"></path>', 34, BLUE, 2.6)}</span>
<img src="{PH_PAN}" alt="" style="position: absolute; right: 52px; bottom: 56px; width: 88px; height: 88px; border-radius: 22px; object-fit: cover; transform: rotate(-6deg); box-shadow: 0 10px 24px rgba(16,24,40,0.18)">
</div>'''
C2S1c = slide_hook_v3()
open(os.path.join(ROOT2, "C2_S1.dc.html"), "w").write(page("C2 · tela 1 (gancho)", C2S1c, PW, PH))
open("/home/claude/posts/prev_C2_S1.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{C2S1c.replace(PH_PAN,'/home/claude/fotos/panetone_400.jpg')}</body></html>")

# ---------- C2 S1 v4: foto em faixa na parte de baixo ----------
BOLO_BAND = "/_blob/ceb14bb853b7ca9211644d8772e03041"
def slide_hook_v4():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: #FFFFFF; {F}">
<div style="position: absolute; left: 0; top: 0; right: 0; height: 440px; box-sizing: border-box; padding: 64px 52px 0; display: flex; flex-direction: column; justify-content: center; gap: 26px">
<span style="font-size: 33px; font-weight: 600; line-height: 1.22; color: {DARK}; letter-spacing: -0.8px; padding-right: 20px">Receber encomenda de Natal pelo WhatsApp tem um problema.</span>
<span style="display: flex; align-items: center; gap: 12px; font-size: 33px; font-weight: 700; line-height: 1.2; color: {BLUE}; letter-spacing: -0.8px">E tem como evitar {svg('<path d="M5 12h14M13 6l6 6-6 6"></path>', 32, BLUE, 2.6)}</span>
</div>
<img src="{BOLO_BAND}" alt="Bolo de Natal" style="position: absolute; left: 0; right: 0; bottom: 0; width: 100%; height: 300px; object-fit: cover">
</div>'''
C2S1d = slide_hook_v4()
open(os.path.join(ROOT2, "C2_S1.dc.html"), "w").write(page("C2 · tela 1 (gancho)", C2S1d, PW, PH))
open("/home/claude/posts/prev_C2_S1.html", "w").write(f"<html><head><meta charset='utf-8'><style>body{{margin:0}}</style></head><body>{C2S1d.replace(BOLO_BAND,'/home/claude/fotos/bolo_natal_band.jpg')}</body></html>")
