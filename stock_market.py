from datetime import date
import os
import json
import requests
import time
access_key = ' ' # Get you API key from http://api.marketstack.com and paste here...
print('Stock checking app by Aditya!!')

def get_stocks():
    n = int(input("How may stocks do you want to check: "))
    stocks = []
    for i in range(n):
        x = input("Enter Symbol :\n")
        stocks.append(x)
    print("Thank you for entering the symbols...")
    time.sleep(1)
    print("processing requests...")
    time.sleep(2)
    print('======================================')
    for j in range(0,n):
        url = 'http://api.marketstack.com/v1/eod?access_key={}&symbols={}'.format(access_key,stocks[j])
        headers = {
            'access_key' : access_key
        }
        response = requests.request("GET", url, headers=headers)
        response_text = response.text
        with open("file1.json", "w") as file1:
            file1.write(response_text)
        file1.close()
        with open("file1.json", 'r+') as file:
            data = json.load(file)
            open_stock_data = data['data'][0]['open']
            close_stock_data = data['data'][0]['close']
            ex_date = data['data'][0]['date'][:10]
            print(stocks[j])
            print('======')
            if open_stock_data > close_stock_data:
                print('\tDate: {}'.format(ex_date))
                print('\tOpened at: {}'.format(open_stock_data))
                print('\tColsed at: {}'.format(close_stock_data))
                print('\t↓↓↓↓↓↓↓ Gone Down...')
            else:
                print('\tDate: {}'.format(ex_date))
                print('\tOpened at: {}'.format(open_stock_data))
                print('\tClosed at: {}'.format(close_stock_data))
                print('\t↑↑↑↑↑↑↑ Gone Up...')
        os.remove('file1.json')
        print('======================================')
        time.sleep(2)


def get_stock_exchanges():
    name = input('Enter the symbol of the stock exchange you are searching for: ')
    url = 'http://api.marketstack.com/v1/exchanges?access_key={}'.format(access_key)
    headers = {
            'access_key' : access_key
    }
    response = requests.request("GET", url, headers=headers)
    response_text = response.text        
    with open("file2.json", "w") as file2:
        file2.write(response_text)
    file2.close()
    with open("file2.json", "r+") as file:
        data = json.load(file)
    print('========================================')
    for i in range(68):
        if name == data['data'][i]['acronym']:
            print('\tName: ' + data['data'][i]['name'])
            print('\tSymbol: ' + data['data'][i]['acronym'])
            print('\tCity: ' + data['data'][i]['city'])
            print('\tCurrency: ' + data['data'][i]['currency']['code'])
    print('========================================')
    os.remove('file2.json')
    

def get_stocks_by_date():
    n = int(input("How may stocks do you want to check: "))
    stocks = []

    for i in range(0,n):
        x = input("Enter Symbol :\n")
        stocks.append(x)
    print("Thank you for entering the symbols...")
    time.sleep(1)
    print("processing requests...")
    time.sleep(1)
    get_date = input('Enter the date to get the stock details: (in YYYY-MM-DD format) \n')

    for j in range(0,n):
        url = 'http://api.marketstack.com/v1/eod?access_key={}&symbols={}'.format(access_key,stocks[j])
        headers = {
            'access_key' : access_key
        }

        response = requests.request("GET", url, headers=headers)
        response_text = response.text        
        with open("file3.json", "w") as file3:
            file3.write(response_text)
        file3.close()
        with open("file3.json", "r+") as file:
            data = json.load(file)
        print('========================================')

        try:
            for k in range(data['pagination']['count']):
                if get_date == data['data'][k]['date'][:10]:
                    print('\t{}'.format(stocks[j]))
                    print('\t=====')
                    print('\tExchange: ' + data['data'][k]['exchange'])
                    print('\tSymbol: ' + data['data'][k]['symbol'])
                    print('\tOpened: {}'.format(data['data'][k]['open']))
                    print('\tClosed: {}'.format(data['data'][k]['close']))
                    if data['data'][k]['open'] > data['data'][k]['close']:
                        print("\t'↓↓↓↓↓↓↓ Gone Down...")
                    elif data['data'][k]['open'] < data['data'][k]['close']:
                        print("\t↑↑↑↑↑↑↑ Gone Up...")
                    print('========================================')
                    time.sleep(2)
        except TypeError:
            print("\tCouldn't get the values")
        finally:
            os.remove('file3.json')

print('1. Stock Exchanges \n2. Stock Market Values \n3. Prevoius Stock Details(Based on a date):')
choice = int(input('Enter an Option: '))
if choice == 1:
    get_stock_exchanges()
elif choice == 2:
    get_stocks()
elif choice == 3:
    get_stocks_by_date()
else:
    print('Invalid option entered...')

print('Thank you!!!')