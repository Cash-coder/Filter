

import json
import csv
from os import extsep
import random
from re import T
import traceback
from ebaysdk.finding import Connection
from ebaysdk.shopping import Connection as Shopping
from bs4 import BeautifulSoup
from datetime import date
import datetime
import calendar 
import logging
from openpyxl import load_workbook


logging.basicConfig(level=logging.INFO)

DEEPL_AUTH_KEY = 'ea826f71-83b5-f5aa-231f-aad69f95aec2:fx'

PICS_DB    = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\PICS_DB.xlsx"
# INPUT_FILE = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.csv"
INPUT_FILE = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.json"
OUTPUT_FILE= r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\FILTER_OUTPUT.xlsx" 

FILTER_OUTPUT_PATH =r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\FILTER_OUTPUT.xlsx"
LOGS_FOLDER        =r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\logs_folder"


# JSON FILTER INPUT NAMES, CRAWLER OUTPUT
#NOW USING CSV, IN DESUSE
EBAY_QUERY_NAME     = 'query'
EBAY_TITLE_NAME     = 'title'
EBAY_PRICE_NAME     = 'price'
EBAY_SHIPPING_TIME  = 'shipping_time'
EBAY_VARIABLE_PROD_NAME = 'variable_prod'
EBAY_RETURNS_NAME   = 'returns'
EBAY_SHIPPING_PRICE = 'shipping_price'
EBAY_ID_NAME        = 'ebay_article_id'
EBAY_PROD_URL_NAME  = 'prod_url'
EBAY_VENDOR_NAME    = 'ebay_vendor'
EBAY_SELLER_VOTES_NAME='seller_votes'
EBAY_CATEGORY_NAME  = 'category'
EBAY_PAYMENT_NAME   = 'payment_methods'
EBAY_PROD_SPECS_NAME= 'prod_specs'
EBAY_PROD_STATE_NAME= 'product_state'
EBAY_PROD_DESCRIPTION_NAME = 'prod_description'
EBAY_SERVED_AREA_NAME='served_area'
EBAY_REVIEWS_NAME   = 'reviews'
EBAY_PROD_SOLD_OUT_NAME = 'product_sold_out_text'
EBAY_IMPORT_TAXES_NAME  = 'import_taxes'
TARGET_CATEGORY_NAME    = 'target_category'
TARGET_ATTR_1_NAME   = 'query_attribute_1'
TARGET_ATTR_2_NAME   = 'query_attribute_2'
TARGET_MODEL_NAME    = 'query_model'
TARGET_PROD_STATE    = 'query_prod_state'
EBAY_PICS_URLS       = 'ebay_pics'
EBAY_SUBTITLE        = 'subtitle'
EBAY_IFRAME          = 'iframe_description_url'
AVAILABLE_COLORS_NAME= 'available_colors'
SUBTITLE_NAME        = 'subtitle'

# #CSV ROWS N, FILTER INPUT, CRAWLER OUTPUT
# EBAY_QUERY_NAME       = 2
# EBAY_TITLE_NAME       = 0
# EBAY_PRICE_NAME       = 1
# EBAY_SHIPPING_TIME    = 3
# EBAY_VARIABLE_PROD_NAME=4
# EBAY_RETURNS_NAME     = 5
# EBAY_SHIPPING_PRICE   = 6
# EBAY_ID_NAME          = 7
# EBAY_PROD_URL_NAME    = 8
# EBAY_VENDOR_NAME      = 9
# EBAY_SELLER_VOTES_NAME= 10
# EBAY_CATEGORY_NAME    = 11
# EBAY_PAYMENT_NAME     = 12
# EBAY_PROD_SPECS_NAME  = 13
# EBAY_PROD_STATE_NAME  = 14
# # EBAY_PROD_DESCRIPTION_NAME=
# EBAY_SERVED_AREA_NAME  = 15
# EBAY_REVIEWS_NAME      = 16
# EBAY_PROD_SOLD_OUT_NAME= 17
# EBAY_IMPORT_TAXES_NAME= 18
# TARGET_CATEGORY_NAME  = 19
# TARGET_ATTR_1_NAME    = 20
# TARGET_ATTR_2_NAME    = 21
# TARGET_MODEL_NAME     = 22
# TARGET_PROD_STATE     = 23
# EBAY_PICS_URLS        = 24
# COLORS_AVAILABLE      = 25   

