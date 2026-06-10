import os

# 1. Append to styles.css
css_to_append = """
/* ===========================================================
   GALLERY
   =========================================================== */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    max-width: 1280px;
    margin: 0 auto;
}
.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: var(--radius-lg);
    aspect-ratio: 4 / 3;
    background: var(--navy-mid);
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}
.gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}
.gallery-item:hover img {
    transform: scale(1.08);
}
@media (max-width: 768px) {
    .gallery-grid {
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 1rem;
    }
}
"""

with open("styles.css", "a") as f:
    f.write(css_to_append)

print("CSS appended.")

# 2. Update Navigation
files_to_update = [
    "index.html", "about.html", "privacy.html", "areas.html", "services.html", "toc.html",
    "generate_areas.py", "generate_services.py"
]

target_nav = '<li><a href="areas.html">Service Areas</a></li>'
new_nav = '<li><a href="gallery.html">Our Work</a></li>\n                <li><a href="areas.html">Service Areas</a></li>'

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
        
        # Simple replacement
        if '<li><a href="gallery.html"' not in content:
            new_content = content.replace(target_nav, new_nav)
            with open(filename, "w") as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Already updated {filename}")

# Run generation scripts to propagate the nav change
os.system("python3 generate_areas.py")
os.system("python3 generate_services.py")

print("All updates complete.")
