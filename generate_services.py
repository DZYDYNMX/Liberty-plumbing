import os

SERVICES = [
    {
        "id": "drain",
        "title": "Drain Cleaning",
        "desc": "Professional drain cleaning services using advanced high-pressure water jetting to clear stubborn blockages and restore optimal flow. We remove hair, grease, and debris build-up safely without damaging your pipes.",
        "image": "assets/service-drain.webp",
        "features": [
            {"title": "High-Pressure Hydro Jetting", "desc": "Blast away years of grime, grease, and hard water scale with precision jets that leave your pipes spotless and flowing like new."},
            {"title": "Video Camera Inspections", "desc": "We eliminate the guesswork by feeding an HD camera down your lines to visually identify blockages and structural issues before work begins."},
            {"title": "Preventative Maintenance", "desc": "Keep your drains flowing year-round. Regular maintenance prevents emergency backups and extends the lifespan of your plumbing."},
            {"title": "Safe for All Pipe Types", "desc": "Whether your home has vintage cast iron or modern PVC, we use customized pressures and techniques to clean without causing damage."}
        ]
    },
    {
        "id": "tap",
        "title": "Tap Repair",
        "desc": "Stop the annoying drip and reduce your water bill with our expert tap repair and replacement services. We fix leaking faucets, install new fixtures, and ensure everything seals perfectly.",
        "image": "assets/service-tap.webp",
        "features": [
            {"title": "Drip & Leak Repairs", "desc": "We trace the source of that annoying drip and resolve it permanently, saving you money on wasted water and preventing water damage."},
            {"title": "New Fixture Installation", "desc": "Upgrade your kitchen or bathroom aesthetics. We quickly install high-quality faucets with precision so they work flawlessly."},
            {"title": "Water Pressure Adjustments", "desc": "Frustrated by a weak stream? We adjust your fixture's flow rate or clear out aerator blockages to restore ideal water pressure."},
            {"title": "Cartridge & O-ring Replacement", "desc": "Instead of costly full replacements, we can rebuild your existing faucet internals with high-quality, durable components."}
        ]
    },
    {
        "id": "disposal",
        "title": "Waste Disposal",
        "desc": "Garbage disposal repair and installation services. If your disposal is jammed, leaking, or making strange noises, our technicians can get it running smoothly or install a powerful new unit.",
        "image": "assets/service-disposal.webp",
        "features": [
            {"title": "Jammed Disposal Clearing", "desc": "We safely extract obstructions and reset your disposal without damaging the internal grinding mechanisms."},
            {"title": "New Unit Installation", "desc": "Ready for an upgrade? We install powerful, quiet continuous-feed or batch-feed models tailored to your household's cooking volume."},
            {"title": "Leak Repairs", "desc": "We seal cracked housings and replace worn-out gaskets to stop under-sink leaks dead in their tracks."},
            {"title": "Odor Removal Solutions", "desc": "Eliminate foul kitchen smells. We thoroughly clean the grinding chamber and advise on the best maintenance practices."}
        ]
    },
    {
        "id": "leak",
        "title": "Leak Detection",
        "desc": "Hidden leaks can cause massive water damage and mold growth. We use state-of-the-art acoustic and thermal imaging technology to pinpoint leaks behind walls, under slabs, or underground without destructive digging.",
        "image": "assets/service-leak.webp",
        "features": [
            {"title": "Non-Destructive Thermal Imaging", "desc": "Our infrared cameras detect temperature anomalies behind walls and ceilings, finding hidden moisture without breaking any drywall."},
            {"title": "Acoustic Leak Pinpointing", "desc": "We use ultra-sensitive listening equipment to hear pressurized water escaping underground, allowing for highly accurate, localized repairs."},
            {"title": "Slab Leak Detection", "desc": "Specialized equipment tracks your water lines beneath the concrete foundation to find slab leaks before they compromise your home's structural integrity."},
            {"title": "Rapid Repair Solutions", "desc": "Once the leak is pinpointed, we provide targeted, minimally invasive repair options to stop the damage and restore your peace of mind."}
        ]
    },
    {
        "id": "repipe",
        "title": "System Repipe",
        "desc": "Upgrade your home's aging plumbing with our comprehensive repiping services. We replace corroded galvanized or polybutylene pipes with durable, modern PEX or copper piping for better water pressure and purity.",
        "image": "assets/service-pipes.webp",
        "features": [
            {"title": "Whole-Home Repiping", "desc": "A complete, engineered replacement of your failing supply lines, ensuring clean water, great pressure, and zero leaks for decades to come."},
            {"title": "PEX & Copper Upgrades", "desc": "Choose between premium copper for proven longevity or flexible PEX for cost-effective, freeze-resistant durability."},
            {"title": "Minimal Drywall Damage", "desc": "Our technicians are trained to route new pipes strategically, minimizing the cuts needed in your walls and ceilings."},
            {"title": "Improved Water Pressure", "desc": "Say goodbye to rust-clogged pipes. A new system instantly restores full flow and pressure to every fixture in the house."}
        ]
    },
    {
        "id": "outdoor",
        "title": "Outdoor Plumbing",
        "desc": "From outdoor hose bibbs to sprinkler system feed lines, we handle all exterior plumbing needs. Ensure your outdoor kitchen, pool house, or garden supply lines are winter-ready and leak-free.",
        "image": "assets/service-outdoor.webp",
        "features": [
            {"title": "Hose Bibb Replacement", "desc": "We swap out leaky, stubborn outdoor spigots with durable, frost-proof sillcocks that stand up to the elements."},
            {"title": "Outdoor Kitchen Plumbing", "desc": "Custom gas and water line installations for outdoor sinks, grills, and bars, built safely to local codes."},
            {"title": "Winterization", "desc": "Protect your pipes from freezing. We correctly drain and insulate your outdoor plumbing systems before the cold weather hits."},
            {"title": "Sprinkler Feed Line Repairs", "desc": "We repair broken backflow preventers and primary feed lines to keep your irrigation system running flawlessly."}
        ]
    },
    {
        "id": "sewer",
        "title": "Sewer Cleaning",
        "desc": "Main sewer line blockages require heavy-duty solutions. We provide rooter services, trenchless sewer repair, and thorough cleanouts to prevent hazardous sewage backups into your home.",
        "image": "assets/service-sewer.webp",
        "features": [
            {"title": "Tree Root Removal", "desc": "We use heavy-duty cutting blades to clear aggressive tree roots that have infiltrated and choked your main sewer line."},
            {"title": "Trenchless Repair Options", "desc": "We can patch or line damaged sewer pipes from the inside out, saving your lawn and driveway from expensive excavation."},
            {"title": "Main Line Snaking", "desc": "Our industrial-grade augers quickly break through heavy sludge, paper, and debris clogging your primary drain line."},
            {"title": "Sewer Video Inspections", "desc": "See exactly what’s causing the problem. We provide you with a high-definition recording of your sewer pipe's interior condition."}
        ]
    },
    {
        "id": "sump",
        "title": "Sump Pumps",
        "desc": "Protect your basement from flooding with a reliable sump pump system. We offer installation, maintenance, and battery backup solutions to keep your home dry during the heaviest storms.",
        "image": "assets/service-sump.webp",
        "features": [
            {"title": "Primary Pump Installation", "desc": "We size and install robust, high-capacity submersible pumps capable of handling heavy groundwater intrusion."},
            {"title": "Battery Backup Systems", "desc": "Don’t lose protection during a power outage. Our backup systems automatically take over when the grid fails during major storms."},
            {"title": "Float Switch Replacement", "desc": "A stuck float switch is the most common reason pumps fail. We install reliable, solid-state switches that won't jam."},
            {"title": "Annual Maintenance", "desc": "We clean the pit, test the check valve, and verify the pump's amp draw to ensure it’s ready for the wet season."}
        ]
    },
    {
        "id": "toilet",
        "title": "Shower & Toilet",
        "desc": "Complete bathroom plumbing services. Whether your toilet is constantly running, or you need a brand new shower valve installed during a renovation, our experts deliver flawless results.",
        "image": "assets/service-toilet.webp",
        "features": [
            {"title": "Running Toilet Repair", "desc": "We replace worn flappers, fill valves, and seals to stop the phantom flushing and save thousands of gallons of water."},
            {"title": "Shower Valve Replacement", "desc": "Upgrading to a new thermostatic mixing valve for perfect temperature control and improved shower water pressure."},
            {"title": "Clog Removal", "desc": "We safely snake out hair and soap scum blockages from shower drains and clear dense clogs from toilet traps."},
            {"title": "Renovation Plumbing", "desc": "Moving fixtures? We expertly rough-in new drains and water lines to accommodate your dream bathroom layout."}
        ]
    },
    {
        "id": "waterheater",
        "title": "Water Heaters",
        "desc": "Never run out of hot water again. We repair all models and install high-efficiency tankless and traditional tank water heaters tailored to your family's specific hot water demands.",
        "image": "assets/service-waterheater.webp",
        "features": [
            {"title": "Tankless Upgrades", "desc": "Enjoy endless hot water and lower energy bills with a space-saving, on-demand tankless water heating system."},
            {"title": "Traditional Tank Replacements", "desc": "We install high-recovery gas and electric tank water heaters quickly so you aren't left in the cold."},
            {"title": "Heating Element Repairs", "desc": "If your electric heater is producing lukewarm water, we can test and replace faulty upper and lower heating elements."},
            {"title": "Annual Flushing", "desc": "We drain and flush the sediment from the bottom of your tank, dramatically extending its lifespan and efficiency."}
        ]
    },
    {
        "id": "construction",
        "title": "New Construction",
        "desc": "Partner with us for your new home build or major addition. We design and install complete plumbing systems from the ground up, ensuring code compliance, efficiency, and long-lasting quality.",
        "image": "assets/service-construction.webp",
        "features": [
            {"title": "System Design & Layout", "desc": "We engineer efficient drain and supply plans that optimize water flow and minimize future maintenance issues."},
            {"title": "Code Compliance", "desc": "Our master plumbers ensure every pipe, vent, and trap meets or exceeds stringent local and state building codes."},
            {"title": "Rough-in Plumbing", "desc": "We meticulously run the hidden network of water lines, DWV pipes, and gas lines before the drywall goes up."},
            {"title": "Final Fixture Set", "desc": "We return at the final stages to precisely install sinks, toilets, and appliances, ensuring a flawless finish to your project."}
        ]
    },
    {
        "id": "emergency",
        "title": "Emergency Repairs",
        "desc": "Plumbing disasters don't wait for business hours. Our 24/7 emergency response team is always on standby to tackle burst pipes, major floods, and critical system failures immediately.",
        "image": "assets/service-emergency.webp",
        "features": [
            {"title": "24/7 Rapid Response", "desc": "When disaster strikes at 2 AM, our dispatched trucks arrive quickly to stop the water and secure your property."},
            {"title": "Burst Pipe Isolation", "desc": "We quickly locate the break, shut down the localized water supply, and perform immediate repairs to minimize structural damage."},
            {"title": "Flood Mitigation", "desc": "We provide emergency pumping and direct you to the necessary restoration services to begin the drying process immediately."},
            {"title": "After-Hours Support", "desc": "No answering machines here. You'll speak to a live dispatcher who understands the urgency of your situation."}
        ]
    }
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liberty Plumbing | {title}</title>
    <meta name="description" content="{desc}">
    <link rel="icon" href="data:,">
    <meta property="og:title" content="Liberty Plumbing | {title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="https://libertyplumbing.com/{image}">
    <meta property="og:type" content="website">
    <link rel="stylesheet" href="styles.css?v=14">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap"></noscript>
</head>
<body>
    <header class="navbar">
        <div class="nav-main">
            <a href="index.html" class="logo-text">Liberty <span>Plumbing</span></a>
            <button class="hamburger" aria-label="Toggle navigation" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
            <ul class="nav-links">
                <li><a href="index.html">Overview</a></li>
                <li class="nav-services-list">
                    <a href="services.html" class="active">Services <span class="desktop-only-arrow">▾</span></a>
                    <div class="dropdown-menu">

                        <a href="service-drain.html">Drain Cleaning</a>
                        <a href="service-tap.html">Tap Repair</a>
                        <a href="service-disposal.html">Waste Disposal</a>
                        <a href="service-leak.html">Leak Detection</a>
                        <a href="service-repipe.html">System Repipe</a>
                        <a href="service-outdoor.html">Outdoor Plumbing</a>
                        <a href="service-sewer.html">Sewer Cleaning</a>
                        <a href="service-sump.html">Sump Pumps</a>
                        <a href="service-toilet.html">Shower & Toilet</a>
                        <a href="service-waterheater.html">Water Heaters</a>
                        <a href="service-construction.html">New Construction</a>
                        <a href="service-emergency.html">Emergency Repairs</a>

                    </div>
                </li>
                <li><a href="areas.html">Service Areas</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="tel:+19367552836" class="nav-phone-inline" style="color: var(--cyan); font-weight: 600;">(936) 755-2836</a></li>
                <li><button class="nav-cta-btn contact-btn">Get a Quote</button></li>
            </ul>
        </div>
    </header>

    <main class="main-content">
        <!-- HERO SECTION -->
        <section class="hero" style="background-image: url('{image}');">
            <div class="hero-inner fade-in">
                <div class="hero-text">
                    <h1>{title}</h1>
                    <div class="label" style="background: rgba(255,255,255,0.2); color: white;">Expert Plumbing Services</div>
                    <p style="font-size: 1.1rem; color: #e2e8f0; margin-bottom: 2rem; line-height: 1.6;">{desc}</p>
                </div>
            </div>
        </section>

        <!-- FEATURES SECTION -->
        <section class="section section-mid" style="padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container fade-in">
                <div class="section-header center" style="margin-bottom: 3rem;">
                    <div class="label">Why Choose Us</div>
                    <h2>Our {title} Solutions Include</h2>
                </div>
                <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                    {features_html}
                </div>
            </div>
        </section>
        
        <!-- OTHER SERVICES -->
        <section class="section section-light" style="padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container fade-in">
                <div class="section-header center" style="margin-bottom: 2rem;">
                    <h2>Other Services We Provide</h2>
                </div>
                <div class="other-services-grid mobile-collapse" data-collapse-limit="4" style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
                    {other_services_html}
                </div>
            </div>
        </section>
        
        <!-- CTA SECTION -->
        <section class="section section-dark" style="padding-top: 4rem; padding-bottom: 4rem; text-align: center;">
            <div class="container fade-in" style="max-width: 800px; margin: 0 auto;">
                <h2 style="margin-bottom: 1.5rem;">Ready to Get Started?</h2>
                <p style="color: var(--light-gray); margin-bottom: 2rem;">Contact our licensed professionals today for fast, reliable, and upfront pricing on all your plumbing needs.</p>
                <button class="btn btn-cyan contact-btn" style="font-size: 1.2rem; padding: 1rem 2.5rem;">Get a Free Estimate</button>
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <a href="index.html" class="logo-text" style="display:inline-block; margin-bottom:1rem;">Liberty <span>Plumbing</span></a>
                <p>For a trusted local plumber, simply fill out our booking form. Our friendly team is always here to offer the help you need. Providing upfront quotes with no hidden fees!</p>
                <div class="nav-social" style="margin-top: 1rem;">
                    <a href="#" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.04C6.5 2.04 2 6.53 2 12.06C2 17.06 5.66 21.21 10.44 21.96V14.96H7.9V12.06H10.44V9.85C10.44 7.34 11.93 5.96 14.22 5.96C15.31 5.96 16.45 6.15 16.45 6.15V8.62H15.19C13.95 8.62 13.56 9.39 13.56 10.18V12.06H16.34L15.89 14.96H13.56V21.96A10 10 0 0 0 22 12.06C22 6.53 17.5 2.04 12 2.04Z"/></svg></a>
                    <a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                    <a href="#" aria-label="YouTube"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M21.58 7.19C21.36 6.35 20.71 5.7 19.87 5.48C18.36 5.08 12 5.08 12 5.08C12 5.08 5.64 5.08 4.13 5.48C3.29 5.7 2.64 6.35 2.42 7.19C2 8.7 2 12 2 12C2 12 2 15.3 2.42 16.81C2.64 17.65 3.29 18.3 4.13 18.52C5.64 18.92 12 18.92 12 18.92C12 18.92 18.36 18.92 19.87 18.52C20.71 18.3 21.36 17.65 21.58 16.81C22 15.3 22 12 22 12C22 12 22 8.7 21.58 7.19ZM9.98 15.17V8.83L15.48 12L9.98 15.17Z"/></svg></a>
                    <a href="#" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
                </div>
            </div>
            <div class="footer-col">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="index.html#faq">FAQ</a></li>
                    <li><a href="#" class="contact-btn">Contact Us</a></li>
                    <li><a href="https://maps.app.goo.gl/vxtPHzGMrj5JPKM39" target="_blank" rel="noopener">Google Reviews</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h3>Services</h3>
                <ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                    <li><a href="service-drain.html">Drain Cleaning</a></li>
                    <li><a href="service-tap.html">Tap Repair</a></li>
                    <li><a href="service-disposal.html">Waste Disposal</a></li>
                    <li><a href="service-leak.html">Leak Detection</a></li>
                    <li><a href="service-repipe.html">System Repipe</a></li>
                    <li><a href="service-outdoor.html">Outdoor Plumbing</a></li>
                    <li><a href="service-sewer.html">Sewer Cleaning</a></li>
                    <li><a href="service-sump.html">Sump Pumps</a></li>
                    <li><a href="service-toilet.html">Shower & Toilet</a></li>
                    <li><a href="service-waterheater.html">Water Heaters</a></li>
                    <li><a href="service-construction.html">New Construction</a></li>
                    <li><a href="service-emergency.html">Emergency Repairs</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contact Info</h4>
                <ul>
                    <li style="color:var(--muted); font-size:0.9rem;"><strong>Phone:</strong> <a href="tel:+19367552836">(936) 755-2836</a></li>
                    <li style="color:var(--muted); font-size:0.9rem;"><strong>Email:</strong> <a href="mailto:info@libertyplumbing.com" style="color: inherit; text-decoration: none;">info@libertyplumbing.com</a></li>
                    <li style="color:var(--muted); font-size:0.9rem;"><strong>Hours:</strong> 24/7 Emergency Service</li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2026 Liberty Plumbing. All Rights Reserved. Licensed & Insured.</p>
            <div class="footer-legal">
                <a href="toc.html">Terms & Conditions</a>
                <a href="privacy.html">Privacy Policy</a>
            </div>
        </div>
    </footer>

    <!-- Contact Modal -->
    <div class="modal-overlay" id="contact-modal">
        <div class="modal-content">
            <button class="modal-close">&times;</button>
            <h2>Request Service</h2>
            <p style="color: var(--muted); margin-bottom: 1rem; font-size: 0.95rem;">Fill out the form below or call us directly at <a href="tel:+19367552836" class="text-cyan">(936) 755-2836</a>.</p>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Message sent!'); this.closest('.modal-overlay').classList.remove('active'); document.body.classList.remove('no-scroll');">
                <input type="text" placeholder="Full Name" required>
                <input type="tel" placeholder="Phone Number" required>
                <input type="email" placeholder="Email Address">
                <select id="modal-service" aria-label="Select a service" required>
                    <option value="" disabled selected>Select Service Needed</option>
                    <option value="emergency">Emergency Repair</option>
                    <option value="repiping">Whole-Home Repiping</option>
                    <option value="water_heater">Water Heater Repair/Install</option>
                    <option value="drain">Drain Cleaning</option>
                    <option value="other">Other / General Inquiry</option>
                </select>
                <textarea placeholder="Tell us about the issue..." rows="4" required></textarea>
                <button type="submit" class="btn btn-cyan" style="width:100%; border:none; margin-top:0.5rem;">Submit Request</button>
            </form>
        </div>
    </div>

    <script src="script.js?v=3"></script>
</body>
</html>"""

def main():
    print("Generating Service Pages...")
    for svc in SERVICES:
        # Build features HTML
        features_html = ""
        for feat in svc["features"]:
            features_html += f'''
                    <div style="background: var(--navy-dark); padding: 2rem; border-radius: var(--radius); border-left: 4px solid var(--cyan);">
                        <h3 style="margin-bottom: 0.5rem;">{feat["title"]}</h3>
                        <p style="color: var(--light-gray); font-size: 0.95rem;">{feat["desc"]}</p>
                    </div>'''
        
        # Build Other Services HTML
        other_services_html = ""
        for other_svc in SERVICES:
            if other_svc["id"] != svc["id"]:
                other_services_html += f'<a href="service-{other_svc["id"]}.html" class="btn btn-outline" style="margin: 0.5rem;">{other_svc["title"]}</a>'
                
        content = TEMPLATE.format(
            title=svc["title"],
            desc=svc["desc"],
            image=svc["image"],
            features_html=features_html,
            other_services_html=other_services_html
        )
        filename = f"service-{svc['id']}.html"
        with open(filename, "w") as f:
            f.write(content)
        print(f"Created {filename}")
        
if __name__ == "__main__":
    main()