#FILTER_OUTPUT COLUMNS
QUERY_COL             = 1
TARGET_PROD_STATE_COL = 2
EBAY_PROD_STATE_COL   = 3
EBAY_TITLE_COL        = 4
AVAILABLE_COLORS_COL  = 5
DETECTED_COLOR_COL    = 6
DETECTED_WARRANTY_COL = 7
EBAY_TOTAL_PRICE_COL  = 8
SUBTITLE_COL          = 9
EBAY_VENDOR_NOTES_COL = 10
# EBAY_PROD_DESCRIPTION_LINK = 7 #description already included in prod_url
# CHECKMARK RESERVED  = 11 RESERVED!
EBAY_PROD_URL_COL     = 12
#EMPTY CELL TO LEAVE THE ACCEPT MARK= 10
EBAY_SELLER_VOTES_COL = 13
EBAY_RETURNS_COL      = 14
EBAY_SHIPPING_TIME_COL= 15
EBAY_SHIPPING_PRICE_COL=16
#from here I don't care for the order, random
EBAY_PRICE_COL     = 17
WP_PRICE_COL       = 18
PICTURES_COL       = 19
# PROD_BRAND_COL   = 17
EBAY_PROD_ID_COL   = 20
EBAY_CATEGORY_COL  = 21
TARGET_CATEGORY_COL= 22
TARGET_ATTR_1_COL  = 23
TARGET_ATTR_2_COL  = 24 
EBAY_PROD_SPECS_COL= 25
EBAY_VENDOR_NAME_COL=26
WP_SHIPPING_TIME_COL=27
EBAY_PROD_DESCRIPTION_COL = 28


def apply_wp_price(ebay_total_price):
    print(ebay_total_price)

    if int(ebay_total_price) > 1001:
        margin = 0.03
    elif int(ebay_total_price) in range(800,1000):
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

    stripe_fee = 0.014 # 1.4%
    benefit = ebay_total_price * margin
    taxes = benefit * 0.21 #21%
    #not 100% correct, stripe charges in the final amount
    stripe_fee_n =  (ebay_total_price + benefit + taxes) * stripe_fee
    final_price = ebay_total_price + benefit + taxes + stripe_fee_n

    #add attractive termination to the price: 55 -> 54,45
    terminator_options = [0.14,0.23,0.24,0.34,0.49,0.57,0.83,0.97]
    terminator = random.choice(terminator_options)
    final_price_decorated = final_price + terminator
    #delete unwanted decimals
    final_price_decorated = round(final_price_decorated,2)
    # print(ebay_total_price,'\t', 'f_price_deco',final_price_decorated, '\t',"margin:",margin,'\t','benefit', benefit)
    print(f'ebay_total_price: {ebay_total_price} \t benefit: {benefit}, taxes {taxes}, stripe_fee_n {stripe_fee_n}, finalP: {final_price_decorated} ')

    return final_price_decorated

#ebay API, in desuse
def get_ebay_pictures(ebay_prod_id):
    #not working because of ebay authentication issue
    try:
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
    except Exception as e:
        print(e)
        pass

def make_ebay_pics_urls(url_list):
    #replace the last url parametter for s-l600.jpg to get the big pic instead of the thumbnail
    modified_urls = []
    for url in url_list:
        chunks = url.split('/')
        tail   = chunks[-1]
        new_url = url.replace(tail, 's-l500.jpg') #ls600 accepted as well
        modified_urls.append(new_url)
    return modified_urls

