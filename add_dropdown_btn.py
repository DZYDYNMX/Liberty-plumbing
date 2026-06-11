import glob
import re

button_html = """
                        <div style="padding: 0.5rem; border-top: 1px solid var(--border-color); margin-top: 0.5rem;">
                            <a href="services.html" class="btn btn-cyan" style="width: 100%; justify-content: center; padding: 0.5rem; font-size: 0.85rem;">View All Services &rarr;</a>
                        </div>
                    </div>"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # We want to replace the end of the dropdown-menu
    # specifically the <a href="service-emergency.html">Emergency Repairs</a> followed by spaces and </div>
    new_html = re.sub(r'<a href="service-emergency\.html">Emergency Repairs</a>\s*</div>', 
                      r'<a href="service-emergency.html">Emergency Repairs</a>' + button_html, html)
    
    with open(filepath, 'w') as f:
        f.write(new_html)
print("Updated all HTML files")
