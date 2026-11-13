import os, re
src = open('/home/claude/assets/gen.py').read()
exec(src.split("files = {")[0])
ROOT2 = "/mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project"
F = "font-family: 'Poppins', sans-serif"
ITA = "font-family: 'Instrument Serif', Georgia, serif; font-style: italic"
NAVY = "#101828"; LB = "#EBF5FF"
PH = os.environ.get("PH_BRW", "/home/claude/fotos/brownie2_sq.jpg")
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap"
ps = src[src.index("def product_screen"):src.index("def phone(")]
ps = ps.replace("def product_screen", "def brownie_screen").replace('{BRIG}" alt="Brigadeiro gourmet"', '{PH}" alt="Brownie"').replace(">Brigadeiro gourmet<", ">Brownie<")
ps = ps.replace('channel_card("DIRETA", "#EBF4FF", "2,25", "1,46", "65%")', 'channel_card("DIRETA", "#EBF4FF", "8,00", "5,20", "65%", None, "2,80")')
ps = ps.replace('channel_card("IFOOD", "#F0F0F0", "3,20", "1,45", "45%", ("R$ 0,96", "30%"))', 'channel_card("IFOOD", "#F0F0F0", "10,50", "4,55", "43%", ("R$ 3,15", "30%"), "2,80")')
assert ps.count("2,80") == 2
exec(ps)

def f1():
    return f'''<div style="width: {PW}px; height: {PH_}px; position: relative; overflow: hidden; background: {LB}">
<div style="position: absolute; left: 46px; right: 46px; top: 56px; {F}; color: {NAVY}; font-size: 33px; font-weight: 700; line-height: 1.14; letter-spacing: -1.2px">O mesmo brownie dá um lucro na venda direta <span style="{ITA}; font-weight: 400; font-size: 42px; letter-spacing: -0.3px">e outro no iFood.</span></div>
<div style="position: absolute; left: 46px; right: 46px; top: 206px; {F}; color: {NAVY}; font-size: 16px; line-height: 1.4">O Receitech mostra quanto sobra de cada produto em cada canal.</div>
<img src="{PH}" alt="Brownie" style="position: absolute; left: 310px; top: 440px; width: 196px; height: 196px; object-fit: cover; border-radius: 14px">
<div style="position: absolute; left: 30px; top: 262px">{phone(brownie_screen(), 548)}</div>
</div>'''

PH_ = PH_TMP = None
PH_ = 720
S = f1()
if os.environ.get("PH_BRW"):
    html = page("F1 · foto única (lucro por canal)", S, PW, 720).replace("family=Poppins:wght@400;500;600;700&amp;display=swap", "family=Poppins:wght@400;500;600;700&amp;family=Instrument+Serif:ital@0;1&amp;display=swap")
    assert "Instrument+Serif" in html
    open(os.path.join(ROOT2, "F1_foto.dc.html"), "w").write(html)
open("/home/claude/posts/prev_F1.html", "w").write(f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{S}</body></html>")
print("ok")
