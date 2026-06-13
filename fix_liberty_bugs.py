import re
import glob

# 1. Update styles.css
with open("styles.css", "r") as f:
    css = f.read()

append_css = """
/* Hero Marquee for Liberty Areas */
.hero-marquee-container {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    width: 100%;
    margin-top: 2rem;
}
.hero-marquee-track {
    display: inline-flex;
    white-space: nowrap;
    animation: marquee-scroll 50s linear infinite;
}
.hero-marquee-item {
    color: var(--light-gray);
    font-size: 1.1rem;
    font-weight: 500;
    padding: 0 1.5rem;
    position: relative;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 50px;
    margin: 0 0.5rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 40px;
}

.hero-text {
    min-width: 0;
}

.hero-form select {
    appearance: none;
    -webkit-appearance: none;
    background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2300D4FF%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    background-size: 0.8rem auto;
    padding-right: 2.5rem;
}
"""
if ".hero-marquee-container {" not in css:
    css += append_css
    with open("styles.css", "w") as f:
        f.write(css)


# 2. Fix generate_areas.py
with open("generate_areas.py", "r") as f:
    gen_areas = f.read()

# Fix phone number color
gen_areas = gen_areas.replace('color: var(--cyan);', 'color: var(--red);')

# Fix marquee classes
gen_areas = gen_areas.replace('class="marquee-container"', 'class="hero-marquee-container"')
gen_areas = gen_areas.replace('class="marquee-track"', 'class="hero-marquee-track"')
gen_areas = gen_areas.replace('class="marquee-item"', 'class="hero-marquee-item"')

# Fix mid section background gradient issue (missing dark background)
gen_areas = gen_areas.replace('<section class="section section-mid">', '<section class="section section-mid" style="background-color: var(--navy-dark);">')

# Fix the missing Service Areas dropdown in nav
old_nav_item = '<li><a href="areas.html" class="active">Service Areas</a></li>'
dropdown_nav = """                <li class="nav-services-list">
                    <a href="areas.html" class="active">Service Areas <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu">
                        <a href="areas.html">View All Areas</a>
                        <a href="area-houston.html">Houston</a>
                        <a href="area-katy.html">Katy</a>
                        <a href="area-sugar-land.html">Sugar Land</a>
                        <a href="area-cypress.html">Cypress</a>
                        <a href="area-spring.html">Spring</a>
                        <a href="area-bellaire.html">Bellaire</a>
                        <a href="area-richmond.html">Richmond</a>
                    </div>
                </li>"""

if old_nav_item in gen_areas:
    gen_areas = gen_areas.replace(old_nav_item, dropdown_nav)

with open("generate_areas.py", "w") as f:
    f.write(gen_areas)

# 3. Bump cache
max_v = 0
for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    match = re.search(r'v=(\d+)', content)
    if match:
        max_v = max(max_v, int(match.group(1)))

new_v = max_v + 1

for file in glob.glob("*.html") + glob.glob("*.py"):
    if file == "fix_liberty_bugs.py": continue
    with open(file, "r") as f:
        content = f.read()
    
    if file.endswith(".html"):
        content = re.sub(r'v=\d+', f'v={new_v}', content)
        
    with open(file, "w") as f:
        f.write(content)

print(f"Fixed bugs and bumped cache to v={new_v}")
