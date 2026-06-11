import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()

    # Add aria-label if not present on inputs
    # E.g. <input type="text" placeholder="Full Name" required>
    # -> <input type="text" placeholder="Full Name" aria-label="Full Name" required>
    
    def repl_input(m):
        tag = m.group(0)
        if 'aria-label' in tag:
            return tag
        
        # Extract placeholder
        ph_match = re.search(r'placeholder="([^"]+)"', tag)
        if ph_match:
            placeholder = ph_match.group(1)
            # Insert aria-label just before placeholder
            return tag.replace(f'placeholder="{placeholder}"', f'aria-label="{placeholder}" placeholder="{placeholder}"')
        return tag

    html = re.sub(r'<input[^>]+>', repl_input, html)
    html = re.sub(r'<textarea[^>]+>', repl_input, html)
    html = re.sub(r'<select[^>]+>', repl_input, html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Added aria-labels to forms")
