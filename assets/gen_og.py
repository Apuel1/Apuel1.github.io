#!/usr/bin/env python3
"""Genera la og:image 1200x630 del portfolio de Manuel. Requiere Pillow.
   Salida: assets/og.png"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(__file__), "og.png")

# fondo: degradado vertical oscuro azul
img = Image.new("RGB", (W, H), "#0b1220")
px = img.load()
top = (12, 19, 34); bot = (8, 13, 26)
for y in range(H):
    f = y / H
    r = int(top[0] + (bot[0]-top[0])*f)
    g = int(top[1] + (bot[1]-top[1])*f)
    b = int(top[2] + (bot[2]-top[2])*f)
    for x in range(W):
        px[x, y] = (r, g, b)
d = ImageDraw.Draw(img)

# glow de acento (círculos suaves) arriba a la derecha
glow = Image.new("RGBA", (W, H), (0,0,0,0))
gd = ImageDraw.Draw(glow)
for rad, alpha in [(420, 26), (300, 30), (180, 34)]:
    gd.ellipse([W-rad+120, -rad+80, W+rad+120, rad+80], fill=(79,195,232,alpha))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
d = ImageDraw.Draw(img)

def font(sz, bold=True):
    cands = ([r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"] if bold
             else [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"])
    for c in cands:
        try: return ImageFont.truetype(c, sz)
        except Exception: pass
    return ImageFont.load_default()

PAD = 84
# barra de acento
d.rounded_rectangle([PAD, 150, PAD+72, 162], radius=6, fill="#4fc3e8")
# nombre
d.text((PAD, 184), "Manuel Albar Diaz", font=font(74), fill="#eef2f9")
# rol
d.text((PAD, 286), "Oracle APEX  &  PL/SQL  Developer", font=font(40), fill="#4fc3e8")
# tagline (2 lineas)
d.text((PAD, 372), "Premium custom dashboards — from the", font=font(34, False), fill="#9aa8c2")
d.text((PAD, 418), "data model to the last pixel.", font=font(34, False), fill="#9aa8c2")
# url
d.text((PAD, 520), "apuel1.github.io", font=font(30), fill="#6ee7c0")

# mini-dashboard motif abajo a la derecha
bx, by = 800, 360
d.rounded_rectangle([bx, by, bx+316, by+200], radius=16, fill="#111a2e", outline="#1f2c49", width=2)
d.rounded_rectangle([bx, by, bx+316, by+4], radius=2, fill="#4fc3e8")
for i in range(3):
    cx = bx+22+i*98
    d.rounded_rectangle([cx, by+24, cx+82, by+74], radius=8, fill="#15203a", outline="#243056")
# sparkline area
pts = [(bx+24, by+170),(bx+74, by+150),(bx+124, by+158),(bx+174, by+132),(bx+224, by+140),(bx+274, by+118),(bx+292, by+124)]
d.line(pts, fill="#4fc3e8", width=4, joint="curve")

img.save(OUT, "PNG")
print("OK ->", OUT, os.path.getsize(OUT), "bytes")
