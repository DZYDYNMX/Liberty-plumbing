import os
import re

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# Update .btn-cyan
btn_blue_old = """.btn-cyan {
    background: var(--cyan);
    color: var(--navy-dark);
}
.btn-cyan:hover {
    background: #fff;
    color: var(--navy-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,212,255,0.3);
}"""

btn_blue_new = """.btn-cyan {
    background: var(--white);
    color: var(--cyan);
}
.btn-cyan:hover {
    background: var(--cyan);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}"""
css = css.replace(btn_blue_old, btn_blue_new)

# Update nav-cta-btn
nav_cta_old = """    background: var(--cyan);
    color: var(--navy-dark);"""
nav_cta_new = """    background: var(--white);
    color: var(--cyan);"""
css = css.replace(nav_cta_old, nav_cta_new)

nav_hover_old = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: #fff; 
    color: var(--navy-dark); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,212,255,0.3);
}"""
nav_hover_new = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--cyan); 
    color: var(--white); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}"""
css = css.replace(nav_hover_old, nav_hover_new)

# Write CSS
with open(css_path, 'w') as f:
    f.write(css)

# Update all HTML and python generator files
for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py')):
            if file == 'fix_all_buttons.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content
            # Change any btn-cyan back to btn-cyan
            new_content = new_content.replace('btn-cyan', 'btn-cyan')
            # Fix any inline box-shadows using the blue color
            new_content = new_content.replace('rgba(0, 212, 255, 0.3)', 'rgba(0, 212, 255, 0.3)')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("All buttons fixed!")
