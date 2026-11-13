src = open("/home/claude/posts/c3.py").read().split("S1 = slide_hook_c3()")[0]
exec(src)
BL = "#3D86F7"
def slide2(screen_html):
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {LBLUE}; {F}">
<div style="position: absolute; left: 44px; right: 44px; top: 48px; display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 30px; font-weight: 700; line-height: 1.14; color: {DARK}; letter-spacing: -0.9px">A compra dos ingredientes.</span>
<span style="font-size: 30px; font-weight: 700; line-height: 1.14; color: {BL}; letter-spacing: -0.9px">O app te mostra exatamente o&nbsp;que comprar.</span>
</div>
<img src="{LD}" alt="Receitech" style="position: absolute; left: 44px; top: 232px; height: 22px; width: auto; opacity: 0.85">
<div style="position: absolute; left: 186px; top: 214px">{phone(screen_html, 660)}</div>
<img src="{PH_CASA}" alt="Casadinhos" style="position: absolute; left: -70px; bottom: -50px; width: 270px; height: 270px; border-radius: 135px; object-fit: cover; box-shadow: 0 20px 50px rgba(16,24,40,0.25); border: 6px solid #FFFFFF">
</div>'''
S2 = slide2(lista_screen())
open(os.path.join(ROOT2, "C3_S2.dc.html"), "w").write(page("C3 · tela 2 (app)", S2, PW, PH))
loc = S2.replace(PH_CASA, "/home/claude/fotos/casadinho_sq.jpg").replace(LD, "logo_dark.png")
open("/home/claude/posts/prev_C3_S2.html", "w").write(f"<html><head><meta charset='utf-8'><link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{loc}</body></html>")
print("ok")
