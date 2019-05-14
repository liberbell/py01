from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print('Encountered comment: ', data)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' positon ', pos[1])

    def handle_starttag(self, tag, attrs):

    def handle_endtag(self, tag):

    def handle_data(self, data)

def main():
    parser = MyHTMLParser()
    f = open('samplehtml.html')
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

if __name__ == '__main__':
    main()
