import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# Fix footer hovers
css = css.replace('.footer-col ul a:hover { color: var(--cyan); }', '.footer-col ul a:hover { color: var(--red); }')
css = css.replace('.footer-legal a:hover {\n    color: var(--cyan);\n}', '.footer-legal a:hover {\n    color: var(--red);\n}')

# Fix service text card hovers
css = css.replace('.service-text-card:hover {\n    transform: translateY(-5px);\n    border-color: var(--cyan);\n}', '.service-text-card:hover {\n    transform: translateY(-5px);\n    border-color: var(--red);\n}')
css = css.replace('.explore-link:hover {\n    color: var(--cyan);\n}', '.explore-link:hover {\n    color: var(--red);\n}')

# Fix glow-card hovers to red (the user wanted the glow gradient to be cyan but hover is "for things" - I'll leave the glow card as cyan for now, but button hovers are definitely red)

with open(css_path, 'w') as f:
    f.write(css)

print("Missed hovers fixed!")
