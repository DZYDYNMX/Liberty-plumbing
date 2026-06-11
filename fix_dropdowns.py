import glob
import re

old_services_button = """                        <div style="padding: 0.5rem; border-top: 1px solid var(--border-color); margin-top: 0.5rem;">
                            <a href="services.html" class="btn btn-cyan" style="width: 100%; justify-content: center; padding: 0.5rem; font-size: 0.85rem;">View All Services &rarr;</a>
                        </div>"""

new_services_button = """                        <a href="services.html" style="border-top: 1px solid var(--border-color); margin-top: 0.5rem; padding-top: 0.8rem; font-weight: 600; color: var(--cyan);">View All Services &rarr;</a>"""

areas_dropdown = """                <li>
                    <a href="areas.html"{active_class}>Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu">
                        <a href="area-houston.html">Houston</a>
                        <a href="area-katy.html">Katy</a>
                        <a href="area-sugar-land.html">Sugar Land</a>
                        <a href="area-spring.html">Spring</a>
                        <a href="area-cypress.html">Cypress</a>
                        <a href="area-galveston.html">Galveston</a>
                        <a href="areas.html" style="border-top: 1px solid var(--border-color); margin-top: 0.5rem; padding-top: 0.8rem; font-weight: 600; color: var(--cyan);">View All Areas &rarr;</a>
                    </div>
                </li>"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Replace services button
    if old_services_button in html:
        html = html.replace(old_services_button, new_services_button)
    
    # Replace areas link with dropdown
    # We might have <li><a href="areas.html">Service Areas</a></li>
    # Or <li><a href="areas.html" class="active">Service Areas</a></li>
    
    html = re.sub(
        r'<li>\s*<a href="areas\.html">Service Areas</a>\s*</li>',
        areas_dropdown.replace('{active_class}', ''),
        html
    )
    
    html = re.sub(
        r'<li>\s*<a href="areas\.html" class="active">Service Areas</a>\s*</li>',
        areas_dropdown.replace('{active_class}', ' class="active"'),
        html
    )
    
    with open(filepath, 'w') as f:
        f.write(html)
        
print("Updated all navs")
