import os
from PIL import Image

ASSETS_DIR = 'assets'

def optimize_images():
    for filename in os.listdir(ASSETS_DIR):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            filepath = os.path.join(ASSETS_DIR, filename)
            webp_filepath = os.path.join(ASSETS_DIR, os.path.splitext(filename)[0] + '.webp')
            
            try:
                with Image.open(filepath) as img:
                    # Convert to RGB if necessary
                    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                        bg = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'RGBA':
                            bg.paste(img, mask=img.split()[3])
                        else:
                            bg.paste(img)
                        img = bg
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')
                        
                    # Resize if too large
                    max_size = (800, 800)
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    
                    # Save as WebP
                    img.save(webp_filepath, 'WEBP', quality=85, method=6)
                    print(f"Optimized: {filename} -> {os.path.basename(webp_filepath)}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    optimize_images()