def check_pics_db(target_model, target_attr_1):
    from openpyxl import load_workbook

    wb = load_workbook(PICS_DB)
    ws = wb.active

    #for pics in list:
        #if pic in pics_db:
            #use pictures from db
        #else:
            #return 'there aren\'t any pics in pics_db for this item'

    pics_list = []
    for row in ws.iter_rows(min_row=2):
        row_number = row[0].row

        pic_model   = ws.cell(row=row_number, column=1).value
        pic_attr  = ws.cell(row=row_number, column=2).value
        # print('----------', pic_model, pic_attr)

        if target_model == pic_model and target_attr_2 == pic_attr:
            n = 3
            for _ in range(15): #15 pics as max
                pic_url = ws.cell(row=row_number, column=n).value
                if pic_url != None and pic_url != '':
                    pics_list.append(pic_url)
                    n += 1
                else:
                    break
        else:
            continue
    if len(pics_list) > 0:
        return pics_list
    else:
        return 'there aren\'t any pics in pics_db for this item'


    #if item==  and attr ==:
    
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
            #UPDATE RETURN ONLY THE DAYS
            # return wp_shipping_text, shipping_days
            return shipping_days

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

            #UPDATE RETURN ONLY SHIPPING DAYS
            # return wp_shipping_text, shipping_days
            return shipping_days

# def apply_category(ebay_category):
    # #using target_db_category to guide, from scrapper_output file
    # if ebay_category == 'Movilesytelefonia' or 'Movilesysmartphones':
        # prod_db_category = 'smartphones'   
    # #apply undefined if it's out of range
    # else:
        # prod_db_category = 'undefined'
    # return prod_db_category

# def apply_prod_brand(ebay_title):
    # #do the same, using data from target
    # if 'iphone' or 'Iphone' or 'iPhone' or 'IPhone' in ebay_title:
        # prod_brand = 'iphone'
    # elif 'samsung' or 'Samsung' in ebay_title:
        # prod_brand = 'samsung'
    # return prod_brand

def copy_move_file(src_dir, dst_dir, mode='time'):
    '''file_name, src_dir, dst_dir, mode=time or no_time // absolute paths'''
    #if mode=time -> include time on file title, elif normal -> not include time
    import os
    import shutil
    import datetime

    #detect file_name and file_format
    file = src_dir.split('\\')[-1]
    file_name = file.split('.')[0]
    file_format = file.split('.')[1]
    file_format = '.' + file_format

    #create time id to rename the file
    now = str(datetime.datetime.now())[:16]
    now = now.replace(' ', '_')
    now = now.replace(':', '-')

    #include time or not based on specified mode
    if mode == 'time':
        abs_path = file_name + str(now) + file_format
    elif mode == 'no_time':
        abs_path = file_name + file_format

    dst_path = dst_dir + '\\' + abs_path

    shutil.copy(src_dir, dst_path)
    print(f'file {file} moved to {dst_path}')

def clean_excel(EXCEL_FILE):
    from openpyxl import load_workbook
    import logging

    wb = load_workbook(EXCEL_FILE)
    ws = wb.active

    #starting at 3, delete all rows
    ws.delete_rows(3, ws.max_row+1)
    wb.save(EXCEL_FILE)

    logging.info(f'cleaned set_prod_db  and gaps_file to begin fresh writing')

def color_detector(ebay_title):
    ebay_title = ebay_title.lower()
    # ordering all colors in the same order, the using index, if the first match in iatlina, you know it's negro, second mattch= azul
    spanish_colors = ['negro',  'azul',  'marrón',  'gris',  'verde',   'naranja',  ' rosa',    'violeta',  'rojo', 'blanco',    'amarillo', 'oro', 'plata']
    english_colors = ['black',  'blue',  'brown',   'grey',   'green',   'orange',   'pink',    'purple',   'red',  'white',    'yellow',   'gold', 'silver']
    italian_colors = ['nero',   'blu',   'marrone', 'grigio', 'verde',  'arancione', 'rosa',    'viola',    'rosso', 'bianco',   'giallo'   'oro',  'argento'] 
    german_colors  = ['schwarz', 'blau', 'braun',    'grau',  'grün',   'orange',    'rosa',     'lila',     'rot',   'weiß',    'gelb',     'gold', 'silber']
    french_colors  = [ 'noir',    'bleu', 'brun',   'gris',   'vert',   'orange',   'rose',      'pourpre', 'rouge', 'blanc',   'jaune',   '----',  'argent'] #mising golden in french because it's 'or', will make a lot of false postives

    #some standalone colors
    if 'grafito' in ebay_title:
        return 'grafito'

    #spanish
    for color in spanish_colors:
        if color in ebay_title:
            detected_color = color
            return detected_color
    #english
    for color in english_colors:
        if color in ebay_title:
            i = english_colors.index(color)
            detected_color = spanish_colors[i]
            return detected_color
    #italian
    for color in italian_colors:
        if color in ebay_title:
            i = italian_colors.index(color)
            detected_color = spanish_colors[i]
            return detected_color
    #german
    for color in german_colors:
        if color in ebay_title:
            i = german_colors.index(color)
            detected_color = spanish_colors[i]
    #french
    for color in french_colors:
        if color in ebay_title:
            i = french_colors.index(color)
            detected_color = spanish_colors[i]

    return None

