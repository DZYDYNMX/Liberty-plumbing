import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()

    # Remove <div class="label">...</div> globally
    new_html = re.sub(r'<div class="label">.*?</div>\s*', '', html, flags=re.DOTALL)

    if new_html != html:
        with open(filepath, 'w') as f:
            f.write(new_html)

print("Removed all labels from HTML files")
