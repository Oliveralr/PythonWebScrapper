from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def open_text(url):
    try:
        data = urlopen(url)
    except HTTPError as e:
        print(e)

    try: 
        content = BeautifulSoup(data.read(),"html.parser")
        print(content.body)
    except AttributeError as error:
        print("Something is wrong")
    return content

start = open_text("http://www.pythonscraping.com/pages/page1.html")

if start == None:
    print("Does not work at all!")
else:
    print(start)

