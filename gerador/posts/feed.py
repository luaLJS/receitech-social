"""Feed proposto: 9 capas, cada uma copiando o layout de uma referência da Luana, nas cores do Receitech."""
import json, os
exec(open('/home/claude/assets/gen.py').read().split("files = {")[0])
ROOT2 = "/mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project"

A = {  # asset url -> local file (pra prévia)
    "PAN": ("/_blob/d09537f0aaea7ebf87458d390c0973c2", "/home/claude/cut2/panetone_s.png"),
    "RAB": ("/_blob/368aaf8c3fdf4fdc327f9df0a1af8e84", "/home/claude/cut2/rabanada_s.png"),
    "BRG": ("/_blob/966bc7eb61d56942585082ee9bbb5162", "/home/claude/cut2/brig_single_s.png"),
    "BIS": ("/_blob/81506860bca52ffbcd00795f6aaa7940", "/home/claude/cut2/biscoitos_s.png"),
    "CAS": ("/_blob/9cdca5c0ccd849cbf1deb9d85edbe7e9", "/home/claude/cut2/casadinho_s.png"),
    "CHO": ("/_blob/1b5a17fbb7cbd63005c01243d178d806", "/home/claude/cut2/chocotone_s.png"),
    "CX2": ("/_blob/d2f74279467fb93c3c1095ca4848e1ab", "/home/claude/cut2/caixa2_full.jpg"),
    "PAO": ("/_blob/dfc3cd9c8811429deaebd3bb6fe65239", "/home/claude/fotos/paodemel_full.jpg"),
    "CX1F": ("/_blob/70ca3d6b36ae60563041ade9ecaa3fd8", "/home/claude/fotos/caixa1_full.jpg"),
    "CASF": ("/_blob/8ae1036d486554ad5cf3daa9a912669d", "/home/claude/fotos/casadinho_full.jpg"),
    "CHOF": ("/_blob/84b72941bbb57b11ac27e98dfee38ae1", "/home/claude/fotos/chocotone_full.jpg"),
    "BOLF": ("/_blob/d880039d46d27947bd42085a73f2e52b", "/home/claude/fotos/bolo_full.jpg"),
    "RABF": ("/_blob/db1be0e2412aafeff19ec7f5ac62ec49", "/home/claude/fotos/rabanada_full.jpg"),
    "LOGOW": ("/_blob/c900d55a8870af975f0e491905355cb1", "/home/claude/posts/logo_white.png"),
    "LOGOB": ("/_blob/f2996fe4c9fb0951e6c5b11ec42e37da", "/home/claude/posts/logo_dark.png"),
}
U = {k: v[0] for k, v in A.items()}

NAVY, BLUE, LB, SKY, CREAM = "#101828", "#3D86F7", "#EBF5FF", "#CFE2FF", "#F3EDE3"
POP = "font-family: 'Poppins', sans-serif"
SER = "font-family: 'Libre Caslon Text', Georgia, serif"
ITA = "font-family: 'Instrument Serif', Georgia, serif; font-style: italic"
HVY = "font-family: 'Inter Tight', 'Poppins', sans-serif"
CND = "font-family: 'Anton', 'Inter Tight', sans-serif"
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500;1,600&family=Libre+Caslon+Text:wght@400;700&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@800;900&family=Anton&display=swap"

STICKER = "filter: drop-shadow(4px 0 0 #fff) drop-shadow(-4px 0 0 #fff) drop-shadow(0 4px 0 #fff) drop-shadow(0 -4px 0 #fff) drop-shadow(0 8px 14px rgba(16,24,40,0.15))"


def box(bg, inner, extra=""):
    return f'<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {bg}; {extra}">{inner}</div>'


def hand_arrow(c, w=190):
    return (f'<svg width="{w}" height="48" viewBox="0 0 190 48" aria-hidden="true">'
            f'<path d="M6 27 C 50 22, 104 30, 168 23" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"></path>'
            f'<path d="M144 8 C 156 14, 166 19, 180 23 C 166 28, 156 34, 146 41" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"></path></svg>')


