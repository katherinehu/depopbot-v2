from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def findPrice(my_url):

    #grab page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("span",{"class": "Pricestyles__FullPrice-sc-1vj3zjr-0 fvDOul"})
    price = containers[0].text.strip()
    price = price[1:]
    print(price)

