from core.ibkr_client import connect_ib, get_xsp_price
from datetime import datetime 
def run_trade_cycle() -> bool:
    print(f"[{datetime.now()}] Starting XSP Trade Cycle...")

    ib = connect_ib()
    if not ib:
        return False
    
    price = get_xsp_price(ib)

    ib.disconnect()