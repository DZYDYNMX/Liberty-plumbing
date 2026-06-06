import re

with open('index.html', 'r') as f:
    content = f.read()

# Split the file into main parts
header_end = content.find('<!-- HERO -->')
footer_start = content.find('</main>')

header = content[:header_end]
main_content = content[header_end:footer_start]
footer = content[footer_start:]

# Define the section markers
markers = [
    '<!-- HERO -->',
    '<!-- WHY CHOOSE US -->',
    '<!-- HOW IT WORKS -->',
    '<!-- SERVICES PREVIEW GRID -->',
    '<!-- EMERGENCY SPLIT -->',
    '<!-- REVIEWS -->',
    '<!-- SERVICE AREAS -->',
    '<!-- FAQ -->'
]

# Extract sections
sections = {}
for i, marker in enumerate(markers):
    start = main_content.find(marker)
    if i < len(markers) - 1:
        end = main_content.find(markers[i+1])
        sections[marker] = main_content[start:end]
    else:
        sections[marker] = main_content[start:]

# Desired order
desired_order = [
    '<!-- HERO -->',
    '<!-- HOW IT WORKS -->',
    '<!-- EMERGENCY SPLIT -->',
    '<!-- SERVICES PREVIEW GRID -->',
    '<!-- WHY CHOOSE US -->',
    '<!-- REVIEWS -->',
    '<!-- SERVICE AREAS -->',
    '<!-- FAQ -->'
]

# Reassemble
new_main = "".join([sections[m] for m in desired_order])
new_content = header + new_main + footer

with open('index.html', 'w') as f:
    f.write(new_content)

print("Reordered successfully!")
