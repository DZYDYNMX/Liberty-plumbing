import os

cities_data = {
    "Bellaire": {
        "desc": "Enhance the comfort of the \"City of Homes.\" We replace bulky tanks with high-performance tankless technology, delivering instant, endless hot water to Bellaire residents.",
        "neighborhoods": ["Southampton", "Braeswood Place", "Meyerland", "West University Place", "Gulfton", "Midtown", "Afton Oaks", "River Oaks", "Greenway Plaza", "Bellaire Junction"]
    },
    "Missouri City": {
        "desc": "Bring modern luxury to the \"Show Me City.\" We replace outdated tanks with efficient tankless systems, ensuring Missouri City homes enjoy endless hot water on demand.",
        "neighborhoods": ["Sienna", "Quail Valley", "Riverstone", "Lake Olympia", "Brightwater", "Hunters Glen", "Colony Lakes", "Meadowcreek", "Glenn Lakes", "Lexington"]
    },
    "Richmond": {
        "desc": "Merge historic charm with modern innovation in the heart of Fort Bend. We upgrade Richmond homes from outdated tanks to premium tankless systems for instant, endless hot water.",
        "neighborhoods": ["Aliana", "Pecan Grove", "Long Meadow Farms", "Waterside Estates", "Lakes of Bella Terra", "Grand Mission", "Harvest Green", "Fieldstone", "Weston Lakes", "River Park West"]
    },
    "Brookshire": {
        "desc": "Bring state-of-the-art efficiency to the \"Gateway to the Katy Prairie.\" We replace aging tanks with advanced tankless systems, ensuring Brookshire homes enjoy instant, endless hot water.",
        "neighborhoods": ["Crystal Lakes", "Willow Creek Farms", "Patti Lynn", "Brookwood", "Fulbrook", "Weston Lakes", "Cross Creek Ranch", "Jordan Ranch", "Woodland Lakes", "Brazos Country"]
    },
    "Jersey Village": {
        "desc": "Experience reliable tankless water heating in Jersey Village. Our expert team delivers professional installation and maintenance services for this thriving northwest Houston community, ensuring your home enjoys endless hot water year-round.",
        "neighborhoods": ["Jersey Village Country Club", "Winchester", "Steeplechase", "White Oak Falls", "Eldridge", "Wortham Estates", "Windermere Lakes", "Tower Oaks", "Westbridge", "Stone Gables"]
    },
    "Magnolia": {
        "desc": "Experience modern comfort in the heart of the Piney Woods. We upgrade Magnolia homes with advanced tankless water heaters, providing on-demand hot water and exceptional energy efficiency.",
        "neighborhoods": ["High Meadow Ranch", "Thousand Oaks", "Indigo Lake Estates", "Sendera Lake Estates", "Westwood", "Ranch Crest", "Clear Creek Forest", "Durango Creek", "Mostyn Manor", "North Grove"]
    },
    "Conroe": {
        "desc": "Enhance your daily routine near Lake Conroe. We replace outdated units with modern tankless water heaters in Conroe, delivering on-demand hot water and efficiency.",
        "neighborhoods": ["Grand Central Park", "Woodforest", "April Sound", "Walden", "Barton Creek Ranch", "Rivershire", "Stewart's Forest", "Teas Lakes", "Water Crest on Lake Conroe", "Harper's Preserve"]
    },
    "Splendora": {
        "desc": "Experience the comfort of constant hot water in the \"City of Splendor.\" We replace inefficient tanks with modern tankless systems, delivering instant performance to Splendora homes.",
        "neighborhoods": ["Timberland Estates", "Pinewood", "Splendora Fields", "Peach Creek Plantation", "Cole Camp", "Tullis Farms", "Enclave at Splendora", "Midline Crossing", "Deerwood", "Northwood"]
    },
    "Cleveland": {
        "desc": "Bring modern efficiency to the gateway of the Piney Woods. We replace bulky tanks with advanced tankless technology, ensuring Cleveland homes enjoy endless hot water instantly.",
        "neighborhoods": ["Tarkington Prairie", "Kirbywood", "Glen Fenner", "Oakwood", "Grand San Jacinto", "Santa Fe", "Trails End", "Pin Oak", "Plum Grove", "Splendora Woods"]
    },
    "Willis": {
        "desc": "Bring modern tankless efficiency to your Willis home. We replace aging tanks with sophisticated tankless technology that delivers immediate hot water without the wait.",
        "neighborhoods": ["Point Aquarius", "Corinthian Point", "Seven Coves", "Clear Water Cove", "Lake Conroe Hills", "Arrowhead Lakes", "Texas Grand Ranch", "Huntsville", "Cove on Lake Conroe", "Harbor Town"]
    },
    "Houston": {
        "desc": "Stop fighting over the shower. We help Houston homeowners transition from bulky, failing tanks to streamlined on-demand systems that provide a constant flow of hot water, regardless of your household size.",
        "neighborhoods": ["River Oaks", "Houston Heights", "Montrose", "Memorial", "Midtown", "EaDo", "Upper Kirby", "West University Place", "Meyerland", "Tanglewood", "Bellaire", "Rice Village"]
    },
    "Spring": {
        "desc": "Reclaim your garage space and lower your monthly utility costs. We install high-efficiency tankless units across Spring that are perfectly suited for the modern residential infrastructure of North Houston.",
        "neighborhoods": ["Gleannloch Farms", "Windrose", "Champion Forest", "Augusta Pines", "Auburn Lakes", "Benders Landing", "Spring Trails", "Harmony", "Legends Run", "Imperial Oaks"]
    },
    "Tomball": {
        "desc": "Protect your home from the sediment buildup common in our local water. Our Tomball tankless solutions are engineered for longevity and consistent temperature control, even during peak usage hours.",
        "neighborhoods": ["Wildwood at Northpointe", "Lakewood Grove", "Village Creek", "Treeline", "Rosehill Reserve", "Amira", "Woodtrace", "Lakes at Creekside", "Raleigh Creek", "Inverness Estates"]
    },
    "Cypress": {
        "desc": "Cypress families in Bridgeland, Towne Lake, and Coles Crossing trust us for tankless installation, repair, and annual maintenance. Appointments available across 77429 and 77433.",
        "neighborhoods": ["Bridgeland", "Towne Lake", "Coles Crossing", "Fairfield", "Cypress Creek Lakes", "Blackhorse Ranch", "Lakeland Village", "Canyon Lakes", "Rock Creek", "Longwood"]
    },
    "Sugar Land": {
        "desc": "Bring the latest in home efficiency to the 'Sweetest City in Texas.' We replace aging tanks with sophisticated tankless technology that delivers immediate hot water without the wait or the waste.",
        "neighborhoods": ["First Colony", "Telfair", "Riverstone", "Greatwood", "New Territory", "Sugar Creek", "Sweetwater", "Avalon", "Commonwealth", "Aliana"]
    },
    "Katy": {
        "desc": "Don't let a traditional water heater limit your comfort. We provide Katy households with rapid-response tankless systems that handle simultaneous showers and laundry without skipping a beat.",
        "neighborhoods": ["Cinco Ranch", "Seven Meadows", "Cross Creek Ranch", "Firethorne", "Grand Lakes", "Elyson", "Cane Island", "Pine Mill Ranch", "Silver Ranch", "Nottingham Country"]
    },
    "Galveston": {
        "desc": "Defend your home against the coastal elements with a system built for the island. Our Galveston tankless installations are ideal for beach houses and rentals where hot water demand is high and space is at a premium.",
        "neighborhoods": ["East End Historical District", "Pirates Beach", "Sea Isle", "Jamaica Beach", "Tiki Island", "Evia", "Campeche Cove", "San Jacinto", "Laffites Cove", "Beachtown"]
    },
    "Brazoria": {
        "desc": "Whether you're by the river or in the heart of town, we bring reliable, modern water heating to Brazoria. Our systems are designed to offer consistent heat and lower maintenance compared to traditional tanks.",
        "neighborhoods": ["Lake Jackson", "Angleton", "Freeport", "Clute", "Sweeny", "West Columbia", "Richwood", "Danbury", "Holiday Lakes", "Bailey's Prairie"]
    },
    "Waller": {
        "desc": "As Waller grows, so does the need for efficient home technology. We help local residents install suitcase-sized water heaters that offer a massive upgrade in performance over old-fashioned bulky tanks.",
        "neighborhoods": ["Hockley", "Rose Hill", "Prairie View", "Monaville", "Fields Store", "Pine Island", "Macedonia", "Howth", "Hempstead", "Katy"]
    },
    "Fort Bend": {
        "desc": "Serving the diverse needs of the entire county, we provide high-flow tankless solutions that ensure every bathroom in your home has access to instant, steaming water whenever it's needed.",
        "neighborhoods": ["Richmond", "Rosenberg", "Needville", "Fulshear", "Meadows Place", "Stafford", "Arcola", "Thompsons", "Pleak", "Fairchilds"]
    },
    "Montgomery": {
        "desc": "Perfect for lakefront living, our Montgomery tankless systems provide the volume needed for busy households while resisting the mineral buildup often found in Montgomery County water.",
        "neighborhoods": ["Walden", "Bentwater", "April Sound", "Grand Harbor", "Crown Oaks", "Blue Heron Bay", "Del Lago", "Buffalo Springs", "Ridgelake Shores", "Waterford Estates"]
    },
    "Liberty": {
        "desc": "Bring modern convenience to one of Texas's most historic cities. We specialize in retrofitting Liberty homes with sleek, on-demand water heaters that provide a steady flow of hot water without the threat of a major tank leak.",
        "neighborhoods": ["Cypress Point", "Dayton (Liberty side)", "Downtown Liberty", "Grand San Jacinto", "Hidden Lake", "Horseshoe Lake Estates", "Knights Forest", "Liberty Forest", "Liberty Heights", "Moss Bluff", "Old River-Winfree (Liberty side)", "Palmer Place", "Raywood", "Riverside", "South Liberty", "Trinity River Estates", "Twin Island", "West Liberty", "Woods of Liberty"]
    }
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liberty Plumbing | Expert Plumbers in {city}, TX</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="plumber {city}, emergency plumbing {city}, tankless water heater {city}, leak detection {city}, repiping {city}">
    <link rel="stylesheet" href="styles.css">
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
            <li><a href="areas.html" class="active">Areas</a></li>
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

                    <h3 style="color:var(--text-main); font-size: 1.5rem; margin-bottom: 1rem;">Neighborhoods We Serve in {city}</h3>
                    <ul style="color:var(--text-muted); font-size: 1.05rem; column-count: 2; column-gap: 2rem; padding-left: 1.5rem; margin-bottom: 2rem;">
                        {neighborhoods_html}
                    </ul>

                    <div style="text-align: center; margin-top: 3rem;">
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
                <a href="areas.html" style="color: var(--primary); font-size: 0.9rem; margin-right: 1rem;">View All Service Areas</a>
                <a href="services.html" style="color: var(--primary); font-size: 0.9rem;">View Services & FAQs</a>
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

    <script src="script.js"></script>
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
        
    areas_html_items.append(f"""
        <a href="{filename}" class="glass-card" style="text-decoration: none; text-align: left; transition: transform 0.2s;">
            <h3 style="color:var(--primary); font-size:1.5rem; margin-bottom:0.5rem;">{city}</h3>
            <p style="color:var(--text-muted); font-size: 0.95rem;">{data['desc']}</p>
        </a>
    """)

# Generate areas.html
areas_hub_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liberty Plumbing | Service Areas</title>
    <meta name="description" content="View all of the areas Liberty Plumbing services across the Greater Houston Area including Katy, Sugar Land, Cypress, and more.">
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800;900&display=swap"></noscript>
    <link rel="canonical" href="https://liberty-plumbing-example.com/areas.html">
</head>
<body>
    <div class="bg-container">
        <img src="assets/plumbing-light-2.png" alt="Copper pipes" id="bg-image">
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
            <li><a href="areas.html" class="active">Areas</a></li>
            <li><a href="about.html">About</a></li>
            <li><button class="nav-cta contact-btn" style="border:none; cursor:pointer; font-family:inherit; font-size:inherit;">Contact</button></li>
        </ul>
    </nav>

    <main class="main-content">
        <section class="overview-section" style="padding-top: 5vh;">
            <div class="title-wrapper">
                <h1 class="section-title" style="font-size: clamp(2.5rem, 6vw, 4.5rem);"><span class="line-halo">Areas We <span class="hero-accent">Serve.</span></span></h1>
                <p class="hero-sub" style="margin-top: 1rem;"><span class="line-halo">Click a city below to view our dedicated local services. Note: Some remote areas are subject to an additional travel fee.</span></p>
            </div>
            
            <div class="grid-container" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                {items}
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <div class="logo-text" style="font-size: 1.2rem; justify-content: center;">Liberty <span>Plumbing</span></div>
            <p class="footer-copy">© 2026 Liberty Plumbing. Licensed & Insured.<br>Emergency Service: (555) 019-8123</p>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>"""

with open("areas.html", "w") as f:
    f.write(areas_hub_template.replace("{items}", "".join(areas_html_items)))

print("Successfully generated 21 area pages and areas.html!")
