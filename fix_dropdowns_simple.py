import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Clean out the old "View All Services" link
    html = re.sub(
        r'<a href="services\.html"[^>]*>View All Services.*?</a>\s*',
        '',
        html
    )
    # Clean out the old "View All Areas" link
    html = re.sub(
        r'<a href="areas\.html"[^>]*>View All Areas.*?</a>\s*',
        '',
        html
    )
    
    # Insert "View All Services" at the top of the Services dropdown
    html = re.sub(
        r'<a href="service-drain\.html">Drain Cleaning</a>',
        r'<a href="services.html">View All Services</a>\n                        <a href="service-drain.html">Drain Cleaning</a>',
        html
    )
    
    # Insert "View All Areas" at the top of the Areas dropdown
    html = re.sub(
        r'<a href="area-houston\.html">Houston</a>',
        r'<a href="areas.html">View All Areas</a>\n                        <a href="area-houston.html">Houston</a>',
        html
    )

    with open(filepath, 'w') as f:
        f.write(html)
        
print("Updated all navs")
