import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. Glow card hover
glow_hover_old = """.glow-card:hover {
    transform: translateY(-8px);
    border-color: rgba(239, 68, 68, 0.4);
    box-shadow: 0 15px 35px rgba(239, 68, 68, 0.15);
}
.glow-card:hover::before {
    background: radial-gradient(circle at top left, rgba(239, 68, 68, 0.25), transparent 70%);
}"""
glow_hover_new = """.glow-card:hover {
    transform: translateY(-8px);
    border-color: rgba(239, 68, 68, 0.4);
    box-shadow: 0 15px 35px rgba(0, 212, 255, 0.15);
}
.glow-card:hover::before {
    background: radial-gradient(circle at top left, rgba(0, 212, 255, 0.25), transparent 70%);
}"""
css = css.replace(glow_hover_old, glow_hover_new)

# 2. Button outline hover
outline_hover_old = """.btn-outline:hover {
    background: transparent;
    border-color: var(--cyan);
    color: var(--red);
}"""
outline_hover_new = """.btn-outline:hover {
    background: transparent;
    border-color: var(--red);
    color: var(--red);
}"""
css = css.replace(outline_hover_old, outline_hover_new)

# 3. Label color
css = css.replace('.section-header .label {\n    color: var(--cyan);', '.section-header .label {\n    color: var(--red);')
css = css.replace('.emergency-text .label {\n    color: var(--cyan);', '.emergency-text .label {\n    color: var(--red);')

with open(css_path, 'w') as f:
    f.write(css)

print("Final tweaks applied.")
