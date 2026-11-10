"""Generator faviconow i bannerow - Auto-Serwis Kowalski."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "C:/Users/anysz/Desktop/garage-nuxt/public"
SOC = os.path.join(OUT, "social")
os.makedirs(SOC, exist_ok=True)

INK = (19, 19, 22)        # #131316
INK2 = (30, 30, 36)
RED = (225, 6, 0)          # racing red
WHITE = (255, 255, 255)
GRAY = (170, 170, 180)
DARKRED = (140, 5, 0)

FB = "C:/Windows/Fonts/arialbd.ttf"   # bold
FR = "C:/Windows/Fonts/arial.ttf"     # regular

def font(size, bold=True):
    return ImageFont.truetype(FB if bold else FR, size)

def gradient_bg(w, h):
    img = Image.new("RGB", (w, h), INK)
    d = ImageDraw.Draw(img, "RGBA")
    # vertical gradient INK2 top -> INK bottom
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(INK2[0] + (INK[0] - INK2[0]) * t)
        g = int(INK2[1] + (INK[1] - INK2[1]) * t)
        b = int(INK2[2] + (INK[2] - INK2[2]) * t)
        d.line([(0, y), (w, y)], fill=(r, g, b))
    # red glow top-right
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gx, gy, gr = int(w * 0.85), int(h * 0.1), int(min(w, h) * 0.9)
    for i in range(10, 0, -1):
        alpha = int(14 * (10 - i))
        gd.ellipse([gx - gr * i / 10, gy - gr * i / 10, gx + gr * i / 10, gy + gr * i / 10],
                   fill=(RED[0], RED[1], RED[2], alpha))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    return img

def checkers_strip(img, h_px=22):
    w, h = img.size
    d = ImageDraw.Draw(img)
    s = max(11, h_px // 2)
    y0 = h - h_px
    d.rectangle([0, y0, w, h], fill=(10, 10, 12))
    for x in range(0, w, s):
        for yi, row in enumerate(range(y0, h, s)):
            if (x // s + yi) % 2 == 0:
                d.rectangle([x, row, x + s - 1, min(row + s - 1, h - 1)], fill=(235, 235, 235))
    # red line above checkers
    d.rectangle([0, y0 - 3, w, y0 - 1], fill=RED)
    return img

def text_w(draw, txt, fnt):
    b = draw.textbbox((0, 0), txt, font=fnt)
    return b[2] - b[0], b[3] - b[1]

def draw_monogram(img, cx, cy, R):
    """Kolko z monogramem AK."""
    d = ImageDraw.Draw(img, "RGBA")
    # outer red ring + dark fill
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(16, 16, 20))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=RED, width=max(3, R // 12))
    # inner thin ring
    r2 = int(R * 0.82)
    d.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], outline=(255, 255, 255, 40), width=2)
    # AK letters
    fs = int(R * 0.95)
    f = font(fs, bold=True)
    # white AK with red K? draw "A" white + "K" red
    wa, _ = text_w(d, "A", f)
    wk, hk = text_w(d, "K", f)
    tot = wa + wk
    d.text((cx - tot / 2, cy - hk / 2 - fs * 0.06), "A", font=f, fill=WHITE)
    d.text((cx - tot / 2 + wa, cy - hk / 2 - fs * 0.06), "K", font=f, fill=RED)
    return d

def wide_banner(w, h, fname, title_size=None):
    img = gradient_bg(w, h)
    R = int(min(w, h) * (0.30 if w / h > 2 else 0.26))
    cx = int(w * (0.13 if w > 1200 else 0.16))
    cy = h // 2 - 8
    draw_monogram(img, cx, cy, R)
    d = ImageDraw.Draw(img)
    x0 = cx + R + int(w * 0.04)
    ts = title_size or int(w * 0.062)
    f1 = font(ts, bold=True)
    f2 = font(int(ts * 0.62), bold=True)
    f3 = font(max(14, int(w * 0.016)), bold=False)
    # title two lines
    d.text((x0, cy - ts * 1.35), "AUTO-SERWIS", font=f1, fill=WHITE)
    d.text((x0, cy - ts * 0.35), "KOWALSKI", font=f1, fill=RED)
    # red underline
    uw = int(w * 0.10)
    d.rectangle([x0, cy + ts * 0.78, x0 + uw, cy + ts * 0.78 + max(3, ts // 14)], fill=RED)
    d.text((x0, cy + ts * 0.95), "Mechanika  •  Diagnostyka  •  Klimatyzacja", font=f2, fill=(230, 230, 235))
    d.text((x0, cy + ts * 0.95 + int(ts * 0.62) + 8),
           "ul. Przykładowa 12, Lublin   •   tel. 500 600 700", font=f3, fill=GRAY)
    checkers_strip(img, h_px=max(16, h // 28))
    img.save(os.path.join(SOC, fname))
    print("OK", fname, img.size)

def square_center(w, h, fname, story=False):
    img = gradient_bg(w, h)
    if story:
        R = int(w * 0.26)
        cx, cy = w // 2, int(h * 0.30)
        draw_monogram(img, cx, cy, R)
        d = ImageDraw.Draw(img)
        ts = int(w * 0.105)
        f1 = font(ts, bold=True)
        for i, (t, col) in enumerate([("AUTO-SERWIS", WHITE), ("KOWALSKI", RED)]):
            tw, th = text_w(d, t, f1)
            d.text(((w - tw) / 2, cy + R + 30 + i * (th + 6)), t, font=f1, fill=col)
        f2 = font(int(w * 0.042), bold=True)
        t2 = "Mechanika • Diagnostyka • Klimatyzacja"
        tw, _ = text_w(d, t2, f2)
        d.text(((w - tw) / 2, cy + R + 34 + 2 * (ts + 8)), t2, font=f2, fill=(230, 230, 235))
        f3 = font(int(w * 0.036), bold=False)
        t3 = "ul. Przykładowa 12, Lublin"
        t4 = "tel. 500 600 700"
        for j, t in enumerate([t3, t4]):
            tw, _ = text_w(d, t, f3)
            d.text(((w - tw) / 2, int(h * 0.62) + j * 44), t, font=f3, fill=GRAY if j == 0 else WHITE)
    else:
        R = int(min(w, h) * 0.20)
        cx, cy = w // 2, int(h * 0.36)
        draw_monogram(img, cx, cy, R)
        d = ImageDraw.Draw(img)
        ts = int(w * (0.085 if w <= 900 else 0.06))
        f1 = font(ts, bold=True)
        for i, (t, col) in enumerate([("AUTO-SERWIS", WHITE), ("KOWALSKI", RED)]):
            tw, th = text_w(d, t, f1)
            d.text(((w - tw) / 2, cy + R + 24 + i * (th + 4)), t, font=f1, fill=col)
        f2 = font(int(ts * 0.42), bold=False)
        t2 = "ul. Przykładowa 12, Lublin  •  500 600 700"
        tw, _ = text_w(d, t2, f2)
        d.text(((w - tw) / 2, cy + R + 30 + 2 * (ts + 2)), t2, font=f2, fill=GRAY)
    checkers_strip(img, h_px=max(16, h // 40))
    img.save(os.path.join(SOC, fname))
    print("OK", fname, img.size)

# ---------- FAVICON MASTER ----------
def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m

S = 1024
master = Image.new("RGB", (S, S), (16, 16, 20))
md = ImageDraw.Draw(master, "RGBA")
# subtle diagonal stripes
for i in range(-S, S * 2, 64):
    md.polygon([(i, 0), (i + 28, 0), (i + 28 - S, S), (i - S, S)], fill=(255, 255, 255, 7))
# red ring + AK
R = 330
cx = cy = S // 2
md.ellipse([cx - R - 26, cy - R - 26, cx + R + 26, cy + R + 26], fill=RED)
md.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(16, 16, 20))
f_ak = font(430, bold=True)
tmp = ImageDraw.Draw(master)
wa, _ = text_w(tmp, "A", f_ak)
wk, hk = text_w(tmp, "K", f_ak)
tot = wa + wk
tmp.text((cx - tot / 2, cy - hk / 2 - 30), "A", font=f_ak, fill=WHITE)
tmp.text((cx - tot / 2 + wa, cy - hk / 2 - 30), "K", font=f_ak, fill=RED)
# rounded corners
mask = rounded_mask(S, 220)
master.putalpha(mask)
master_rgb = Image.new("RGB", (S, S), (19, 19, 22))
master_rgb.paste(master, mask=master)
master = master_rgb

master.save(os.path.join(OUT, "icon-1024.png"))
for name, px in [("favicon-16x16.png", 16), ("favicon-32x32.png", 32),
                 ("apple-touch-icon.png", 180), ("android-chrome-192x192.png", 192),
                 ("android-chrome-512x512.png", 512), ("mstile-150x150.png", 150)]:
    master.resize((px, px), Image.LANCZOS).save(os.path.join(OUT, name))
# multi-size ICO
icons = [master.resize((s, s), Image.LANCZOS) for s in (16, 32, 48)]
icons[0].save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
print("OK favicons")

# ---------- BANERY ----------
# OG / strona (Facebook, LinkedIn post, Discord, Google): 1200x630 -> JPG do / + PNG do social/
og = gradient_bg(1200, 630)
draw_monogram(og, 150, 300, 105)
d = ImageDraw.Draw(og)
f1 = font(76, bold=True); f2 = font(44, bold=True); f3 = font(24, bold=False)
d.text((290, 170), "AUTO-SERWIS", font=f1, fill=WHITE)
d.text((290, 255), "KOWALSKI", font=f1, fill=RED)
d.rectangle([292, 352, 410, 360], fill=RED)
d.text((292, 375), "Mechanika  •  Diagnostyka  •  Klimatyzacja", font=f2, fill=(230, 230, 235))
d.text((292, 445), "ul. Przykładowa 12, Lublin   •   tel. 500 600 700", font=f3, fill=GRAY)
checkers_strip(og, h_px=24)
og.save(os.path.join(OUT, "og-cover.jpg"), quality=88)
og.save(os.path.join(SOC, "og-cover-1200x630.png"))
print("OK og-cover")

wide_banner(1640, 624, "facebook-cover-1640x624.png")
wide_banner(1500, 500, "x-header-1500x500.png")
wide_banner(1584, 396, "linkedin-cover-1584x396.png")
wide_banner(2560, 1440, "youtube-banner-2560x1440.png", title_size=150)
square_center(1080, 1080, "instagram-post-1080x1080.png")
square_center(1080, 1920, "instagram-story-1080x1920.png", story=True)
# awatar uniwersalny (FB/IG/TT/YT profil)
av = gradient_bg(800, 800)
draw_monogram(av, 400, 350, 210)
d = ImageDraw.Draw(av)
f = font(72, bold=True)
tw, th = text_w(d, "KOWALSKI", f)
d.text(((800 - tw) / 2, 590), "KOWALSKI", font=f, fill=WHITE)
checkers_strip(av, h_px=26)
av.save(os.path.join(SOC, "profile-avatar-800x800.png"))
print("OK avatar")
print("DONE")
