import urllib.request
from lxml import etree, html

# Obtaining a HTML version of the site

contents = urllib.request.urlopen("https://9gag.com").read().decode("utf-8")

document_html = html.fromstring(contents)

parsed_xml = etree.tostring(document_html, encoding='unicode', pretty_print=True)

# Saving the result in the text format

output_text = open("webSite.txt", "w")

output_text.write(parsed_xml)

output_text.close()