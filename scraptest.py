#Web Scrapper with excpetion Handling
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
        
        #Scrapps every child of table with giftList id
        for child in content.find_all('table', id = 'giftList'):
            print(child)

        selection = input("Enter any kind of HTML tag to Scrap: ")
        #Scans every <div> living on the HTML
        final = content.find_all(selection) 

    except AttributeError as error:
        print("Something is wrong")
    return final

start = open_text("http://www.pythonscraping.com/pages/page3.html")

if start == None:
    print("Does not work at all!")
else:
    print(start)

