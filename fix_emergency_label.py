import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# Revert emergency-text label to cyan
css = css.replace('.emergency-text .label {\n    color: var(--red);', '.emergency-text .label {\n    color: var(--cyan);')

with open(css_path, 'w') as f:
    f.write(css)

print("Emergency label reverted to cyan.")
