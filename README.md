Crypto-Carousel
==========

This python script crawling the [coinmarketcap.com](https://coinmarketcap.com), obtains a list of existing crypto currency and then in each of them selects unique tradable pairs on exchanges and makes a comparison between items on which of them the difference in value is greater.


### Quick start

Assuming you have a Python client::

```sh
./scan.py
```

### Example output:
```javascript
[{
	"Bitcoin": {
		"Differnce": [
			[{
				"pair": "XDN/BTC",
				"max diff": "27.2738809414 %",
				"HitBTC": 17336.0,
				"Bittrex": 12607.8
			}],
			[{
				"pair": "EOS/BTC",
				"Coinrail": 12751.2,
				"Kraken": 16818.5,
				"max diff": "31.8973900496 %"
			}, {
				"pair": "EOS/BTC",
				"ZB.COM": 13420.4,
				"Kraken": 16818.5,
				"max diff": "25.3204077375 %"
			}],
			[{
				"pair": "XLM/BTC",
				"Binance": 13950.2,
				"max diff": "30.5244704746 %",
				"Kraken": 20079.3
			}, {
				"pair": "XLM/BTC",
				"max diff": "29.9582156748 %",
				"Kraken": 20079.3,
				"Bittrex": 14063.9
			}],
			[{
				"pair": "BTC/KRW",
				"Coinrail": 14151.2,
				"max diff": "29.0752727684 %",
				"Bithumb": 18265.7
			}, {
				"pair": "BTC/KRW",
				"Coinone": 18596.0,
				"Coinrail": 14151.2,
				"max diff": "31.4093504438 %"
			}]
		],
		"Market Cap": "$237,241,768,665",
		"Coin URL": "https://coinmarketcap.com/currencies/bitcoin/",
		"Coin ID": "1",
		"Price": "$14123.10",
		"Change": "3.53%"
	}
}, {
	"Ethereum": {
		"Differnce": [
			[{
				"pair": "ETH/KRW",
				"Coinrail": 1304.56,
				"max diff": "26.6358005764 %",
				"Bithumb": 1652.04
			}, {
				"pair": "ETH/KRW",
				"Coinrail": 1304.56,
				"GOPAX": 1657.21,
				"max diff": "21.2797412519 %"
			}],
			[{
				"pair": "ITC/ETH",
				"Huobi": 1329.12,
				"Bibox": 1103.35,
				"max diff": "20.4622286672 %"
			}],
			[{
				"pair": "EOS/ETH",
				"max diff": "21.1222461151 %",
				"Kraken": 1492.65,
				"HitBTC": 1232.35
			}, {
				"pair": "EOS/ETH",
				"Liqui": 1235.27,
				"max diff": "20.8359306063 %",
				"Kraken": 1492.65
			}],
			[{
				"pair": "WAX/ETH",
				"Tidex": 1705.72,
				"Huobi": 1254.2,
				"max diff": "26.4709330957 %"
			}],
			[{
				"pair": "ETC/ETH",
				"Bibox": 1467.66,
				"Kraken": 1222.4,
				"max diff": "20.0638089005 %"
			}],
			[{
				"pair": "ETH/EUR",
				"CoinFalcon": 1099.68,
				"Exmo": 1360.8,
				"max diff": "23.7450894806 %"
			}]
		],
		"Market Cap": "$119,116,252,263",
		"Coin URL": "https://coinmarketcap.com/currencies/ethereum/",
		"Coin ID": "2",
		"Price": "$1228.88",
		"Change": "1.29%"
	}
}]
```
