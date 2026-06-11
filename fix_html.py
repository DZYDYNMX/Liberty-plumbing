with open('index.html', 'r') as f:
    html = f.read()

# Update Nav
html = html.replace('>Our Work</a>', '>Gallery</a>')

gallery_html = '''
        <!-- GALLERY MARQUEE -->
        <section class="section section-mid">
            <div class="container fade-in">
                <div class="section-header center">
                    <div class="label">Our Recent Work</div>
                    <h2>Gallery</h2>
                </div>
            
                <div class="image-marquee-container marquee-container">
                    <div class="image-marquee-track marquee-track">
                        <div class="image-marquee-item"><img src="assets/gallery/custom-lavatory.webp" alt="Custom Lavatory Installation" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/free-standing-tub.webp" alt="Free Standing Tub Installation" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/His-andd-hers-sink.webp" alt="His and Hers Sink Installation" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/hdroelectric-shower-system.webp" alt="Hydroelectric Shower System" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/farm-sink-kitchen-sink.webp" alt="Farm Sink Installation" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/shower-bathtub-combo.webp" alt="Shower Bathtub Combo" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/outdoor-tankless-heater-installation.webp" alt="Outdoor Tankless Heater" loading="lazy"></div>
                        <div class="image-marquee-item"><img src="assets/gallery/new-construction-dayton-texas.webp" alt="New Construction Plumbing" loading="lazy"></div>
                    </div>
                </div>

                <div style="margin-top: 2rem; text-align: center;">
                    <a href="gallery.html" class="btn btn-cyan">See All Our Work</a>
                </div>
            </div>
        </section>

'''

if 'GALLERY MARQUEE' not in html:
    html = html.replace('        <!-- EMERGENCY SPLIT -->', gallery_html + '        <!-- EMERGENCY SPLIT -->')

with open('index.html', 'w') as f:
    f.write(html)
