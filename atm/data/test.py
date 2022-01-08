
import csv
from pathlib import Path
import sys


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('data/accounts.csv')
    accounts = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        print accounts