# T2 — referência "The Symple Method": creme, serifa centralizada, seta desenhada
def t_serif():
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 64px; text-align: center; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 4px; color: {BLUE}">RECEITECH</div>
<div style="position: absolute; left: 40px; right: 40px; top: 0; bottom: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 22px; text-align: center; {SER}; color: {NAVY}; font-size: 34px; line-height: 1.22; letter-spacing: -0.6px">
<span>Encomenda de Natal fechada.</span>
<span>Agora vem a parte que mais dá prejuízo.</span>
<div style="margin-top: 28px">{hand_arrow(BLUE)}</div>
</div>'''
    return box(CREAM, inner)


# T6 — referência "Esenciales": fundo colorido, título itálico, recortes com contorno branco em volta do centro
def t_colagem():
    def stk(k, l, t, w, r):
        return f'<img src="{U[k]}" alt="" style="position: absolute; left: {l}px; top: {t}px; width: {w}px; height: auto; transform: rotate({r}deg); {STICKER}">'
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 92px; text-align: center; {POP}; font-style: italic; font-weight: 500; font-size: 40px; letter-spacing: -1.4px; color: #FFFFFF">ENCOMENDAS DE NATAL</div>
<div style="position: absolute; left: 172px; top: 196px; transform: rotate(-3deg)">{phone(product_screen(), 440)}</div>
{stk("PAN", 40, 200, 150, -8)}{stk("BIS", 362, 196, 150, 9)}{stk("RAB", 30, 430, 160, 6)}{stk("CAS", 370, 470, 140, -7)}{stk("BRG", 200, 600, 140, 4)}'''
    return box("#9EC3FF", inner)


# T8 — referência "what you get as a client": foto inteira, texto branco no alto à esquerda, selo redondo
def t_foto_texto():
    inner = f'''<img src="{U["CX2"]}" alt="Caixa de brigadeiros de Natal" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover">
<div style="position: absolute; left: 0; right: 0; top: 0; height: 300px; background: linear-gradient(rgba(16,24,40,0.45), rgba(16,24,40,0))"></div>
<div style="position: absolute; left: 44px; right: 120px; top: 56px; {POP}; color: #FFFFFF; font-size: 36px; font-weight: 600; line-height: 1.12; letter-spacing: -1.2px">Antes de vender o próximo brigadeiro, veja isso.</div>
<div style="position: absolute; right: 36px; bottom: 40px; width: 92px; height: 92px; border-radius: 46px; background: {BLUE}; display: flex; align-items: center; justify-content: center; text-align: center; transform: rotate(-12deg); {POP}; color: #FFFFFF; font-size: 15px; font-weight: 600; line-height: 1.1">próxima<br>tela</div>'''
    return box(NAVY, inner)


# T5 — referência "I DON'T NEED SOCIAL MEDIA": frase em caixa alta centralizada + asterisco e texto pequeno
def t_citacao():
    ast = ('<svg width="40" height="40" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"></path></svg>')
    inner = f'''<div style="position: absolute; left: 34px; right: 34px; top: 0; bottom: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 34px">
<div style="{POP}; text-align: center; color: #FFFFFF; font-size: 38px; font-weight: 700; line-height: 1.18; letter-spacing: -0.5px; word-spacing: 10px">“EU JÁ SEI QUANTO COBRAR.”</div>
<div style="display: flex; align-items: center; gap: 16px">{ast}<span style="{POP}; color: #FFFFFF; font-size: 17px; line-height: 1.35; max-width: 240px">Será? Tem um custo que quase ninguém coloca no preço.</span></div>
</div>'''
    return box(BLUE, inner)


