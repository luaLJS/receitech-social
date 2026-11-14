"""Posts de 14/11/2026 (formato novo: funcionalidade dita na tela 1, carrossel de 3 telas).
C1 produção para estoque + estoque pronto (12h) · C2 custo atualiza quando o ingrediente sobe (19h).
Uso: python3 d1114.py local|canvas [OUT]"""
import json, os, sys
exec(open('/home/claude/receitech-social/gerador/assets/gen.py').read().split("files = {")[0])

MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1114"
os.makedirs(OUT, exist_ok=True)
BANK = "/home/claude/receitech-social/banco-imagens/"
IMGS = {"COX": "salg_coxinha_2.jpg", "BOL": "salg_bolinha_2.jpg", "CXB": "natal_caixabrig_1.jpg"}
LOGOS = {"LOGOB": "/home/claude/receitech-social/gerador/posts/logo_dark.png",
         "LOGOW": "/home/claude/receitech-social/gerador/posts/logo_white.png"}
BLOBS = {"LOGOB": "/_blob/f2996fe4c9fb0951e6c5b11ec42e37da", "LOGOW": "/_blob/c900d55a8870af975f0e491905355cb1"}
bf = "/home/claude/receitech-social/gerador/posts/d1114_blobs.json"
if os.path.exists(bf):
    BLOBS.update(json.load(open(bf)))


def U(k):
    if MODE == "canvas":
        return BLOBS[k]
    return "file://" + (LOGOS[k] if k in LOGOS else BANK + IMGS[k])


NAVY, CREAM, SKY = "#101828", "#F3EDE3", "#CFE2FF"
POP = "font-family: 'Poppins', sans-serif"
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap"


def box(bg, inner):
    return f'<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {bg}; {POP}">{inner}</div>'


def status_bar():
    return '<div style="height: 54px"></div>'


def home_ind():
    return f'<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>'


def chip(t, bg="#F2F4F7", fg=SEC):
    return f'<span style="background: {bg}; color: {fg}; font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 20px; white-space: nowrap">{t}</span>'


def bottom_nav(active):
    items = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == active else 500}; color: {BLUE if n == active else "#98A2B3"}">{n}</span>' for n in ["Rotina", "Vendas", "Lucro", "Produtos", "Perfil"])
    return f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; background: #FFFFFF; border-top: 1px solid {DIV}; display: flex; justify-content: space-around; padding-top: 14px; box-sizing: border-box">{items}</div>'


# ================= C1 · produção para estoque =================
def c1_s1():
    tabs = [("Preço", False), ("Pedidos", False), ("Estoque", True), ("Lucro", False)]
    t = "".join(
        f'<div style="height: 96px; width: 38px; background: {SKY if on else "#FFFFFF"}; border: 1.5px solid {NAVY}; border-left: none; border-radius: 0 12px 12px 0; display: flex; align-items: center; justify-content: center">'
        f'<span style="transform: rotate(90deg); font-size: 15px; font-weight: {700 if on else 400}; color: {NAVY}; white-space: nowrap">{n}</span></div>' for n, on in tabs)
    inner = f'''<div style="position: absolute; left: 60px; top: 60px; width: 380px; height: 600px; background: #FFFFFF; border: 1.5px solid {NAVY}; border-radius: 10px; box-sizing: border-box">
<div style="position: absolute; left: 30px; right: 30px; top: 40px; color: {NAVY}; font-size: 29px; font-weight: 600; line-height: 1.18; letter-spacing: -0.8px">Planeje a produção da semana. O que fica pronto já entra no estoque.</div>
<img src="{U("COX")}" alt="Coxinhas de frango cortadas ao meio" style="position: absolute; left: 30px; top: 262px; width: 317px; height: 250px; object-fit: cover; object-position: 50% 45%; border-radius: 8px">
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; left: 30px; bottom: 30px; height: 20px; width: auto">
</div>
<div style="position: absolute; left: 440px; top: 120px; display: flex; flex-direction: column; gap: 4px">{t}</div>'''
    return box(NAVY, inner)


