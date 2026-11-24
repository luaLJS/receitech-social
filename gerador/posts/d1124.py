"""Posts de 24/11/2026.
Post 1 (foto única, 11h): taxa do cartão repassada ao cliente (retomado do P2 de 23/11, N6, pudim) -> ver d1123.py NEW.
Post 2 (carrossel, 18h): investimentos no negócio (batedeira nova fica fora do lucro do mês), N5 ou N4, pão de mel.
Uso: [FINAL=1] python3 d1124.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1124"
_argv = sys.argv
sys.argv = ["d1123.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1123.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

IMGS["MEL"] = "natal_paodemel_1.jpg"
BLOBS["MEL"] = "/_blob/PENDENTE_MEL"
ALT_MEL = "Pão de mel de Natal coberto de chocolate, um deles mordido mostrando o recheio de doce de leite"

# ================= Post 2 · investimentos no negócio =================
P2B = {
    "a": ("DEZ", "BATEDEIRA NOVA NÃO É GASTO DO MÊS"),
    "b": ("DEZ", "COMPROU FORNO PRO NATAL? O LUCRO NÃO CAI POR ISSO"),
    "c": ("DEZ", "EQUIPAMENTO NOVO FICA FORA DO LUCRO DO MÊS"),
}
SUB_INV = "No Receitech, batedeira, forno e freezer entram como investimento: aparecem à parte e não diminuem o lucro do mês."
S2_INV = "A batedeira fica em Investimentos. O lucro de dezembro mostra o que as vendas renderam."


def p2_n5(k):
    big, title = P2B[k]
    inner = f'''<div style="position: absolute; left: 22px; right: 22px; top: 22px; bottom: 22px; border-radius: 28px; background: {BLUE}"></div>
<div style="position: absolute; left: 50px; top: 50px; {CND}; color: #FFFFFF; font-size: 50px; line-height: 1">{big}</div>
<div style="position: absolute; left: 150px; right: 50px; top: 50px; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; color: {SKY}">RECEITECH MOSTRA</div>
<div style="position: absolute; left: 150px; right: 46px; top: 66px; {CND}; color: #FFFFFF; font-size: 31px; line-height: 1.02">{title}</div>
<img src="{U("MEL")}" alt="{ALT_MEL}" style="position: absolute; left: 50px; top: {168 if k != "b" else 176}px; width: 440px; height: {400 if k != "b" else 392}px; object-fit: cover; object-position: 50% 55%; border-radius: 16px">
<div style="position: absolute; left: 56px; right: 56px; bottom: 44px; text-align: center; font-size: 14px; font-weight: 600; line-height: 1.35; color: #FFFFFF">{SUB_INV}</div>'''
    return box("#FFFFFF", inner)


def p2_n4(k):
    big, title = P2B[k]
    inner = f'''<img src="{U("MEL")}" alt="{ALT_MEL}" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover; object-position: 50% 50%; filter: blur(9px); transform: scale(1.08)">
<div style="position: absolute; inset: 0; background: rgba(16,24,40,0.30)"></div>
<div style="position: absolute; left: 40px; right: 40px; top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; gap: 22px">
<div style="font-weight: 600; color: #FFFFFF; font-size: 46px; line-height: 1.06; letter-spacing: 0.5px; text-shadow: 0 1px 12px rgba(0,0,0,0.3)">{title}</div>
<div style="color: #FFFFFF; font-size: 18px; font-weight: 500; line-height: 1.35; text-shadow: 0 1px 10px rgba(0,0,0,0.35)">{SUB_INV}</div></div>
<img src="{U("LOGOW")}" alt="receitech" style="position: absolute; left: 50%; margin-left: -45px; bottom: 34px; width: 90px; height: auto">'''
    return box(NAVY, inner)


def lucro_inv_screen():
    chev = svg('<path d="M6 9l6 6 6-6"></path>', 16, DARK, 2.4)
    GRN = "#067647"

    def line(n, v, minus=False, bold=False, top=False):
        return (f'<div style="display: flex; justify-content: space-between; padding: 8px 0; gap: 10px; font-size: 15px; {"font-weight: 700; border-top: 1px solid " + DIV + ";" if top else ""}">'
                f'<span style="color: {DARK if bold else SEC}">{"− " if minus else ""}{n}</span><span style="font-weight: {700 if bold else 500}; white-space: nowrap">R$ {v}</span></div>')
    items = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == "Lucro" else 500}; color: {BLUE if n == "Lucro" else "#98A2B3"}">{n}</span>' for n in ["Rotina", "Vendas", "Lucro", "Produtos", "Perfil"])
    mixer = svg('<path d="M6 4h9a3 3 0 0 1 3 3v1H6z"></path><path d="M9 8v4"></path><path d="M7 12h6l-1 4H8z"></path><path d="M5 20h14"></path>', 22, "#6B4F3A", 1.8)
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="padding: 4px 20px 0; display: flex; align-items: center; justify-content: space-between"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.5px">Lucro</span>
<span style="display: flex; align-items: center; gap: 4px; font-size: 14px; font-weight: 600">Dezembro 2026 {chev}</span></div>
<div style="padding: 16px 20px 0">
<span style="font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">LUCRO FINAL DO MÊS</span>
<div style="margin-top: 2px; font-size: 38px; font-weight: 700; letter-spacing: -1px; color: {GRN}">R$ 3.780,00</div>
<div style="margin-top: 8px">
{line("Vendas", "7.200,00")}
{line("Custos de ingredientes e embalagens", "2.520,00", True)}
{line("Resultado das vendas", "4.680,00", bold=True, top=True)}
{line("Gastos do negócio", "900,00", True)}
{line("Lucro final", "3.780,00", bold=True, top=True)}
</div>
<div style="margin-top: 16px; border: 1px solid {DIV}; border-radius: 16px; padding: 14px 16px">
<div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 13px; font-weight: 600; color: {SEC}; letter-spacing: 0.4px">INVESTIMENTOS NO NEGÓCIO</span><span style="font-size: 13px; font-weight: 600; color: {BLUE}">Ver todos</span></div>
<div style="margin-top: 6px; font-size: 22px; font-weight: 700; letter-spacing: -0.5px">R$ 1.890,00 <span style="font-size: 14px; font-weight: 500; color: {SEC}; letter-spacing: 0">investidos em dezembro</span></div>
<div style="margin-top: 12px; display: flex; align-items: center; gap: 12px">
<span style="width: 40px; height: 40px; border-radius: 12px; background: #EFE8E2; display: flex; align-items: center; justify-content: center; flex: none">{mixer}</span>
<div style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Batedeira planetária</span><span style="font-size: 13px; color: {SEC}">Equipamento · 3 de dezembro</span></div>
<span style="font-size: 15px; font-weight: 600">R$ 1.890,00</span></div>
<div style="margin-top: 12px; padding: 8px 12px; border-radius: 10px; background: {LBLUE}; font-size: 13px; color: {DARK}; line-height: 1.35">Fica fora do lucro final. A batedeira dura anos, não é gasto de um mês só.</div>
<div style="margin-top: 12px; height: 44px; border-radius: 12px; border: 1px solid {BLUE}; color: {BLUE}; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600">+ Adicionar investimento</div>
</div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; background: #FFFFFF; border-top: 1px solid {DIV}; display: flex; justify-content: space-around; padding-top: 14px; box-sizing: border-box">{items}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


# conta: 7.200 - 2.520 = 4.680; 4.680 - 900 = 3.780 (a batedeira de 1.890 não entra)
assert 7200 - 2520 == 4680 and 4680 - 900 == 3780


def p2_inv_s2():
    inner = f'''<div style="position: absolute; left: 44px; right: 44px; top: 50px; color: {NAVY}; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.8px; text-wrap: balance">{S2_INV}</div>
<div style="position: absolute; left: 50%; top: 176px; transform: translateX(-50%)">{phone(lucro_inv_screen(), 500)}</div>
<img src="{U("LOGOB")}" alt="receitech" style="position: absolute; right: 44px; bottom: 30px; height: 20px; width: auto">'''
    return box(SKY, inner)


SLIDES24 = [
    ("D24_P2_T1a", "24/11 · P2 · tela 1 · 4.1 (N5)", lambda: p2_n5("a")),
    ("D24_P2_T1b", "24/11 · P2 · tela 1 · 4.2 (N5)", lambda: p2_n5("b")),
    ("D24_P2_T1c", "24/11 · P2 · tela 1 · 4.3 (N5)", lambda: p2_n5("c")),
    ("D24_P2_T1n4", "24/11 · P2 · tela 1 · layout N4 (4.1)", lambda: p2_n4("a")),
    ("D24_P2_S2", "24/11 · P2 · tela 2 (Investimentos na aba Lucro)", p2_inv_s2),
]

if __name__ == "__main__":
    for code, title, fn in SLIDES24:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)
