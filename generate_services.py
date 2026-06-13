import os

SERVICES = [
    {
        "id": "drain",
        "title": "Drain Cleaning",
        "desc": "Professional drain cleaning services using advanced high-pressure water jetting to clear stubborn blockages and restore optimal flow. We safely remove hair, grease, and debris build-up without damaging your pipes.",
        "image": "assets/service-drain.webp",
        "seo_intro": "When local residents need a professional to take care of stubborn clogs and backed-up pipes, they turn to Liberty Plumbing. We’re known for our skilled plumbing repairs and other plumbing services, including intensive drain cleaning and maintenance. It’s important to have your lines cleared by an industry expert so they’re ready to function properly and provide you with years of peak performance. Don't make the mistake of trying to DIY a clog with harsh chemicals that corrode your pipes. Avoid the hassle and potential plumbing disasters by calling us to schedule your drain cleaning appointment.",
        "problems_title": "SIGNS YOU NEED PROFESSIONAL DRAIN CLEANING",
        "problems_intro": "It’s difficult to gauge if you can trust a company that claims you need an entire pipe replaced when a simple clearing would do. At Liberty Plumbing, we promise you’ll only receive fair and honest feedback from our pros. What are some signs you can look for to tell when your drains need professional attention?",
        "problems": [
            {"title": "SLOW DRAINAGE", "desc": "If water is pooling around your feet in the shower or your sinks take forever to empty, a deep blockage is forming."},
            {"title": "FOUL ODORS", "desc": "Persistent bad smells coming from your drains usually indicate rotting food or sewage trapped in the lines."},
            {"title": "GURGLING SOUNDS", "desc": "If you hear bubbling or gurgling when you flush the toilet or use the sink, it means air is trapped due to a severe clog."},
            {"title": "FREQUENT CLOGS", "desc": "If you find yourself plunging the same toilet multiple times a week, there is an underlying issue in the main line."}
        ],
        "features_title": "OUR DRAIN CLEANING SERVICES",
        "features": [
            {"title": "High-Pressure Hydro Jetting", "desc": "Blast away years of grime, grease, and hard water scale with precision jets that leave your pipes spotless and flowing like new."},
            {"title": "Video Camera Inspections", "desc": "We eliminate the guesswork by feeding an HD camera down your lines to visually identify blockages and structural issues before work begins."},
            {"title": "Preventative Maintenance", "desc": "Keep your drains flowing year-round. Regular maintenance prevents emergency backups and extends the lifespan of your plumbing."},
            {"title": "Safe for All Pipe Types", "desc": "Whether your home has vintage cast iron or modern PVC, we use customized pressures and techniques to clean without causing damage."}
        ]
    },
    {
        "id": "tap",
        "title": "Tap & Fixture Repair",
        "desc": "Stop the annoying drip and reduce your water bill with our expert tap repair and replacement services. We fix leaking faucets, install new fixtures, and ensure everything seals perfectly.",
        "image": "assets/service-tap.webp",
        "seo_intro": "One of the best reasons to hire a plumber for your household is for installing and repairing plumbing fixtures. Faucets and sinks are the most common fixture installation requests we receive. It's essential to feel confident that the work is done correctly to avoid devastating leaks or low water pressure. Whether you're remodeling your kitchen, updating a bathroom, or simply replacing outdated and broken fixtures, the dedicated team at Liberty Plumbing is here to help. We guarantee a perfect seal and flawless operation every time.",
        "problems_title": "WHEN DO YOU NEED FIXTURE REPAIR OR REPLACEMENT?",
        "problems_intro": "Not every dripping faucet needs to be thrown out, but sometimes repairing a deeply corroded fixture costs more than installing a new one. We’ll be upfront with you about whether you need repairs or replacement. Here are the signs it’s time to call the experts:",
        "problems": [
            {"title": "PERSISTENT LEAKS", "desc": "Even a slow drip can waste hundreds of gallons of water a month, driving up your utility bills and causing sink damage."},
            {"title": "LOW WATER PRESSURE", "desc": "If a single faucet has low pressure while the rest of the house is fine, the aerator or cartridge is likely failing."},
            {"title": "SQUEAKING HANDLES", "desc": "If the handles are difficult to turn or squeak loudly, the internal threads are wearing down and need replacement."},
            {"title": "VISIBLE RUST OR MINERAL BUILDUP", "desc": "Heavy corrosion not only looks bad but eventually eats through the metal, leading to sudden, catastrophic leaks."}
        ],
        "features_title": "OUR FIXTURE SERVICES",
        "features": [
            {"title": "Drip & Leak Repairs", "desc": "We trace the source of that annoying drip and resolve it permanently, saving you money on wasted water and preventing water damage."},
            {"title": "New Fixture Installation", "desc": "Upgrade your kitchen or bathroom aesthetics. We quickly install high-quality faucets with precision so they work flawlessly."},
            {"title": "Water Pressure Adjustments", "desc": "Frustrated by a weak stream? We adjust your fixture's flow rate or clear out aerator blockages to restore ideal water pressure."},
            {"title": "Cartridge Replacement", "desc": "Instead of costly full replacements, we can rebuild your existing faucet internals with high-quality, durable components."}
        ]
    },
    {
        "id": "disposal",
        "title": "Waste Disposal",
        "desc": "Garbage disposal repair and installation services. If your disposal is jammed, leaking, or making strange noises, our technicians can get it running smoothly or install a powerful new unit.",
        "image": "assets/service-disposal.webp",
        "seo_intro": "As a top local plumbing company, of course, we take care of garbage disposals. Don't take chances with the quality of work that goes into your kitchen plumbing. A poorly installed disposal can lead to severe under-sink flooding and recurring electrical issues. At Liberty Plumbing, we understand the specific demands put on household disposals. We provide rapid repairs, rigorous maintenance, and complete replacements using only the most reliable units on the market.",
        "problems_title": "SIGNS YOU NEED REPAIR OR REPLACEMENT",
        "problems_intro": "For the best plumbing experience, you can count on our team. We’ll be upfront with you about whether you need garbage disposal repairs or a total replacement. What are some signs you can look for to tell when a garbage disposal is failing?",
        "problems": [
            {"title": "POOR PERFORMANCE", "desc": "If you're noticing your disposal is always a bit sluggish or needs frequent resets, it may be better to replace it entirely considering the age of the system."},
            {"title": "STRANGE NOISES", "desc": "Unusual grinding or metal-on-metal sounds suggest a hard obstruction or severe internal damage to the grinding impellers."},
            {"title": "NO POWER", "desc": "If the unit hums but won't spin, or if it won't turn on at all despite hitting the reset button, the motor is likely burned out."},
            {"title": "UNDER-SINK LEAKS", "desc": "Puddles forming under the disposal usually mean the internal seals have cracked, which often requires a full replacement to fix securely."}
        ],
        "features_title": "OUR DISPOSAL SOLUTIONS",
        "features": [
            {"title": "Jammed Disposal Clearing", "desc": "We safely extract obstructions and reset your disposal without damaging the delicate internal grinding mechanisms."},
            {"title": "New Unit Installation", "desc": "Ready for an upgrade? We install powerful, quiet continuous-feed or batch-feed models tailored to your household's cooking volume."},
            {"title": "Leak Repairs", "desc": "We seal cracked housings and replace worn-out connection gaskets to stop under-sink leaks dead in their tracks."},
            {"title": "Odor Removal", "desc": "Eliminate foul kitchen smells. We thoroughly clean the grinding chamber and advise on the best maintenance practices."}
        ]
    },
    {
        "id": "leak",
        "title": "Leak Detection",
        "desc": "Hidden leaks can cause massive water damage and mold growth. We use state-of-the-art acoustic and thermal imaging technology to pinpoint leaks behind walls or under slabs without destructive digging.",
        "image": "assets/service-leak.webp",
        "seo_intro": "Water leaks are a homeowner's worst nightmare. What starts as a minor drip behind drywall can quickly escalate into devastating structural damage and severe mold infestations. At Liberty Plumbing, we employ advanced, non-invasive leak detection technology to find the exact source of water intrusion. You don't want an amateur tearing up your floors guessing where the leak is. Trust our certified specialists to isolate the problem accurately and provide minimally invasive repair options.",
        "problems_title": "HOW TO KNOW YOU HAVE A HIDDEN LEAK",
        "problems_intro": "Because most of your home's plumbing is hidden behind walls and beneath concrete slabs, leaks can go unnoticed for months. Watch out for these critical warning signs that indicate you need our leak detection team immediately:",
        "problems": [
            {"title": "SPIKING WATER BILLS", "desc": "If your water usage hasn't changed but your bill has skyrocketed, a hidden pipe is almost certainly leaking continuously."},
            {"title": "WARM SPOTS ON FLOORS", "desc": "Feeling unusual warmth beneath your feet, especially on concrete slab floors, is a strong indicator of a hot water line leak."},
            {"title": "MOLD AND MILDEW SMELLS", "desc": "A persistent musty odor in certain rooms, cabinets, or basements means water is pooling in dark, unventilated spaces."},
            {"title": "CRACKS IN FOUNDATION", "desc": "Slab leaks can wash away the soil supporting your home, leading to visible cracks in walls, flooring, and the foundation itself."}
        ],
        "features_title": "OUR LEAK DETECTION METHODS",
        "features": [
            {"title": "Thermal Imaging", "desc": "Our infrared cameras detect temperature anomalies behind walls and ceilings, finding hidden moisture without breaking any drywall."},
            {"title": "Acoustic Pinpointing", "desc": "We use ultra-sensitive listening equipment to hear pressurized water escaping underground, allowing for highly accurate localized repairs."},
            {"title": "Slab Leak Detection", "desc": "Specialized equipment tracks your water lines beneath the concrete foundation to find slab leaks before they compromise structural integrity."},
            {"title": "Rapid Repair Solutions", "desc": "Once the leak is pinpointed, we provide targeted, minimally invasive repair options to stop the damage and restore your peace of mind."}
        ]
    },
    {
        "id": "repipe",
        "title": "System Repipe",
        "desc": "Upgrade your home's aging plumbing with our comprehensive repiping services. We replace corroded galvanized or polybutylene pipes with durable, modern PEX or copper piping for better pressure and purity.",
        "image": "assets/service-pipes.webp",
        "seo_intro": "Hiring a professional plumber for major home renovations often means tackling challenging projects like full waste and water repiping. We offer complete supply line replacement because we want to help local homeowners enjoy updated, upgraded, and safe plumbing. Once your house is completely repiped by Liberty Plumbing, you’ll never have to worry about sudden bursts, toxic rust in your drinking water, or crippling low pressure. We handle the entire process cleanly, efficiently, and up to the strictest building codes.",
        "problems_title": "WHEN DOES YOUR HOME NEED A FULL REPIPE?",
        "problems_intro": "Repiping is a significant investment, but delaying it can result in catastrophic floods and massive mold remediation bills. Here are the telltale signs that your home is a prime candidate for a complete plumbing system overhaul:",
        "problems": [
            {"title": "GALVANIZED PIPES", "desc": "If your home was built before the 1980s and still has its original steel pipes, they are actively rusting from the inside out and must be replaced."},
            {"title": "RUST-COLORED WATER", "desc": "If brown or yellow water comes out when you turn on the tap, your pipes are heavily corroded and contaminating your water supply."},
            {"title": "FREQUENT LEAKS", "desc": "Dealing with pinhole leaks every few months? Patching them is just a band-aid; the entire line is structurally compromised."},
            {"title": "SEVERE PRESSURE DROP", "desc": "Scale and rust buildup inside old pipes restricts water flow so severely that you can't run a dishwasher and shower simultaneously."}
        ],
        "features_title": "OUR REPIPING PROCESS",
        "features": [
            {"title": "Whole-Home Repiping", "desc": "A complete, engineered replacement of your failing supply lines, ensuring clean water, great pressure, and zero leaks for decades."},
            {"title": "PEX & Copper Upgrades", "desc": "Choose between premium copper for proven longevity or flexible PEX for cost-effective, freeze-resistant durability."},
            {"title": "Minimal Drywall Damage", "desc": "Our technicians are trained to route new pipes strategically, minimizing the cuts needed in your walls and ceilings."},
            {"title": "Post-Install Testing", "desc": "We rigorously pressure test the entire new network to guarantee absolutely zero leaks before we consider the job complete."}
        ]
    },
    {
        "id": "outdoor",
        "title": "Outdoor Plumbing",
        "desc": "From outdoor hose bibbs to sprinkler system feed lines, we handle all exterior plumbing needs. Ensure your outdoor kitchen, pool house, or garden supply lines are winter-ready and leak-free.",
        "image": "assets/service-outdoor.webp",
        "seo_intro": "Your outdoor plumbing is just as important as your indoor plumbing, yet it faces the harshest conditions. From freezing winter temperatures to scorching summer heat, exterior pipes and fixtures take a beating. We’ll take care of all your service needs, like replacing cracked hose bibbs, running new lines for outdoor kitchens, and securing your irrigation feeds. Call Liberty Plumbing to protect your exterior investments and prevent outdoor leaks from flooding your yard and foundation.",
        "problems_title": "COMMON OUTDOOR PLUMBING ISSUES",
        "problems_intro": "Because outdoor plumbing is out of sight, problems are often ignored until a massive puddle forms or a pipe bursts in the winter. Keep an eye out for these frequent exterior plumbing emergencies:",
        "problems": [
            {"title": "FROZEN PIPES", "desc": "Exposed pipes that aren't properly winterized will freeze, expand, and rupture, causing massive flooding when the ice thaws."},
            {"title": "LEAKING HOSE BIBBS", "desc": "A spigot that constantly drips wastes an incredible amount of water and can seep into your home's foundation over time."},
            {"title": "BROKEN SPRINKLER LINES", "desc": "A sudden drop in water pressure to your irrigation system usually points to a cracked underground feed line that needs excavation."},
            {"title": "CLOGGED EXTERIOR DRAINS", "desc": "Leaves, mud, and debris can easily clog patio and driveway drains, leading to standing water that damages concrete and masonry."}
        ],
        "features_title": "OUTDOOR SERVICES WE PROVIDE",
        "features": [
            {"title": "Hose Bibb Replacement", "desc": "We swap out leaky, stubborn outdoor spigots with durable, frost-proof sillcocks that stand up to freezing weather."},
            {"title": "Outdoor Kitchen Plumbing", "desc": "Custom gas and water line installations for outdoor sinks, grills, and bars, built safely to local codes."},
            {"title": "Winterization Services", "desc": "Protect your pipes from freezing. We correctly drain and insulate your outdoor plumbing systems before the extreme cold hits."},
            {"title": "Sprinkler Feed Repairs", "desc": "We repair broken backflow preventers and primary feed lines to keep your irrigation system running flawlessly."}
        ]
    },
    {
        "id": "sewer",
        "title": "Sewer Cleaning",
        "desc": "Main sewer line blockages require heavy-duty solutions. We provide rooter services, trenchless sewer repair, and thorough cleanouts to prevent hazardous sewage backups into your home.",
        "image": "assets/service-sewer.webp",
        "seo_intro": "A compromised main sewer line is one of the most stressful plumbing emergencies a homeowner can face. Raw sewage backing up into your bathtubs and sinks is not just a mess; it's a severe health hazard. Liberty Plumbing provides rapid, heavy-duty sewer cleaning and repair services. We utilize advanced camera inspection technology to find the exact location of tree roots or collapsed pipes, and we offer cutting-edge trenchless repair options that save your beautiful landscaping from being destroyed.",
        "problems_title": "WARNING SIGNS OF SEWER LINE FAILURE",
        "problems_intro": "Never ignore the early symptoms of a main line blockage. If you wait until a full backup occurs, the cleanup costs will be staggering. Contact us immediately if you experience any of the following:",
        "problems": [
            {"title": "MULTIPLE BACKED-UP FIXTURES", "desc": "If flushing the toilet causes water to rise in the shower drain, your main sewer line is deeply obstructed."},
            {"title": "SEWAGE ODORS", "desc": "You should never smell raw sewage in or around your home. If you do, there is a crack or severe clog in the main drain line."},
            {"title": "SOGGY, GREEN LAWN SPOTS", "desc": "An unusually lush, green, and soggy patch of grass in your yard is often nourished by raw sewage leaking from a broken pipe underground."},
            {"title": "BUBBLING TOILETS", "desc": "Air trapped by a blockage in the main sewer line will force its way up through the water in your toilet bowls, causing them to bubble."}
        ],
        "features_title": "OUR SEWER LINE SOLUTIONS",
        "features": [
            {"title": "Tree Root Removal", "desc": "We use heavy-duty cutting blades to clear aggressive tree roots that have infiltrated and choked your main sewer line."},
            {"title": "Trenchless Repair", "desc": "We can patch or line damaged sewer pipes from the inside out, saving your lawn and driveway from expensive, messy excavation."},
            {"title": "Main Line Snaking", "desc": "Our industrial-grade augers quickly break through heavy sludge, paper products, and dense debris clogging your primary drain line."},
            {"title": "Video Inspections", "desc": "See exactly what’s causing the problem. We provide you with a high-definition recording of your sewer pipe's interior condition."}
        ]
    },
    {
        "id": "sump",
        "title": "Sump Pumps",
        "desc": "Protect your basement from flooding with a reliable sump pump system. We offer installation, maintenance, and battery backup solutions to keep your home dry during the heaviest storms.",
        "image": "assets/service-sump.webp",
        "seo_intro": "Sump pumps have an incredibly important job to do: protecting your basement and foundation from catastrophic water damage during heavy rainfall. However, they require professional maintenance to ensure they function perfectly when you need them most. Let Liberty Plumbing evaluate, repair, or upgrade your sump pump system. We specialize in installing high-capacity primary pumps and robust battery backup systems, so even if the power goes out during a severe storm, your home remains completely dry.",
        "problems_title": "WHEN DO YOU NEED SUMP PUMP REPAIR?",
        "problems_intro": "Of course, if your existing pump is older than 10 years, it might be time to think about proactively replacing it. You can’t expect it to perform reliably if the motor is worn out. Look out for these signs of sump pump failure:",
        "problems": [
            {"title": "PUMP NOT RUNNING", "desc": "If water is filling the pit and the pump doesn't engage, the float switch is likely stuck or the motor has burned out."},
            {"title": "CONSTANT CYCLING", "desc": "If the pump turns on and off every few seconds, the check valve may be broken, allowing water to immediately flow back into the pit."},
            {"title": "LOUD RATTLING NOISES", "desc": "Excessive noise or vibration usually indicates a jammed impeller or a failing motor bearing that is about to seize up completely."},
            {"title": "CONSTANTLY RUNNING", "desc": "A pump that never turns off will quickly overheat and die. This means the pump is underpowered for the volume of water entering the pit."}
        ],
        "features_title": "OUR SUMP PUMP SERVICES",
        "features": [
            {"title": "Primary Pump Installation", "desc": "We size and install robust, high-capacity submersible pumps capable of handling massive groundwater intrusion."},
            {"title": "Battery Backup Systems", "desc": "Don’t lose protection during a power outage. Our backup systems automatically take over when the grid fails during major storms."},
            {"title": "Float Switch Repair", "desc": "A stuck float switch is the most common reason pumps fail. We install reliable, solid-state switches that won't jam."},
            {"title": "Annual Maintenance", "desc": "We clean the pit, test the check valve, and verify the pump's electrical amp draw to ensure it’s ready for the wet season."}
        ]
    },
    {
        "id": "toilet",
        "title": "Shower & Toilet",
        "desc": "Complete bathroom plumbing services. Whether your toilet is constantly running, or you need a brand new shower valve installed during a renovation, our experts deliver flawless results.",
        "image": "assets/service-toilet.webp",
        "seo_intro": "Among some of the most important plumbing services we provide are bathtub, shower, and toilet repairs. We provide the meticulous services you need for these essential bathroom fixtures. Changing out your tub or upgrading a toilet will do wonders for improving the look and efficiency of your bathroom. As far as plumbing fixtures go, bathtubs and showers are the most daunting of projects. Save yourself the headache and structural water damage by letting the certified experts at Liberty Plumbing take care of the job for you.",
        "problems_title": "COMMON TOILET & SHOWER PROBLEMS",
        "problems_intro": "Maybe you’ve already experienced what it’s like to be in the middle of a plumbing crisis and not know who to call for help. Have Liberty Plumbing on speed dial for when you end up with unexpected issues like:",
        "problems": [
            {"title": "SLUGGISH TOILETS", "desc": "When you flush your toilet and it seems weak or slow, there's a good chance there's a problem in the trap or drain line."},
            {"title": "ROCKING TOILETS", "desc": "A toilet that rocks from side to side needs to be stabilized and reseated immediately before you end up with leaks that rot the subfloor."},
            {"title": "WHISTLING SOUNDS", "desc": "Whistling or hissing from the toilet tank is an indication that the fill valve is faulty and wasting water constantly."},
            {"title": "LEAKING SHOWER PANS", "desc": "If water is dripping into the room below your bathroom, your shower pan or drain seal has failed and requires urgent replacement."}
        ],
        "features_title": "BATHROOM PLUMBING EXPERTISE",
        "features": [
            {"title": "Running Toilet Repair", "desc": "We replace worn flappers, fill valves, and seals to stop phantom flushing and save thousands of gallons of wasted water."},
            {"title": "Shower Valve Upgrades", "desc": "Upgrading to a new thermostatic mixing valve provides perfect temperature control and dramatically improved shower water pressure."},
            {"title": "Clog & Blockage Removal", "desc": "We safely snake out hair and soap scum blockages from shower drains and clear dense clogs from toilet traps."},
            {"title": "Renovation Rough-ins", "desc": "Moving fixtures during a remodel? We expertly route new drains and water lines to accommodate your dream bathroom layout."}
        ]
    },
    {
        "id": "waterheater",
        "title": "Water Heaters",
        "desc": "Never run out of hot water again. We repair all models and install high-efficiency tankless and traditional tank water heaters tailored to your family's specific hot water demands.",
        "image": "assets/service-waterheater.webp",
        "seo_intro": "A functioning water heater is vital for your home’s comfort and sanitation. When your heater fails, you need a plumbing team that responds instantly. Liberty Plumbing is the premier choice for diagnosing, repairing, and installing both traditional tank heaters and modern tankless systems. We assess your household's daily hot water usage to recommend the perfect, energy-efficient unit. Don't suffer through freezing showers-rely on our master plumbers to restore your hot water safely and swiftly.",
        "problems_title": "SIGNS YOUR WATER HEATER IS FAILING",
        "problems_intro": "Water heaters operate under immense pressure and heat, meaning they degrade over time. If your heater is over 10 years old, it is nearing the end of its lifespan. Watch for these clear signs that your system is failing:",
        "problems": [
            {"title": "NO HOT WATER", "desc": "The most obvious sign. This usually means a burned-out heating element in electric heaters or a extinguished pilot light/gas valve failure in gas models."},
            {"title": "RUSTY WATER", "desc": "If hot water comes out brown or rusty, the inside of your water heater tank is corroding and is at risk of bursting."},
            {"title": "RUMBLING OR POPPING NOISES", "desc": "Heavy sediment buildup at the bottom of the tank traps water, which boils violently and creates loud popping sounds, drastically lowering efficiency."},
            {"title": "LEAKING TANK", "desc": "If water is pooling around the base of the heater, the internal steel tank has fractured. It cannot be repaired and must be replaced immediately."}
        ],
        "features_title": "OUR HEATING SOLUTIONS",
        "features": [
            {"title": "Tankless Upgrades", "desc": "Enjoy endless hot water and lower energy bills with a space-saving, on-demand tankless water heating system."},
            {"title": "Traditional Tank Replacement", "desc": "We install high-recovery gas and electric tank water heaters quickly so your family isn't left in the cold."},
            {"title": "Heating Element Repairs", "desc": "If your electric heater is producing lukewarm water, we can digitally test and replace faulty upper and lower heating elements."},
            {"title": "Annual Flushing", "desc": "We drain and flush the sediment from the bottom of your tank, dramatically extending its lifespan and operating efficiency."}
        ]
    },
    {
        "id": "construction",
        "title": "New Construction",
        "desc": "Partner with us for your new home build or major addition. We design and install complete plumbing systems from the ground up, ensuring code compliance, efficiency, and long-lasting quality.",
        "image": "assets/service-construction.webp",
        "seo_intro": "Building a new home or adding a major extension requires flawless plumbing execution from day one. Mistakes made during the rough-in phase will haunt a property for decades. Liberty Plumbing partners with leading contractors and ambitious homeowners to provide elite new construction plumbing services. We handle everything from underground pipe laying and meticulous venting design to the final installation of high-end fixtures. Our work is engineered to exceed all municipal building codes, guaranteeing a robust, silent, and highly efficient plumbing infrastructure.",
        "problems_title": "WHY HIRE US FOR NEW CONSTRUCTION?",
        "problems_intro": "When building a home, you only have one chance to get the pipes right before the drywall goes up. Trusting an inexperienced contractor can lead to disastrous consequences. Here is why Liberty Plumbing is the right choice:",
        "problems": [
            {"title": "MUNICIPAL CODE COMPLIANCE", "desc": "We have intimate knowledge of local building codes. Our systems pass municipal inspections on the first try, keeping your build schedule on track."},
            {"title": "EXPERT ENGINEERING", "desc": "Poorly designed venting and drain lines cause gurgling, slow drains, and sewer smells. We engineer layouts for optimal flow and acoustics."},
            {"title": "PREMIUM MATERIALS", "desc": "We never cut corners. We utilize the highest grade PEX, heavy-duty PVC, and premium brass fittings to ensure your system lasts a lifetime."},
            {"title": "SEAMLESS COORDINATION", "desc": "We work seamlessly alongside electricians, framers, and HVAC technicians to ensure all utilities are routed logically without conflict."}
        ],
        "features_title": "CONSTRUCTION PLUMBING PHASES",
        "features": [
            {"title": "System Design & Layout", "desc": "We engineer efficient drain and supply plans that optimize water flow, balance pressure, and minimize future maintenance issues."},
            {"title": "Underground Plumbing", "desc": "We lay the critical foundation plumbing, including main sewer tie-ins and slab penetrations, before the concrete is poured."},
            {"title": "Rough-in Installation", "desc": "We meticulously route the hidden network of water lines, DWV (drain-waste-vent) pipes, and gas lines inside the wall framing."},
            {"title": "Final Fixture Set", "desc": "We return at the final finishing stages to precisely install sinks, toilets, and luxury appliances, ensuring a flawless visual finish."}
        ]
    },
    {
        "id": "emergency",
        "title": "Emergency Repairs",
        "desc": "Plumbing disasters don't wait for business hours. Our 24/7 emergency response team is always on standby to tackle burst pipes, major floods, and critical system failures immediately.",
        "image": "assets/service-emergency.webp",
        "seo_intro": "When a pipe bursts at 2 AM or raw sewage floods your basement on a holiday weekend, you don't have time to leave voicemails. Liberty Plumbing provides uncompromising, 24/7 emergency plumbing response. Our dispatchers are always on standby, and our trucks are fully stocked with advanced repair equipment. We prioritize rapid arrival times to mitigate water damage and secure your property. When disaster strikes, rely on our experienced master plumbers to bring calm to the chaos and implement permanent, high-quality repairs immediately.",
        "problems_title": "WHAT CONSTITUTES A PLUMBING EMERGENCY?",
        "problems_intro": "Not every plumbing issue requires an after-hours call, but some situations will cause catastrophic damage to your home if not addressed immediately. Call our emergency hotline if you encounter:",
        "problems": [
            {"title": "BURST WATER PIPES", "desc": "A ruptured pressurized water line can pump hundreds of gallons of water into your home in minutes, destroying drywall, flooring, and electronics."},
            {"title": "SEWAGE BACKUPS", "desc": "Raw sewage flowing out of your drains is a severe biohazard that makes your home uninhabitable and requires immediate main line clearing."},
            {"title": "GAS LEAKS", "desc": "If you smell sulfur or rotten eggs, leave the house immediately and call us. Gas line leaks are incredibly dangerous and require certified emergency repair."},
            {"title": "NO WATER OR HEAT IN WINTER", "desc": "A total failure of your water heater or main supply line during freezing temperatures can lead to further burst pipes and unsafe living conditions."}
        ],
        "features_title": "OUR EMERGENCY PROTOCOLS",
        "features": [
            {"title": "24/7 Rapid Response", "desc": "When disaster strikes, our dispatched trucks arrive quickly with the necessary equipment to stop the water and secure your property immediately."},
            {"title": "Burst Pipe Isolation", "desc": "We rapidly locate the break, shut down the localized water supply, and perform immediate structural repairs to minimize damage."},
            {"title": "Flood Mitigation", "desc": "We provide emergency pumping and connect you with trusted local restoration services to begin the drying process as fast as possible."},
            {"title": "Live Dispatch Support", "desc": "No answering machines here. You'll speak to a live human dispatcher who understands the urgency of your situation and tracks the technician's arrival."}
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
    <link rel="stylesheet" href="styles.css?v=38">
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
                <li><a href="gallery.html">Our Work</a></li>
                <li><a href="areas.html">Service Areas</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="tel:+19367552836" class="nav-phone-inline" style="color: var(--red); font-weight: 600;">(936) 755-2836</a></li>
                <li><button class="nav-cta-btn contact-btn">Get a Quote</button></li>
            </ul>
        </div>
    </header>

    <main class="main-content">
        <!-- HERO SECTION -->
        <section class="hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.7), rgba(10, 22, 40, 0.7)), url('{image}');">
            <div class="hero-inner fade-in">
                <div class="hero-text">
                    <h1>{title}</h1>
                    <p style="font-size: 1.1rem; color: #e2e8f0; margin-bottom: 2rem; line-height: 1.6;">{desc} {seo_intro}</p>
                    <button class="btn btn-cyan hide-on-desktop contact-btn" style="width: 100%; max-width: 400px; padding: 1rem; font-size: 1.15rem; font-weight: 600;">Get My Free Quote</button>
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
{dropdown_options}
                            </select>
                            <button type="submit" class="full-width btn-cyan">Get My Free Quote</button>
                        </div>
                    </form>
                </div>
            </div>
        </section>

        <!-- PROBLEMS / WARNING SIGNS SECTION -->
        <section class="section section-mid" style="padding-top: 4rem; padding-bottom: 4rem; background: var(--navy-mid);">
            <div class="container fade-in">
                <div class="section-header center" style="margin-bottom: 3rem;">
                    <div class="label">Expert Insights</div>
                    <h2>{problems_title}</h2>
                    <p style="color: var(--light-gray); max-width: 800px; margin: 1rem auto; font-size: 1.05rem;">{problems_intro}</p>
                </div>
                <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                    {problems_html}
                </div>
            </div>
        </section>

        <!-- FEATURES / SOLUTIONS SECTION -->
        <section class="section section-dark" style="padding-top: 4rem; padding-bottom: 2rem;">
            <div class="container fade-in">
                <div class="section-header center" style="margin-bottom: 3rem;">
                    <div class="label">Why Choose Us</div>
                    <h2>{features_title}</h2>
                </div>
                <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                    {features_html}
                </div>
            </div>
        </section>
        

        <!-- CTA SECTION -->
        <section class="section" style="padding-top: 4rem; padding-bottom: 4rem; text-align: center; background: var(--navy-mid);">
            <div class="container fade-in" style="max-width: 800px; margin: 0 auto;">
                <h2 style="margin-bottom: 1.5rem;">Ready to Get Started?</h2>
                <p style="color: var(--light-gray); margin-bottom: 2rem;">Contact our licensed professionals today for fast, reliable, and upfront pricing on all your plumbing needs.</p>
                <div class="btn-group" style="justify-content: center;">
                    <a href="tel:+19367552836" class="btn btn-cyan">Call (936) 755-2836</a>
                    <button class="btn btn-outline contact-btn">Get a Free Estimate</button>
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
{dropdown_options}
                </select>
                <textarea placeholder="Tell us about the issue..." rows="4" required></textarea>
                <button type="submit" class="btn btn-cyan" style="width:100%; border:none; margin-top:0.5rem;">Submit Request</button>
            </form>
        </div>
    </div>

    <script src="script.js?v=37"></script>
</body>
</html>"""

def main():
    print("Generating Detailed SEO Service Pages...")
    for svc in SERVICES:
        # Build problems HTML
        problems_html = ""
        for prob in svc["problems"]:
            problems_html += f'''
                    <div class="premium-card">
                        <h3>{prob["title"]}</h3>
                        <p>{prob["desc"]}</p>
                    </div>'''

        # Build features HTML
        features_html = ""
        for feat in svc["features"]:
            features_html += f'''
                    <div class="premium-card">
                        <h3>{feat["title"]}</h3>
                        <p>{feat["desc"]}</p>
                    </div>'''
        
        # Build Other Services HTML (Text Links)
        other_services_html = ""
        for other_svc in SERVICES:
            if other_svc["id"] != svc["id"]:
                other_services_html += f'<a href="service-{other_svc["id"]}.html" style="margin: 0.5rem; color: var(--navy-dark); font-weight: 500; text-decoration: underline;">{other_svc["title"]}</a>'
                
        # Build Dropdown Options
        dropdown_options = '                                <option value="" disabled>Service Required</option>\n'
        for opt_svc in SERVICES:
            selected = " selected" if opt_svc["id"] == svc["id"] else ""
            dropdown_options += f'                                <option value="{opt_svc["id"]}"{selected}>{opt_svc["title"]}</option>\n'
        dropdown_options += f'                                <option value="other">Other / General Inquiry</option>'
                
        content = TEMPLATE.format(
            title=svc["title"],
            desc=svc["desc"],
            image=svc["image"],
            seo_intro=svc["seo_intro"],
            problems_title=svc["problems_title"],
            problems_intro=svc["problems_intro"],
            problems_html=problems_html,
            features_title=svc["features_title"],
            features_html=features_html,
            other_services_html=other_services_html,
            dropdown_options=dropdown_options
        )
        filename = f"service-{svc['id']}.html"
        with open(filename, "w") as f:
            f.write(content)
        print(f"Created {filename}")
        
if __name__ == "__main__":
    main()