#get warranty searching for text match
def detect_warranty(subtitle, description):
    #notice monate != monaten
    one_year  = ['garantía 1 año', '1 año garantía','garantía 12 meses', '12 meses garantía', '12 monate gewährleistung', '12 monaten gewährleistung' ,'12 monate herstellergarantie', '1 jahr gewährleistung' , '1 jahr herstellergarantie', '12 mesi garanzia', 'garanzia 12 mesi' , 'garanzia 1 anni']
    half_year = ['6 meses garantía', 'garantía 6 meses', '6 monate gewährleistung' , '6 monate herstellergarantie', '6 mesi garanzia', 'garanzia 6 mesi']
    two_years = ['2 años de garantía','24 meses garantía','garantía 24 meses' ,'24 monate gewährleistung' , '24 monate herstellergarantie', '2 jahr gewährleistung' , '2 jahr herstellergarantie', '24 mesi garanzia', 'garanzia 24 mesi' , 'garanzia 1 anni']

    #check in subtitle
    try:
        subtitle = str(subtitle)
        subtitle = subtitle.lower()
        for item in one_year:
            if item in subtitle:
                return '12 months'
        for item in half_year:
            if item in subtitle:
                return '6 months'
        for item in two_years:
            if item in subtitle:
                return '24 months'
    except AttributeError as e:
        print('asdadasdsd')
        print(e)
        pass #subtitle not present

    #check in description
    try:
        description = str(description)
        description = description.lower()
        for item in one_year:
            if item in description:
                return '12 months'
        for item in half_year:
            if item in description:
                return '6 months'
        for item in two_years:
            if item in description:
                return '24 months'
    except AttributeError: pass


def deepl_translate(text, target_language='ES'):
    import deepl
    global DEEPL_AUTH_KEY 
    
    translator = deepl.Translator(DEEPL_AUTH_KEY) 
    result = translator.translate_text(text, target_lang=target_language) 
    translated_text = result.text
    return translated_text

def get_ebay_vendor_notes(ebay_prod_specs):
    #vendor notes are OFTEN in the 2º place of the list prod_specs. Get that, if "Notas del vendedor in list", translate and return

    try:
        vendor_notes = ebay_prod_specs.split('\n')[0]
        translated_notes=deepl_translate(vendor_notes)
        return translated_notes

        # for item in ebay_prod_specs:
        #     print(f'this is the item {item}')
        #     notes_title = item[0]
        #     vendor_notes = item[1]

        #     print(notes_title, vendor_notes, 'yyy')
        #     if notes_title == 'Notas del vendedor:':
        #         print('match!')
        #         translated_notes=deepl_translate(vendor_notes)
        #         print('translated_notes= ',translated_notes)
        #         return translated_notes
        
        # notes_title = raw_vendor_notes[0]
        # vendor_notes = raw_vendor_notes[1]
        
    except Exception as e:
        print('exception in get_ebay_vendor_notes',e)
        return 'this item does not have Vendor Notes at that location or don\t have any notes at all'


