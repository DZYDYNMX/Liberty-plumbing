import re

mapping = {
    'Custom Lavatory Installation': 'Bespoke Lavatory Design',
    'Free Standing Tub Installation': 'Luxury Freestanding Tub',
    'His And Hers Sink Installation': 'Dual Vanity Installation',
    'Hydroelectric Shower System': 'Advanced Hydroelectric Shower',
    'Farm Sink Installation': 'Rustic Farmhouse Sink',
    'Shower Bathtub Combo': 'Versatile Shower-Tub Combo',
    'Outdoor Tankless Heater': 'Exterior Tankless Water Heater',
    'New Construction Plumbing': 'New Home Plumbing Rough-In'
}

with open('index.html', 'r') as f:
    html = f.read()

def replacer(match):
    prefix = match.group(1)
    old_text = match.group(2)
    new_text = mapping.get(old_text, old_text)
    suffix = match.group(3)
    return f'{prefix}{new_text}{suffix}'

new_html = re.sub(r'(<div class="image-marquee-overlay">)(.*?)(</div>)', replacer, html)

with open('index.html', 'w') as f:
    f.write(new_html)

print("Names updated on index!")
