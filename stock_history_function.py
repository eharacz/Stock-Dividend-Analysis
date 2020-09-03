def stock_history(ticker):
### this function runs two functions to compile history stock price
### and dividend data. It then compiles it into one dataframe
    divy=historical_dividends(ticker)
    pricy=historical_price(ticker)
    historics= pd.merge(pricy, divy, how='outer')
    historics=historics.sort_values(by='Date',ascending=False)
    cols = list(historics.columns.values)
    column_titles = ['Date','Close*','Volume','Dividends']
    historics=historics.reindex(columns=column_titles)
    historics.reset_index(drop=True, inplace=True)
    historics['Ticker']= ticker
    historics.set_index('Date', inplace=True)
    # Below is growth rate and outputs
    divgrowthrate=(divy['Dividends'].iloc[0]-divy['Dividends'].iloc[-1])/divy['Dividends'].iloc[0]*100
    print (f'Historical Stock Price & Dividends for {ticker.upper()}')
    print ('----------------------------------------------------------')
    print (f'Five Year Dividend Growth Rate: {divgrowthrate}%')
    return historics
