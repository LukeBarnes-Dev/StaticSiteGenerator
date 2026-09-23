import sys
from textnode import TextNode, TextType
from copy_static import copy_static
from generate_page import extract_title, generate_pages_recursive

def main() -> None:
    base_path = sys.argv
    if base_path is None or base_path == "":
        base_path = "/"
    copy_static("/home/sonic/workspace/NewStaticSiteGenerator/static", "/home/sonic/workspace/NewStaticSiteGenerator/public")
    content_path = "/home/sonic/workspace/NewStaticSiteGenerator/content/"
    template_path = "/home/sonic/workspace/NewStaticSiteGenerator/template.html"
    destination_path = "/home/sonic/workspace/NewStaticSiteGenerator/docs/"
    generate_pages_recursive(content_path, template_path, destination_path, base_path)
main()
