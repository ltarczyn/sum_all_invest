import ccxt


def binance():

    exchange_id = 'binance'
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'apiKey': '**************************************************',
        'secret': '***************************************************',
    })
    balances = exchange.fetch_balance()

    total = balances['total']
    binance_currency = {}
    binance_currency_in_usd = {}
    for x, y in total.items():

        if y > 0:
            #print (x, y)
            binance_currency[x] = y

    del binance_currency["SHIB"]
    del binance_currency["MANA"]

    binance_currency["SHIB"] = binance_currency.pop("LDSHIB2")
    binance_currency["MANA"] = binance_currency.pop("LDMANA")

    for i, j in binance_currency.items():
        w = i + '/USDT'

        price = exchange.fetch_ticker(w)
        #print (f"{w}: {price['close']*j}")
        binance_currency_in_usd[i] = price['close'] * j
    #print(binance_currency_in_usd)
    return(binance_currency_in_usd)


