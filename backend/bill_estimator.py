# backend/bill_estimator.py

RATE = 8.5

def estimate_bill(kwh):

    return round(
        kwh * RATE,
        2
    )