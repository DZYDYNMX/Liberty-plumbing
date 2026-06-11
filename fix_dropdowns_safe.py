import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()

    # The exact block to remove from Services
    old_services_link = r'<a href="services.html" style="border-top: 1px solid var\(--border-color\); margin-top: 0.5rem; padding-top: 0.8rem; font-weight: 600; color: var\(--cyan\);">View All Services &rarr;</a>'
    html = re.sub(old_services_link, '', html)

    # The exact block to remove from Areas
    old_areas_link = r'<a href="areas.html" style="border-top: 1px solid var\(--border-color\); margin-top: 0.5rem; padding-top: 0.8rem; font-weight: 600; color: var\(--cyan\);">View All Areas &rarr;</a>'
    html = re.sub(old_areas_link, '', html)

    # Replace the start of the Services dropdown menu
    html = html.replace(
        '<div class="dropdown-menu">\n\n                        <a href="service-drain.html">Drain Cleaning</a>',
        '<div class="dropdown-menu">\n                        <a href="services.html">View All Services</a>\n                        <a href="service-drain.html">Drain Cleaning</a>'
    )
    
    # In some places it might have just one newline or different spacing. Let's be safer:
    html = re.sub(
        r'<div class="dropdown-menu">\s*<a href="service-drain.html">Drain Cleaning</a>',
        '<div class="dropdown-menu">\n                        <a href="services.html">View All Services</a>\n                        <a href="service-drain.html">Drain Cleaning</a>',
        html
    )

    # Replace the start of the Areas dropdown menu
    html = re.sub(
        r'<div class="dropdown-menu">\s*<a href="area-houston.html">Houston</a>',
        '<div class="dropdown-menu">\n                        <a href="areas.html">View All Areas</a>\n                        <a href="area-houston.html">Houston</a>',
        html
    )

    with open(filepath, 'w') as f:
        f.write(html)

print("Updated all navs safely")
