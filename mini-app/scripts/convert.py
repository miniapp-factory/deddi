#!/usr/bin/env python3
"""
Simple currency converter using fixed exchange rates.
"""

def convert(amount: float, from_currency: str, to_currency: str) -> float:
    rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.0,
        "GBP": 0.75,
        "AUD": 1.35,
    }
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Unsupported currency")
    return amount / rates[from_currency] * rates[to_currency]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert currency using fixed rates.")
    parser.add_argument("amount", type=float, help="Amount to convert")
    parser.add_argument("from", dest="from_currency", help="Source currency code")
    parser.add_argument("to", dest="to_currency", help="Target currency code")
    args = parser.parse_args()
    result = convert(args.amount, args.from_currency, args.to_currency)
    print(f"{args.amount} {args.from_currency} = {result:.2f} {args.to_currency}")

if __name__ == "__main__":
    main()
