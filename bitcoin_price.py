
import requests
from bs4 import BeautifulSoup
page = requests.get('https://markets.businessinsider.com/currencies/btc-usd')
def main(page):
    details = [] # list which contain the bitcoin details
    
    
    # ==> format the web code
    src = page.content
    soup = BeautifulSoup(src, 'lxml')

    # ==> the section which contain the the main code
    section = soup.find('div' , {'class' : 'price-section-with-button__price-section-col price-section--negative'})
    
    boysection = soup.find('div' , {
        'class' : 'price-section__row'
    })

    # ==> the pricesection which contain all details
    pricesection = boysection.find('div' , {
        'class' : 'price-section__values'
    })

    # ==> here the details 
    bitcoinprice = pricesection.find('span' , {
        'class' : 'price-section__current-value'
    }).text.strip()
    
    realative = pricesection.find('span' , {
        'class' : 'price-section__relative-value'
    }).text.strip()

    # ==> append the data to list 
    details.append({
        'btc' : bitcoinprice,
        'realative' : realative
    })
    print(details)
    

main(page)
# |= ~~> web scraping get btc price 
# </> Thomas#8988