def write_to_excel(data_to_dump, FILTER_OUTPUT):

    wb = load_workbook(FILTER_OUTPUT)
    ws = wb.active 

    query =         data_to_dump.get('query') 
    ebay_title=     data_to_dump.get('ebay_title')     
    prod_state =    data_to_dump.get('prod_state')
    # prod_db_category=data_to_dump.get('prod_db_category')
    # prod_brand =    data_to_dump.get('prod_brand')
    ebay_price =    data_to_dump.get('ebay_price')
    ebay_shipping_time = data_to_dump.get('ebay_shipping_time')
    ebay_prod_id =  data_to_dump.get('ebay_prod_id')
    ebay_category = data_to_dump.get('ebay_category')
    ebay_prod_description =     data_to_dump.get('ebay_prod_description')
    target_category=data_to_dump.get('target_category')
    target_attr_2 = data_to_dump.get('target_attr_2')
    ebay_price =    data_to_dump.get('ebay_price')
    ebay_shipping_price = data_to_dump.get('ebay_shipping_price')
    ebay_returns =  data_to_dump.get('ebay_returns')
    ebay_prod_url = data_to_dump.get('ebay_prod_url')
    ebay_prod_specs=data_to_dump.get('ebay_prod_specs')
    wp_price =      data_to_dump.get('wp_price')
    wp_shipping_time=data_to_dump.get('wp_shipping_time')
    target_attr_1 = data_to_dump.get('target_attr_1')
    ebay_pics     = data_to_dump.get('pictures')
    ebay_total_price=data_to_dump.get('ebay_total_price')
    ebay_vendor_notes=data_to_dump.get('ebay_vendor_notes')
    target_prod_state=data_to_dump.get('target_prod_state')
    detected_color=data_to_dump.get('detected_color')
    warranty    =data_to_dump.get('warranty')
    available_colors  =data_to_dump.get('available_colors')
    subtitle  =data_to_dump.get('subtitle')



    last_row = ws.max_row + 1

    ws.cell(row=last_row, column= QUERY_COL,value=  query)
    ws.cell(row=last_row, column= EBAY_TITLE_COL,value=     ebay_title)
    ws.cell(row=last_row, column= EBAY_PROD_STATE_COL,value=prod_state)
    ws.cell(row=last_row, column= EBAY_PRICE_COL,value=     ebay_price)
    ws.cell(row=last_row, column= EBAY_SHIPPING_TIME_COL,value=ebay_shipping_time)
    ws.cell(row=last_row, column= EBAY_PROD_ID_COL,value=   ebay_prod_id)
    ws.cell(row=last_row, column= EBAY_CATEGORY_COL,value=  ebay_category)
    ws.cell(row=last_row, column= EBAY_PROD_DESCRIPTION_COL,value= ebay_prod_description)
    ws.cell(row=last_row, column= PICTURES_COL,value=        ebay_pics)
    ws.cell(row=last_row, column= TARGET_CATEGORY_COL,value= target_category)
    ws.cell(row=last_row, column= TARGET_ATTR_2_COL,value=  target_attr_2)
    ws.cell(row=last_row, column= EBAY_PRICE_COL,value=     ebay_price)
    ws.cell(row=last_row, column= EBAY_SHIPPING_PRICE_COL,value=ebay_shipping_price)
    ws.cell(row=last_row, column= EBAY_RETURNS_COL,value=   ebay_returns)
    ws.cell(row=last_row, column= EBAY_PROD_URL_COL,value=  ebay_prod_url)
    ws.cell(row=last_row, column= EBAY_PROD_SPECS_COL,value=ebay_prod_specs)
    ws.cell(row=last_row, column= WP_PRICE_COL,value=       wp_price)
    ws.cell(row=last_row, column= WP_SHIPPING_TIME_COL,value=  wp_shipping_time)
    ws.cell(row=last_row, column= TARGET_ATTR_1_COL,value=     target_attr_1)
    ws.cell(row=last_row, column= EBAY_TOTAL_PRICE_COL,value=  ebay_total_price)
    ws.cell(row=last_row, column= EBAY_VENDOR_NOTES_COL,value= ebay_vendor_notes)
    ws.cell(row=last_row, column= TARGET_PROD_STATE_COL,value= target_prod_state)
    ws.cell(row=last_row, column= EBAY_SELLER_VOTES_COL,value= seller_votes)
    ws.cell(row=last_row, column= DETECTED_COLOR_COL ,value= detected_color)
    ws.cell(row=last_row, column= DETECTED_WARRANTY_COL ,value= warranty)
    ws.cell(row=last_row, column= AVAILABLE_COLORS_COL ,value= available_colors)
    ws.cell(row=last_row, column= SUBTITLE_COL ,value= subtitle)

    wb.save(OUTPUT_FILE)