def prod_row(qty_name, status):
    styles = {"Produzido": ("#ECFDF3", "#067647"), "Em produção": (LBLUE, "#175CD3"), "Pendente": ("#F2F4F7", SEC)}
    bg, fg = styles[status]
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; padding: 14px 0; border-bottom: 1px solid {DIV}">
<span style="font-size: 15px; font-weight: 500">{qty_name}</span>{chip(status, bg, fg)}</div>'''


def rotina_prod_screen():
    plus = svg('<path d="M12 5v14M5 12h14"></path>', 15, BLUE, 2.4)
    arrow = svg('<path d="M5 12h14M13 6l6 6-6 6"></path>', 15, BLUE, 2.4)
    stock = "".join(f'<div style="display: flex; justify-content: space-between; padding: 9px 0"><span style="font-size: 14px">{n}</span><span style="font-size: 14px; font-weight: 600">{q}</span></div>'
                    for n, q in [("Coxinha", "100"), ("Kibe", "12"), ("Esfiha de carne", "8")])
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
{status_bar()}
<div style="padding: 4px 20px 0"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.5px">Minha rotina</span></div>
<div style="padding: 22px 20px 0">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 18px; font-weight: 600">Produção para estoque</span>
<span style="display: flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 600; color: {BLUE}">{plus}Adicionar</span></div>
<span style="display: block; margin-top: 2px; font-size: 13px; color: {SEC}">Esta semana · 16 a 22 de novembro</span>
<div style="margin-top: 6px">
{prod_row("100 coxinhas", "Produzido")}
{prod_row("80 bolinhas de queijo", "Em produção")}
{prod_row("60 kibes", "Pendente")}
{prod_row("40 esfihas de carne", "Pendente")}
</div></div>
<div style="padding: 26px 20px 0">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 18px; font-weight: 600">Estoque pronto</span>
<span style="display: flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 600; color: {BLUE}">Ver tudo {arrow}</span></div>
<div style="margin-top: 6px">{stock}</div></div>
{bottom_nav("Rotina")}
{home_ind()}
</div>'''


