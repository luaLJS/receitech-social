"""C3 · Lista de compras (Necessário para a semana) — ângulo de Natal."""
import json, os, sys
sys.path.insert(0, "/home/claude/assets")
exec(open('/home/claude/assets/gen.py').read().split("files = {")[0])
ROOT2 = "/mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project"
LD = "/_blob/f2996fe4c9fb0951e6c5b11ec42e37da"
LW = "/_blob/c900d55a8870af975f0e491905355cb1"
F = "font-family: 'Poppins', sans-serif"
PH_SALG = "/_blob/fca930829a7de45535f18718f6bf32cf"
PH_CASA = "/_blob/496bd383e94fc79bd7331378550a6cd1"
NAVY = "#0F1F3D"


PH_PAO = "/_blob/b47b7bc214a7fe1741a5bef518658dfd"
CREAM = "#FBF6EF"; WINE = "#B42318"


PH_PAO_S = "/_blob/1039e0e17a6d701ee36300106d40ebd5"
PH_PAO_F = "/_blob/dfc3cd9c8811429deaebd3bb6fe65239"
PM_STK = "/_blob/05e8e6be755fd49a5018947301c706ff"


def slide_hook_c3():
    chev = svg('<path d="M9 6l6 6-6 6"></path>', 26, DARK, 2.6)
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: #F7F1E8; {F}">
<div style="position: absolute; left: 48px; right: 56px; top: 64px; display: flex; flex-direction: column; gap: 22px; color: {DARK}; font-size: 29px; font-weight: 600; line-height: 1.22; letter-spacing: -0.5px">
<span>Encomenda de Natal fechada.</span>
<span>Agora vem a parte que mais dá prejuízo<span style="display: inline-block; vertical-align: -5px; margin-left: 4px">{chev}</span></span>
</div>
<img src="{PH_PAO_S}" alt="Pão de mel de Natal" style="position: absolute; left: 50%; margin-left: -150px; top: 272px; width: 300px; height: 360px; object-fit: cover; border-radius: 6px">
</div>'''


def row(name, qty, open_=False, origins=None):
    chev = svg('<path d="M6 9l6 6 6-6"></path>', 16, SEC, 2.2)
    if open_:
        chev = svg('<path d="M18 15l-6-6-6 6"></path>', 16, SEC, 2.2)
    o = ""
    if open_ and origins:
        lines = "".join(f'<div style="display: flex; justify-content: space-between; font-size: 12px; color: {SEC}; padding: 5px 0"><span>{a}</span><span style="font-weight: 500; color: {DARK}">{b}</span></div>' for a, b in origins)
        o = f'<div style="margin: 2px 0 8px 0; padding: 6px 12px; background: #F9FAFB; border-radius: 10px">{lines}</div>'
    return f'''<div style="border-bottom: 1px solid {DIV}; padding: 12px 0 4px 0">
<div style="display: flex; align-items: center; justify-content: space-between; padding-bottom: 8px">
<span style="font-size: 15px; font-weight: 500; color: {DARK}">{name}</span>
<span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 15px; font-weight: 600; color: {DARK}">{qty}</span>{chev}</span>
</div>{o}</div>'''


def lista_screen():
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {F}; color: {DARK}; overflow: hidden; display: flex; flex-direction: column; box-sizing: border-box; padding: 0 20px">
<div style="height: 56px"></div>
<div style="display: flex; align-items: center; gap: 12px; padding: 6px 0 14px">{svg('<path d="M15 18l-6-6 6-6"></path>', 22, DARK, 2.4)}<span style="font-size: 20px; font-weight: 700; letter-spacing: -0.4px">Necessário para a semana</span></div>
<span style="font-size: 13px; line-height: 1.4; color: {SEC}">Com base no que ainda falta produzir. Confira o que você já tem antes de comprar.</span>
<div style="margin-top: 18px; display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; font-weight: 700; letter-spacing: 1px; color: {SEC}">INGREDIENTES</span><span style="font-size: 11px; font-weight: 600; color: {BLUE}; background: {LBLUE}; padding: 4px 10px; border-radius: 20px">15 a 21 dez</span></div>
{row("Leite condensado", "6,4 caixas", True, [("Rabanadas da Dona Lúcia (30 un.)", "1,5 caixa"), ("100 brigadeiros pra estoque", "3,4 caixas"), ("Casadinhos da festa da Bia (60 un.)", "1,5 caixa")])}
{row("Chocolate em pó 50%", "1,2 kg")}
{row("Coco ralado", "350 g")}
{row("Peito de frango", "1,8 kg")}
{row("Farinha de trigo", "2,5 kg")}
<div style="margin-top: 18px; font-size: 11px; font-weight: 700; letter-spacing: 1px; color: {SEC}">EMBALAGENS</div>
{row("Forminha nº 4", "160 un.")}
{row("Caixa 4 doces", "15 un.")}
<div style="flex: 1"></div>
<div style="display: flex; gap: 10px; padding-bottom: 28px">
<span style="flex: 1; text-align: center; padding: 14px 0; border-radius: 12px; border: 1.5px solid {DIV}; font-size: 14px; font-weight: 600; color: {DARK}">Copiar lista</span>
<span style="flex: 1; text-align: center; padding: 14px 0; border-radius: 12px; background: {BLUE}; font-size: 14px; font-weight: 600; color: #FFFFFF">Compartilhar</span>
</div>
</div>'''


