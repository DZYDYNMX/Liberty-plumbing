import os
import glob
import re

# 1. Update styles.css
with open("styles.css", "r") as f:
    css = f.read()

append_css = """
/* Ported from BigLionPlumbing */
.marquee-container {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    width: 100%;
    margin-top: 2rem;
}
.marquee-track {
    display: inline-flex;
    white-space: nowrap;
    animation: marquee-scroll 50s linear infinite;
}
.marquee-item {
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
@keyframes marquee-scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
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

/* Gradient stacking fixes */
.hero::before, .hero::after, .section::before, .section::after {
    z-index: 0;
}
"""

if ".marquee-container {" not in css:
    css += append_css
    with open("styles.css", "w") as f:
        f.write(css)

# 2. Update index.html
with open("index.html", "r") as f:
    idx = f.read()

# Remove review avatars
idx = re.sub(r'[ \t]*<div class="review-avatar[^>]*>.*?</div>\n*', '', idx)
# Update mobile contact button
idx = idx.replace('btn btn-cyan hide-on-desktop contact-btn', 'btn btn-outline hide-on-desktop contact-btn')

with open("index.html", "w") as f:
    f.write(idx)

# 3. Update generate_areas.py
with open("generate_areas.py", "r") as f:
    gen_areas = f.read()

# Change the mobile button
gen_areas = gen_areas.replace('btn btn-cyan hide-on-desktop contact-btn', 'btn btn-outline hide-on-desktop contact-btn')

# Highlight Service Areas link
gen_areas = gen_areas.replace('<a href="areas.html">Service Areas</a>', '<a href="areas.html" class="active">Service Areas</a>')

# Move neighborhoods to marquee
# The old HTML had a list in the mid section
old_mid_section_regex = r'<div class="about-split" style="background: var\(--navy-dark\);">.*?<ul class="mobile-collapse".*?\{neighborhoods_html\}.*?</ul>.*?<div class="btn-group">.*?</div>.*?</div>'
# We will just replace the ul with empty, or remove the about-text entirely since it's just map now.
# Wait, let's just do a string replacement for the parts.
if "marquee-container" not in gen_areas:
    # 1. Add marquee to hero
    hero_marquee = """
                    <button class="btn btn-outline hide-on-desktop contact-btn" style="width: 100%; max-width: 400px; padding: 1rem; font-size: 1.15rem; font-weight: 600; margin-top: 1rem;">Get My Free Quote</button>
                    
                    <div class="marquee-container" style="margin-top: 2rem;">
                        <div class="marquee-track">
                            {marquee_html}
                            {marquee_html}
                        </div>
                    </div>"""
    
    gen_areas = gen_areas.replace(
        '<button class="btn btn-outline hide-on-desktop contact-btn" style="width: 100%; max-width: 400px; padding: 1rem; font-size: 1.15rem; font-weight: 600; margin-top: 1rem;">Get My Free Quote</button>',
        hero_marquee
    )
    
    # 2. Update python logic to generate marquee_html
    py_logic_old = """    neighborhoods_html = ""
    for nh in data['neighborhoods']:
        neighborhoods_html += f"<li>{nh}</li>\\n                            "
        
    content = html_template.format(
        city=city,
        city_slug=city_slug,
        desc=data['desc'],
        neighborhoods_html=neighborhoods_html.strip()
    )"""
    
    py_logic_new = """    neighborhoods_html = ""
    marquee_html = ""
    for nh in data['neighborhoods']:
        neighborhoods_html += f"<li>{nh}</li>\\n                            "
        marquee_html += f'<div class="marquee-item">{nh}</div>'
        
    content = html_template.format(
        city=city,
        city_slug=city_slug,
        desc=data['desc'],
        neighborhoods_html=neighborhoods_html.strip(),
        marquee_html=marquee_html
    )"""
    gen_areas = gen_areas.replace(py_logic_old, py_logic_new)
    
    # 3. Simplify mid section to just map
    mid_section_old = """<div class="about-split" style="background: var(--navy-dark);">
                    <div class="about-text">
                        <div class="label">Coverage Area</div>
                        <h2>Neighborhoods We Serve in {city}</h2>
                        <ul class="mobile-collapse" data-collapse-limit="4" style="color:var(--light-gray); font-size: 1.05rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 0.75rem 1.5rem; padding-left: 1.25rem; margin-top: 1.5rem; margin-bottom: 2rem;">
                            {neighborhoods_html}
                        </ul>
                        <div class="btn-group">
                            <a href="tel:+19367552836" class="btn btn-cyan">(936) 755-2836</a>
                            <button class="btn btn-outline contact-btn">Request Service in {city}</button>
                        </div>
                    </div>
                    <div class="about-image">
                        <iframe"""
    
    mid_section_new = """<div class="container fade-in" style="padding-top: 2rem;">
                    <div class="text-center" style="margin-bottom: 2rem;">
                        <div class="label">Coverage Area</div>
                        <h2>Proudly Serving {city}</h2>
                    </div>
                    <div class="map-container" style="border-radius: var(--radius-lg); overflow: hidden; height: 500px; border: 1px solid var(--border-color);">
                        <iframe"""
    
    gen_areas = gen_areas.replace(mid_section_old, mid_section_new)
    
    # fix the closing div tag mapping
    gen_areas = gen_areas.replace('</iframe>\n                    </div>\n                </div>\n            </div>\n        </section>', '</iframe>\n                    </div>\n            </div>\n        </section>')

with open("generate_areas.py", "w") as f:
    f.write(gen_areas)

# 4. Em-dash replacement & Cache Bumping
# Find the highest v number
max_v = 0
for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    match = re.search(r'v=(\d+)', content)
    if match:
        max_v = max(max_v, int(match.group(1)))

new_v = max_v + 1

for file in glob.glob("*.html") + glob.glob("*.py"):
    if file == "sync_biglion_changes.py": continue
    with open(file, "r") as f:
        content = f.read()
    
    content = content.replace("—", "-")
    
    if file.endswith(".html"):
        content = re.sub(r'v=\d+', f'v={new_v}', content)
        
    with open(file, "w") as f:
        f.write(content)

print(f"Applied all UI changes. Cache bumped to v={new_v}")
