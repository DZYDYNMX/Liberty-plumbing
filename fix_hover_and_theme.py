import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. Update root variables
root_old = """:root {
    --navy-dark: #0a1628;
    --navy-mid: #0f2145;
    --navy-light: #162d5a;
    --red: #d93838;
    --red-dark: #a82020;
    --red-gradient: linear-gradient(135deg, #d93838, #a82020);
    --cyan: #00d4ff;
    --cyan-dark: #0284c7;
    --cyan-gradient: linear-gradient(135deg, #00d4ff, #0284c7);"""

root_new = """:root {
    --navy-dark: #0a1628;
    --navy-mid: #0f2145;
    --navy-light: #162d5a;
    --cyan: #00d4ff;
    --cyan-dark: #0284c7;
    --cyan-gradient: linear-gradient(135deg, #00d4ff, #0284c7);
    --red: #ef4444;"""
css = css.replace(root_old, root_new)

# Clean up any leftover btn-white-red rules
white_red_css = """
.btn-white-cyan {
    background: var(--white);
    color: var(--cyan);
}
.btn-white-cyan:hover {
    background: var(--cyan);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}
"""
css = css.replace(white_red_css, "")

# 2. Update button styles in CSS to have RED hovers instead of white/cyan hovers
btn_cyan_old = """.btn-cyan {
    background: var(--white);
    color: var(--cyan);
}
.btn-cyan:hover {
    background: var(--cyan);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}"""
btn_cyan_new = """.btn-cyan {
    background: var(--cyan);
    color: var(--navy-dark);
}
.btn-cyan:hover {
    background: var(--red);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
css = css.replace(btn_cyan_old, btn_cyan_new)

nav_cta_old = """    background: var(--white);
    color: var(--cyan);"""
nav_cta_new = """    background: var(--cyan);
    color: var(--navy-dark);"""
css = css.replace(nav_cta_old, nav_cta_new)

nav_cta_hover_old = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--cyan); 
    color: var(--white); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}"""
nav_cta_hover_new = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--red); 
    color: var(--white); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
css = css.replace(nav_cta_hover_old, nav_cta_hover_new)

btn_outline_old = """.btn-outline {
    background: transparent;
    color: var(--cyan);
    border: 2px solid var(--cyan);
}
.btn-outline:hover {
    background: var(--cyan);
    color: var(--navy-dark);
}"""
btn_outline_new = """.btn-outline {
    background: transparent;
    color: var(--cyan);
    border: 2px solid var(--cyan);
}
.btn-outline:hover {
    background: var(--red);
    border-color: var(--red);
    color: var(--white);
}"""
css = css.replace(btn_outline_old, btn_outline_new)

# 3. Logo and Nav Hovers to RED
css = css.replace('.logo-text span { color: var(--cyan); }', '.logo-text span { color: var(--red); }')
css = css.replace('.nav-links > li > button:hover { color: var(--cyan); }', '.nav-links > li > button:hover { color: var(--red); }')
css = css.replace('.nav-links a.active {\n    color: var(--cyan);\n}', '.nav-links a.active {\n    color: var(--red);\n}')

# Global link hovers? Original had a { transition } but no global a:hover. Let's add it.
if 'a:hover { color: var(--red); }' not in css:
    css = css.replace('a { color: var(--cyan); text-decoration: none; transition: all 0.3s ease; }', 
                      'a { color: var(--cyan); text-decoration: none; transition: all 0.3s ease; }\na:hover { color: var(--red); }')

with open(css_path, 'w') as f:
    f.write(css)

# Update HTML files
for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py')):
            if file == 'fix_hover_and_theme.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content.replace('btn-white-cyan', 'btn-cyan')
            new_content = new_content.replace('btn-white-red', 'btn-cyan')
            # Remove any subtle red text-red from the footer "24/7" I added previously:
            new_content = new_content.replace('<strong>Hours:</strong> <span class="text-cyan">24/7</span> Emergency Service', '<strong>Hours:</strong> 24/7 Emergency Service')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("Theme reset to cyan with red hovers and logo.")
