import sqlite3
import quandl
from stock_api.celery import app
from stock.models import ticker
import datetime
import requests
@app.task
def get_data():
    api_key = 'EodLUktVMExBHFnjW5BC'
    resp = requests.get('https://www.quandl.com/api/v3/datatables/SHARADAR/SEP.json?qopts.columns=ticker,date,open,high,low,close,volume&date.gte=2017-01-01&ticker=AAPL,AXP,BA,CAT,CSCO,CVX,DWDP,GE,HD,IBM,INTC,JNJ,JPM,KO,MCD,MMM,MRK,MSFT,NKE,PFE,PG,TRV,TSLA,UNH,UTX,VZ,WMT&api_key=EodLUktVMExBHFnjW5BC')
    print(resp)
    print(type(resp))
    data=resp.json()
    print(type(data))
    print(data)
    a=[]
    c=0
    for i in data['datatable']['data']:
        c=c+1
        print(i)
        symbol=i[0]
        print('symbol:',symbol)
        date=i[1]
        print('date:',date)
        open=i[2]
        high=i[3]
        low=i[4]
        close=i[5]
        volume=i[6]
        ticker.objects.get_or_create(symbol=symbol,date=date,open=open,high=high,low=low,close=close,volume=volume)
        print("iNserted")