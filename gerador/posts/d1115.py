"""Posts de 15/11/2026 (2 carrosséis de 3 telas).
C1 sinal da encomenda de Natal (18h) · C2 formas de uso, brownie simples e recheado (20h).
Uso: python3 d1115.py local|canvas [OUT]"""
import json, os, sys
exec(open('/home/claude/receitech-social/gerador/assets/gen.py').read().split("files = {")[0])

MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1115"
os.makedirs(OUT, exist_ok=True)
BANK = "/home/claude/receitech-social/banco-imagens/"
IMGS = {"CXN": "natal_encomenda_1.jpg"}
LOGOS = {"LOGOB": "/home/claude/receitech-social/gerador/posts/logo_dark.png",
         "LOGOW": "/home/claude/receitech-social/gerador/posts/logo_white.png"}
BLOBS = {"LOGOB": "/_blob/f2996fe4c9fb0951e6c5b11ec42e37da", "LOGOW": "/_blob/c900d55a8870af975f0e491905355cb1"}
bf = "/home/claude/receitech-social/gerador/posts/d1115_blobs.json"
if os.path.exists(bf):
    BLOBS.update(json.load(open(bf)))


def U(k):
    if MODE == "canvas":
        return BLOBS[k]
    return "file://" + (LOGOS[k] if k in LOGOS else BANK + IMGS[k])


NAVY, CREAM, SKY = "#101828", "#F3EDE3", "#CFE2FF"
AMBER_BG, AMBER = "#FFFAEB", "#B54708"
POP = "font-family: 'Poppins', sans-serif"
SER = "font-family: 'Libre Caslon Text', Georgia, serif"
ITA = "font-family: 'Instrument Serif', Georgia, serif; font-style: italic"
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Libre+Caslon+Text:wght@400;700&family=Instrument+Serif:ital@0;1&display=swap"


def box(bg, inner):
    return f'<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {bg}; {POP}">{inner}</div>'


def home_ind():
    return f'<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>'


def chip(t, bg="#F2F4F7", fg=SEC):
    return f'<span style="background: {bg}; color: {fg}; font-size: 13px; font-weight: 600; padding: 5px 12px; border-radius: 20px; white-space: nowrap">{t}</span>'


def bottom_nav(active):
    items = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == active else 500}; color: {BLUE if n == active else "#98A2B3"}">{n}</span>' for n in ["Rotina", "Vendas", "Lucro", "Produtos", "Perfil"])
    return f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; background: #FFFFFF; border-top: 1px solid {DIV}; display: flex; justify-content: space-around; padding-top: 14px; box-sizing: border-box">{items}</div>'


# ================= C1 · sinal da encomenda de Natal =================
def c1_s1():
    inner = f'''<div style="position: absolute; left: 40px; right: 40px; top: 50px; {SER}; color: {BLUE}; font-size: 46px; line-height: 1.08; letter-spacing: -1.5px">Encomenda de Natal<br><span style="{ITA}; font-size: 60px; letter-spacing: -0.5px">com sinal.</span> <span style="font-size: 36px">🎄</span></div>
<img src="{U("CXN")}" alt="Mãos segurando uma caixa de bombons de Natal com laço" style="position: absolute; left: 40px; top: 262px; width: 236px; height: 330px; object-fit: cover; object-position: 50% 52%; border-radius: 6px">
<div style="position: absolute; left: 300px; right: 40px; top: 270px; {SER}; color: {BLUE}; font-size: 26px; line-height: 1.22">“Te pago o resto na entrega.”</div>
<div style="position: absolute; left: 300px; right: 40px; top: 470px; color: {NAVY}; font-size: 17px; font-weight: 500; line-height: 1.4">O Receitech anota quanto falta receber de cada cliente.</div>'''
    return box(LBLUE, inner)


def sale_card(cliente, item, entrega, total, status, falta=None):
    if status == "Sinal pago":
        st = chip("Sinal pago", AMBER_BG, AMBER)
    elif status == "Pago":
        st = chip("Pago", "#ECFDF3", "#067647")
    else:
        st = chip(status)
    falta_html = (f'<div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed {DIV}; display: flex; justify-content: space-between; font-size: 16px">'
                  f'<span style="color: {SEC}">Falta receber</span><span style="font-weight: 700; color: {AMBER}">R$ {falta}</span></div>') if falta else ""
    return f'''<div style="border: 1px solid {DIV}; border-radius: 16px; padding: 16px 16px; margin-top: 14px">
<div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 18px; font-weight: 600">{cliente}</span><span style="font-size: 18px; font-weight: 600">R$ {total}</span></div>
<div style="margin-top: 3px; font-size: 15px; color: {SEC}">{item}</div>
<div style="margin-top: 10px; display: flex; justify-content: space-between; align-items: center"><span style="font-size: 14px; color: {SEC}">Entrega {entrega}</span>{st}</div>
{falta_html}</div>'''


