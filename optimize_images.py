import os
from PIL import Image

targets = [
    'assets/service-emergency.webp',
    'assets/hero-plumber.webp'
]

gallery_dir = 'assets/gallery'
if os.path.exists(gallery_dir):
    for f in os.listdir(gallery_dir):
        if f.endswith('.webp'):
            targets.append(os.path.join(gallery_dir, f))

for filepath in targets:
    if os.path.exists(filepath):
        try:
            with Image.open(filepath) as img:
                # Resize if larger than 600px width/height
                max_dim = 600
                if img.width > max_dim or img.height > max_dim:
                    img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
                
                # Save with compression
                img.save(filepath, 'WEBP', quality=75, method=6)
                print(f"Optimized {filepath}")
        except Exception as e:
            print(f"Failed to optimize {filepath}: {e}")

