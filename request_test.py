from urllib.request import urlopen
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()

with urlopen("https://www.baidu.com") as f:
    html = f.read(500)
    parser.feed(f"{html}")
