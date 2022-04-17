import os
import pandas as pd
import json
import urllib.request

coins=pd.DataFrame()
dict=[]

#get coins
for page in range(1,15):
    with urllib.request.urlopen(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={page}&sparkline=false") as response: 
        res = response.read()
        jres = json.loads(res)
        for item in jres:
            dict.append(item)

df=pd.DataFrame(dict) 

"""
columns ['id', 'symbol', 'name', 'image', 'current_price', 'market_cap',
       'market_cap_rank', 'fully_diluted_valuation', 'total_volume',
       'high_24h', 'low_24h', 'price_change_24h',
       'price_change_percentage_24h', 'market_cap_change_24h',
       'market_cap_change_percentage_24h', 'circulating_supply',
       'total_supply', 'max_supply', 'ath', 'ath_change_percentage',
       'ath_date', 'atl', 'atl_change_percentage', 'atl_date', 'roi',
       'last_updated'],

"""

inteldf = df.filter(['name','market_cap_rank','fully_diluted_valuation'])

try:
    os.remove("intel.csv")
except:
    pass
inteldf.to_csv('intel.csv', index=False) 