import re
import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown: str):
    header = re.findall("#{1} (.*)", markdown)
    if header == []:
        raise ValueError("Invalid markdown, no header found.")
    print(header)
    return header[0]

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    for p in os.listdir(dir_path_content):
        new_dir_path = os.path.join(dir_path_content, p)
        new_dest_path = os.path.join(dest_dir_path, p)
        if os.path.isfile(new_dir_path):
            new_dest_path = Path(new_dest_path).with_suffix(".html")
            generate_page(new_dir_path, template_path, new_dest_path)
        else:
            generate_pages_recursive(new_dir_path, template_path, new_dest_path)
