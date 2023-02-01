from datetime import datetime as dt
import schedule
import time
from dolar_quotation_class import DollarQuotation


def job():
    print(f"Starting at {dt.now().strftime('%Y-%m-%dT%H:%M:%S')}")
    call = DollarQuotation()
    call.get_quotation()     
    print(f"Done at  {dt.now().strftime('%Y-%m-%dT%H:%M:%S')}")
schedule.every().day.at("20:42").do(job)

while True:
    print(f"Running at {dt.now().strftime('%Y-%m-%dT%H:%M:%S')}")
    schedule.run_pending()
    time.sleep(1*60)
