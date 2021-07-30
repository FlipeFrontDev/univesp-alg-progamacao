from urllib.request import urlopen

from html.parser import HTMLParser

'Retorna o código fonte de uma página HTML'

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('http://www.uol.com.br')

parser = HTMLParser()
parser.feed(html)


'Retorna todos os elementos href (ou seja, os hiperlinks) de uma página HTML'
class MyParser(HTMLParser):
     def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

