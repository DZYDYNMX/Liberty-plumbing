import re

with open('index.html', 'r') as f:
    index_html = f.read()

with open('areas.html', 'r') as f:
    areas_html = f.read()

footer_match = re.search(r'<footer>.*?</footer>', index_html, re.DOTALL)
if footer_match:
    good_footer = footer_match.group(0)
    # The header used <h4> in some older versions, but index.html uses <h3> now.
    # We will just replace the entire footer block.
    areas_html = re.sub(r'<footer>.*?</footer>', good_footer, areas_html, flags=re.DOTALL)
    
    with open('areas.html', 'w') as f:
        f.write(areas_html)
    print("Fixed footer in areas.html")
else:
    print("Could not find footer in index.html")
