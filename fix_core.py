import os
import re

files = ["index.html", "about.html", "areas.html", "services.html", "toc.html", "privacy.html"]
base_dir = "/Users/Cyanide/.gemini/antigravity/scratch/plumbing-website"

for fname in files:
    path = os.path.join(base_dir, fname)
    if not os.path.exists(path):
        continue
    with open(path, "r") as f:
        content = f.read()

    # 1. Fix tel:5550198
    content = content.replace("tel:5550198", "tel:+15550198123")

    # 2. Fix email in footer
    content = re.sub(r'<strong>Email:</strong>\s*info@libertyplumbing\.com', '<strong>Email:</strong> <a href="mailto:info@libertyplumbing.com" style="color:var(--muted); text-decoration:none;">info@libertyplumbing.com</a>', content)

    # 5. Add favicon and open graph to head
    if '<link rel="icon" href="data:,">' not in content:
        head_end = content.find('</head>')
        if head_end != -1:
            injection = """    <link rel="icon" href="data:,">
    <meta property="og:title" content="Liberty Plumbing">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://liberty-plumbing-example.com/">
"""
            content = content[:head_end] + injection + content[head_end:]

    # 6. Add LocalBusiness JSON-LD schema to index.html
    if fname == "index.html" and "application/ld+json" not in content:
        head_end = content.find('</head>')
        if head_end != -1:
            schema = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Liberty Plumbing",
      "image": "https://liberty-plumbing-example.com/assets/logo.png",
      "@id": "https://liberty-plumbing-example.com/",
      "url": "https://liberty-plumbing-example.com/",
      "telephone": "+15550198123",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "123 Plumbing Way",
        "addressLocality": "Houston",
        "addressRegion": "TX",
        "postalCode": "77001",
        "addressCountry": "US"
      }
    }
    </script>
"""
            content = content[:head_end] + schema + content[head_end:]

    # 7. Consistentize footer Services links
    footer_services = """<h4>Services</h4>
                <ul>
                    <li><a href="service-drain.html">Drain Cleaning</a></li>
                    <li><a href="service-repipe.html">Repiping</a></li>
                    <li><a href="service-waterheater.html">Water Heaters</a></li>
                    <li><a href="service-leak.html">Leak Detection</a></li>
                    <li><a href="service-sewer.html">Sewer Repair</a></li>
                </ul>"""
    content = re.sub(r'<h4>Services</h4>\s*<ul>.*?</ul>', footer_services, content, flags=re.DOTALL)

    # 3. Fix service cards in index.html and services.html
    if fname in ["index.html", "services.html"]:
        pattern = r'<div class="service-card" onclick="location\.href=\'([^\']+)\'">(.*?)</div>\s*</div>'
        def repl(m):
            href = m.group(1)
            inner = m.group(2)
            # inner will contain the <img> and the <div class="service-card-overlay">...
            # The regex matched up to the FIRST </div> which is the closing of the overlay
            # and then \s*</div> matched the closing of the card.
            return f'<a href="{href}" class="service-card" style="text-decoration:none; color:inherit; display:block;">{inner}</div>\n                    </a>'
        content = re.sub(pattern, repl, content, flags=re.DOTALL)

    with open(path, "w") as f:
        f.write(content)

print("Done phase 1")
