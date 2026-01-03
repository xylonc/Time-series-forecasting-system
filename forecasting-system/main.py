from pipeline import run_pipeline

import sys

if __name__ == "__main__":
    ticker = sys.argv[1] if len(sys.argv) > 1 else "invalid ticker name"
    run_pipeline(ticker)
