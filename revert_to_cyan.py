import os
import re

for root, dirs, files in os.walk('.'):
    if 'assets' in root: continue
    for file in files:
        if file.endswith(('.html', '.py', '.js', '.css')):
            if file == 'revert_to_cyan.py': continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Revert the classes and inline vars
            new_content = content.replace('var(--blue)', 'var(--cyan)')
            new_content = new_content.replace('var(--red)', 'var(--cyan)')
            new_content = new_content.replace('text-blue', 'text-cyan')
            new_content = new_content.replace('text-red', 'text-cyan')
            new_content = new_content.replace('btn-blue', 'btn-cyan')
            
            # Revert inline red values in generated html/py
            new_content = new_content.replace('rgba(217, 56, 56', 'rgba(0, 212, 255')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print("Reverted to cyan everywhere.")
