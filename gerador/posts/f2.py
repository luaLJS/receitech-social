import os
exec(open('/home/claude/assets/gen.py').read().split("files = {")[0])
ROOT2 = "/mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project"
F = "font-family: 'Poppins', sans-serif"
ITA = "font-family: 'Instrument Serif', Georgia, serif; font-style: italic"
NAVY = "#101828"
PH_BROW = os.environ.get("PH_BROW", "/home/claude/fotos/brownie_natal_sq.jpg")
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap"

def line(label, val, color=DARK, bold=False, top=False):
    bt = f"border-top: 1px solid {DIV}; margin-top: 4px; padding-top: 10px;" if top else ""
    w = 600 if bold else 400
    return f'<div style="display: flex; justify-content: space-between; padding: 6px 0; {bt} font-size: 14px"><span style="color: {DARK if bold else SEC}; font-weight: {w}">{label}</span><span style="color: {color}; font-weight: {600 if bold else 500}">{val}</span></div>'

def lucro_screen():
    chev = svg('<path d="M6 9l6 6 6-6"></path>', 16, DARK, 2.2)
    return f'''<div style="width: 390px; height: 844px; background: #FFFFFF; {F}; color: {DARK}; overflow: hidden; box-sizing: border-box; padding: 0 20px">
<div style="height: 56px"></div>
<div style="display: flex; align-items: center; justify-content: space-between; padding: 6px 0 18px"><span style="font-size: 24px; font-weight: 700; letter-spacing: -0.5px">Lucro</span><span style="display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 500; padding: 8px 12px; border: 1px solid {DIV}; border-radius: 10px">Dezembro 2026 {chev}</span></div>
<div style="font-size: 11px; font-weight: 700; letter-spacing: 1px; color: {SEC}">LUCRO FINAL DO MÊS</div>
<div style="font-size: 38px; font-weight: 700; color: {GREEN}; letter-spacing: -1px; margin-top: 4px">R$ 3.482,60</div>
<div style="font-size: 12px; color: {SEC}; margin-top: 2px">O que sobrou das vendas depois de descontar custos, taxas e gastos</div>
<div style="margin-top: 18px; padding: 16px; border-radius: 16px; background: {LBLUE}">
<div style="font-size: 15px; font-weight: 700">Sua retirada do mês</div>
<div style="display: flex; height: 12px; border-radius: 6px; overflow: hidden; margin: 12px 0 10px"><div style="width: 65.5%; background: {BLUE}"></div><div style="flex: 1; background: #B9D3FB"></div></div>
<div style="display: flex; justify-content: space-between; font-size: 14px; padding: 4px 0"><span style="display: flex; align-items: center; gap: 8px"><span style="width: 10px; height: 10px; border-radius: 5px; background: {BLUE}"></span>Retirada para você</span><span style="font-weight: 700">R$ 2.282,60</span></div>
<div style="display: flex; justify-content: space-between; font-size: 14px; padding: 4px 0"><span style="display: flex; align-items: center; gap: 8px"><span style="width: 10px; height: 10px; border-radius: 5px; background: #B9D3FB"></span>Valor mantido no negócio</span><span style="font-weight: 600">R$ 1.200,00</span></div>
<div style="margin-top: 8px; font-size: 12px; color: {GREEN}; font-weight: 600">114% da sua meta de retirada (R$ 2.000,00)</div>
</div>
<div style="margin-top: 20px; font-size: 15px; font-weight: 700">Resumo</div>
<div style="margin-top: 6px">
{line("Vendas", "R$ 7.940,00")}
{line("Custos das vendas", "− R$ 3.716,40", "#D92D20")}
{line("Resultado das vendas", "R$ 4.223,60", DARK, True, True)}
{line("Gastos do negócio", "− R$ 741,00", "#D92D20")}
{line("Lucro final", "R$ 3.482,60", GREEN, True, True)}
</div>
</div>'''

def f2():
    return f'''<div style="width: {PW}px; height: {PH}px; position: relative; overflow: hidden; background: {NAVY}">
<div style="position: absolute; left: 36px; right: 36px; top: 54px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 10px">
<span style="{F}; color: #FFFFFF; font-size: 17px; font-weight: 500">Dezembro vende muito. 🎄</span>
<span style="{ITA}; color: #FFFFFF; font-size: 50px; line-height: 1.02; text-wrap: balance">Mas quanto sobra pra você?</span>
<span style="{F}; color: rgba(255,255,255,0.78); font-size: 14px; line-height: 1.4; max-width: 380px; margin-top: 4px">O Receitech mostra o lucro de cada venda e quanto dá pra tirar pro bolso.</span>
</div>
<img src="{PH_BROW}" alt="Brownie de Natal" style="position: absolute; left: 34px; top: 430px; width: 196px; height: 200px; object-fit: cover; border-radius: 14px">
<div style="position: absolute; left: 236px; top: 262px">{phone(lucro_screen(), 560)}</div>
</div>'''

S = f2()
if os.environ.get("PH_BROW"):
    html = page("F2 · foto única (lucro)", S, PW, PH).replace("family=Poppins:wght@400;500;600;700&amp;display=swap", "family=Poppins:wght@400;500;600;700&amp;family=Instrument+Serif:ital@0;1&amp;display=swap")
    assert "Instrument+Serif" in html
    open(os.path.join(ROOT2, "F2_lucro.dc.html"), "w").write(html)
open("/home/claude/posts/prev_F2.html", "w").write(f"<html><head><meta charset='utf-8'><link href='{FONTS}' rel='stylesheet'><style>body{{margin:0}}</style></head><body>{S}</body></html>")
print("ok")
