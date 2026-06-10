import os
import re

# 1. Update styles.css
css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# Replace glow-card cyan with red
# Only in the .glow-card rules. Since they are the only ones around line 490.
glow_old = """.glow-card {
    background: rgba(10, 22, 40, 0.6);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 1.25rem;
    padding: 3rem 2rem;
    text-align: left;
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease;
    z-index: 1;
}
.glow-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at top left, rgba(0, 212, 255, 0.15), transparent 60%);
    z-index: -1;
    transition: all 0.4s ease;
}
.glow-card:hover {
    transform: translateY(-8px);
    border-color: rgba(0, 212, 255, 0.4);
    box-shadow: 0 15px 35px rgba(0, 212, 255, 0.15);
}
.glow-card:hover::before {
    background: radial-gradient(circle at top left, rgba(0, 212, 255, 0.25), transparent 70%);
}"""

glow_new = """.glow-card {
    background: rgba(10, 22, 40, 0.6);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 1.25rem;
    padding: 3rem 2rem;
    text-align: left;
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease;
    z-index: 1;
}
.glow-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at top left, rgba(0, 212, 255, 0.15), transparent 60%);
    z-index: -1;
    transition: all 0.4s ease;
}
.glow-card:hover {
    transform: translateY(-8px);
    border-color: rgba(0, 212, 255, 0.4);
    box-shadow: 0 15px 35px rgba(0, 212, 255, 0.15);
}
.glow-card:hover::before {
    background: radial-gradient(circle at top left, rgba(0, 212, 255, 0.25), transparent 70%);
}"""
css = css.replace(glow_old, glow_new)

# Add .btn-cyan
btn_white_red_css = """
.btn-cyan {
    background: var(--white);
    color: var(--cyan);
}
.btn-cyan:hover {
    background: var(--cyan);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}
"""
if '.btn-cyan {' not in css:
    css = css.replace('.btn-cyan {', btn_white_red_css + '\n.btn-cyan {')

with open(css_path, 'w') as f:
    f.write(css)

# 2. Update all HTML/PY files
for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py')):
            if file == 'targeted_fixes.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content
            # Remove inline border-color on marquee
            new_content = new_content.replace(' style="border-color: #ef4444;"', '')
            
            # Replace form submit button class
            new_content = new_content.replace('class="full-width btn-cyan"', 'class="full-width btn-cyan"')
            new_content = new_content.replace('class="btn btn-cyan" style="width:100%; border:none; margin-top:0.5rem;"', 'class="btn btn-cyan" style="width:100%; border:none; margin-top:0.5rem;"')
            
            # Replace mobile CTA button class
            new_content = new_content.replace('class="btn btn-cyan hide-on-desktop contact-btn"', 'class="btn btn-cyan hide-on-desktop contact-btn"')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("Targeted fixes applied!")
