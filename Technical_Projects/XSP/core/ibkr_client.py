from ib_async import IB, Index 

def get_xsp_price_fallback():
    import yfinance as yf
    try:
        data = yf.Ticker("^XSP").history(period="1d", interval="1m")
        latest = data['Close'].dropna().iloc[-1]
        print(f"[INFO] Fallback XSP price (Yahoo): {latest}")
        return float(latest)
    except Exception as e: 
        print(f"[ERROR] Yahoo fallback failed: {e}")


def connect_ib():
    ib = IB()
    ib.connect('127.0.0.1',4002, clientId="123")
    print(ib.positions.__dict__)
    if not ib.isConnected():
        print(f"[ERROR] Failed to connect to IBKR. Please check your TWS/IB Gateway settings.")
        return None
    return ib

def get_xsp_price(ib, retries = 5, delay = 5):
    contract = Index(symbol='XSP', exchange='CBOE', currency='USD')
    ib.qualifyContracts(contract)
    ib.reqMarketDataType(3)

    for attempt in range(1,retries+1):
        ticker = ib.reqMktData(contract)
        ib.sleep(delay)
        print(f"[DEBUG] Attempt {attempt} - last={ticker.last}, marketPrice={ticker.marketPrice()}, close = {ticker.close}")
        price = ticker.marketPrice() or ticker.last 
        if price and price > 0:
            print(f"[INFO] IBKR XSP Market Price: {price}")
            return float(price)
        print(f"[RETRY] Failed to get XSP market price (attempt {attempt})")
        ib.sleep(delay)

def get_option_chain():
    pass

def get_vix_level():
    pass

