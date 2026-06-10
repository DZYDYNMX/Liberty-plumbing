import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. nav-cta-btn
nav_hover_old = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--cyan); 
    color: var(--red); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
nav_hover_new = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--red); 
    color: var(--white); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
css = css.replace(nav_hover_old, nav_hover_new)

# 2. btn-cyan
btn_cyan_hover_old = """.btn-cyan:hover {
    background: var(--cyan);
    color: var(--red);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
btn_cyan_hover_new = """.btn-cyan:hover {
    background: var(--red);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
css = css.replace(btn_cyan_hover_old, btn_cyan_hover_new)

# 3. form submit button
submit_hover_old = """.hero-form button[type="submit"]:hover {
    background: var(--cyan);
    color: var(--red);
}"""
submit_hover_new = """.hero-form button[type="submit"]:hover {
    background: var(--red);
    color: var(--white);
}"""
css = css.replace(submit_hover_old, submit_hover_new)

# 4. feature card
feature_hover_old = """.feature-card:hover {
    transform: translateY(-5px);
    border-color: var(--cyan);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.feature-card:hover h3 {
    color: var(--red);
}"""
feature_hover_new = """.feature-card:hover {
    transform: translateY(-5px);
    border-color: var(--red);
    box-shadow: 0 10px 30px rgba(239, 68, 68, 0.15);
}"""
css = css.replace(feature_hover_old, feature_hover_new)

# 5. label
css = css.replace('\n.label:hover, .emergency-text .label:hover { color: var(--red); }\n', '')

# write
with open(css_path, 'w') as f:
    f.write(css)

print("Reverted others to red fill.")
