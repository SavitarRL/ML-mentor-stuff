#getting the data by writing a csv file
from alpha_vantage.fundamentaldata import FundamentalData as FD
import pandas as pd
import csv
import os
import requests
import urllib
import json

comp_dict ={"facebook":'FB',
            "apple":'AAPL',
            "amazon":'AMZN',
            "netflix":'NFLX',
            "google":'GOOG'}
def getAnnualCashFlow():
    for name, symb in comp_dict.items():
        fd = FD(key='E3YVKWX4MG1AN2OA',output_format='pandas')
        data, meta_data = fd.get_cash_flow_annual(symbol=symb)
        data.to_csv(name+"_annual_cash flow.csv")
def getQuarterlyCashFlow():
    for name, symb in comp_dict.items():
        fd = FD(key='E3YVKWX4MG1AN2OA',output_format='pandas')
        data, meta_data = fd.get_cash_flow_quarterly(symbol=symb)
        data.to_csv(name+"_quarterly_cash flow.csv")

def getEarnings():
    api_key = os.getenv('E3YVKWX4MG1AN2OA')
    base_url = 'https://www.alphavantage.co/query?'
    for name, symb in comp_dict.items():
        params = {'function': 'CASH_FLOW',
                 'symbol' : symb,
		         'apikey': "E3YVKWX4MG1AN2OA"}
        resp_data = requests.get(base_url, params=params)
#         print(type(resp_data.json()))
        data_dict = resp_data.json()
        filename = name+"_Earnings"
        with open(filename+".json",'w') as f:
            json.dump(data_dict, f) #everything from the json file

### continue ###            

#         a_data = data_dict.get("annualReports")
#         print(a_data)
#         annual_data = a_data[0]
# #         print(annual_data)
#         with open(filename+'_annual_.csv', 'w') as filea:  # You will need 'wb' mode in Python 2.x
#             w = csv.DictWriter(filea, annual_data.keys())
#             w.writeheader()
#             w.writerow(annual_data)
            
#         q_data = data_dict.get("quarterlyReports")
#         quarterly_data = q_data[0]
#         with open(filename+'_quarterly_.csv', 'w') as fileq:  # You will need 'wb' mode in Python 2.x
#             w = csv.DictWriter(fileq, quarterly_data.keys())
#             w.writeheader()
#             w.writerow(annual_data)



getCashFlow()
getQuarterlyCashFlow()
getEarnings()