# T3 — referência "Brand-Kit Worthy Fonts": foto inteira, serifa itálica grande centralizada
def t_foto_serif():
    inner = f'''<img src="{U["PAO"]}" alt="Pães de mel de Natal" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.28)"></div>
<div style="position: absolute; left: 0; right: 0; top: 46px; text-align: center; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 4px; color: #FFF4D2">RECEITECH</div>
<div style="position: absolute; left: 40px; right: 40px; top: 0; bottom: 0; display: flex; align-items: center; justify-content: center; text-align: center; {ITA}; color: #FFF4D2; font-size: 60px; line-height: 1.02; letter-spacing: -0.5px">Tem um motivo pro Natal não dar lucro.</div>'''
    return box(NAVY, inner)


# T1 — referência "This Month's Favorites": título pesado, 2x2 numerado de recortes, rodapé
def t_favoritos():
    def item(n, k, w):
        return f'''<div style="position: relative; height: 210px; display: flex; align-items: center; justify-content: center">
<span style="position: absolute; left: 6px; top: 4px; {POP}; font-size: 17px; color: {NAVY}">{n}</span>
<img src="{U[k]}" alt="" style="max-width: {w}px; max-height: 180px"></div>'''
    inner = f'''<div style="position: absolute; left: 30px; right: 30px; top: 52px; text-align: center; {HVY}; font-weight: 900; color: {NAVY}; font-size: 58px; line-height: 0.92; letter-spacing: -3px">O Natal de quem vende</div>
<div style="position: absolute; left: 50px; right: 50px; top: 196px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px 18px">
{item("01", "PAN", 190)}{item("02", "RAB", 200)}{item("03", "BIS", 210)}{item("04", "CHO", 210)}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 34px; text-align: center; {HVY}; font-weight: 800; color: {NAVY}; font-size: 21px; letter-spacing: -0.8px">Qual deles dá mais lucro? <span style="color: {BLUE}">›</span></div>'''
    return box("#FFFFFF", inner)


# T7 — referência "Do I really need a website?": título com palavra em serifa itálica, objeto no canto de baixo
def t_titulo_objeto():
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 54px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 3px; color: {NAVY}">RECEITECH</div>
<div style="position: absolute; left: 46px; right: 46px; top: 104px; {POP}; color: {NAVY}; font-size: 36px; font-weight: 700; line-height: 1.12; letter-spacing: -1.3px">Encomenda pelo WhatsApp <span style="{ITA}; font-weight: 400; font-size: 44px; letter-spacing: -0.4px">tem um problema.</span></div>
<div style="position: absolute; left: 46px; top: 268px; {POP}; color: {NAVY}; font-size: 17px">E tem como evitar.</div>
<div style="position: absolute; left: 236px; top: 330px; transform: rotate(-8deg)">{phone(product_screen(), 560)}</div>'''
    return box(LB, inner)


# T4 — referência "get people talking about your brand.": recortes no topo, texto pesado à esquerda, última palavra colorida
def t_bold():
    inner = f'''<div style="position: absolute; left: 46px; right: 46px; top: 46px; display: flex; justify-content: space-between; align-items: center">
<img src="{U["CAS"]}" alt="" style="height: 96px; width: auto"><img src="{U["BRG"]}" alt="" style="height: 96px; width: auto"><img src="{U["CHO"]}" alt="" style="height: 96px; width: auto"></div>
<div style="position: absolute; left: 50px; right: 40px; top: 196px; {POP}; color: {NAVY}; font-size: 54px; font-weight: 800; line-height: 1.02; letter-spacing: -2.4px">vender brigadeiro a R$ 2 parece <span style="color: {BLUE}">lucro.</span></div>
<div style="position: absolute; left: 50px; bottom: 48px; {POP}; color: {NAVY}; font-size: 15px">Até ver o que ninguém mostra.</div>'''
    return box("#F2F2F0", inner)


# T9 — referência "according to my calculations...": texto pequeno + serifa itálica, objeto grande embaixo, reto
def t_contas():
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 76px; text-align: center; {POP}; color: #FFFFFF; font-size: 17px; font-weight: 500">o lucro de dezembro</div>
<div style="position: absolute; left: 40px; right: 40px; top: 108px; text-align: center; {ITA}; color: #FFFFFF; font-size: 50px; line-height: 1.04">depende de uma coisa só...</div>
<div style="position: absolute; left: 50%; margin-left: -125px; top: 300px">{phone(product_screen(), 540)}</div>'''
    return box(NAVY, inner)


