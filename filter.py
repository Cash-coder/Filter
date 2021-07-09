import json
import requests
from os import extsep
import random
from ebaysdk.finding import Connection
from ebaysdk.shopping import Connection as Shopping
from bs4 import BeautifulSoup
from datetime import date
import datetime
import calendar 


def apply_wp_price(ebay_total_price):
    #print(ebay_total_price)

    #python in range doesn't allow to process int or floats at the same time
    #one if for int and another for floats with numpy
  
    if int(ebay_total_price) > 1000:
        margin = 0.03
    elif int(ebay_total_price) in range(800,999):
        margin = 0.035 # 3.5%  
    elif int(ebay_total_price) in range(600,800):
        margin = 0.04 # 4%  
    elif int(ebay_total_price) in range(400,600):
        margin = 0.05 # 5%  
    elif int(ebay_total_price) in range(300,400):
        margin = 0.06 # 6%  
    elif int(ebay_total_price) in range(200,300):
        margin = 0.08 # 8%  
    elif int(ebay_total_price) in range(100,200):
        margin = 0.10 # 10%  
    elif int(ebay_total_price) in range(50,100):
        margin = 0.12 # 12%  
    elif int(ebay_total_price) in range(20,50):
        margin = 0.30 # 30%  
    elif int(ebay_total_price) in range(0,20):
        margin = 0.5 # 50%

    benefit = ebay_total_price * margin
    final_price = ebay_total_price + benefit

    #add attractive termination to the price
    terminator_options = [0.14,0.23,0.24,0.34,0.49,0.57,0.83,0.97]
    terminator = random.choice(terminator_options)
    final_price_decorated = final_price + terminator
    #delete unwanted decimals
    final_price_decorated = round(final_price_decorated,2)
    print(ebay_total_price,'\t', final_price_decorated, '\t',"margin:",margin,'\t','benefit', benefit)
    return final_price_decorated

def get_ebay_pictures(ebay_prod_id):
    
    api = Shopping(config_file='ebay.yaml')
    request = {'ItemID':ebay_prod_id}

    response = api.execute('GetSingleItem',request)

    pictures_url_list = []

    soup = BeautifulSoup(response.content,'lxml')
    #print(soup.prettify())
    pictures_url = soup.find_all('pictureurl')
    for url in pictures_url:
        url = str(url)
        url = url.replace('<pictureurl>','')
        url = url.replace('</pictureurl>','')
        pictures_url_list.append(url)
        print(url)
    return pictures_url_list


