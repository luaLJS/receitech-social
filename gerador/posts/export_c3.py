import asyncio
from playwright.async_api import async_playwright
OUT="/home/claude/receitech-social/2026-11-12"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for src, name in [("prev_C3_S1.html","c3_s1_gancho.jpg"),("prev_C3_S2.html","c3_s2_app.jpg")]:
            pg = await b.new_page(viewport={"width":540,"height":720}, device_scale_factor=2)
            await pg.goto(f"file:///home/claude/posts/{src}")
            await pg.wait_for_timeout(1500)
            await pg.screenshot(path=f"{OUT}/{name}", type="jpeg", quality=92, clip={"x":0,"y":0,"width":540,"height":720})
        await b.close()
asyncio.run(main())
