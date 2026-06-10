import os
import re

for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py')):
            if file == 'subtle_red.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Subtle use case: 24/7 in the footer/body gets a red accent
            new_content = content.replace('<strong>Hours:</strong> 24/7 Emergency Service', '<strong>Hours:</strong> 24/7 Emergency Service')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("Subtle red applied.")
