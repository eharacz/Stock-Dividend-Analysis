def dividend_yield(ticker):
    divs=historical_dividends(f'{ticker}')
    curdiv=divs['Dividends'][0]
    numerator=curdiv*4
    prices=data_pull(f'{ticker}')
    price_now=prices['Close'][-1]
    dyr=numerator/price_now*100
    return dyr
