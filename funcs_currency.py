CURRENCY_EQUIVALENCES_FILE = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\filter\exchange_to_EUR.txt'

def delete_file(file_path):
    import os

    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f'this file path doesnt exist: <{file_path}>')


def update_rates_file():
    from time import sleep

    print('updating $€ rate file...')

    # request GBP 
    # sleep to avoid exceed api time speed
    # request USD
    # delete old file
    # create new file with updated data
    # get today's date
    # write today's date
    # write USD and GBP

    CURRENCY_EQUIVALENCES_FILE = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\filter\exchange_to_EUR.txt'

    # request exchange rates
    gbp = get_EUR_rate('GBP')
    sleep(3)
    usd = get_EUR_rate('USD')

    delete_file(CURRENCY_EQUIVALENCES_FILE)

    #get today's date
    today = get_today_date()
    print(f'today rates GBP: {gbp}|USD: {usd}')

    #write new updated file
    with open(CURRENCY_EQUIVALENCES_FILE, 'w+') as f:
        # double curly braces to use {} inside an f string
        f.write(f"{today}\n")
        f.write(f'{{"GBP":{gbp}, "USD":{usd}}}')
        # f.write(f'"GBP":"{gbp}", "USD":"{usd}"')

# return today's date in format: 2022-04-23
def get_today_date():
    from datetime import datetime as d

    date = d.now()
    today = date.strftime("%Y-%m-%d")
    # print(date.strftime("%Y-%m-%d %H:%M:%S"))
    return today

# GBP: esterline pound | USD: US dollar |EUR
def get_EUR_rate(origin_currency):
    import json
    import requests
    import authentications

    _key = authentications.currency_exchange_api

    url = "https://currency-converter5.p.rapidapi.com/currency/convert"

    querystring = {"format":"json","from":origin_currency, "to":"EUR","amount":"1"}

    headers = {
        "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com",
        "X-RapidAPI-Key": _key
    }

    try:
        # response = requests.request("GET", url, headers=headers, params=querystring)
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        # print(response)
        rate = response['rates']['EUR']['rate']
        print(f'rate for {origin_currency} is {rate} EUR')

        return rate
    except Exception as e:
        print(f'error in get_EUR_rate()\nresponse:{response}\nexception: {e}')

def read_doc(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines

def get_today_rates():
    
    # get today's date
    # reads exchange file with rates
    # if date is different:
        # update_rates_file()
    # elif today's date == file's date:
        # return recorded dates

    today = get_today_date()
    
    lines = read_doc(CURRENCY_EQUIVALENCES_FILE)
    recorded_date = lines[0].replace('\n','')
    # print(recorded_date)

    if today == recorded_date:
        string_set = lines[1]
        #eval() to transform from string to set
        data_set = eval(string_set)
        return data_set

    # if date doesn't match, update file, read it again and return updated data
    if today != recorded_date:
        update_rates_file()
        lines = read_doc(CURRENCY_EQUIVALENCES_FILE)
        string_set = lines[1]
        data_set = eval(string_set)
        return data_set


def convert_amount_toEUR(amount, currency_origin):
    '''parameters: amount in int, GBP/USD'''

    amount = int(float(amount))

    #get exchange rates
    rates = get_today_rates()
    
    # from rates get equivalence
    # gbp = rates['GBP']
    # usd = rates['USD']
    # rates[origin]
    equivalence_rate = rates[currency_origin]

    # 3 rule:
    # 1$  = 0.93€
    # 54$ =  X
    # x = (54*0.93)/1
    # x = 54*0.93

    equivalent = amount * equivalence_rate
    equivalent = round(equivalent)
    
    return equivalent