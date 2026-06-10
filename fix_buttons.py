import os
import re

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. Add blue variables
blue_vars = """    --blue: #00d4ff;
    --blue-dark: #0284c7;
    --blue-gradient: linear-gradient(135deg, #00d4ff, #0284c7);"""
if '--blue:' not in css:
    css = css.replace('    --red-gradient: linear-gradient(135deg, #d93838, #a82020);', '    --red-gradient: linear-gradient(135deg, #d93838, #a82020);\n' + blue_vars)

# 2. Change buttons in CSS to use blue
css = css.replace('.btn-cyan {', '.btn-cyan {')
css = css.replace('.btn-cyan:hover {', '.btn-cyan:hover {')

# Find btn-cyan block and replace var(--cyan) with var(--cyan)
# Actually let's just do targeted replaces for the button definitions:
btn_blue_block_old = """.btn-cyan {
    background: var(--cyan);
    color: var(--navy-dark);
}
.btn-cyan:hover {
    background: #fff;
    color: var(--navy-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,212,255,0.3);
}"""

btn_blue_block_new = """.btn-cyan {
    background: var(--cyan);
    color: var(--navy-dark);
}
.btn-cyan:hover {
    background: #fff;
    color: var(--navy-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,212,255,0.3);
}"""
css = css.replace(btn_blue_block_old, btn_blue_block_new)

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
    background: var(--cyan);
    color: var(--navy-dark);
}"""
css = css.replace(btn_outline_old, btn_outline_new)

# nav-cta-btn uses red currently. Change it to blue.
nav_cta_old = """    background: var(--cyan);
    color: var(--navy-dark);
    border: none;
    border-radius: 4px;"""
nav_cta_new = """    background: var(--cyan);
    color: var(--navy-dark);
    border: none;
    border-radius: 4px;"""
css = css.replace(nav_cta_old, nav_cta_new)

# write CSS back
with open(css_path, 'w') as f:
    f.write(css)

# 3. Replace btn-cyan with btn-cyan across all files
for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py', '.js', '.css')):
            if file == 'fix_buttons.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content.replace('btn-cyan', 'btn-cyan')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("Buttons fixed!")
