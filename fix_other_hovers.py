import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. Feature card hover
feature_hover_old = """.feature-card:hover {
    transform: translateY(-5px);
    border-color: var(--red);
    box-shadow: 0 10px 30px rgba(239, 68, 68, 0.15);
}"""
feature_hover_new = """.feature-card:hover {
    transform: translateY(-5px);
    border-color: var(--cyan);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.feature-card:hover h3 {
    color: var(--red);
}"""
css = css.replace(feature_hover_old, feature_hover_new)

# 2. Add label hover
if '.label:hover' not in css:
    css += "\n.label:hover, .emergency-text .label:hover { color: var(--red); }\n"

# write
with open(css_path, 'w') as f:
    f.write(css)

print("Feature cards and labels now use red text on hover.")
