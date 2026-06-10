import os
import re

css_path = 'styles.css'
with open(css_path, 'r') as f:
    css = f.read()

# 1. Clean up duplicate a:hover
css = css.replace('a:hover { color: var(--red); }\na:hover { color: #fff; }', 'a:hover { color: var(--red); }')

# 2. Dropdown menu hover
dropdown_old = """.dropdown-menu a:hover {
    background: rgba(0,212,255,0.1);
    color: var(--cyan);
}"""
dropdown_new = """.dropdown-menu a:hover {
    background: rgba(239, 68, 68, 0.1);
    color: var(--red);
}"""
css = css.replace(dropdown_old, dropdown_new)

# 3. Form submit button hover
form_hover_old = """.hero-form button[type="submit"]:hover {
    background: var(--navy-mid);
}"""
form_hover_new = """.hero-form button[type="submit"]:hover {
    background: var(--red);
    color: var(--white);
}"""
css = css.replace(form_hover_old, form_hover_new)

# Form input focus
css = css.replace('border-color: var(--cyan); }', 'border-color: var(--red); }')

# 4. Feature card hover
feature_hover_old = """.feature-card:hover {
    transform: translateY(-5px);
    border-color: var(--cyan);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}"""
feature_hover_new = """.feature-card:hover {
    transform: translateY(-5px);
    border-color: var(--red);
    box-shadow: 0 10px 30px rgba(239, 68, 68, 0.15);
}"""
css = css.replace(feature_hover_old, feature_hover_new)

# 5. Glow card hover
glow_hover_old = """.glow-card:hover {
    transform: translateY(-8px);
    border-color: rgba(0, 212, 255, 0.4);
    box-shadow: 0 15px 35px rgba(0, 212, 255, 0.15);
}
.glow-card:hover::before {
    background: radial-gradient(circle at top left, rgba(0, 212, 255, 0.25), transparent 70%);
}"""
glow_hover_new = """.glow-card:hover {
    transform: translateY(-8px);
    border-color: rgba(239, 68, 68, 0.4);
    box-shadow: 0 15px 35px rgba(239, 68, 68, 0.15);
}
.glow-card:hover::before {
    background: radial-gradient(circle at top left, rgba(239, 68, 68, 0.25), transparent 70%);
}"""
css = css.replace(glow_hover_old, glow_hover_new)

# 6. Service card overlay hover border
css = css.replace('.service-card:hover .service-card-overlay {\n    border-bottom: 4px solid var(--cyan);\n}', '.service-card:hover .service-card-overlay {\n    border-bottom: 4px solid var(--red);\n}')

# 7. Show more / read more btn
css = css.replace('.show-more-btn:hover {\n        color: #fff;\n    }', '.show-more-btn:hover {\n        color: var(--red);\n    }')
css = css.replace('.read-more-btn:hover {\n        color: #fff;\n    }', '.read-more-btn:hover {\n        color: var(--red);\n    }')

# 8. Sleek service link hover
css = css.replace('.sleek-service-link:hover {\n    border-color: var(--cyan);\n}', '.sleek-service-link:hover {\n    border-color: var(--red);\n}')

# 9. Form inputs focus ring
# Wait, I might have messed up the focus ring replace. Let's ensure it:
css = css.replace('outline: none; border-color: var(--cyan);', 'outline: none; border-color: var(--red);')
css = css.replace('outline: 2px solid var(--cyan);', 'outline: 2px solid var(--red);')

with open(css_path, 'w') as f:
    f.write(css)

print("All hovers made red!")
