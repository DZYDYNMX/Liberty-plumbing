import os

replacements = {
    '--cyan': '--red',
    '--cyan-dark': '--red-dark',
    '--cyan-gradient': '--red-gradient',
    'btn-cyan': 'btn-cyan',
    'text-cyan': 'text-cyan',
    '#00d4ff': '#d93838', # Update colors in styles.css
    '#0284c7': '#a82020',
}

for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.css', '.py', '.js')):
            filepath = os.path.join(root, file)
            if file == 'rename_cyan.py': continue
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)
                
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                    
print("Renamed cyan to red everywhere!")
