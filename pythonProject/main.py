import requests
from bs4 import BeautifulSoup
import json
def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    stock = {
    'title': soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
    'price' : soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,

    'Change_in_price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text}
    return stock
stock_data = []
m = int(input("How many stocks do you need to get info about:\n"))
for i in range(m):
    mystock = input("Enter a stock put its ticker symbol:\n")
    stock_data.append(getData(mystock))
    print("Getting:", mystock)
    print("done with",mystock)






for a in stock_data:
    print(a)
with open('stock_info.json','w') as file:
    json.dump(stock_data, file)