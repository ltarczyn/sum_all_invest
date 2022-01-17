import ccxt


def kraken():

    kraken = ccxt.kraken({
        'apiKey': '********************************',
        'secret': '*******************************',
    })


    balances = kraken.fetch_balance()
    total = balances['total']
    kraken_currency = {}
    kraken_currency_in_usd = {}

    #wartosc = kraken.fetch_ticker('DOT/USD')
    #print(wartosc)
    for x, y in total.items():

        if y > 0 and x != 'EUR':
            #print (x, y)
            kraken_currency[x] = y


    #print(binance_currency.items())

    for i, j in kraken_currency.items():
        w = ""
        if i != "BTC.M":
            w = i.rstrip(".S") + '/USD'
        else:
            w = i.rstrip(".M") + '/USD'

        price = kraken.fetch_ticker(w)
        #print (f"{w}: {price['close']*j}")
        kraken_currency_in_usd[i] = price['close'] * j

        #fetch_ticker zwraca wartosc w słowniku, wyciąc tylko wartość close :)

    #print(binance_currency_in_usd)
    return(kraken_currency_in_usd)


