def historical_dividends(ticker):
    histdivs=pd.read_html(f'https://finance.yahoo.com/quote/{ticker}/history?period1=1438214400&period2=1596067200&interval=div%7Csplit&filter=div&frequency=1mo')
    histdivs=histdivs[0]
    histdivs.drop(histdivs.tail(1).index,inplace=True)
    histdivs.drop(columns= ['Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6'], inplace=True)
    histdivs['Dividends']= histdivs['Dividends'].apply(lambda x: x.replace(' Dividend', ''))
    histdivs['Dividends']=histdivs['Dividends'].astype(float)
    histdivs['Date'] =  pd.to_datetime(histdivs['Date'])
    return histdivs
