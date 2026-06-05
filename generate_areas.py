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
    <link rel="stylesheet" href="styles.css?v=6">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap"></noscript>
    <link rel="canonical" href="https://liberty-plumbing-example.com/area-{city_slug}.html">
</head>
<body>
    <div class="bg-container">
        <img src="assets/plumbing-light-1.png" alt="Luxury Bathroom" id="bg-image">
        <div class="overlay"></div>
    </div>

    <div class="mask-top"></div>
    <div class="mask-bottom"></div>

    <nav class="navbar">
        <a href="index.html" class="logo-text">Liberty <span>Plumbing</span></a>
        <button class="hamburger" aria-label="Toggle navigation" aria-expanded="false">
            <span></span><span></span><span></span>
        </button>
        <ul class="nav-links">
            <li><a href="index.html">Overview</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="about.html">About</a></li>
            <li><button class="nav-cta contact-btn" style="border:none; cursor:pointer; font-family:inherit; font-size:inherit;">Contact</button></li>
        </ul>
    </nav>

    <main class="main-content">
        <section class="overview-section" style="padding-top: 5vh;">
            <div class="title-wrapper">
                <h1 class="section-title" style="font-size: clamp(2.5rem, 6vw, 4.5rem);"><span class="line-halo">Expert Plumbing in<br><span class="hero-accent">{city}.</span></span></h1>
            </div>
            
            <div class="grid-container" style="max-width: 1000px; grid-template-columns: 1fr;">
                <div class="glass-card" style="text-align: left;">
                    <h2 style="color:var(--primary); font-size: 2rem; margin-bottom: 1rem;">Service Area: {city}, TX</h2>
                    <p style="color:var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;">{desc}</p>
                    
                    <div style="border-radius: 12px; overflow: hidden; margin-bottom: 2rem;">
                        <iframe
                            src="https://www.google.com/maps?q={city},+TX&output=embed"
                            width="100%"
                            height="400"
                            style="border:0; display:block;"
                            allowfullscreen=""
                            loading="lazy"
                            referrerpolicy="no-referrer-when-downgrade"
                            title="Plumber in {city} TX Map">
                        </iframe>
                    </div>

                    <h3 style="color:#fff; font-size: 1.5rem; margin-bottom: 1rem;">Neighborhoods We Serve in {city}</h3>
                    <ul style="color:var(--text-muted); font-size: 1.05rem; column-count: 2; column-gap: 2rem; padding-left: 1.5rem; margin-bottom: 2rem;">
                        {neighborhoods_html}
                    </ul>
                    <div style="text-align: center; margin-top: 4rem;">
                        <h3 style="color:#fff; font-size: 1.5rem; margin-bottom: 1.5rem;">Need a Local Emergency Plumber in {city}?</h3>
                        <a href="tel:5550198" class="cta-button" style="padding: 1.2rem 3rem; font-size: 1.1rem;">Call Now for Service in {city}</a>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <div class="logo-text" style="font-size: 1.2rem; justify-content: center;">Liberty <span>Plumbing</span></div>
            <p class="footer-copy">© 2026 Liberty Plumbing. Licensed & Insured.<br>Emergency Service: (555) 019-8123</p>
            <div style="margin-top: 1rem;">
                <a href="index.html#areas" style="color: var(--primary); font-size: 0.9rem; margin-right: 1rem;">View All Service Areas</a>
                <a href="index.html#faq" style="color: var(--primary); font-size: 0.9rem; margin-right: 1rem;">View Plumbing FAQs</a>
                <a href="services.html" style="color: var(--primary); font-size: 0.9rem;">View Services</a>
            </div>
        </div>
    </footer>

    <!-- Contact Modal -->
    <div class="modal-overlay" id="contact-modal">
        <div class="modal-content">
            <button class="modal-close">&times;</button>
            <h2 class="section-title" style="margin-bottom: 0.5rem;"><span class="line-halo">Request Service</span></h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 1rem;">Fill out the form below or call us directly at <a href="tel:5550198" style="color:var(--primary); font-weight: bold;">(555) 019-8123</a>.</p>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Message sent! We will contact you shortly.'); this.closest('.modal-overlay').classList.remove('active'); document.body.classList.remove('no-scroll');">
                <input type="text" placeholder="Full Name" required>
                <input type="tel" placeholder="Phone Number" required>
                <input type="email" placeholder="Email Address">
                <select id="modal-service" required>
                    <option value="" disabled selected>Select Service Needed</option>
                    <option value="emergency">Emergency Repair</option>
                    <option value="repiping">Whole-Home Repiping</option>
                    <option value="water_heater">Water Heater Repair/Install</option>
                    <option value="drain">Drain Cleaning</option>
                    <option value="other">Other / General Inquiry</option>
                </select>
                <textarea placeholder="Tell us about the issue..." rows="4" required></textarea>
                <button type="submit" class="cta-button">Submit Request</button>
            </form>
        </div>
    </div>

    <script src="script.js?v=2"></script>
</body>
</html>"""

areas_html_items = []

for city, data in cities_data.items():
    city_slug = city.lower().replace(" ", "-")
    filename = f"area-{city_slug}.html"
    
    neighborhoods_html = ""
    for nh in data['neighborhoods']:
        neighborhoods_html += f"<li>{nh}</li>\n                        "
        
    content = html_template.format(
        city=city,
        city_slug=city_slug,
        desc=data['desc'],
        neighborhoods_html=neighborhoods_html.strip()
    )
    
    with open(filename, "w") as f:
        f.write(content)
        
    print("Successfully generated 21 area pages!")
