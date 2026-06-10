import os

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. nav-cta-btn
nav_hover_old = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--red); 
    color: var(--white); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
nav_hover_new = """.nav-cta-btn:hover,
.nav-links > li > button.nav-cta-btn:hover { 
    background: var(--cyan); 
    color: var(--red); 
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
css = css.replace(nav_hover_old, nav_hover_new)

# 2. btn-cyan
btn_cyan_hover_old = """.btn-cyan:hover {
    background: var(--red);
    color: var(--white);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
btn_cyan_hover_new = """.btn-cyan:hover {
    background: var(--cyan);
    color: var(--red);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}"""
css = css.replace(btn_cyan_hover_old, btn_cyan_hover_new)

# 3. btn-outline
btn_outline_hover_old = """.btn-outline:hover {
    background: var(--red);
    border-color: var(--red);
    color: var(--white);
}"""
btn_outline_hover_new = """.btn-outline:hover {
    background: transparent;
    border-color: var(--cyan);
    color: var(--red);
}"""
css = css.replace(btn_outline_hover_old, btn_outline_hover_new)

# 4. form submit button
submit_hover_old = """.hero-form button[type="submit"]:hover {
    background: var(--red);
    color: var(--white);
}"""
submit_hover_new = """.hero-form button[type="submit"]:hover {
    background: var(--cyan);
    color: var(--red);
}"""
css = css.replace(submit_hover_old, submit_hover_new)

# write
with open(css_path, 'w') as f:
    f.write(css)

print("Button hovers changed to red text instead of red bg.")
