import urllib.request
from lxml import etree, html
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()

# Obtaining a HTML version of the site

contents = urllib.request.urlopen("https://www.google.com").read().decode("utf-8")

document_html = html.fromstring(contents)

parsed_xml = etree.tostring(document_html, encoding='unicode', pretty_print=True)

parser.feed(parsed_xml)

'''

# Saving the result in the text format

output_text = open("webSite.txt", "w")

output_text.write(parsed_xml)

output_text.close()

'''