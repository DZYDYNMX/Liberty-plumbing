import os
import re

for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py', '.js', '.css')):
            if file == 'revert_red.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Revert the global red text/vars back to blue
            new_content = content.replace('var(--cyan)', 'var(--cyan)')
            new_content = new_content.replace('text-cyan', 'text-cyan')
            new_content = new_content.replace('text-cyan', 'text-cyan')
            new_content = new_content.replace('btn-red', 'btn-cyan')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("Reverted to blue everywhere.")
