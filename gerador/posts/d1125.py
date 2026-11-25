"""Posts de 25/11/2026.
Post 1 (foto única, 11h): taxa do cartão repassada ao cliente (retomado de 23 e 24/11, N6, pudim), frases novas.
Uso: python3 d1125.py local|canvas [OUT]"""
import os, sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "local"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/d1125"
_argv = sys.argv
sys.argv = ["d1123.py", MODE, OUT]
exec(open('/home/claude/receitech-social/gerador/posts/d1123.py').read().rsplit('if __name__ == "__main__":', 1)[0])
sys.argv = _argv
os.makedirs(OUT, exist_ok=True)

SUB25 = "No Receitech, você liga “Repassar taxa” na venda e o total do cliente já sai com a taxa da maquininha."
P2_T1.update({
    "g": ("A maquininha desconta.", "Você recebe o valor inteiro.", SUB25),
    "h": ("Vender no crédito", "sem perder 5% de cada venda.", SUB25),
    "i": ("Pagou no crédito?", "A taxa vai pro total do cliente.", SUB25),
})
TOPS.update({"g": 222, "h": 222, "i": 222})

IMGS["PUD2"] = "doce_pudim_2.jpg"
BLOBS["PUD2"] = "/_blob/b4d6858d13932caf186dfef02fe3fbb8"
# miniatura do app também usa a foto nova
IMGS["PUDIM"], BLOBS["PUDIM"] = IMGS["PUD2"], BLOBS["PUD2"]
ALT_PUD2 = "Pudim de leite com calda de caramelo num prato branco, com uma fatia sendo servida"


# Luana (25/11): "tá péssimo esse fundo do pudim" -> foto nova, fundo branco (doce_pudim_2)
def p1_v2(k, side="R"):
    t1, t2, sub = P2_T1[k]
    txt = t1.upper() + "<br>" + t2.upper()
    top = TOPS[k]
    pos = "8% 50%" if side == "R" else "100% 50%"
    ph = f'right: 26px' if side == "R" else 'left: 26px'
    inner = f"""<img src="{U("PUD2")}" alt="{ALT_PUD2}" style="position: absolute; left: 0; top: {top}px; width: {PW}px; height: {PH - top}px; object-fit: cover; object-position: {pos}">
<div style="position: absolute; left: 40px; right: 40px; top: 40px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; font-weight: 600; color: #FFF4D2; font-size: 31px; line-height: 1.1; letter-spacing: 0.3px">{txt}</div>
<div style="{POP}; font-weight: 500; color: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 440px">{sub}</div></div>
<div style="position: absolute; {ph}; top: {top + 34}px">{phone(pagamento_screen(), 560)}</div>"""
    return box(NAVY, inner)


SLIDES25B = [
    ("D25_P1_F1", "25/11 · P1 · foto única · 1.1 (pudim novo)", lambda: p1_v2("g", "L")),
    ("D25_P1_F2", "25/11 · P1 · foto única · 1.2 (pudim novo)", lambda: p1_v2("h", "L")),
    ("D25_P1_F3", "25/11 · P1 · foto única · 1.3 (pudim novo)", lambda: p1_v2("i", "L")),
]

SLIDES25 = [
    ("D25_P1_F1", "25/11 · P1 · foto única · 1.1", lambda: p2_single("g")),
    ("D25_P1_F2", "25/11 · P1 · foto única · 1.2", lambda: p2_single("h")),
    ("D25_P1_F3", "25/11 · P1 · foto única · 1.3", lambda: p2_single("i")),
]

if __name__ == "__main__":
    for code, title, fn in ([] if (os.environ.get("V3") or os.environ.get("V4") or os.environ.get("V5") or os.environ.get("V6") or os.environ.get("V7")) else SLIDES25B if os.environ.get('V2') else SLIDES25):
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
    print("ok", MODE, OUT)


# ================= Rodada 3 (Luana 25/11: "péssimo essas sugestões, troca de ideia de texto e layout") =================
T3OPTS = {
    "j": ("Crédito ou Pix? Pro seu lucro,", "tanto faz."),
    "k": ("A maquininha come", "5% do pudim."),
    "l": ("O cliente escolheu o crédito.", "A taxa vai junto."),
}
SUB3 = "No Receitech, você liga “Repassar taxa” na venda e a taxa entra no total do cliente."


