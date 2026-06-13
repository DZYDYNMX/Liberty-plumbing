import os

cities_data = {
    "Bellaire": {
        "desc": "Liberty Plumbing delivers top-tier emergency repair and residential plumbing services to the Bellaire community. From sudden pipe bursts in historic properties to comprehensive repiping projects, our certified technicians ensure your plumbing infrastructure is secure and fully operational.",
        "neighborhoods": ["Southampton", "Braeswood Place", "Meyerland", "West University Place", "Gulfton", "Midtown", "Afton Oaks", "River Oaks", "Greenway Plaza", "Bellaire Junction"]
    },
    "Missouri City": {
        "desc": "Residents of Missouri City trust Liberty Plumbing for fast, reliable emergency interventions. Our expert team specializes in advanced leak detection, main sewer line clearing, and complete bathroom plumbing overhauls designed to withstand the Texas climate.",
        "neighborhoods": ["Sienna", "Quail Valley", "Riverstone", "Lake Olympia", "Brightwater", "Hunters Glen", "Colony Lakes", "Meadowcreek", "Glenn Lakes", "Lexington"]
    },
    "Richmond": {
        "desc": "We provide Richmond homeowners with elite, full-service plumbing solutions. Whether you are dealing with a severe slab leak, a backed-up sewer drain, or require emergency gas line repairs, our dispatch teams are available 24/7 to protect your property.",
        "neighborhoods": ["Aliana", "Pecan Grove", "Long Meadow Farms", "Waterside Estates", "Lakes of Bella Terra", "Grand Mission", "Harvest Green", "Fieldstone", "Weston Lakes", "River Park West"]
    },
    "Brookshire": {
        "desc": "When plumbing disasters strike in Brookshire, Liberty Plumbing is ready to respond. We offer heavy-duty hydro-jetting, precise underground pipe repairs, and comprehensive residential plumbing services that prioritize speed and long-term durability.",
        "neighborhoods": ["Crystal Lakes", "Willow Creek Farms", "Patti Lynn", "Brookwood", "Fulbrook", "Weston Lakes", "Cross Creek Ranch", "Jordan Ranch", "Woodland Lakes", "Brazos Country"]
    },
    "Jersey Village": {
        "desc": "Safeguard your Jersey Village home with our premium plumbing services. We handle everything from stubborn clogs and overflowing toilets to full-scale water damage prevention, ensuring your home's water systems function perfectly.",
        "neighborhoods": ["Jersey Village Country Club", "Winchester", "Steeplechase", "White Oak Falls", "Eldridge", "Wortham Estates", "Windermere Lakes", "Tower Oaks", "Westbridge", "Stone Gables"]
    },
    "Magnolia": {
        "desc": "Liberty Plumbing brings high-end plumbing expertise to Magnolia. We are fully equipped to resolve complex well-pump issues, execute deep pipe winterization, and provide immediate emergency relief for catastrophic water leaks.",
        "neighborhoods": ["High Meadow Ranch", "Thousand Oaks", "Indigo Lake Estates", "Sendera Lake Estates", "Westwood", "Ranch Crest", "Clear Creek Forest", "Durango Creek", "Mostyn Manor", "North Grove"]
    },
    "Conroe": {
        "desc": "Homeowners in Conroe rely on our master plumbers for unmatched diagnostic accuracy and repair speed. We excel in locating hidden leaks, repairing compromised main lines, and ensuring your entire plumbing system operates seamlessly.",
        "neighborhoods": ["Grand Central Park", "Woodforest", "April Sound", "Walden", "Barton Creek Ranch", "Rivershire", "Stewart's Forest", "Teas Lakes", "Water Crest on Lake Conroe", "Harper's Preserve"]
    },
    "Splendora": {
        "desc": "We offer Splendora residents uncompromising quality in every plumbing repair. From fixing sudden drop-offs in water pressure to replacing corroded pipes, our licensed professionals deliver permanent solutions to your most stressful plumbing emergencies.",
        "neighborhoods": ["Timberland Estates", "Pinewood", "Splendora Fields", "Peach Creek Plantation", "Cole Camp", "Tullis Farms", "Enclave at Splendora", "Midline Crossing", "Deerwood", "Northwood"]
    },
    "Cleveland": {
        "desc": "Our rapid-response plumbing teams in Cleveland are dedicated to restoring your home's comfort. We utilize state-of-the-art camera inspections to quickly diagnose sewer blockages and execute precise, minimally invasive pipe repairs.",
        "neighborhoods": ["Tarkington Prairie", "Kirbywood", "Glen Fenner", "Oakwood", "Grand San Jacinto", "Santa Fe", "Trails End", "Pin Oak", "Plum Grove", "Splendora Woods"]
    },
    "Willis": {
        "desc": "Liberty Plumbing is the premier choice for Willis homeowners facing severe plumbing issues. We specialize in isolating and repairing destructive slab leaks, upgrading outdated plumbing networks, and providing emergency 24-hour service.",
        "neighborhoods": ["Point Aquarius", "Corinthian Point", "Seven Coves", "Clear Water Cove", "Lake Conroe Hills", "Arrowhead Lakes", "Texas Grand Ranch", "Huntsville", "Cove on Lake Conroe", "Harbor Town"]
    },
    "Houston": {
        "desc": "As a leading plumbing authority in Houston, we tackle the city's most challenging infrastructure issues. From high-rise condo pipe repairs to historic home repiping, we offer comprehensive leak detection and unmatched emergency drain clearing.",
        "neighborhoods": ["River Oaks", "Houston Heights", "Montrose", "Memorial", "Midtown", "EaDo", "Upper Kirby", "West University Place", "Meyerland", "Tanglewood", "Bellaire", "Rice Village"]
    },
    "Spring": {
        "desc": "Protect your Spring property with our expert plumbing interventions. We are highly trained in resolving extensive water damage scenarios, providing rapid main line clog removal, and installing high-performance fixtures for modern homes.",
        "neighborhoods": ["Gleannloch Farms", "Windrose", "Champion Forest", "Augusta Pines", "Auburn Lakes", "Benders Landing", "Spring Trails", "Harmony", "Legends Run", "Imperial Oaks"]
    },
    "Tomball": {
        "desc": "Tomball residents trust our meticulous approach to residential plumbing. We provide deep sewer line cleaning, expert pipe replacement, and immediate emergency response to prevent water damage and restore your home's essential systems.",
        "neighborhoods": ["Wildwood at Northpointe", "Lakewood Grove", "Village Creek", "Treeline", "Rosehill Reserve", "Amira", "Woodtrace", "Lakes at Creekside", "Raleigh Creek", "Inverness Estates"]
    },
    "Cypress": {
        "desc": "We are the trusted plumbing professionals for the Cypress area, offering rapid response for everything from minor leaks to major pipe ruptures. Our team ensures your water pressure is optimal and your drainage systems are completely clear.",
        "neighborhoods": ["Bridgeland", "Towne Lake", "Coles Crossing", "Fairfield", "Cypress Creek Lakes", "Blackhorse Ranch", "Lakeland Village", "Canyon Lakes", "Rock Creek", "Longwood"]
    },
    "Sugar Land": {
        "desc": "Liberty Plumbing delivers sophisticated plumbing solutions to Sugar Land homes. We specialize in non-destructive leak detection, advanced PEX repiping, and resolving critical emergency plumbing failures with white-glove professionalism.",
        "neighborhoods": ["First Colony", "Telfair", "Riverstone", "Greatwood", "New Territory", "Sugar Creek", "Sweetwater", "Avalon", "Commonwealth", "Aliana"]
    },
    "Katy": {
        "desc": "When a plumbing emergency threatens your Katy home, our 24/7 dispatch teams are the solution. We rapidly resolve overflowing fixtures, perform heavy-duty drain cleaning, and repair compromised water mains with minimal disruption.",
        "neighborhoods": ["Cinco Ranch", "Seven Meadows", "Cross Creek Ranch", "Firethorne", "Grand Lakes", "Elyson", "Cane Island", "Pine Mill Ranch", "Silver Ranch", "Nottingham Country"]
    },
    "Galveston": {
        "desc": "We provide Galveston properties with robust, coastal-grade plumbing repairs. From mitigating saltwater corrosion in older pipes to repairing heavy-use vacation home fixtures, our solutions are built for extreme durability.",
        "neighborhoods": ["East End Historical District", "Pirates Beach", "Sea Isle", "Jamaica Beach", "Tiki Island", "Evia", "Campeche Cove", "San Jacinto", "Laffites Cove", "Beachtown"]
    },
    "Brazoria": {
        "desc": "Liberty Plumbing offers Brazoria homeowners precision diagnostics and permanent plumbing fixes. We excel in identifying hidden foundation leaks and repairing critical residential water mains to keep your home safe and dry.",
        "neighborhoods": ["Lake Jackson", "Angleton", "Freeport", "Clute", "Sweeny", "West Columbia", "Richwood", "Danbury", "Holiday Lakes", "Bailey's Prairie"]
    },
    "Waller": {
        "desc": "We bring modern, high-efficiency plumbing services to Waller residents. Our certified experts are equipped to upgrade aging residential piping, resolve severe blockages, and provide immediate, reliable emergency plumbing support.",
        "neighborhoods": ["Hockley", "Rose Hill", "Prairie View", "Monaville", "Fields Store", "Pine Island", "Macedonia", "Howth", "Hempstead", "Katy"]
    },
    "Fort Bend": {
        "desc": "Serving the entire Fort Bend community, we are dedicated to executing flawless plumbing repairs. Whether it's a completely blocked sewer line or a sudden indoor flood, our master plumbers deliver rapid, definitive solutions.",
        "neighborhoods": ["Richmond", "Rosenberg", "Needville", "Fulshear", "Meadows Place", "Stafford", "Arcola", "Thompsons", "Pleak", "Fairchilds"]
    },
    "Montgomery": {
        "desc": "Liberty Plumbing is Montgomery's answer to complex residential plumbing challenges. We offer top-tier fixture installations, rapid emergency pipe patching, and comprehensive system overhauls designed to handle peak household demands.",
        "neighborhoods": ["Walden", "Bentwater", "April Sound", "Grand Harbor", "Crown Oaks", "Blue Heron Bay", "Del Lago", "Buffalo Springs", "Ridgelake Shores", "Waterford Estates"]
    },
    "Liberty": {
        "desc": "We provide the historic city of Liberty with unmatched plumbing expertise. Our professionals are adept at retrofitting older homes with highly durable piping, clearing severe root intrusions, and providing steadfast 24/7 emergency repair.",
        "neighborhoods": ["Cypress Point", "Dayton (Liberty side)", "Downtown Liberty", "Grand San Jacinto", "Hidden Lake", "Horseshoe Lake Estates", "Knights Forest", "Liberty Forest", "Liberty Heights", "Moss Bluff", "Old River-Winfree (Liberty side)", "Palmer Place", "Raywood", "Riverside", "South Liberty", "Trinity River Estates", "Twin Island", "West Liberty", "Woods of Liberty"]
    }
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liberty Plumbing | Expert Emergency Plumbers in {city}, TX</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="plumber {city}, emergency plumbing {city}, leak detection {city}, drain cleaning {city}, repiping {city}, sewer repair {city}">
    <link rel="icon" href="data:,">
    <meta property="og:title" content="Liberty Plumbing | Expert Emergency Plumbers in {city}, TX">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://liberty-plumbing-example.com/area-{city_slug}.html">
    <link rel="stylesheet" href="styles.css?v=13">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap"></noscript>
    <link rel="canonical" href="https://liberty-plumbing-example.com/area-{city_slug}.html">
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
                    <a href="services.html">Services <span class="desktop-only-arrow">▾</span></a>
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
                <li><a href="gallery.html">Our Work</a></li>
                <li><a href="areas.html" class="active">Service Areas</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="tel:+19367552836" class="nav-phone-inline" style="color: var(--cyan); font-weight: 600;">(936) 755-2836</a></li>
                <li><button class="nav-cta-btn contact-btn">Get a Quote</button></li>
            </ul>
        </div>
    </header>

    <main class="main-content">
        <section class="hero" style="background-image: url('assets/areas-hero.webp');">
            <div class="hero-inner fade-in">
                <div class="hero-text">
                    <h1>Expert Plumbing in {city}, TX</h1>
                    <p style="font-size: 1.1rem; color: #e2e8f0; margin-bottom: 2rem; line-height: 1.6;">{desc}</p>
                    
                    <button class="btn btn-outline hide-on-desktop contact-btn" style="width: 100%; max-width: 400px; padding: 1rem; font-size: 1.15rem; font-weight: 600; margin-top: 1rem;">Get My Free Quote</button>
                    
                    <div class="marquee-container" style="margin-top: 2rem;">
                        <div class="marquee-track">
                            {marquee_html}
                            {marquee_html}
                        </div>
                    </div>
                </div>
                <div class="hero-form hide-on-mobile">
                    <h2 style="font-size: 1.8rem; margin-bottom: 0.5rem;">Book Online Now</h2>
                    <p class="form-sub" style="margin-bottom: 1.5rem;">Simply complete the form below & we'll get back to you as soon as possible</p>
                    <form class="contact-form" onsubmit="event.preventDefault(); alert('Message sent!');">
                        <div class="form-grid">
                            <input type="text" placeholder="Name" required>
                            <input type="tel" placeholder="Phone Number" required>
                            <input type="email" placeholder="Email Address">
                            <select class="full-width" aria-label="Select a service" required>
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
                            </select>
                            <button type="submit" class="full-width btn-cyan">Get My Free Quote</button>
                        </div>
                    </form>
                </div>
            </div>
        </section>

        <section class="section section-mid">
            <div class="container fade-in">
                <div class="container fade-in" style="padding-top: 2rem;">
                    <div class="text-center" style="margin-bottom: 2rem;">
                        <div class="label">Coverage Area</div>
                        <h2>Proudly Serving {city}</h2>
                    </div>
                    <div class="map-container" style="border-radius: var(--radius-lg); overflow: hidden; height: 500px; border: 1px solid var(--border-color);">
                        <iframe
                            src="https://www.google.com/maps?q={city},+TX&output=embed"
                            width="100%"
                            height="100%"
                            style="border:0; display:block; min-height: 400px;"
                            allowfullscreen=""
                            loading="lazy"
                            referrerpolicy="no-referrer-when-downgrade"
                            title="Plumber in {city} TX Map">
                        </iframe>
                    </div>
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
                <ul>
                    <li><a href="service-drain.html">Drain Cleaning</a></li>
                    <li><a href="service-repipe.html">Repiping</a></li>
                    <li><a href="service-waterheater.html">Water Heaters</a></li>
                    <li><a href="service-leak.html">Leak Detection</a></li>
                    <li><a href="service-sewer.html">Sewer Repair</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h3>Contact Info</h3>
                <ul>
                    <li style="color:var(--muted); font-size:0.9rem;"><strong>Phone:</strong> <a href="tel:+19367552836">(936) 755-2836</a></li>
                    <li style="color:var(--muted); font-size:0.9rem;"><strong>Email:</strong> <a href="mailto:info@libertyplumbing.com">info@libertyplumbing.com</a></li>
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
            <h2>Request Service in {city}</h2>
            <p style="color: var(--muted); margin-bottom: 1rem; font-size: 0.95rem;">Fill out the form below or call us directly at <a href="tel:+19367552836" class="text-cyan">(936) 755-2836</a>.</p>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Message sent!'); this.closest('.modal-overlay').classList.remove('active'); document.body.classList.remove('no-scroll');">
                <input type="text" placeholder="Full Name" required>
                <input type="tel" placeholder="Phone Number" required>
                <input type="email" placeholder="Email Address">
                <select id="modal-service" aria-label="Select a service" required>
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
                </select>
                <textarea placeholder="Tell us about the issue..." rows="4" required></textarea>
                <button type="submit" class="btn btn-cyan" style="width:100%; border:none; margin-top:0.5rem;">Submit Request</button>
            </form>
        </div>
    </div>

    <script src="script.js?v=3"></script>
</body>
</html>"""

for city, data in cities_data.items():
    city_slug = city.lower().replace(" ", "-")
    filename = f"area-{city_slug}.html"
    
    neighborhoods_html = ""
    marquee_html = ""
    for nh in data['neighborhoods']:
        neighborhoods_html += f"<li>{nh}</li>\n                            "
        marquee_html += f'<div class="marquee-item">{nh}</div>'
        
    content = html_template.format(
        city=city,
        city_slug=city_slug,
        desc=data['desc'],
        neighborhoods_html=neighborhoods_html.strip(),
        marquee_html=marquee_html
    )
    
    with open(filename, "w") as f:
        f.write(content)
        
print("Successfully generated 22 area pages!")