def get_textfrom_html(ebay_prod_description):
    from bs4 import BeautifulSoup
    try:
        text = BeautifulSoup(str(ebay_prod_description), features="html.parser").get_text()
        return text
    except Exception as e:
        print(f'in get_textfrom_html(): {e}')
        traceback.print_exc()

#make a copy in logs_folder
copy_move_file(OUTPUT_FILE, LOGS_FOLDER)
#delete old entries to start fresh
clean_excel(OUTPUT_FILE)

#for item in data:
    #if item is broken,
    #if item seller votes < x
    #other filter rules...
    #items that pass filter:
        #try to use pics from pics_db, if no pics for that prod, use ebay's pics
        #get_wp_price
        #get_shipping_time
        #...
        #append to list
    #write from list to excel

filtered_list = []
with open(INPUT_FILE, encoding='utf8') as json_file:
    scrapper_data = json.load(json_file)
    

    for item in scrapper_data:        #print(item)
        ## JSON IN DESUSE, USING CSV NOW
        # variables to filter:
        variable_prod =   item[EBAY_VARIABLE_PROD_NAME]
        seller_votes=int(item[EBAY_SELLER_VOTES_NAME])
        payment_methods = item[EBAY_PAYMENT_NAME]
        prod_state =      item[EBAY_PROD_STATE_NAME]
        sold_out_text =   str(item[EBAY_PROD_SOLD_OUT_NAME])
        ebay_price =      item[EBAY_PRICE_NAME]
        ebay_shipping_price =  item[EBAY_SHIPPING_PRICE]
        area_served =     item[EBAY_SERVED_AREA_NAME]
        target_category = item[TARGET_CATEGORY_NAME]
        target_attr_1 =   item[TARGET_ATTR_1_NAME]
        target_attr_2 =   item[TARGET_ATTR_2_NAME]
        ebay_pics     =   item[EBAY_PICS_URLS]
        ebay_vendor_name   =item[EBAY_VENDOR_NAME]
        ebay_reviews       =item[EBAY_REVIEWS_NAME]
        ebay_import_taxes  =item[EBAY_IMPORT_TAXES_NAME]
        target_model       =item[TARGET_MODEL_NAME]
        target_prod_state  =item[TARGET_PROD_STATE]
        ebay_title =           item[EBAY_TITLE_NAME]
        # price =           item[]
        query =           item[EBAY_QUERY_NAME]
        ebay_shipping_time = item[EBAY_SHIPPING_TIME]
        ebay_returns =    item[EBAY_RETURNS_NAME]
        ebay_prod_id =    item[EBAY_ID_NAME]
        ebay_prod_url =   item[EBAY_PROD_URL_NAME]
        ebay_category =   item[EBAY_CATEGORY_NAME]
        ebay_subtitle   = item[EBAY_SUBTITLE]
        available_colors =item[AVAILABLE_COLORS_NAME]
        ebay_iframe_url = item[EBAY_IFRAME]
        ebay_prod_description = item[EBAY_PROD_DESCRIPTION_NAME]
        ebay_prod_specs = item[EBAY_PROD_SPECS_NAME]
        subtitle = item[SUBTITLE_NAME]

        if area_served == None: area_served='not result'
        
        
        #SAVING TIME TOTEST, UNCOMENT 
        # ebay_prod_specs= deepl_translate(ebay_prod_specs, target_language='ES')

        #sometimes descriptio is short, only text and helpful. Other times is an iframe full of stuff. Ignore when full
        if len(ebay_prod_description) > 1200:
            ebay_prod_description = 'Too long'
        else:
            ebay_prod_description = get_textfrom_html(ebay_prod_description)

        warranty     = detect_warranty(ebay_subtitle, ebay_prod_description)

        ebay_vendor_notes= get_ebay_vendor_notes(ebay_prod_specs)

        detected_color = color_detector(ebay_title)
        #cash converters includes color in specs
        if ebay_vendor_name == 'cashconverters_es':
            detected_color = color_detector(ebay_prod_specs)
        
        # ebay_vendor_notes= 'test'



