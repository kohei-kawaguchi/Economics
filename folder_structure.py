import os

def generate_tree(startpath, indent=''):
    print(f'{indent}📦 {os.path.basename(startpath)}')
    indent += '  '
    for entry in os.listdir(startpath):
        if entry.startswith('.'):  # Skip hidden files/folders
            continue
        path = os.path.join(startpath, entry)
        if os.path.isdir(path):
            generate_tree(path, indent)
        else:
            print(f'{indent}📄 {entry}')

# Use current directory
generate_tree('.') 