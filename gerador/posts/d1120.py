"""Posts de 20/11/2026. Post 1: orçamento de encomenda (retomado do P2 de 19/11), opção 2 (b).
Uso: python3 d1120.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1120"
_argv = sys.argv
sys.argv = ["d1119.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1119.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

P2_PICK = "b"
S2_OLD = "Os preços já vêm dos seus produtos. Aceitaram? Um toque e vira encomenda."
S2_NEW = "Aceitaram? Toque em “Confirmar encomenda” e ela já entra com cliente, data e valor."


def d20_p1_s2(new=True):
    h = d19_p2_s2()
    return h.replace(S2_OLD, S2_NEW) if new else h


SLIDES20 = [
    ("D20_P1_S1", "20/11 · P1 · tela 1 (N5)", lambda: p2_n5("b")),
    ("D20_P1_S2", "20/11 · P1 · tela 2 (orçamento)", d20_p1_s2),
    ("D20_P1_S2_old", "20/11 · P1 · tela 2 (texto de ontem)", lambda: d20_p1_s2(False)),
]


# ================= Post 2 · mais de uma receita no mesmo produto =================
IMGS["MORANGO"] = "doce_bolomorango_1.jpg"
BLOBS["MORANGO"] = "/_blob/3da723bdcc5dc0cad4c2c77e85d0165a"
ALT_MOR = "Fatia de bolo de morango com massa branca, recheio de creme e geleia, chantilly e morangos"
P2_OPTS = {
    "a": ("Massa, recheio e cobertura.", "Cada um com o seu custo.", "No Receitech, o bolo recheado junta as três receitas e mostra quanto custa o bolo inteiro."),
    "b": ("Bolo recheado leva 3 receitas.", "O custo também.", "No Receitech, você monta o produto com várias receitas e o custo soma todas."),
    "c": ("Quanto custa só o recheio", "do seu bolo?", "No Receitech, cada parte do bolo tem a sua receita, e o custo do bolo junta todas."),
}


def p2_n1(k):
    """N1: texto pesado + etiquetas. Fundo branco, foto reta no centro, etiquetas retas nas camadas."""
    t1, t2, sub = P2_OPTS[k]

    def pill(t, bg, fg, css):
        return f'<span style="position: absolute; {css}; padding: 6px 15px; border-radius: 30px; background: {bg}; color: {fg}; {POP}; font-size: 15px; font-weight: 600; box-shadow: 0 2px 8px rgba(16,24,40,0.12)">{t}</span>'
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 34px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 4px; color: {NAVY}">RECEITECH</div>
<div style="position: absolute; left: 34px; right: 34px; top: 62px; text-align: center; {HVY}; font-weight: 900; color: {NAVY}; font-size: 46px; line-height: 0.98; letter-spacing: -2px; text-wrap: balance">{t1} <span style="color: {BLUE}">{t2}</span></div>
<img src="{U("MORANGO")}" alt="{ALT_MOR}" style="position: absolute; left: 110px; top: 214px; width: 320px; height: 400px; object-fit: cover; object-position: 50% 50%; border-radius: 14px">
{pill("cobertura", "#FFE58F", NAVY, "left: 52px; top: 362px")}{pill("recheio", "#B8F5C9", NAVY, "right: 58px; top: 474px")}{pill("massa", BLUE, "#FFFFFF", "left: 66px; top: 534px")}
<div style="position: absolute; left: 50px; right: 50px; bottom: 34px; text-align: center; font-size: 15px; font-weight: 600; line-height: 1.35; color: {NAVY}">{sub}</div>'''
    return box("#FFFFFF", inner)


def p2_t7(k):
    """T7: título + objeto no canto (a foto reta no canto, no lugar do celular)."""
    t1, t2, sub = P2_OPTS[k]
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 46px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 3px; color: {NAVY}">RECEITECH</div>
<div style="position: absolute; left: 46px; right: 46px; top: 92px; {POP}; color: {NAVY}; font-size: 36px; font-weight: 700; line-height: 1.12; letter-spacing: -1.3px">{t1} <span style="{ITA}; font-weight: 400; font-size: 44px; letter-spacing: -0.4px">{t2}</span></div>
<div style="position: absolute; left: 46px; top: 300px; width: 200px; {POP}; color: {NAVY}; font-size: 16px; line-height: 1.4">{sub}</div>
<img src="{U("MORANGO")}" alt="{ALT_MOR}" style="position: absolute; right: 0; bottom: 0; width: 270px; height: 338px; object-fit: cover; border-top-left-radius: 18px">'''
    return box(LBLUE, inner)


def receitas_screen():
    back = svg('<path d="M15 5l-7 7 7 7"></path>', 20, DARK, 2.4)
    chev = svg('<path d="M9 5l7 7-7 7"></path>', 16, SEC, 2)

    def row(n, sub, v):
        return (f'<div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid {DIV}">'
                f'<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {SEC}">{sub}</span></div>'
                f'<div style="display: flex; align-items: center; gap: 6px"><span style="font-size: 16px; font-weight: 600; white-space: nowrap">R$ {v}</span>{chev}</div></div>')

    def head(t):
        return f'<div style="padding: 16px 0 0; font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">{t}</div>'
    tab_on = f'flex: 1; text-align: center; padding: 8px 0; border-radius: 10px; background: #FFFFFF; font-weight: 600; box-shadow: 0 1px 3px rgba(16,24,40,0.1)'
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="height: 48px; display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; padding: 0 6px">
<div style="display: flex; justify-content: center">{back}</div><span style="text-align: center; font-size: 18px; font-weight: 700">Bolo de morango</span><span></span></div>
<div style="margin: 4px 20px 0; display: flex; padding: 4px; border-radius: 12px; background: #F2F4F7; font-size: 15px; color: {SEC}"><span style="flex: 1; text-align: center; padding: 8px 0">Editar</span><span style="{tab_on}; color: {DARK}">Resumo</span></div>
<div style="padding: 14px 20px 0; display: flex; gap: 14px; align-items: center">
<img src="{U("MORANGO")}" alt="Bolo de morango" style="width: 60px; height: 60px; border-radius: 14px; object-fit: cover">
<div style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 20px; font-weight: 700; letter-spacing: -0.4px">Bolo de morango</span>
<span style="font-size: 14px; color: {SEC}">Inteiro, 2 kg</span></div></div>
<div style="padding: 2px 20px 0">
{head("RECEITAS NESTE PRODUTO")}
{row("Massa branca", "1 receita", "16,40")}
{row("Recheio de creme com geleia", "1 receita", "19,80")}
{row("Chantilly com morangos", "1 receita", "24,60")}
{head("EMBALAGEM")}
{row("Caixa e base para bolo", "1 de cada", "7,20")}
<div style="margin-top: 14px; border-radius: 16px; background: {LBLUE}; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center">
<span style="font-size: 15px; font-weight: 500">Custo do bolo</span><span style="font-size: 22px; font-weight: 700; color: {BLUE}">R$ 68,00</span></div>
<div style="display: flex; justify-content: space-between; padding: 14px 2px 4px; font-size: 15px"><span>Preço de venda</span><span style="font-weight: 600">R$ 180,00</span></div>
<div style="display: flex; justify-content: space-between; padding: 4px 2px; font-size: 15px"><span>Lucro por produto</span><span style="font-weight: 700; color: #067647">R$ 112,00</span></div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


P2_S2_TXT = "Cada parte tem a sua receita. O custo do bolo junta tudo, até a caixa."


def p2_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{P2_S2_TXT}</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(receitas_screen(), 500)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(SKY, inner)


SLIDES20B = [
    ("D20_P2_opA", "20/11 · P2 · opção a (N1)", lambda: p2_n1("a")),
    ("D20_P2_opB", "20/11 · P2 · opção b (N1)", lambda: p2_n1("b")),
    ("D20_P2_opC", "20/11 · P2 · opção c (N1)", lambda: p2_n1("c")),
    ("D20_P2_T7", "20/11 · P2 · layout alternativo (T7, frase a)", lambda: p2_t7("a")),
    ("D20_P2_S2", "20/11 · P2 · tela 2 (receitas do produto)", p2_s2),
]

if __name__ == "__main__":
    for code, title, fn in (SLIDES20B if os.environ.get('P2') else SLIDES20):
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
