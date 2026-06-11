import re

mapping = {
    'His And Hers Sink': 'Dual Vanity Installation',
    'Restroom Sink': 'Modern Bathroom Basin',
    'Bathtub Installation': 'Premium Bathtub Fitting',
    'Bathtub': 'Classic Tub Renovation',
    'Clawfoot Bathtub': 'Vintage Clawfoot Tub Upgrade',
    'Custom Lavatory': 'Bespoke Lavatory Design',
    'Energuide': 'Energy Efficient Solutions',
    'Farm Sink Kitchen Sink': 'Rustic Farmhouse Sink',
    'Free Standing Tub': 'Luxury Freestanding Tub',
    'Hdroelectric Shower System': 'Advanced Hydroelectric Shower',
    'Kitchen Sink Installation': 'Professional Kitchen Sink Fit',
    'New Construction Dayton Texas': 'Commercial Plumbing Build-Out',
    'New Construction': 'New Home Plumbing Rough-In',
    'New Construction2': 'Residential Pipe Framework',
    'Outdoor Plumbing': 'Exterior Plumbing Layout',
    'Outdoor Tankless Heater Installation': 'Exterior Tankless Water Heater',
    'Pool Exterior Sink': 'Outdoor Poolside Sink',
    'Restroom Sink 2': 'Elegant Washroom Fixtures',
    'Shower 2': 'Custom Shower Enclosure',
    'Shower 3': 'Rainfall Shower System',
    'Shower Bathtub Combo': 'Versatile Shower-Tub Combo',
    'Shower': 'Walk-In Shower Renovation',
    'Sink': 'Sleek Basin Upgrade',
    'Tank': 'High-Capacity Water Heater',
    'Tankless Water Heater Install': 'Efficient Tankless Installation',
    'Tub And Standing Shower Install': 'Complete Master Bath Remodel'
}

with open('gallery.html', 'r') as f:
    html = f.read()

def replacer(match):
    prefix = match.group(1)
    old_text = match.group(2)
    new_text = mapping.get(old_text, old_text)
    suffix = match.group(3)
    return f'{prefix}{new_text}{suffix}'

new_html = re.sub(r'(<div class="gallery-overlay">)(.*?)(</div>)', replacer, html)

with open('gallery.html', 'w') as f:
    f.write(new_html)

print("Names updated!")