def c1_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 60px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.17; letter-spacing: -0.8px">Cada produção com status: pendente, em produção, produzido.</div>
<img src="{U("BOL")}" alt="Bolinhas de queijo" style="position: absolute; left: 36px; top: 300px; width: 170px; height: 210px; object-fit: cover; object-position: 55% 60%; border-radius: 12px">
<div style="position: absolute; left: 222px; top: 190px">{phone(rotina_prod_screen(), 600)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; left: 36px; bottom: 30px; height: 20px; width: auto">'''
    return box("#FFFFFF", inner)


def stock_screen():
    search = svg('<circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path>', 22, DARK, 2)
    seg = "".join(f'<span style="flex: 1; text-align: center; padding: 7px 0; border-radius: 9px; font-size: 13px; font-weight: {600 if a else 500}; color: {DARK if a else SEC}; background: {"#FFFFFF" if a else "transparent"}; {"box-shadow: 0 1px 3px rgba(16,24,40,0.12);" if a else ""}">{n}</span>'
                  for n, a in [("Produtos", True), ("Receitas", False), ("Insumos", False)])
    chips = chip("Todos", "#FFFFFF", SEC).replace("background: #FFFFFF;", f"background: #FFFFFF; border: 1px solid {DIV};") + chip("Em estoque", DARK, "#FFFFFF")

    def row(n, q, hl=False):
        bg = f"background: #ECFDF3; margin: 0 -12px; padding-left: 12px; padding-right: 12px; border-radius: 12px;" if hl else ""
        return f'''<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid {DIV}; {bg}">
<span style="font-size: 15px; font-weight: 500">{n}</span><span style="font-size: 15px; font-weight: 600; color: {"#067647" if hl else DARK}">{q} un.</span></div>'''
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
{status_bar()}
<div style="display: flex; align-items: center; gap: 14px; padding: 4px 18px 0"><div style="flex: 1; display: flex; background: #F2F4F7; border-radius: 11px; padding: 3px">{seg}</div>{search}</div>
<div style="display: flex; gap: 8px; padding: 16px 20px 6px">{chips}</div>
<div style="padding: 0 20px">
{row("Coxinha", "100", True)}
{row("Kibe", "12")}
{row("Esfiha de carne", "8")}
{row("Bolinha de queijo", "0")}
{row("Risole", "6")}
{row("Empadinha de frango", "20")}
{row("Mini pizza", "15")}
{row("Pão de queijo", "30")}
</div>
{bottom_nav("Produtos")}
{home_ind()}
</div>'''


def c1_s3():
    inner = f'''<div style="position: absolute; left: 127px; top: 36px">{phone(stock_screen(), 520)}</div>
<div style="position: absolute; left: 44px; right: 44px; top: 586px; color: {NAVY}; font-size: 27px; font-weight: 600; line-height: 1.17; letter-spacing: -0.8px">Marcou como produzido, entra no estoque. Se vendeu, sai do estoque.</div>'''
    inner = inner.replace("left: 127px; top: 36px", "left: 60px; top: 36px")
    inner += f'''<img src="{U("COX")}" alt="Coxinha de frango" style="position: absolute; left: 336px; top: 170px; width: 160px; height: 200px; object-fit: cover; object-position: 78% 50%; border-radius: 12px">'''
    return box(LBLUE, inner)


# ================= C2 · custo atualiza quando o ingrediente sobe =================
def c2_s1():
    ast = (f'<svg width="30" height="30" viewBox="0 0 24 24" aria-hidden="true" style="flex: none"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7" stroke="{BLUE}" stroke-width="2.4" stroke-linecap="round"></path></svg>')
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 92px; display: flex; flex-direction: column; align-items: center; gap: 26px">
<div style="text-align: center; color: {NAVY}; font-size: 40px; font-weight: 700; line-height: 1.12; letter-spacing: -0.4px; word-spacing: 6px">LEITE CONDENSADO SUBIU?</div>
<div style="display: flex; align-items: center; gap: 14px">{ast}<span style="color: {NAVY}; font-size: 22px; font-weight: 500; line-height: 1.3; max-width: 330px">A precificação dos doces atualiza na hora.</span></div>
</div>
<img src="{U("CXB")}" alt="Caixinhas de brigadeiro de Natal" style="position: absolute; left: 150px; top: 368px; width: 240px; height: 300px; object-fit: cover; border-radius: 10px">'''
    return box(CREAM, inner)


def field(label, value, focus=False):
    st = f"border: 2px solid {BLUE};" if focus else "border: 1px solid #D0D5DD;"
    return f'''<div style="display: flex; flex-direction: column; gap: 6px; margin-top: 16px">
<span style="font-size: 13px; font-weight: 500; color: {SEC}">{label}</span>
<div style="{st} border-radius: 12px; height: 48px; padding: 0 14px; display: flex; align-items: center; font-size: 16px; font-weight: {600 if focus else 400}">{value}</div></div>'''


def ingredient_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
{status_bar()}
<div style="display: flex; align-items: center; gap: 10px; padding: 6px 16px 0">{back}<span style="font-size: 19px; font-weight: 700">Editar ingrediente</span></div>
<div style="padding: 8px 20px 0">
{field("Nome", "Leite condensado")}
{field("Unidade de compra", "Caixa")}
{field("Peso da embalagem", "395 g")}
{field("Preço pago", "R$ 7,29", True)}
<div style="margin-top: 28px; height: 50px; border-radius: 12px; background: {BLUE}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Salvar</div>
</div>
{home_ind()}
</div>'''


def c2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 48px; text-align: center; color: #FFFFFF; font-size: 28px; font-weight: 600; line-height: 1.17; letter-spacing: -0.8px">Atualize o preço do ingrediente uma vez só.</div>
<img src="{U("CXB")}" alt="Brigadeiros" style="position: absolute; left: 36px; top: 330px; width: 170px; height: 220px; object-fit: cover; object-position: 80% 85%; border-radius: 12px">
<div style="position: absolute; left: 222px; top: 176px">{phone(ingredient_screen(), 600)}</div>
<img src="{U("LOGOW")}" alt="receitech" style="position: absolute; left: 36px; bottom: 30px; height: 20px; width: auto">'''
    return box(BLUE, inner)


def ficha_screen():
    s = product_screen()
    s = s.replace(BRIG, U("CXB")).replace("Brigadeiro gourmet</span>", "Brigadeiro</span>")
    s = s.replace('channel_card', '')
    direta = channel_card("DIRETA", "#EBF4FF", "2,25", "1,43", "64%", None, "0,82")
    ifood = channel_card("IFOOD", "#F0F0F0", "3,20", "1,42", "44%", ("R$ 0,96", "30%"), "0,82")
    a = s.index('<div style="margin-top: 22px; display: flex; flex-direction: column; gap: 18px">')
    b = s.index('<div style="margin-top: auto')
    s = s[:a] + f'<div style="margin-top: 22px; display: flex; flex-direction: column; gap: 18px">{direta}{ifood}</div>\n</div>\n' + s[b:]
    return s


def c2_s3():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 46px; display: flex; flex-direction: column; gap: 10px">
<span style="color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.17; letter-spacing: -0.8px">O brigadeiro já aparece com o custo novo: R$ 0,82.</span>
<span style="color: {SEC}; font-size: 16px; line-height: 1.4">E todos os outros doces que levam leite condensado também.</span></div>
<div style="position: absolute; left: 127px; top: 214px">{phone(ficha_screen(), 600)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 28px; bottom: 26px; height: 20px; width: auto">'''
    return box("#FFFFFF", inner)


SLIDES = [
    ("D14_C1_S1", "14/11 · C1 · tela 1 · 12h", c1_s1),
    ("D14_C1_S2", "14/11 · C1 · tela 2 (produção)", c1_s2),
    ("D14_C1_S3", "14/11 · C1 · tela 3 (estoque pronto)", c1_s3),
    ("D14_C2_S1", "14/11 · C2 · tela 1 · 19h", c2_s1),
    ("D14_C2_S2", "14/11 · C2 · tela 2 (ingrediente)", c2_s2),
    ("D14_C2_S3", "14/11 · C2 · tela 3 (ficha do brigadeiro)", c2_s3),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES:
        html = fn()
        if MODE == "canvas":
            doc = page(title, html, PW, PH)
            assert "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
