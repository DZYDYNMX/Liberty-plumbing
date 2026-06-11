import re

with open('gallery.html', 'r') as f:
    html = f.read()

def format_title(filename):
    # Remove extension
    name = filename.replace('.webp', '')
    # Replace hyphens and underscores with spaces
    name = name.replace('-', ' ').replace('_', ' ')
    # Fix typos like "andd" -> "and"
    name = name.replace('andd', 'and')
    # Title case
    return name.title()

def replace_item(match):
    full_str = match.group(0)
    src = match.group(1)
    alt = match.group(2)
    filename = src.split('/')[-1]
    title = format_title(filename)
    
    # Check if we already have an overlay to avoid duplicating
    if '<div class="gallery-overlay">' in full_str:
        return full_str
        
    return f'<div class="gallery-item"><img src="{src}" alt="{title}"><div class="gallery-overlay">{title}</div></div>'

new_html = re.sub(r'<div class="gallery-item"><img src="([^"]+)" alt="([^"]+)"></div>', replace_item, html)

with open('gallery.html', 'w') as f:
    f.write(new_html)

print("Replaced gallery items!")
