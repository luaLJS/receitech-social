# Layouts novos (N1–N12), carregados por feed.py com exec() depois das definições base.

def photo_bg(k, dark=0.0, blur=0):
    f = f"filter: blur({blur}px); transform: scale(1.06);" if blur else ""
    ov = f'<div style="position: absolute; inset: 0; background: rgba(16,24,40,{dark})"></div>' if dark else ""
    return f'<img src="{U[k]}" alt="" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; object-fit: cover; {f}">{ov}'


# N1 — ref. "what's included in our social media packages"
def n_pilulas():
    def pill(t, bg, fg, l, top, r):
        return f'<span style="position: absolute; left: {l}px; top: {top}px; padding: 6px 16px; border-radius: 30px; background: {bg}; color: {fg}; {POP}; font-size: 17px; font-weight: 500; transform: rotate({r}deg)">{t}</span>'
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 80px; text-align: center; {POP}; font-size: 11px; font-weight: 600; letter-spacing: 4px; color: {NAVY}">PASSE PRO LADO</div>
<div style="position: absolute; left: 40px; right: 40px; top: 0; bottom: 0; display: flex; align-items: center; justify-content: center; text-align: center; {HVY}; font-weight: 900; color: {NAVY}; font-size: 62px; line-height: 0.98; letter-spacing: -3px">o que entra no preço do panetone</div>
{pill("Natal", "#FFE58F", NAVY, 330, 236, -6)}{pill("Encomenda", BLUE, "#FFFFFF", 26, 300, 4)}{pill("Lucro", "#B8F5C9", NAVY, 300, 480, -3)}'''
    return box("#FFFFFF", inner)


# N2 — ref. "let's pick your new brand aesthetic"
def n_enorme():
    arrow = '<svg width="46" height="16" viewBox="0 0 46 16" aria-hidden="true"><path d="M2 8h40M34 2l8 6-8 6" fill="none" stroke="#101828" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
    inner = f'''<div style="position: absolute; left: 34px; top: 30px; {POP}; font-size: 12px; font-weight: 600; letter-spacing: 2px; color: {NAVY}">RECEITECH</div>
<div style="position: absolute; left: 30px; right: 26px; top: 66px; {HVY}; font-weight: 900; color: {NAVY}; font-size: 90px; line-height: 0.9; letter-spacing: -4.5px">o preço do seu <span style="text-decoration: underline; text-decoration-thickness: 7px; text-underline-offset: 8px">panetone</span> está certo?</div>
<div style="position: absolute; left: 34px; right: 34px; bottom: 40px; display: flex; align-items: flex-end; justify-content: space-between">
<div style="{POP}; font-size: 15px; font-weight: 600; line-height: 1.4; color: {NAVY}">A CONTA <span style="background: {NAVY}; color: #FFFFFF; padding: 1px 8px; border-radius: 6px">COMPLETA</span><br>NA PRÓXIMA TELA</div>{arrow}</div>'''
    return box(SKY, inner)


# N3 — ref. "WHAT INSPIRED US THIS WEEK"
def n_caixa_alta():
    inner = f'''{photo_bg("CHOF", 0.45)}
<div style="position: absolute; left: 0; right: 0; top: 150px; text-align: center; {POP}; font-size: 14px; font-weight: 500; color: #FFFFFF">receitech</div>
<div style="position: absolute; left: 36px; right: 36px; top: 0; bottom: 0; display: flex; align-items: center; justify-content: center; text-align: center; {CND}; color: #CFE2FF; font-size: 86px; line-height: 0.95; letter-spacing: 0.5px">O QUE MAIS DÁ LUCRO NO NATAL</div>'''
    return box(NAVY, inner)


# N4 — ref. "BECAUSE GROWTH STARTS WHEN SOMEONE FEELS YOUR BRAND BELONGS."
def n_desfocada():
    inner = f'''{photo_bg("CASF", 0.12, 10)}
<div style="position: absolute; left: 34px; right: 34px; top: 0; bottom: 0; display: flex; align-items: center">
<div style="width: 100%; text-align: justify; text-align-last: justify; {POP}; font-weight: 600; color: #FFFFFF; font-size: 30px; line-height: 1.12; letter-spacing: 0.5px; word-spacing: 6px; text-shadow: 0 1px 10px rgba(0,0,0,0.25)">LUCRO DE VERDADE COMEÇA QUANDO VOCÊ SABE O CUSTO.</div></div>
<img src="{U["LOGOW"]}" alt="receitech" style="position: absolute; left: 50%; margin-left: -45px; bottom: 34px; width: 90px; height: auto">'''
    return box(NAVY, inner)


# N5 — ref. pôster "GRETA EVANS"
def n_moldura():
    inner = f'''<div style="position: absolute; left: 22px; right: 22px; top: 22px; bottom: 22px; border-radius: 34px; background: {BLUE}; overflow: hidden">
