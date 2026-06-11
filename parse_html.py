from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.indent = 0
        self.recording = False
    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == 'section' and 'section-mid' in attr_dict.get('class', ''):
            self.recording = True
        if self.recording:
            print("  " * self.indent + f"<{tag} class=\"{attr_dict.get('class', '')}\">")
            self.indent += 1
    def handle_endtag(self, tag):
        if self.recording:
            self.indent -= 1
            print("  " * self.indent + f"</{tag}>")
            if tag == 'section' and self.indent == 0:
                self.recording = False

parser = MyHTMLParser()
with open("index.html") as f:
    parser.feed(f.read())