def slide_app_c3(title, sub, screen_html):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {LBLUE}; {F}">
<div style="position: absolute; left: 44px; right: 44px; top: 48px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 30px; font-weight: 700; line-height: 1.14; color: {DARK}; letter-spacing: -0.9px">{title}</span>
<span style="font-size: 16px; line-height: 1.4; color: {SEC}; padding-right: 30px">{sub}</span>
</div>
<div style="position: absolute; left: 186px; top: 214px">{phone(screen_html, 660)}</div>
<img src="{PH_CASA}" alt="Casadinhos" style="position: absolute; left: -70px; bottom: -50px; width: 270px; height: 270px; border-radius: 135px; object-fit: cover; box-shadow: 0 20px 50px rgba(16,24,40,0.25); border: 6px solid #FFFFFF">
</div>'''


S1 = slide_hook_c3()
S2 = slide_app_c3("O app soma os ingredientes de tudo que falta produzir.",
                  "Encomendas e produção da semana viram uma lista de compras, com o quanto cada pedido consome.",
                  lista_screen())

open(os.path.join(ROOT2, "C3_S1.dc.html"), "w").write(page("C3 · tela 1 (gancho)", S1, PW, PH))
open(os.path.join(ROOT2, "C3_S2.dc.html"), "w").write(page("C3 · tela 2 (app)", S2, PW, PH))

canvas_path = os.path.join(ROOT2, "canvas.json")
canvas = json.load(open(canvas_path))
Y = 3 * (PH + 160)
canvas["notes"]["t_c3"] = {"x": 0, "y": Y - 230, "text": "C3 · Lista de compras: ingredientes da semana somados", "kind": "title1", "maxW": 1160}
canvas["boards"]["C3_S1.dc.html"] = {"x": 0, "y": Y, "w": PW, "h": PH, "title": "C3 · tela 1 (gancho)"}
canvas["boards"]["C3_S2.dc.html"] = {"x": PW + 80, "y": Y, "w": PW, "h": PH, "title": "C3 · tela 2 (app)"}
for fn in ["C3_S1.dc.html", "C3_S2.dc.html"]:
    if fn not in canvas["order"]:
        canvas["order"].append(fn)
json.dump(canvas, open(canvas_path, "w"), ensure_ascii=False, indent=1)

# previews
rep = [(PM_STK, "/home/claude/cut/pm2_sticker.png"), (PH_PAO_F, "/home/claude/fotos/paodemel_full.jpg"), (PH_PAO_S, "/home/claude/fotos/paodemel_small.jpg"), (PH_PAO, "/home/claude/fotos/paodemel_strip.jpg"), (PH_SALG, "/home/claude/fotos/salgados_full.jpg"), (PH_CASA, "/home/claude/fotos/casadinho_sq.jpg"), (LW, "logo_white.png"), (LD, "logo_dark.png")]
for name, html in [("C3_S1", S1), ("C3_S2", S2)]:
    loc = html
    for a, b in rep:
        loc = loc.replace(a, b)
    open(f"/home/claude/posts/prev_{name}.html", "w").write(f"<html><head><meta charset='utf-8'><link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{loc}</body></html>")
print("ok")
