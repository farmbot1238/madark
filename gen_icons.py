from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

def make_icon(size):
    img = Image.new('RGBA', (size, size), (10, 10, 15, 255))
    draw = ImageDraw.Draw(img)
    
    # Gold gradient circle background
    cx, cy = size // 2, size // 2
    r = int(size * 0.45)
    
    # Draw multiple circles for gradient effect
    for i in range(r, 0, -1):
        ratio = i / r
        g_r = int(255 * (0.7 + 0.3 * ratio))
        g_g = int(215 * ratio)
        g_b = 0
        draw.ellipse([cx-i, cy-i, cx+i, cy+i], fill=(g_r, g_g, g_b, 255))
    
    # Crown emoji approximation - text
    try:
        font_size = int(size * 0.35)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Draw crown
    text = "م"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw//2, cy - th//2), text, fill=(10, 10, 15, 255), font=font)
    
    return img

for s in [192, 512]:
    icon = make_icon(s)
    icon.save(f'icons/icon-{s}.png')
    print(f"Created icon-{s}.png")
