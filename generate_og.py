from PIL import Image
import os

bg_color = (245, 240, 232) # #f5f0e8
og_width = 1200
og_height = 630

# Create background image
img_out = Image.new('RGB', (og_width, og_height), color=bg_color)

# Load envelope_closed.webp
try:
    env_img = Image.open('themes/vintage/envelope_closed.webp').convert("RGBA")
    
    # Resize envelope to fit nicely
    target_height = int(og_height * 0.95)
    aspect_ratio = env_img.width / env_img.height
    target_width = int(target_height * aspect_ratio)
    
    env_img = env_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Calculate position to center
    pos_x = (og_width - target_width) // 2
    pos_y = (og_height - target_height) // 2
    
    # Paste using alpha composite
    img_out.paste(env_img, (pos_x, pos_y), env_img)
    
    # Save as og-image.jpg
    img_out.save('themes/vintage/og-image.jpg', quality=90)
    print("OG image generated successfully at themes/vintage/og-image.jpg")
except Exception as e:
    print(f"Error: {e}")
