def historical_price(ticker):
    pricer=pd.read_html(f'https://finance.yahoo.com/quote/{ticker}/
                        history?period1=1438214400&period2=1596067200&
                        interval=1mo&filter=history&frequency=1mo')
    pricer=pricer[0]
    pricer.drop(pricer.tail(1).index,inplace=True)
    pricer.drop(columns= ['Open', 'High','Low','Adj Close**'], inplace=True)
    pricer['Date'] =  pd.to_datetime(pricer['Date'])
    droplist = [2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78]
    pricer.drop(index=droplist, inplace=True)
    return pricer