TILES = [
    ("T2", "Serifa centralizada", "ref. The Symple Method", t_serif),
    ("T6", "Colagem de recortes", "ref. Esenciales", t_colagem),
    ("T8", "Foto inteira + texto", "ref. what you get as a client", t_foto_texto),
    ("T5", "Frase em caixa alta", "ref. I don't need social media", t_citacao),
    ("T3", "Foto + serifa itálica", "ref. Brand-Kit Worthy Fonts", t_foto_serif),
    ("T1", "Título + 4 recortes", "ref. This Month's Favorites", t_favoritos),
    ("T7", "Título + objeto no canto", "ref. Do I really need a website?", t_titulo_objeto),
    ("T4", "Texto pesado + palavra azul", "ref. get people talking", t_bold),
    ("T9", "Frase + objeto embaixo", "ref. according to my calculations", t_contas),
]


exec(open('/home/claude/posts/feed_new.py').read())
TILES = TILES + NEW_TILES


def feed_board():
    tw = 340
    s = tw / PW
    th = round(PH * s)
    cells = "".join(
        f'<div style="width: {tw}px; height: {th}px; overflow: hidden; position: relative"><div style="width: {PW}px; height: {PH}px; transform: scale({s:.5f}); transform-origin: 0 0">{fn()}</div></div>'
        for _, _, _, fn in TILES)
    header = f'''<div style="display: flex; align-items: center; gap: 22px; padding: 30px 26px 18px">
<div style="width: 92px; height: 92px; border-radius: 46px; background: {BLUE}; display: flex; align-items: center; justify-content: center"><img src="{U["LOGOW"]}" alt="receitech" style="width: 70px; height: auto"></div>
<div style="display: flex; flex-direction: column; gap: 4px; {POP}"><span style="font-size: 20px; font-weight: 600; color: {NAVY}">receitech_</span>
<span style="font-size: 14px; color: #475467">Preço, encomendas e lucro pra quem faz e vende doces, bolos e salgados.</span></div></div>
<div style="display: flex; justify-content: space-around; border-top: 1px solid #EAECF0; padding: 12px 0; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 1px; color: {NAVY}"><span>POSTS</span><span style="color: #98A2B3">REELS</span><span style="color: #98A2B3">MARCADOS</span></div>'''
    grid = f'<div style="display: grid; grid-template-columns: repeat(3, {tw}px); gap: 4px; padding: 0 26px 30px">{cells}</div>'
    rows = (len(TILES) + 2) // 3
    return f'<div style="width: 1080px; background: #FFFFFF">{header}{grid}</div>', 190 + rows * th + (rows - 1) * 4 + 30


def page2(title, body, w, h):
    return f'''<!doctype html>
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
<link href="{FONTS.replace('&', '&amp;')}" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>'''


def local(html):
    for _, (u, p) in A.items():
        html = html.replace(u, p)
    return f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>"


if __name__ == "__main__":
    fb, fh = feed_board()
    out = [("Feed.dc.html", "Feed proposto", fb, 1080, fh)]
    for code, name, ref, fn in TILES:
        out.append((f"Feed_{code}.dc.html", f"{code} · {name} ({ref})", fn(), PW, PH))
    for fn_, title, html, w, h in out:
        open(os.path.join(ROOT2, fn_), "w").write(page2(title, html, w, h))
        open(f"/home/claude/posts/prev_{fn_.split('.')[0]}.html", "w").write(local(html))
    json.dump([(o[0], o[1], o[3], o[4]) for o in out], open("/home/claude/posts/feed_boards.json", "w"))
    print("ok", fh)
