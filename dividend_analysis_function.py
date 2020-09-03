def analyze_dividend_performance(ticker):
    ### this function runs multiple functions to analyze stock dividend performance
    try:
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
        dyr=dividend_yield(f'{ticker}')
        dpr=dividend_payout(f'{ticker}')
        print (f'Dividend Performance for {ticker.upper()}')
        print ('----------------------------------------------------------')
        print (f'Five Year Dividend Growth Rate: {divgrowthrate}%')
        print (f'Dividend Yield Ratio: {dyr}%')
        print (f'Dividend Payout Ratio: {dpr}%')
        ########
        return historics
    except:
        print (f'Could not analyze {ticker.upper()}. Confirm stock ticker is correct and the stock pays dividends.')
