import re

with open('styles.css', 'r') as f:
    css = f.read()

# Fix the a selector
css = css.replace('.dropdown-menu a {', '.dropdown-menu a:not(.btn) {')
css = css.replace('.dropdown-menu a:hover {', '.dropdown-menu a:not(.btn):hover {')

with open('styles.css', 'w') as f:
    f.write(css)
print("Fixed CSS specificity")
