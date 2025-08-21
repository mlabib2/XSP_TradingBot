from core.trade_logic import run_trade_cycle

def trigger_trade_now():
    print("Manual-Trigger: Run one trade cycle immediately")
    success = run_trade_cycle()
    if success:
        print("[MANUAL] Trade completed end-to-end.")
    else:
        print("[Manual] Trade skipped or failed; check logs.")


def schedule_weekly_trade():
    print("Scheduling weekly trade")