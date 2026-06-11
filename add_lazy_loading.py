import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()

    # Find all <img> tags
    # Add loading="lazy" if not present, UNLESS it's the hero image (e.g., id="bg-image" or assets/areas-hero.png)
    
    def repl(m):
        tag = m.group(0)
        if 'loading="lazy"' in tag:
            return tag
        if 'id="bg-image"' in tag or 'hero-bg' in tag or 'areas-hero' in tag or 'assets/bg-1.png' in tag:
            return tag
        
        # Insert loading="lazy" before the closing bracket
        return tag[:-1] + ' loading="lazy">'

    html = re.sub(r'<img[^>]+>', repl, html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Added lazy loading to images")
