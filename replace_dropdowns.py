import os
import re

full_hero_dropdown = """                            <select class="full-width" aria-label="Select a service" required>
                                <option value="" disabled selected>Service Required</option>
                                <option value="drain">Drain Cleaning</option>
                                <option value="tap">Tap & Fixture Repair</option>
                                <option value="disposal">Waste Disposal</option>
                                <option value="leak">Leak Detection</option>
                                <option value="repipe">System Repipe</option>
                                <option value="outdoor">Outdoor Plumbing</option>
                                <option value="sewer">Sewer Cleaning</option>
                                <option value="sump">Sump Pumps</option>
                                <option value="toilet">Shower & Toilet</option>
                                <option value="waterheater">Water Heaters</option>
                                <option value="construction">New Construction</option>
                                <option value="emergency">Emergency Repairs</option>
                                <option value="other">Other / General Inquiry</option>
                            </select>"""

full_modal_dropdown = """                <select id="modal-service" aria-label="Select a service" required>
                    <option value="" disabled selected>Service Required</option>
                    <option value="drain">Drain Cleaning</option>
                    <option value="tap">Tap & Fixture Repair</option>
                    <option value="disposal">Waste Disposal</option>
                    <option value="leak">Leak Detection</option>
                    <option value="repipe">System Repipe</option>
                    <option value="outdoor">Outdoor Plumbing</option>
                    <option value="sewer">Sewer Cleaning</option>
                    <option value="sump">Sump Pumps</option>
                    <option value="toilet">Shower & Toilet</option>
                    <option value="waterheater">Water Heaters</option>
                    <option value="construction">New Construction</option>
                    <option value="emergency">Emergency Repairs</option>
                    <option value="other">Other / General Inquiry</option>
                </select>"""

hero_regex = re.compile(r'                            <select class="full-width" aria-label="Select a service" required>.*?                            </select>', re.DOTALL)
modal_regex = re.compile(r'                <select id="modal-service"[^>]*>.*?                </select>', re.DOTALL)

for f in os.listdir('.'):
    if f.endswith('.html') or f == 'generate_areas.py':
        # Don't touch service-*.html as they are handled by generate_services.py
        if f.startswith('service-'): continue
        
        with open(f, 'r') as file:
            content = file.read()
            
        content = hero_regex.sub(full_hero_dropdown, content)
        content = modal_regex.sub(full_modal_dropdown, content)
        
        with open(f, 'w') as file:
            file.write(content)
            
print("Dropdowns replaced!")