def get_wp_shipping_time(ebay_shipping_time):
    print(ebay_shipping_time)

    #split ebay dates "vie. 9 jul. y el lun. 12 jul."
    ebay_date = ebay_shipping_time.split('.')
    ##get today's current day and month number
    current_day = str(date.today()).split('-')[2]
    current_month = str(date.today()).split('-')[1]
    current_month = int(current_month)
    current_month_name = calendar.month_name[current_month].lower()
    current_month_letters = current_month_name[0:3]

    # it can be one date(jul 12) or a range between 2 days (jul. 12 and jul. 16)
    #if it's a range of 2 dates:
    if len(ebay_date) == 5: 
        #select chunk like (9 jul)
        ebay_first_date = ebay_date[1]
        #select the number (9)
        ebay_first_day = ebay_first_date.split(' ')[1]
        #select the month name (jul)
        ebay_first_month = ebay_first_date.split(' ')[2]
        #second_date = ebay_date[3]
        #second_day = second_date.split(' ')[1]
        #ebay_second_month = second_date.split(' ')[2]
        
        #first letters from current month name to compare with ebay's
        # if it's the same month: jul == jul        
        if current_month_letters == ebay_first_month:
            shipping_days = int(ebay_first_day) - int(current_day)

            if shipping_days == 1:
                wp_shipping_text = "Envío en 24h"
            elif shipping_days == 2:
                wp_shipping_text = "Envío en 48h"
            elif shipping_days == 3:
                wp_shipping_text = "Envío en 72h"
            elif shipping_days > 3: #if thre's more than 3 days return just the number of days
                return shipping_days
            return wp_shipping_text, shipping_days

        #if it's a different month, like jul-aug
        elif current_month_letters != ebay_first_month:
            #sample date: today's 27 jul, shipping arrival on 2 aug = 6 days
            # (from today's number to the end month) + ebay 1º day
            # (31-27)+2
            now = datetime.datetime.now()
            current_month_total_days = calendar.monthrange(now.year,now.month)[1]        
            daysto_end_month = current_month_total_days - now.month
            wp_shipping_days = daysto_end_month + int(ebay_first_day)
            return wp_shipping_days
   
    elif len(ebay_date) == 3: #there's only one date, like in "vie. 12 jul."
        ebay_day_number = ebay_shipping_time.split('.')[1]
        ebay_day_number = ebay_day_number.split(' ')[1]
        ebay_month_name = ebay_shipping_time.split('.')[1].split(' ')[2]

        #if it's the same month
        if current_month_letters == ebay_month_name:
            shipping_days = int(ebay_day_number) - int(current_day)
            if shipping_days == 1:
                wp_shipping_text = "Envío en 24h"
            elif shipping_days == 2:
                wp_shipping_text = "Envío en 48h"
            elif shipping_days == 3:
                wp_shipping_text = "Envío en 72h"
            elif shipping_days > 3: #if thre's more than 3 days return just the number of days
                return shipping_days
            return shipping_days
        
        #if it's a different month
        elif current_month_letters != ebay_month_name:

            now = datetime.datetime.now()
            current_month_total_days = calendar.monthrange(now.year,now.month)[1]        
            daysto_end_month = current_month_total_days - now.month
            shipping_days = daysto_end_month + int(ebay_day_number)

            if shipping_days == 1:
                wp_shipping_text = "Envío en 24h"
            elif shipping_days == 2:
                wp_shipping_text = "Envío en 48h"
            elif shipping_days == 3:
                wp_shipping_text = "Envío en 72h"
            elif shipping_days > 3: #if thre's more than 3 days return just the number of days
                return shipping_days
            return wp_shipping_text, shipping_days

def get_EUR_GBP_exchange():

    api_key = '5efad85ac008571f2d938413de17d8ab'
    end_point = 'http://api.exchangeratesapi.io/v1/latest?access_key=5efad85ac008571f2d938413de17d8ab'#&base=GBP'
    response = requests.get(end_point)
    #print(response.status_code)
    response_dict = response.json()
    GBP_value = response_dict["rates"]['GBP']
    print(GBP_value)
    return GBP_value


GBP_value = get_EUR_GBP_exchange()

entry = []
with open('scrapper_output.json',encoding='utf8') as json_file:
    scrapper_data = json.load(json_file)
    
    for item in scrapper_data:
        #print(item)

        #variables to filter:
        variable_prod =   item['variable_prod']
        seller_sold_number=int(item['seller_votes'])
        payment_methods = item['payment_methods']
        prod_state =      item['product_state']
        sold_out_text =   str(item['product_sold_out_text'])
        ebay_price =      item['price']
        ebay_shipping_price =  item['shipping_price']
        area_served =     item['served_area']

        #variables no need to filter:
        title =           item['title']
        price =           item['price']
        query =           item['query']
        ebay_shipping_time = item['shipping_time']
        ebay_returns =    item['returns']
        ebay_prod_id =    item['ebay_article_id']
        ebay_prod_url =   item['prod_url']
        ebay_category =   item['category']
        ebay_prod_specs = item['prod_specs']
        ebay_prod_description = item['prod_description']
        ebay_import_taxes = item['import_taxes']



        #this is the filter, only prods that meet the requierments can pass through
        if variable_prod != None: #avoid product if it's a variable prod
            print("this item is variable",item['title'])
            continue
        elif  seller_sold_number < 50: #if very little sells
            print('not enough votes',item['title'])
            continue
        elif 'PayPal' not in payment_methods:
            print('not payment',item['title'])
            continue
        elif 'Visa' not in payment_methods:
            print('not payment',item['title'])
            continue
        elif 'Para desguace' in prod_state: #if the prod is broken
            print('broken item',item['title'])
            continue
        elif '[]' not in sold_out_text : # if the product is NOT sold out it's an empty list
            print('prod sold out',item['title'])
            continue
        elif ebay_price == '':
            print('no price',item['title'])
            continue
        elif ebay_shipping_price == '':
            print('not shipping price',item['title'])
            continue
        elif 'Solo recogida local' in area_served:
            print('no shippiing service',item['title'])
            continue


        #apply re_price function
        #clean price and convert to float
        print(".-------------",ebay_price)
        #in the case of a price with comma like "1.102,95 EUR"
        if ('.') in ebay_price and (',') in ebay_price: 
            #print("detected!!!", ebay_price)
            ebay_price = ebay_price.split(',')[0]
            ebay_price = ebay_price.replace('.','')
            ebay_price = float(ebay_price)

        else: #if its a number like  "516,95 EUR"
            ebay_price = ebay_price.replace('EUR','').replace(',','.').replace('c/u','').replace(' ','').strip()
            ebay_price = float(ebay_price)

