# main.py
import argparse
from core.scheduler import trigger_trade_now, schedule_weekly_trade

def main():
    parser = argparse.ArgumentParser(
        description="XSP Bot: scheduled weekly trades or one-off manual trigger"
    )
    parser.add_argument(
        "--now",
        action="store_true",
        help="Run a one-off trade immediately (Immediate Mode)"
    )
    args = parser.parse_args()

    if args.now:
        trigger_trade_now()
    else:
        schedule_weekly_trade()

if __name__ == "__main__":
    main()

    