# with open(INPUT_FILE, encoding='utf-8') as csv_file:
# filtered_list = []
# with open(INPUT_FILE, encoding='ISO-8859-1') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     next(reader) # 1º 
#     next(reader) #and 2º rows
#     for row in reader:
        
#         # print(row)
   
#         #READING CSV ROW COLUMNS
#         variable_prod =   row[EBAY_VARIABLE_PROD_NAME]
#         seller_votes= row[EBAY_SELLER_VOTES_NAME]
#         seller_votes = int(seller_votes)
#         payment_methods = row[EBAY_PAYMENT_NAME]
#         prod_state =      row[EBAY_PROD_STATE_NAME]
#         # sold_out_text =   str(row[EBAY_PROD_SOLD_OUT_NAME])
#         sold_out_text =   row[EBAY_PROD_SOLD_OUT_NAME]
#         ebay_price =      row[EBAY_PRICE_NAME]
#         ebay_shipping_price =  row[EBAY_SHIPPING_PRICE]
#         area_served =     row[EBAY_SERVED_AREA_NAME]
#         target_category = row[TARGET_CATEGORY_NAME]
#         target_attr_1 =   row[TARGET_ATTR_1_NAME]
#         target_attr_2 =   row[TARGET_ATTR_2_NAME]
#         ebay_pics     =   row[EBAY_PICS_URLS]

#         #not included yet DELETE THIS COMMENT WHEN DONE
#         ebay_vendor_name   =row[EBAY_VENDOR_NAME]
#         ebay_reviews       =row[EBAY_REVIEWS_NAME]
#         ebay_import_taxes  =row[EBAY_IMPORT_TAXES_NAME]
#         target_model       =row[TARGET_MODEL_NAME]
#         target_prod_state  =row[TARGET_PROD_STATE]
        
#         #variables need to filter:
#         ebay_title =           row[EBAY_TITLE_NAME]
#         # price =           row[]
#         query =           row[EBAY_QUERY_NAME]
#         ebay_shipping_time = row[EBAY_SHIPPING_TIME]
#         ebay_returns =    row[EBAY_RETURNS_NAME]
#         ebay_prod_id =    row[EBAY_ID_NAME]
#         ebay_prod_url =   row[EBAY_PROD_URL_NAME]
#         ebay_category =   row[EBAY_CATEGORY_NAME]
#         ebay_prod_specs = row[EBAY_PROD_SPECS_NAME]
#         # ebay_prod_description = row[EBAY_PROD_DESCRIPTION_NAME]

#         #1º use the specs_list to find vendor_notes inside, then convert prod_specs to a str to save it in excel
#         # ebay_vendor_notes= get_ebay_vendor_notes(ebay_prod_specs)
#         ebay_vendor_notes= 'test'

