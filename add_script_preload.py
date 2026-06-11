import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()

    # Move script.js to head with defer
    # 1. Remove from bottom
    script_regex = r'<script src="script\.js\?v=[0-9]+"></script>\s*'
    html = re.sub(script_regex, '', html)
    
    # 2. Add to head
    head_close_idx = html.find('</head>')
    if head_close_idx != -1 and 'script.js' not in html:
        insert_script = '    <script src="script.js?v=33" defer></script>\n'
        html = html[:head_close_idx] + insert_script + html[head_close_idx:]

    # Add preload for hero images
    if '<link rel="preload"' not in html:
        # Determine hero image
        # Simple heuristic: if it contains assets/areas-hero.png use that, else assets/bg-1.png
        if 'assets/areas-hero.png' in html:
            preload = '    <link rel="preload" href="assets/areas-hero.png" as="image">\n'
        else:
            preload = '    <link rel="preload" href="assets/bg-1.png" as="image">\n'
        
        html = html[:head_close_idx] + preload + html[head_close_idx:]

    with open(filepath, 'w') as f:
        f.write(html)

print("Moved script and added preload")
