import os
from PIL import Image

source_dir = "/Users/Cyanide/Downloads/untitled folder"
target_dir = "/Users/Cyanide/.gemini/antigravity/scratch/plumbing-website/assets/gallery"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

valid_extensions = {".jpg", ".jpeg", ".png", ".webp"}

for filename in os.listdir(source_dir):
    ext = os.path.splitext(filename)[1].lower()
    if ext in valid_extensions:
        source_path = os.path.join(source_dir, filename)
        
        # We will save everything as webp to be modern and efficient
        target_filename = os.path.splitext(filename)[0] + ".webp"
        target_path = os.path.join(target_dir, target_filename)
        
        try:
            with Image.open(source_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Double the resolution
                new_width = img.width * 2
                new_height = img.height * 2
                
                print(f"Upscaling {filename} from {img.width}x{img.height} to {new_width}x{new_height}...")
                
                # Resize using LANCZOS for high quality upscaling
                upscaled_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Save as webp with high quality
                upscaled_img.save(target_path, "WEBP", quality=90)
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Image processing complete.")
