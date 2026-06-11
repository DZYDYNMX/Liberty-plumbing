import os
import re

for filename in ['toc.html', 'privacy.html']:
    with open(filename, 'r') as f:
        html = f.read()
    
    # Change section-light to section-dark
    html = html.replace('class="section section-light"', 'class="section section-dark"')
    
    # Wrap container content in legal-card
    # We find the start of the container
    container_start = '<div class="container fade-in" style="max-width: 800px; line-height: 1.8;">'
    if container_start in html:
        parts = html.split(container_start)
        # We know the end is </section>
        inner_parts = parts[1].split('</section>')
        inner_html = inner_parts[0]
        
        # Remove the closing div of the container
        inner_html = inner_html.rsplit('</div>', 1)[0]
        
        # Build new inner HTML
        new_inner = f'\n                <div class="legal-card">{inner_html}</div>\n            </div>\n'
        
        html = parts[0] + container_start + new_inner + '</section>' + inner_parts[1]
    
    with open(filename, 'w') as f:
        f.write(html)

print("Updated legal pages!")