def vendas_screen():
    search = svg('<circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path>', 22, DARK, 2)
    chips = (chip("Todas", "#FFFFFF", SEC).replace("background: #FFFFFF;", f"background: #FFFFFF; border: 1px solid {DIV};")
             + chip("Encomendas", DARK, "#FFFFFF")
             + chip("Pronta entrega", "#FFFFFF", SEC).replace("background: #FFFFFF;", f"background: #FFFFFF; border: 1px solid {DIV};"))
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 20px 0"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.5px">Vendas</span>{search}</div>
<div style="display: flex; gap: 8px; padding: 14px 20px 4px">{chips}</div>
<div style="padding: 6px 20px 0">
<span style="font-size: 13px; font-weight: 600; color: {SEC}">Dezembro 2026</span>
{sale_card("Ana Paula", "2 caixas de bombons de Natal", "19 de dezembro", "180,00", "Sinal pago", "90,00")}
{sale_card("Carla", "Cento de docinhos", "20 de dezembro", "150,00", "Pago")}
{sale_card("Mariana", "3 panetones trufados", "22 de dezembro", "210,00", "Sinal pago", "105,00")}
</div>
{bottom_nav("Vendas")}
{home_ind()}
</div>'''


def c1_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 48px; color: {NAVY}; font-size: 27px; font-weight: 600; line-height: 1.18; letter-spacing: -0.8px">Toda encomenda com sinal fica marcada na lista de vendas, com quanto falta.</div>
<div style="position: absolute; left: 40px; top: 186px">{phone(vendas_screen(), 510)}</div>
<img src="{U("CXN")}" alt="Caixa de bombons de Natal" style="position: absolute; left: 318px; top: 300px; width: 180px; height: 230px; object-fit: cover; object-position: 55% 55%; border-radius: 12px">
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 42px; bottom: 30px; height: 20px; width: auto">'''
    return box("#FFFFFF", inner)


def lucro_screen():
    chev = svg('<path d="M6 9l6 6 6-6"></path>', 16, DARK, 2.4)

    def line(n, v, minus=False, bold=False):
        return (f'<div style="display: flex; justify-content: space-between; padding: 10px 0; gap: 10px; font-size: 15px; {"font-weight: 700; border-top: 1px solid " + DIV + ";" if bold else ""}">'
                f'<span style="color: {DARK if bold else SEC}">{"− " if minus else ""}{n}</span><span style="font-weight: {700 if bold else 500}; white-space: nowrap">R$ {v}</span></div>')
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="padding: 4px 20px 0; display: flex; align-items: center; justify-content: space-between"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.5px">Lucro</span>
<span style="display: flex; align-items: center; gap: 4px; font-size: 14px; font-weight: 600">Dezembro 2026 {chev}</span></div>
<div style="padding: 18px 20px 0">
<span style="font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">LUCRO FINAL DO MÊS</span>
<div style="margin-top: 2px; font-size: 38px; font-weight: 700; letter-spacing: -1px">R$ 1.842,30</div>
<div style="margin-top: 14px">
{line("Vendas", "3.120,00")}
{line("Custos de ingredientes e embalagens", "1.050,00", True)}
{line("Gastos do negócio", "227,70", True)}
{line("Lucro final", "1.842,30", bold=True)}
</div>
<div style="margin-top: 18px; background: {AMBER_BG}; border-radius: 16px; padding: 14px 16px">
<div style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 14px; font-weight: 600; color: {AMBER}">A receber</span><span style="font-size: 22px; font-weight: 700; color: {AMBER}">R$ 275,00</span></div>
<div style="margin-top: 6px; font-size: 15px; color: {SEC}; line-height: 1.4">3 encomendas com sinal pago. Entram no lucro do mês quando estiverem pagas e entregues.</div>
</div>
</div>
{bottom_nav("Lucro")}
{home_ind()}
</div>'''


def c1_s3():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 48px; color: #FFFFFF; font-size: 28px; font-weight: 600; line-height: 1.17; letter-spacing: -0.8px">E ela só entra no lucro do mês quando você recebe tudo e entrega.</div>
<img src="{U("CXN")}" alt="Bombons de Natal na caixa" style="position: absolute; left: 40px; top: 300px; width: 172px; height: 230px; object-fit: cover; object-position: 40% 62%; border-radius: 12px">
<div style="position: absolute; left: 232px; top: 190px">{phone(lucro_screen(), 500)}</div>
<img src="{U("LOGOW")}" alt="receitech" style="position: absolute; left: 40px; bottom: 30px; height: 20px; width: auto">'''
    return box(BLUE, inner)


SLIDES = [
    ("D15_C1_S1", "15/11 · C1 · tela 1 · 18h", c1_s1),
    ("D15_C1_S2", "15/11 · C1 · tela 2 (vendas com sinal)", c1_s2),
    ("D15_C1_S3", "15/11 · C1 · tela 3 (a receber no lucro)", c1_s3),
]


def page_f(title, body, w, h):
    return page(title, body, w, h).replace(
        "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap", FONTS.replace("&", "&amp;"))


if __name__ == "__main__":
    for code, title, fn in SLIDES:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "Libre+Caslon" in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