###################### THIS GOES IN SCRAPPER#################
        try:
            ebay_shipping_price = ebay_shipping_price.replace('EUR','').replace(',','.').strip()
            ebay_shipping_price = float(ebay_shipping_price)
        except Exception as e:
            #print(e)
            pass
        try:
            if 'Rápido y gratis' in ebay_shipping_price:
                ebay_shipping_price = 0                
        except Exception as e:
            #print(e)
            pass
        try:
            if 'GRATIS' in ebay_shipping_price:
                ebay_shipping_price = 0
        except:
            pass
        
        ################################### this goes here


        ebay_total_price = ebay_price + ebay_shipping_price
        
        if ebay_import_taxes: #GBP_value obtained with API function get_EUR_GBP_value()
            ebay_import_taxes = ebay_import_taxes.replace('GBP','').replace(',','.')
            EUR_value = float(ebay_import_taxes) * GBP_value
            
            ebay_total_price = ebay_price + EUR_value + ebay_shipping_price
            
            print('taxes_GBP=',ebay_import_taxes)
            print('taxes EUR=',EUR_value)
            print('shipping_price=',ebay_shipping_price)
            print('ebay_total_price=', ebay_total_price)
        
        wp_price = apply_wp_price(ebay_total_price)

        pictures = 'uncomment this fucntion'#get_ebay_pictures(ebay_prod_id)
        wp_shipping_time = get_wp_shipping_time(ebay_shipping_time)

        #print("there are products with wanted characteristics!!")
        data_to_dump = [{'query':query,'title':title,
        'prod_state':prod_state,
        'ebay_price':ebay_price,'ebay_shipping_price':ebay_shipping_price,
        'ebay_shipping_time':ebay_shipping_time,'ebay_returns':ebay_returns,
        'ebay_prod_id':ebay_prod_id,'ebay_prod_url':ebay_prod_url,
        'ebay_category':ebay_category,'ebay_prod_specs':ebay_prod_specs,
        'ebay_prod_description':ebay_prod_description,'wp_price':wp_price,
        'pictures':pictures,'wp_shipping_time':wp_shipping_time, 
        'ebay_import_taxes':ebay_import_taxes,
         }]

        entry.append(data_to_dump)
        #variables I don't need in filtered csv
        #'payment_methods':payment_methods, sold_out_text,'seller_votes':seller_sold_number,
        #area_served,'var_prod':variable_prod

    with open('filtered.json','w') as new_file: #,encoding='utf8')
        json.dump(entry, new_file, indent=4)
        # new_file.write(",")
        # new_file.close()

#####################
#csv.field_size_limit(sys.maxint)
# maxInt = sys.maxsize

# #this is to avoid error while reding row "row character lentgh exceeds maximum"
# while True:
#     # decrease the maxInt value by factor 10 
#     # as long as the OverflowError occurs.

#     try:
#         csv.field_size_limit(maxInt)
#         break
#     except OverflowError:
#         maxInt = int(maxInt/10)
######################
