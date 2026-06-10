import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# Remove the global label rule I added
css = css.replace('\n.label { color: var(--red) !important; }\n', '')

# Make sure .section-header .label is red (this covers the ones above <h2> elements in sections)
if '.section-header .label {\n    color: var(--cyan);' in css:
    css = css.replace('.section-header .label {\n    color: var(--cyan);', '.section-header .label {\n    color: var(--red);')

# Wait, in an earlier fix I might have already replaced section-header .label to red. Let's make sure it's strictly correct.
# The user pasted: ".section-header .label { color: #ef4444; ... }"
# I'll just forcefully ensure .section-header .label is red.
css = css.replace('.section-header .label {\n    color: var(--cyan);', '.section-header .label {\n    color: var(--red);')

# Also, ensure stat-label and other specific labels don't get the red if they were overridden. 
# They shouldn't be affected if the global rule is gone.

with open(css_path, 'w') as f:
    f.write(css)

print("Label fixes applied.")