SER = "font-family: 'Libre Caslon Text', Georgia, serif"
CREAM = "#F3EDE3"


def p1_t4(k):
    a, b = T3OPTS[k]
    inner = f'''<div style="position: absolute; left: 44px; right: 40px; top: 44px; {POP}; color: {NAVY}; font-size: 46px; font-weight: 800; line-height: 1.04; letter-spacing: -2px">{a} <span style="color: {BLUE}">{b}</span></div>
<img src="{U("PUD2")}" alt="{ALT_PUD2}" style="position: absolute; left: 44px; top: 262px; width: 236px; height: 340px; object-fit: cover; object-position: 80% 50%; border-radius: 18px">
<div style="position: absolute; left: 300px; top: 236px">{phone(pagamento_screen(), 396)}</div>
<div style="position: absolute; left: 44px; right: 44px; bottom: 40px; {POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB3}</div>'''
    return box("#F2F2F0", inner)


def p1_t2(k):
    a, b = T3OPTS[k]
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 40px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 4px; color: {BLUE}">RECEITECH</div>
<div style="position: absolute; left: 50px; right: 50px; top: 70px; text-align: center; {SER}; color: {NAVY}; font-size: 40px; line-height: 1.15; letter-spacing: -0.8px; text-wrap: balance">{a} <i>{b}</i></div>
<img src="{U("PUD2")}" alt="{ALT_PUD2}" style="position: absolute; left: 40px; top: 290px; width: 250px; height: 290px; object-fit: cover; object-position: 88% 50%; border-radius: 14px">
<div style="position: absolute; left: 306px; top: 236px">{phone(pagamento_screen(), 396)}</div>
<div style="position: absolute; left: 50px; right: 50px; bottom: 38px; text-align: center; {POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB3}</div>'''
    return box(CREAM, inner)


SLIDES25C = [
    ("D25_P1_R1", "25/11 · P1 · 2.1 (T4)", lambda: p1_t4("j")),
    ("D25_P1_R2", "25/11 · P1 · 2.2 (T4)", lambda: p1_t4("k")),
    ("D25_P1_R3", "25/11 · P1 · 2.3 (T4)", lambda: p1_t4("l")),
    ("D25_P1_R4", "25/11 · P1 · 2.4 (layout T2, frase 2.2)", lambda: p1_t2("k")),
]
if __name__ == "__main__" and os.environ.get("V3") and not os.environ.get("V4"):
    for code, title, fn in SLIDES25C:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")


# ================= Rodada 4 (Luana 25/11: funcionalidade mais gritante; foto do pudim horrível) =================
IMGS["PUD3"] = "doce_pudim_3.jpg"
BLOBS["PUD3"] = "/_blob/62ad94c4649c463ae6c60e4466a1c5bf"
ALT_PUD3 = "Pudim de leite inteiro com calda de caramelo num prato branco"
IMGS["PUDIM"], BLOBS["PUDIM"] = IMGS["PUD3"], BLOBS["PUD3"]
T4OPTS = {
    "m": ("Repasse a taxa do cartão", "pro cliente.", "Um toque na venda e o total do cliente já sai com a taxa somada. Você recebe o valor inteiro."),
    "n": ("Taxa do cartão?", "Quem paga é o cliente.", "Você liga “Repassar taxa” na venda e o total já sai com a taxa somada."),
    "o": ("O Receitech soma a taxa do cartão", "no total do cliente.", "Você liga “Repassar taxa” na venda e recebe o valor inteiro do pudim."),
}


