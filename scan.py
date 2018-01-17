#!/usr/bin/python

import requests
import json
import logging
import lxml.html

data_url = "https://coinmarketcap.com"
percentage_difference = 20
min_trading_volume = 100000

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'carousel_log.log')

def scan_cryptocoins():
    page = requests.get(data_url).text
    parser = lxml.html.fromstring(page)
    coins_result = []
    coins = parser.cssselect("div[class='container'] tbody tr")

    for i in coins:
        pair_array = []
        diff_pair_forshow = []
        coin_id = i.cssselect("tr td")[0].text.strip()
        coin_name = i.cssselect("tr td a.currency-name-container")[0].text
        coin_url = data_url+i.cssselect("tr td a.currency-name-container")[0].get("href")
        coin_marketcap = i.cssselect("tr td")[2].text.strip()
        coin_price = i.cssselect("tr td a.price")[0].text
        coin_change = i.cssselect("tr td")[6].text
        page2 = requests.get(coin_url).text
        parser2 = lxml.html.fromstring(page2)
    
        exchanges = parser2.cssselect("div[class='container'] div.table-responsive tbody tr")

        for p in exchanges:
            pair = p.cssselect("tr td a")[1].text
            pair_array.append(pair)

        pair_uniq = set(pair_array)
        
#        print coin_name
        for pu_item in pair_uniq: 
            diff_exchange_pair_array = []
            diff20_exchange_pair_array = []

            for tb_row in exchanges: # make uniq pair {exchange: price}
                if (pu_item == tb_row.cssselect("tr td a")[1].text):
                    volume = tb_row.cssselect("tr td span")[0].get("data-usd")
                    if (float(volume) > min_trading_volume): 
                        exchange_price = tb_row.cssselect("tr td span")[1].get("data-usd")
                        exchange_source = tb_row.cssselect("tr td a")[0].text
                        bunch = {exchange_source: exchange_price}
                        diff_exchange_pair_array.append(bunch)

            if (len(diff_exchange_pair_array) > 1):
#                print diff_exchange_pair_array
                for index, pair_price in enumerate(diff_exchange_pair_array):
                    exchange_analyze1 = pair_price.keys()[0]
                    price_analyze1 = float(pair_price.values()[0])

                    for next_item_pair in diff_exchange_pair_array[index+1:]:
                        exchange_analyze2 = next_item_pair.keys()[0]
                        price_analyze2 = float(next_item_pair.values()[0])
                        percentage_price = 100-(price_analyze1*100/price_analyze2)
                        if (percentage_price <0):
                            percentage_price = percentage_price*(-1)

#                        print percentage_price
                        if (percentage_difference <= percentage_price):
                            bunch = {"pair": pu_item,exchange_analyze1: price_analyze1, exchange_analyze2: price_analyze2 , "max diff": str(percentage_price)+" %"}
#                            print bunch
                            diff20_exchange_pair_array.append(bunch)

                if (len(diff20_exchange_pair_array)> 0):
                    diff_pair_forshow.append(diff20_exchange_pair_array)
        
        if (len(diff_pair_forshow)> 0):
            coin_result = { 
                    coin_name: {
                                "Coin ID": coin_id,
                                "Coin URL": coin_url,    
                                "Market Cap": coin_marketcap,
                                "Price": coin_price,
                                "Change": coin_change,
                                "Differnce": diff_pair_forshow                
                                } 
                    }

            coins_result.append(coin_result)
#        print json.dumps(coin_result)

    print json.dumps(coins_result)



scan_cryptocoins()

