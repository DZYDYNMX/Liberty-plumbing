import re

# 1. Update areas.html
with open('areas.html', 'r') as f:
    html = f.read()

# Replace <ul class="area-directory"> with <div class="area-directory-pills">
html = html.replace('<ul class="area-directory">', '<div class="area-directory-pills">')
# Replace </ul> with </div>
html = html.replace('</ul>', '</div>')
# Replace <li><a href="..." class="...">...</a></li> with <a href="..." class="pill-btn">...</a>
html = re.sub(r'<li>\s*<a href="([^"]+)">([^<]+)</a>\s*</li>', r'<a href="\1" class="pill-btn">\2</a>', html)

with open('areas.html', 'w') as f:
    f.write(html)


# 2. Update styles.css
with open('styles.css', 'r') as f:
    css = f.read()

# Remove the hover effect for marquee-item
hover_pattern = r'@media \(min-width: 769px\) \{\s*\.marquee-item:hover \{\s*transform: translateY\(-2px\);\s*background: rgba\(255, 255, 255, 0\.08\);\s*border-color: var\(--cyan\);\s*color: var\(--white\);\s*box-shadow: 0 4px 12px rgba\(0, 0, 0, 0\.3\);\s*\}\s*\}'
css = re.sub(hover_pattern, '', css)

# Replace area-directory with area-directory-pills
pill_css = """
/* ===========================================================
   AREA DIRECTORY LIST (SERVICE AREAS)
   =========================================================== */
.area-directory-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    max-width: 900px;
    margin: 0 auto;
}
.pill-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.6rem 1.5rem;
    color: var(--light-gray);
    font-weight: 600;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    text-decoration: none;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 50px;
    background: rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}
.pill-btn:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.08);
    border-color: var(--cyan);
    color: var(--white);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}
"""

old_area_css = """/* ===========================================================
   AREA DIRECTORY LIST (SERVICE AREAS)
   =========================================================== */
.area-directory {
    column-count: 3;
    column-gap: 3rem;
    list-style: none;
    padding: 0;
    margin: 0 auto;
    max-width: 800px;
}
.area-directory li {
    margin-bottom: 1rem;
    break-inside: avoid;
}
.area-directory a {
    color: var(--white);
    text-decoration: none;
    font-size: 1.1rem;
    display: inline-block;
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    width: 100%;
    transition: all 0.3s ease;
}
.area-directory a:hover {
    color: var(--cyan);
    border-bottom-color: var(--cyan);
    transform: translateX(5px);
}
@media (max-width: 768px) {
    .area-directory {
        column-count: 2;
        column-gap: 1.5rem;
    }
}
@media (max-width: 480px) {
    .area-directory {
        column-count: 1;
    }
}"""

if old_area_css in css:
    css = css.replace(old_area_css, pill_css)
else:
    print("WARNING: Could not find old area-directory CSS block. Appending instead.")
    css += pill_css

with open('styles.css', 'w') as f:
    f.write(css)

print("Updated areas.html and styles.css!")