#         #excel can't save a list, convert to str
#         ebay_prod_specs = str(ebay_prod_specs)


        # later to re-convert to string use:
        # take the string from the excel: excel_string = ws.cell(row=1, column=1).value
        #list_again = excel_string.replace(']','').split('[')
        
        # print(
        #     'variable_prod :',      variable_prod,
        #     'seller_votes :', seller_votes,
        #     'payment_methods :',    payment_methods,
        #     'prod_state :',         prod_state,
        #     'sold_out_text :',      sold_out_text,
        #     'ebay_price :',         ebay_price,
        #     'ebay_shipping_price :',ebay_shipping_price,
        #     'area_served :',        area_served,
        #     'target_category :',    target_category,
        # )
        
        #this is the filter, only prods that meet the requierments can pass through
        if variable_prod != None: #avoid product if it's a variable prod
            # print("this item is variable",item['title'])
            continue
        elif  seller_votes < 30: #if very little sells
            # print('not enough votes',item['title'])
            continue
        elif 'PayPal' not in payment_methods:
            # print('not payment',item['title'])
            continue
        elif 'Visa' not in payment_methods:
            # print('not payment',item['title'])
            continue
        elif 'Para desguace' in prod_state: #if the prod is broken
            # print('broken item',item['title'])
            continue
        elif '[]' not in sold_out_text : # if the product is NOT sold out it's an empty list
            # print('prod sold out',item['title'])
            continue
        elif ebay_price == '':
            # print('no price',item['title'])
            continue
        elif ebay_shipping_price == '':
            # print('not shipping price ',item['title'])
            continue
        elif 'Solo recogida local' in area_served:
            # print('only local pick up no shipping prod: ',item['title'])
            continue

        #apply re_price function
        #clean price and convert to float
        #in the case of a price with comma like "1.102,95 EUR"
        if ('.') in ebay_price and (',') in ebay_price: 
            # print("detected!!!", ebay_price)
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
            print(f'this ebaby id has shipping {ebay_prod_id}')
            pass
        try:
            if 'Rápido y gratis' in ebay_shipping_price:
                ebay_shipping_price = 0                
        except Exception as e:
            #print(e)
            pass
        try:
            if 'gratis' in ebay_shipping_price.lower():
                ebay_shipping_price = 0
        except:
            pass
        
        ################################### this goes here
        
        ebay_total_price = ebay_price + ebay_shipping_price
        wp_price = apply_wp_price(ebay_total_price)

        #check if there're pictures for this prod in pics_db
        pictures = check_pics_db(target_model, target_attr_2)
        # if any pic in pics_db, use ebay's pictures
        if pictures == 'there aren\'t any pics in pics_db for this item':
            logging.info(f'there aren\'t any pics in pics_db for this item <{target_model} {target_attr_2}>')
            print(f'going to search this ebay_id {ebay_prod_id}')
            pictures = make_ebay_pics_urls(ebay_pics)
            # pictures = get_ebay_pictures(ebay_prod_id)# through api
        
        #to avoid error can't convert to excel, convert from list to string
        pics_string = ''
        for pic in pictures:
            pic = str(pic)
            pics_string += pic
            pics_string += ','
        # print(f'this is the string_pics {pics_string}')
        pictures = pics_string

        wp_shipping_time = get_wp_shipping_time(ebay_shipping_time)

        #apply our category based on Ebay's category
        # prod_db_category = apply_category(ebay_category)
        # prod_brand = apply_prod_brand(ebay_title)

        #print("there are products with wanted characteristics!!")
        data_to_dump = {
            'query':query,
            'ebay_title':ebay_title,
            'prod_state':prod_state,
            # 'prod_db_category':prod_db_category,
            # 'brand_prod_filter':prod_brand,
            'ebay_price':ebay_price,
            'ebay_shipping_price':ebay_shipping_price,
            'ebay_shipping_time':ebay_shipping_time,
            'ebay_returns':ebay_returns,
            'ebay_prod_id':ebay_prod_id,
            'ebay_prod_url':ebay_prod_url,
            'ebay_category':ebay_category,
            'ebay_prod_specs':ebay_prod_specs,
            'ebay_prod_description':ebay_prod_description,
            'wp_price':wp_price,
            'pictures':pictures,
            'wp_shipping_time':wp_shipping_time,
            'target_category':target_category,
            'target_attr_1':target_attr_1,
            'target_attr_2':target_attr_2,
            'ebay_total_price':ebay_total_price,
            'ebay_vendor_notes':ebay_vendor_notes,
            'target_prod_state':target_prod_state,
            'seller_votes':seller_votes,
            'detected_color':detected_color,
            'warranty':warranty,
            'available_colors':available_colors
        }

        filtered_list.append(data_to_dump)
        #variables I don't need in filtered csv
        #'payment_methods':payment_methods, sold_out_text,'seller_votes':seller_votes,
        #area_served,'var_prod':variable_prod

        # with open('filter_output.json','w',) as new_file: #,encoding='utf8')
            # json.dump(entry, new_file, indent=4)
            # # new_file.write(",")
            # # new_file.close()


        write_to_excel(data_to_dump, OUTPUT_FILE)
        print('written to excel')

################################
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
