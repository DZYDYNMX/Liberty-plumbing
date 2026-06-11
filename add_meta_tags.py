import glob
import re

meta_additions = """    <meta property="og:image" content="https://liberty-plumbing-example.com/assets/hero-bg.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Liberty Plumbing">
    <meta name="twitter:description" content="Premium 24/7 plumbing services for residential and commercial.">
    <meta name="twitter:image" content="https://liberty-plumbing-example.com/assets/hero-bg.jpg">"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()

    # Look for the last og: tag and insert after it
    if 'twitter:card' not in html:
        html = re.sub(
            r'(<meta property="og:url"[^>]+>)',
            r'\1\n' + meta_additions,
            html
        )
        with open(filepath, 'w') as f:
            f.write(html)

print("Added meta tags")