def p1_r4(k):
    a, b, sub = T4OPTS[k]
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">NO RECEITECH</div>
<div style="position: absolute; left: 44px; right: 40px; top: 64px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; color: {NAVY}; font-size: {44 if k == "m" else 38}px; font-weight: 800; line-height: 1.04; letter-spacing: -1.8px">{a} <span style="color: {BLUE}">{b}</span></div>
<div style="{POP}; color: {NAVY}; font-size: 15px; font-weight: 500; line-height: 1.4">{sub}</div></div>
<img src="{U("PUD3")}" alt="{ALT_PUD3}" style="position: absolute; left: 44px; top: 300px; width: 250px; height: 300px; object-fit: cover; object-position: 72% 50%; border-radius: 18px">
<div style="position: absolute; left: 310px; top: 262px">{phone(pagamento_screen(), 420)}</div>'''
    return box("#F2F2F0", inner)


SLIDES25D = [
    ("D25_P1_S1", "25/11 · P1 · 3.1", lambda: p1_r4("m")),
    ("D25_P1_S2", "25/11 · P1 · 3.2", lambda: p1_r4("n")),
    ("D25_P1_S3", "25/11 · P1 · 3.3", lambda: p1_r4("o")),
]
if __name__ == "__main__" and os.environ.get("V4") and not os.environ.get("V5"):
    for code, title, fn in SLIDES25D:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")


# ================= Rodada 5 (Luana 25/11: funcionalidade fraca; escolheu Meta de vendas do mês pro P1) =================
for _k, _f in [("BOLOM", "doce_bolomorango_1.jpg"), ("BISC", "natal_biscoito_1.jpg"), ("KIBE", "salg_kibe_2.jpg")]:
    IMGS[_k] = _f
    BLOBS[_k] = {"BOLOM": "/_blob/75e04a74a2d4ad1e084cd1495d369fdf", "BISC": "/_blob/928737f0edc80ff85bd16c0097a78621", "KIBE": "/_blob/ae0850cfb05afeef070a3916d679f039"}[_k]
GREEN = "#039855"

# plano: 15 x 160 + 30 x 90 + 60 x 35 + 12 x 150 = 2.400 + 2.700 + 2.100 + 1.800 = 9.000
# vendido: 9 x 160 + 14 x 90 + 32 x 35 + 6 x 150 = 1.440 + 1.260 + 1.120 + 900 = 4.720; falta 4.280
PLANO = [("BOLOM", "Bolos de festa", 9, 15, 160), ("PUD3", "Pudins", 14, 30, 90), ("BISC", "Biscoitos de Natal", 32, 60, 35), ("KIBE", "Quibes (cento)", 6, 12, 150)]
assert sum(q * p for _, _, _, q, p in PLANO) == 9000 and sum(v * p for _, _, v, _, p in PLANO) == 4720


def meta_screen():
    chevl = svg('<path d="M15 5l-7 7 7 7"></path>', 18, DARK, 2.4)
    chevr = svg('<path d="M9 5l7 7-7 7"></path>', 18, DARK, 2.4)
    inbox = svg('<path d="M22 12h-6l-2 3h-4l-2-3H2"></path><path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"></path>', 22, DARK, 1.8)
    plus = svg('<path d="M12 5v14M5 12h14"></path>', 18, BLUE, 2.4)

    def line(k, name, v, q, p):
        pct = min(100, round(100 * v / q))
        return f'''<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0">
