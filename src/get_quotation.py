from datetime import datetime as dt
from dolar_quotation_class import DollarQuotation


def Main():
    print(f"Started at {dt.now().strftime('%Y-%m-%dT%H:%M:%S')}")
    call = DollarQuotation()
    call.get_quotation()     
    print(f"Done at  {dt.now().strftime('%Y-%m-%dT%H:%M:%S')}")

if __name__ == "__main__":
    Main()