<div style="position: absolute; left: 26px; right: 26px; top: 22px; display: flex; align-items: flex-start; gap: 14px">
<span style="{CND}; color: #FFFFFF; font-size: 54px; line-height: 0.9">DEZ</span>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="{POP}; color: #FFFFFF; font-size: 11px; font-weight: 600; letter-spacing: 1px">RECEITECH APRESENTA</span>
<span style="{CND}; color: #FFFFFF; font-size: 42px; line-height: 0.95">QUANTO CUSTA UM PANETONE</span></div></div>
<img src="{U["CHOF"]}" alt="" style="position: absolute; left: 22px; top: 168px; width: 452px; height: 452px; object-fit: cover; border-radius: 22px">
<div style="position: absolute; left: 0; right: 0; bottom: 14px; text-align: center; {POP}; color: #FFFFFF; font-size: 12px; font-weight: 600; letter-spacing: 1px">A CONTA COMPLETA NA PRÓXIMA TELA</div></div>'''
    return box("#FFFFFF", inner)


# N6 — ref. "THE EXACT EMAIL TO SEND TO YOUR CLIENT WHEN..."
def n_bloco():
    inner = f'''{photo_bg("BOLF", 0.35)}
<div style="position: absolute; left: 60px; right: 60px; top: 0; bottom: 0; display: flex; align-items: center">
<div style="width: 100%; text-align: justify; text-align-last: justify; {POP}; font-weight: 600; color: #FFF4D2; font-size: 34px; line-height: 1.02; word-spacing: 14px">A CONTA QUE FALTA FAZER ANTES DO NATAL...</div></div>'''
    return box(NAVY, inner)


# N7 — ref. "5 Canva Apps Every Social Media Manager Should Know About"
def n_caderno():
    rings = "".join(f'<div style="position: absolute; left: -10px; top: {60 + i * 90}px; width: 24px; height: 10px; border-radius: 5px; background: #98A2B3"></div>' for i in range(5))
    inner = f'''{photo_bg("CX1F", 0.1)}
<div style="position: absolute; left: 92px; top: 120px; width: 356px; height: 470px; background: #FBF8F2; border-radius: 6px; box-shadow: 0 18px 40px rgba(0,0,0,0.25); transform: rotate(-2deg)">{rings}
<div style="position: absolute; left: 34px; right: 30px; top: 0; bottom: 0; display: flex; align-items: center; text-align: center; {SER}; color: {BLUE}; font-size: 36px; line-height: 1.15; letter-spacing: -0.8px">5 contas que quem vende no Natal precisa fazer</div></div>
<img src="{U["BIS"]}" alt="" style="position: absolute; left: 330px; top: 520px; width: 160px; {STICKER}; transform: rotate(8deg)">
<img src="{U["BRG"]}" alt="" style="position: absolute; left: 60px; top: 92px; width: 110px; {STICKER}; transform: rotate(-10deg)">'''
    return box(NAVY, inner)


# N8 — ref. "summer want list"
def n_lista():
    words = [("leite condensado", 60, 120), ("forminhas nº 4", 330, 100), ("caixinhas", 30, 300), ("granulado", 420, 280), ("fita vermelha", 40, 470), ("chocolate 50%", 400, 452), ("coco ralado", 220, 76), ("gás", 470, 380)]
    w = "".join(f'<span style="position: absolute; left: {x}px; top: {y}px; {POP}; font-size: 13px; color: #FFFFFF">{t}</span>' for t, x, y in words)
    inner = f'''<img src="{U["CX1F"]}" alt="" style="position: absolute; left: 90px; top: 110px; width: 360px; height: 480px; object-fit: cover">{w}
<div style="position: absolute; left: 0; right: 0; bottom: 92px; text-align: center; {ITA}; color: #FFFFFF; font-size: 104px; line-height: 1">natal</div>
<div style="position: absolute; left: 60px; right: 60px; bottom: 44px; display: flex; justify-content: space-between; {POP}; color: #FFFFFF; font-size: 40px; font-weight: 600; letter-spacing: -1px"><span>lista de</span><span>compras</span></div>'''
    return box("#8DB8FF", inner)


# N9 — ref. "hot take"
def n_hot_take():
    inner = f'''<div style="position: absolute; left: 40px; top: 52px; {SER}; color: {BLUE}; font-size: 76px; line-height: 1; letter-spacing: -2.5px">verdade <span style="{ITA}; font-size: 86px; letter-spacing: -1px">dura</span></div>
