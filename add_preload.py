import os

preload_link = '    <link rel="preload" as="image" href="assets/hero-plumber.webp" fetchpriority="high">\n'

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        if preload_link not in content:
            content = content.replace('</head>', preload_link + '</head>')
            with open(f, 'w') as file:
                file.write(content)
            print(f"Added preload to {f}")
