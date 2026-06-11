import re

with open('index.html', 'r') as f:
    html = f.read()

def replace_item(match):
    full_str = match.group(0)
    src = match.group(1)
    alt = match.group(2)
    return f'<div class="image-marquee-item"><img src="{src}" alt="{alt}" loading="lazy"><div class="image-marquee-overlay">{alt}</div></div>'

new_html = re.sub(r'<div class="image-marquee-item"><img src="([^"]+)" alt="([^"]+)" loading="lazy"></div>', replace_item, html)

with open('index.html', 'w') as f:
    f.write(new_html)

print("Replaced!")
