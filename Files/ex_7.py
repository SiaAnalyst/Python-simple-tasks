import re

def sanitize_file(source, output):
    lines = ''
    with open(source, 'r') as f:
        lines = f.read()
    lines = re.sub(r'\d+', r'', lines)
    print(lines)
    with open(output, 'w') as fh:
        fh.write(lines)