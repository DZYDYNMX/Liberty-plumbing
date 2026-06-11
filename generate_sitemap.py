import glob
from datetime import datetime

html_files = glob.glob('*.html')
base_url = "https://liberty-plumbing-example.com"
sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for f in html_files:
    priority = "0.8"
    if f == "index.html":
        priority = "1.0"
    elif f.startswith("area-") or f.startswith("service-"):
        priority = "0.6"
    
    sitemap_content.append("  <url>")
    sitemap_content.append(f"    <loc>{base_url}/{f}</loc>")
    sitemap_content.append(f"    <priority>{priority}</priority>")
    sitemap_content.append("  </url>")

sitemap_content.append("</urlset>")

with open('sitemap.xml', 'w') as f:
    f.write('\n'.join(sitemap_content))
print("Sitemap generated successfully.")
