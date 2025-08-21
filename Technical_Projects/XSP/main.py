import argparse

def main():
    parser = argparse.ArgumentParser(
        description="XSP Bot: scheduled weekly trades or one-off manual trigger"
    )
    parser.add_argument(
        "--now",
        action = "store_true",
        help = "Run a one-off trade immediately (Immediate Mode)"
    )
    arguments = parser.parse_args()

    if arguments.now:
        trigger_trade_now()
    else:
        schedule_weekly_trade()
    