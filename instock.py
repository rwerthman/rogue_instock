from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
from twilio.rest import Client
from datetime import datetime
import re

# @todo: add doxygen to functions and additional comments to code


def checkStock( page, itemsToCheck ):
    pageSoup = BeautifulSoup( page, 'html.parser' )

    itemsOnPage = pageSoup.find_all( 'div', attrs={ 'class' : 'grouped-item' } )

    for itemToCheck in itemsToCheck:
        for itemOnPage in itemsOnPage:
    
            name = itemOnPage.find( 'div', attrs={ 'class' : 'item-name' } ).text
            inStock = True if not itemOnPage.find( 'div', attrs={ 'class' : 'bin-out-of-stock' } ) else False
            
            if itemToCheck == name and inStock:
                itemsToCheck[itemToCheck] = True
                print( name, 'is in stock' )
            elif itemToCheck == name and not inStock:
                print( name, 'is out of stock' )
                itemsToCheck[itemToCheck] = False

def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    account_sid = '<get from twilio>'
    auth_token = '<get from twilio>'
    client = Client(account_sid, auth_token)

    sslContext = ssl.SSLContext( ssl.PROTOCOL_TLSv1 )


    url = 'https://www.roguefitness.com/rogue-us-mil-sprc-bumper-plates'

    items = {
        '25LB Rogue US-MIL Spec Bumper Pair' : False,
        '10LB Rogue US-MIL Spec Bumper Pair' : False }

    request = Request( url, headers={'User-Agent': 'Mozilla/5.0'} )
    page = urlopen( request, context=sslContext )

    checkStock( page, items )

    if any( value is True for value in items.values() ):
        messageBody = url
        for item in items:
            if items[item]:
                messageBody = messageBody + '\n' + item

        print( 'Sending text message body' )
        print( messageBody )

        client.messages \
            .create(
                body=messageBody,
                from_='<get from twilio>',
                to='<personal phone number>' )

if __name__ == "__main__":
    main()
