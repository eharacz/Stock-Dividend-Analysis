def dividend_payout(ticker):
    inc_st = pd.read_html(f'https://www.marketwatch.com/investing/stock/{ticker}/financials')
    income_state = pd.DataFrame(inc_st[1])
    income_state = income_state.transpose()
    new_header = income_state.iloc[0]
    income_state = income_state[1:]
    income_state.columns = new_header
    eps_df = income_state['EPS (Basic)']
    eps_df = eps_df.to_frame()
    eps_df.reset_index(inplace=True)
    eps_df.drop([0,1,2,3,5],inplace=True)
    eps_df.rename(columns={"index": "date", "EPS (Basic)": "eps"}, inplace=True)
    eps_df.reset_index(inplace=True, drop=True)
    use_year=int(eps_df['date'][0])
    eps=float(eps_df['eps'][0])
    divs=historical_dividends(f'{ticker}')
    divs_use_year = divs[divs['Date'].dt.year == use_year]
    numerator=divs_use_year['Dividends'].sum()
    dpr=(numerator/eps)*100
    return dpr
