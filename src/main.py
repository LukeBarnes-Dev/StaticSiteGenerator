import sys
from textnode import TextNode, TextType
from copy_static import copy_static
from generate_page import extract_title, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = ""

def main() -> None:
    base_path = default_basepath
    ##if len(sys.argv) > 1:
    #    base_path = sys.argv[1]
    copy_static(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, base_path)
main()
