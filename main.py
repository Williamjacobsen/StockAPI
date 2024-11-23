import os
os.system('cls')
import requests
import pandas as pd
import json

headers = {'User-Agent': "villi05.v.j@gmail.com"}

tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)
tickers_cik = pd.json_normalize(pd.json_normalize(tickers_cik.json(), max_level=0).values[0])
tickers_cik["cik_str"] = tickers_cik["cik_str"].astype(str).str.zfill(10)
tickers_cik.set_index("ticker", inplace=True)
#print(tickers_cik)


# https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json 


