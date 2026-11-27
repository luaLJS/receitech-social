"""Posts de 27/11/2026.
Post 1 (carrossel, 11h): compras de ingrediente: onde está mais barato (página do insumo, aba Resumo),
foto natal_cesta_1 (cesta de Natal, banco; Chrome sem captura de tela nesta manhã).
Uso: python3 d1127.py local|canvas [OUT]   (env P1V=1 rodada 1 do Post 1)"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1127"
_argv = sys.argv
sys.argv = ["d1126.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1126.py').read().split('\nif __name__ == "__main__"', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

IMGS["CESTA"] = "natal_cesta_1.jpg"
BLOBS["CESTA"] = "/_blob/f165352f08d49c050476ab5f34481c9b"
ALT_CESTA = "Cesta de Natal com laço vermelho, panetone, biscoitos e pote de doce de leite embalados"
ORANGE = "#F79009"
SERIF = "font-family: 'Instrument Serif', Georgia, serif"

# Leite condensado, lata de 395 g. Compra mais recente (24 de novembro, Atacarejo) = preço atual.
# 5,49 / 395 g = R$ 0,0139 por grama -> "R$ 0,014 por grama". Doce de leite: 6 latas x 5,49 = 32,94.
assert round(5.49 / 395, 3) == 0.014 and round(6 * 5.49, 2) == 32.94


def insumo_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 22, DARK, 2.4)
    dots = svg('<circle cx="12" cy="5" r="1.4"></circle><circle cx="12" cy="12" r="1.4"></circle><circle cx="12" cy="19" r="1.4"></circle>', 22, DARK, 2)
    can = svg('<ellipse cx="12" cy="6" rx="7" ry="2.5"></ellipse><path d="M5 6v12c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5V6"></path>', 18, BLUE, 2)
    cake = svg('<path d="M4 21h16"></path><path d="M5 21v-8h14v8"></path><path d="M5 13c2 1.5 4 1.5 7 0s5-1.5 7 0"></path><path d="M12 9V5"></path>', 18, BLUE, 2)
    cap = lambda t: f'<div style="margin-top: 26px; font-size: 12px; font-weight: 600; letter-spacing: 1.2px; color: #98A2B3">{t}</div>'

    def place(name, pkg, best=False):
        badge = f'<span style="padding: 3px 9px; border-radius: 10px; background: #ECFDF3; color: {GREEN}; font-size: 11px; font-weight: 600">Mais barato</span>' if best else ""
        return f'''<div style="display: flex; align-items: center; gap: 10px; padding: 11px 0; border-bottom: 1px solid {DIV}">
<div style="flex: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 15px; font-weight: 600">{name}</span>
<span style="font-size: 12px; color: {SEC}">{pkg}</span></div>{badge}</div>'''

    def buy(name, val, sub, atual=False):
        tag = f'<span style="margin-left: 6px; padding: 2px 7px; border-radius: 8px; background: {LBLUE}; color: {BLUE}; font-size: 10px; font-weight: 600">pacote atual</span>' if atual else ""
        return f'''<div style="display: flex; align-items: center; gap: 10px; padding: 10px 0; border-bottom: 1px solid {DIV}">
<div style="width: 36px; height: 36px; border-radius: 10px; background: {LBLUE}; display: flex; align-items: center; justify-content: center; flex: none">{can}</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 14px; font-weight: 600">{name}{tag}</span>
<span style="font-size: 12px; color: {SEC}">{sub}</span></div>
<span style="font-size: 16px; font-weight: 500">R$ {val}</span></div>'''

    thumb = (f'<div style="width: 44px; height: 44px; border-radius: 12px; overflow: hidden; position: relative; flex: none">'
             f'<img src="{U("CESTA")}" alt="Pote de doce de leite" style="position: absolute; left: -96px; top: -128px; width: 260px; height: 260px"></div>')
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="padding: 4px 16px 0; display: flex; align-items: center; gap: 10px">{back}<span style="flex: 1; font-size: 18px; font-weight: 600">Leite condensado</span>{dots}</div>
<div style="margin-top: 14px; display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid {DIV}; font-size: 15px; text-align: center">
<span style="padding-bottom: 10px; color: #98A2B3; font-weight: 500">Editar</span>
<span style="padding-bottom: 8px; font-weight: 700; color: {BLUE}; border-bottom: 2px solid {BLUE}">Resumo</span></div>
<div style="padding: 18px 20px 0">
<div style="font-size: 13px; color: {SEC}">Atualizado em 24 de novembro</div>
<div style="margin-top: 4px; font-size: 24px; font-weight: 700; letter-spacing: -0.5px">R$ 5,49 a lata de 395 g</div>
<div style="margin-top: 2px; font-size: 13px; color: {SEC}">Nas receitas, R$ 0,014 por grama.</div>
{cap("ONDE ESTÁ MAIS BARATO")}
{place("Atacarejo", "Lata de 395 g por R$ 5,49", True)}
{place("Supermercado do centro", "Lata de 395 g por R$ 5,89")}
{place("Mercadinho da rua", "Lata de 395 g por R$ 6,90")}
{cap("ÚLTIMAS COMPRAS")}
{buy("Atacarejo", "5,49", "Lata de 395 g · 24 de novembro", True)}
{buy("Mercadinho da rua", "6,90", "Lata de 395 g · 18 de novembro")}
{buy("Supermercado do centro", "5,89", "Lata de 395 g · 9 de novembro")}
{cap("RECEITAS QUE USAM")}
<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0">{thumb}
<div style="flex: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 14px; font-weight: 600">Doce de leite de pote</span>
<span style="font-size: 12px; color: {SEC}">Usa 6 latas · R$ 32,94 do custo</span></div></div>
</div></div>'''


P1T = {
    "a": "O Receitech mostra em qual mercado o seu leite condensado sai mais barato.",
    "b": "Leite condensado, chocolate, caixinha: o Receitech mostra onde cada um sai mais barato.",
    "c": "Anotou a compra do mercado? O Receitech mostra onde cada ingrediente sai mais barato.",
}
P1S2 = "Cada compra anotada atualiza o custo das receitas. E mostra onde está mais barato."


def rings(n=7, top=34, gap=44):
    return "".join(f'<div style="position: absolute; left: -9px; top: {top + i * gap}px; width: 22px; height: 8px; border-radius: 4px; background: #98A2B3"></div>' for i in range(n))


def p1_n7(k, size=41):
    """N7 (ref. 5 Canva Apps): folha de caderno reta sobre a foto; texto em serifa azul na folha."""
    inner = f'''<img src="{U("CESTA")}" alt="{ALT_CESTA}" style="position: absolute; left: -110px; top: 0; width: 760px; height: 760px; object-fit: cover">
<div style="position: absolute; left: 70px; right: 70px; top: 50px; height: 320px; background: #FBF8F2; border-radius: 6px; box-shadow: 0 14px 30px rgba(16,24,40,0.28)">
{rings(6, 34, 44)}
<div style="position: absolute; left: 34px; right: 26px; top: 0; bottom: 0; display: flex; align-items: center; justify-content: center; text-align: center; {SERIF}; color: {BLUE}; font-size: {size}px; line-height: 1.12">{P1T[k]}</div></div>'''
    return box(NAVY, inner)


def p1_t7(k):
    """T7 (ref. Do I really need a website?): título grande em cima à esquerda + objeto no canto de baixo; creme."""
    words = P1T[k]
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">RECEITECH</div>
<div style="position: absolute; left: 44px; right: 44px; top: 72px; {POP}; color: {NAVY}; font-size: 33px; font-weight: 700; line-height: 1.12; letter-spacing: -1.1px">{words}</div>
<img src="{U("CESTA")}" alt="{ALT_CESTA}" style="position: absolute; right: 40px; bottom: 40px; width: 330px; height: 380px; object-fit: cover; object-position: 50% 75%; border-radius: 16px">'''
    return box(CREAM, inner)


def p1_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 46px; color: {NAVY}; font-size: 27px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{P1S2}</div>
<div style="position: absolute; left: 50%; top: 178px; transform: translateX(-50%)">{phone(insumo_screen(), 510)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 26px; height: 20px; width: auto">'''
    return box(CREAM, inner)


SLIDES27P1 = [
    ("D27_P1_T1a", "27/11 · P1 · tela 1 · 1.1 (N7)", lambda: p1_n7("a")),
    ("D27_P1_T1b", "27/11 · P1 · tela 1 · 1.2 (N7)", lambda: p1_n7("b", 37)),
    ("D27_P1_T1c", "27/11 · P1 · tela 1 · 1.3 (N7)", lambda: p1_n7("c", 37)),
    ("D27_P1_T1t7", "27/11 · P1 · tela 1 · 1.4 layout T7 (frase 1.1)", lambda: p1_t7("a")),
    ("D27_P1_S2", "27/11 · P1 · tela 2 (Leite condensado: onde está mais barato)", p1_s2),
]

if __name__ == "__main__":
    if os.environ.get("P1V"):
        emit(SLIDES27P1)
    print("ok", MODE, OUT)