<img src="{U(k)}" alt="{name}" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover; flex: none">
<div style="flex: 1; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 15px; font-weight: 600">{name}</span>
<div style="height: 6px; border-radius: 3px; background: #F2F4F7"><div style="width: {pct}%; height: 6px; border-radius: 3px; background: {BLUE}"></div></div></div>
<div style="width: 74px; text-align: right"><span style="font-size: 24px; font-weight: 700">{v}</span> <span style="font-size: 13px; color: {SEC}">de {q}</span></div>
<span style="width: 38px; height: 38px; border-radius: 12px; border: 1px solid {BLUE}; box-shadow: 0 3px 0 #1F6AD8; display: flex; align-items: center; justify-content: center; flex: none">{plus}</span></div>'''
    rows = "".join(line(*x) for x in PLANO)
    items = "".join(f'<span style="font-size: 11px; font-weight: {700 if n == "Vendas" else 500}; color: {BLUE if n == "Vendas" else "#98A2B3"}">{n}</span>' for n in ["Vendas", "Rotina", "Finanças", "Produtos", "Perfil"])
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {POP}; color: {DARK}; overflow: hidden; position: relative">
<div style="height: 54px"></div>
<div style="padding: 4px 20px 0; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; gap: 22px; font-size: 17px"><span style="font-weight: 700; border-bottom: 2px solid {DARK}; padding-bottom: 6px">Meta</span><span style="color: #98A2B3; font-weight: 500">Vendas</span></div>{inbox}</div>
<div style="padding: 22px 20px 0">
<div style="display: flex; align-items: center; justify-content: center; gap: 14px; font-size: 15px; font-weight: 600">{chevl}<span>Dezembro</span>{chevr}</div>
<div style="margin-top: 18px; font-size: 15px; color: {SEC}">Pra bater dezembro falta vender</div>
<div style="margin-top: 2px; display: flex; align-items: baseline; justify-content: space-between"><span style="font-size: 38px; font-weight: 700; letter-spacing: -1px">R$ 4.280</span><span style="font-size: 15px; font-weight: 600; color: {GREEN}">+ R$ 160 hoje</span></div>
<div style="margin-top: 12px; height: 14px; border-radius: 7px; background: #F2F4F7"><div style="width: 52.4%; height: 14px; border-radius: 7px; background: {BLUE}"></div></div>
<div style="margin-top: 8px; font-size: 13px; color: {SEC}">R$ 4.720 vendidos de R$ 9.000</div>
<div style="margin-top: 14px; padding: 12px 14px; border-radius: 12px; background: {LBLUE}; font-size: 13px; line-height: 1.4">A meta de R$ 9.000 paga as contas do negócio e o seu salário de dezembro.</div>
<div style="margin-top: 26px; display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 18px; font-weight: 700">Plano de vendas</span><span style="font-size: 14px; font-weight: 600; color: {BLUE}">Ajustar plano ›</span></div>
<div style="margin-top: 6px">{rows}</div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 74px; background: #FFFFFF; border-top: 1px solid {DIV}; display: flex; justify-content: space-around; padding-top: 14px; box-sizing: border-box">{items}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 8px; display: flex; justify-content: center"><div style="width: 134px; height: 5px; border-radius: 3px; background: {DARK}"></div></div>
</div>'''


T5OPTS = {
    "p": ("O Receitech te diz quanto vender pra pagar as contas e", "o seu salário."),
    "q": ("Quanto você precisa vender em dezembro?", "O Receitech calcula."),
    "r": ("Sua meta de vendas do mês,", "calculada pelo Receitech."),
}
SUB5 = "A meta sai das contas do negócio + o seu salário. A cada venda, você vê quanto falta e quantos de cada produto vender."


def p1_meta(k, photo=True):
    a, b = T5OPTS[k]
    ph = f'<img src="{U("PUD3")}" alt="{ALT_PUD3}" style="position: absolute; left: 40px; top: 372px; width: 222px; height: 290px; object-fit: cover; object-position: 72% 50%; border-radius: 18px">' if photo else ""
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">NOVO NO RECEITECH · META DE VENDAS</div>
<div style="position: absolute; left: 44px; right: 40px; top: 64px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; color: {NAVY}; font-size: {34 if k == "p" else 40}px; font-weight: 800; line-height: 1.04; letter-spacing: -1.6px">{a} <span style="color: {BLUE}">{b}</span></div>
<div style="{POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB5}</div></div>
{ph}
<div style="position: absolute; left: 278px; top: 292px">{phone(meta_screen(), 418)}</div>'''
    return box("#F2F2F0", inner)


SLIDES25E = [
    ("D25_P1_M1", "25/11 · P1 · 4.1 (meta de vendas)", lambda: p1_meta("p")),
    ("D25_P1_M2", "25/11 · P1 · 4.2 (meta de vendas)", lambda: p1_meta("q")),
    ("D25_P1_M3", "25/11 · P1 · 4.3 (meta de vendas)", lambda: p1_meta("r")),
]
if __name__ == "__main__" and os.environ.get("V5") and not os.environ.get("V6") and not os.environ.get("V7"):
    for code, title, fn in SLIDES25E:
        html = fn()
        if MODE == "canvas":
            doc = page_f(title, html, PW, PH)
            assert "file://" not in doc and "PENDENTE" not in doc
            open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
        else:
            open(os.path.join(OUT, code + ".html"), "w").write(
                f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")


# ================= Rodada 6 (Luana 25/11: frase 2 com salário de R$ 3.000; foto que remeta a venda de doces) =================
IMGS["COOK"] = "doce_cookie_1.jpg"
BLOBS["COOK"] = "/_blob/807c8d945256f8f64dca3f6dd222bbb8"
ALT_COOK = "Pilha de cookies recheados cortados ao meio, com recheio de chocolate, red velvet com creme branco e cookie de chocolate"
T5OPTS["s"] = ("Quanto você precisa vender em dezembro pra tirar R$ 3.000 de salário?", "O Receitech calcula.")


def p1_meta6():
    a, b = T5OPTS["s"]
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">NOVO NO RECEITECH · META DE VENDAS</div>
<div style="position: absolute; left: 44px; right: 40px; top: 64px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; color: {NAVY}; font-size: 35px; font-weight: 800; line-height: 1.05; letter-spacing: -1.4px">{a}<br><span style="color: {BLUE}">{b}</span></div>
<div style="{POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB5}</div></div>
<img src="{U("COOK")}" alt="{ALT_COOK}" style="position: absolute; left: 40px; top: 372px; width: 222px; height: 290px; object-fit: cover; object-position: 48% 50%; border-radius: 18px">
<div style="position: absolute; left: 278px; top: 292px">{phone(meta_screen(), 418)}</div>'''
    return box("#F2F2F0", inner)


