from textnode import TextNode, TextType
from copy_static import copy_static
from generate_page import extract_title, generate_pages_recursive
def main() -> None:
    copy_static("/home/sonic/workspace/NewStaticSiteGenerator/static", "/home/sonic/workspace/NewStaticSiteGenerator/public")
    content_path = "/home/sonic/workspace/NewStaticSiteGenerator/content/"
    template_path = "/home/sonic/workspace/NewStaticSiteGenerator/template.html"
    destination_path = "/home/sonic/workspace/NewStaticSiteGenerator/public/"
    generate_pages_recursive(content_path, template_path, destination_path)
main()
