import glob
import re

new_v = 37

for file in glob.glob("*.py") + glob.glob("*.html"):
    if file == "fix_generators_cache.py": continue
    with open(file, "r") as f:
        content = f.read()
    
    # Replace v=XX with v=37 in all link/script tags globally in py and html files
    content = re.sub(r'(styles\.css\?v=)\d+', rf'\g<1>{new_v}', content)
    content = re.sub(r'(script\.js\?v=)\d+', rf'\g<1>{new_v}', content)
    
    with open(file, "w") as f:
        f.write(content)

print(f"Fixed all hardcoded cache versions to {new_v}")