if __name__ == "__main__" and os.environ.get("V6") and not os.environ.get("V7"):
    html = p1_meta6().replace("o seu salário de dezembro.", "o seu salário de R$ 3.000.")
    code, title = "D25_P1_M4", "25/11 · P1 · 4.4 (salário de R$ 3.000, cookies)"
    if MODE == "canvas":
        doc = page_f(title, html, PW, PH)
        assert "file://" not in doc and "PENDENTE" not in doc
        open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
    else:
        open(os.path.join(OUT, code + ".html"), "w").write(
            f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")


# ================= Rodada 7 (Luana 25/11: "uma imagem melhor de cookies, de vender") =================
IMGS["COOK2"] = "doce_cookie_2.jpg"
BLOBS["COOK2"] = "/_blob/1439eb6df97d81ca855807288e875cd6"
ALT_COOK2 = "Caixa de presente com seis cookies recheados vista de cima, escrito COOKIES feitos com amor"


def p1_meta7():
    a, b = T5OPTS["s"]
    inner = f'''<div style="position: absolute; left: 44px; top: 40px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 3px; color: {BLUE}">NOVO NO RECEITECH · META DE VENDAS</div>
<div style="position: absolute; left: 44px; right: 40px; top: 64px; display: flex; flex-direction: column; gap: 14px">
<div style="{POP}; color: {NAVY}; font-size: 35px; font-weight: 800; line-height: 1.05; letter-spacing: -1.4px">{a}<br><span style="color: {BLUE}">{b}</span></div>
<div style="{POP}; color: {NAVY}; font-size: 14px; font-weight: 500; line-height: 1.4">{SUB5}</div></div>
<img src="{U("COOK2")}" alt="{ALT_COOK2}" style="position: absolute; left: 32px; top: 424px; width: 280px; height: 174px; object-fit: cover; border-radius: 14px">
<div style="position: absolute; left: 318px; top: 304px">{phone(meta_screen(), 400)}</div>'''
    return box("#F2F2F0", inner)


if __name__ == "__main__" and os.environ.get("V7"):
    html = p1_meta7().replace("o seu salário de dezembro.", "o seu salário de R$ 3.000.")
    code, title = "D25_P1_M5", "25/11 · P1 · 4.5 (caixa de cookies)"
    if MODE == "canvas":
        doc = page_f(title, html, PW, PH)
        assert "file://" not in doc and "PENDENTE" not in doc
        open(os.path.join(OUT, code + ".dc.html"), "w").write(doc)
    else:
        open(os.path.join(OUT, code + ".html"), "w").write(
            f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{html}</body></html>")