<img src="{U["CAS"]}" alt="" style="position: absolute; left: -30px; bottom: 30px; width: 300px">
<div style="position: absolute; left: 290px; right: 40px; top: 200px; {SER}; color: {BLUE}; font-size: 22px; line-height: 1.22">"O doce que mais vende no Natal nem sempre é o que mais dá lucro. A diferença aparece na conta."</div>
<div style="position: absolute; right: 40px; bottom: 40px; text-align: right; {POP}; color: {BLUE}; font-size: 11px; line-height: 1.3">veja a conta<br>na próxima tela</div>'''
    return box("#FBF6E8", inner)


# N10 — ref. "5 subtle ways to catch attention with summer content"
def n_dois_blocos():
    inner = f'''<div style="position: absolute; left: 44px; top: 110px; {SER}; color: #FFF4D2; font-size: 40px; letter-spacing: -1px">3 jeitos</div>
<div style="position: absolute; right: 44px; top: 300px; width: 330px; text-align: right; {POP}; color: #FFF4D2; font-size: 32px; line-height: 1.12; letter-spacing: -1px">de ter prejuízo nas encomendas de Natal</div>
<div style="position: absolute; left: 0; right: 0; bottom: 34px; text-align: center; {POP}; color: #FFF4D2; font-size: 11px; letter-spacing: 1px">@receitech_</div>'''
    return box(BLUE, inner)


# N11 — ref. "This Month's Favorites" com moldura e abas laterais
def n_abas():
    tabs = [("Preço", False), ("Pedidos", False), ("Lucro", True), ("Estoque", False)]
    t = "".join(f'<div style="height: 96px; width: 38px; background: {"#FFE58F" if on else "#FFFFFF"}; border: 1.5px solid {NAVY}; border-left: none; border-radius: 0 12px 12px 0; display: flex; align-items: center; justify-content: center"><span style="transform: rotate(90deg); {POP}; font-size: 15px; font-weight: {700 if on else 400}; color: {NAVY}; white-space: nowrap">{n}</span></div>' for n, on in tabs)

    def it(n, k):
        return f'<div style="position: relative; display: flex; align-items: center; justify-content: center; height: 150px"><span style="position: absolute; left: 0; top: 0; {POP}; font-size: 13px; color: {NAVY}">{n}</span><img src="{U[k]}" alt="" style="max-width: 150px; max-height: 128px"></div>'
    inner = f'''<div style="position: absolute; left: 64px; top: 64px; width: 372px; height: 592px; background: #FFFFFF; border: 1.5px solid {NAVY}; border-radius: 10px">
<div style="position: absolute; left: 20px; right: 20px; top: 40px; text-align: center; {HVY}; font-weight: 900; color: {NAVY}; font-size: 46px; line-height: 0.92; letter-spacing: -2.4px">Os mais lucrativos de dezembro</div>
<div style="position: absolute; left: 26px; right: 26px; top: 170px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px 14px">{it("01", "PAN")}{it("02", "CAS")}{it("03", "RAB")}{it("04", "CHO")}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 26px; text-align: center; {HVY}; font-weight: 800; color: {NAVY}; font-size: 20px; letter-spacing: -0.8px">receitech</div></div>
<div style="position: absolute; left: 436px; top: 104px; display: flex; flex-direction: column; gap: 4px">{t}</div>'''
    return box(BLUE, inner)


# N12 — ref. "my summer non-negotiables"
def n_objeto_centro():
    inner = f'''{photo_bg("RABF", 0.25)}
<div style="position: absolute; left: 0; right: 0; top: 70px; text-align: center; color: #FFFFFF; line-height: 1.02">
<div style="{POP}; font-size: 40px; font-weight: 600; letter-spacing: -1.4px">um Natal</div>
<div style="{ITA}; font-size: 54px">sem prejuízo</div></div>
<div style="position: absolute; left: 50%; margin-left: -118px; top: 214px">{phone(product_screen(), 480)}</div>'''
    return box(NAVY, inner)


NEW_TILES = [
    ("N8", "Foto no meio + palavras soltas", "ref. summer want list", n_lista),
    ("N3", "Caixa alta condensada na foto", "ref. what inspired us this week", n_caixa_alta),
    ("N11", "Moldura com abas laterais", "ref. This Month's Favorites", n_abas),
    ("N10", "Serifa em dois blocos", "ref. 5 subtle ways", n_dois_blocos),
    ("N6", "Caixa alta em bloco na foto", "ref. the exact email to send", n_bloco),
    ("N1", "Texto pesado + etiquetas", "ref. what's included", n_pilulas),
    ("N4", "Foto desfocada + caixa alta", "ref. because growth starts", n_desfocada),
    ("N9", "Título serifa + citação", "ref. hot take", n_hot_take),
    ("N2", "Texto enorme + sublinhado", "ref. let's pick your new brand aesthetic", n_enorme),
    ("N5", "Pôster com moldura", "ref. Greta Evans", n_moldura),
    ("N12", "Foto + objeto no centro", "ref. my summer non-negotiables", n_objeto_centro),
    ("N7", "Caderno sobre foto", "ref. 5 Canva Apps", n_caderno),
]
