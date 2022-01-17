import yfinance

def akcje_from_yahoo(nazwa):

    akcje_info = yfinance.Ticker(nazwa)

    return(akcje_info.info['regularMarketPrice'])



