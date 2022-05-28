# import json
# from filter import TARGET_MODEL_NAME, EBAY_PRICE_NAME, EBAY_SHIPPING_PRICE, EBAY_IMPORT_TAXES_NAME, TARGET_ATTR_1_NAME, EBAY_ID_NAME
# from filter import process_shipping_price

def substitute(items_list, old_title, alternative_phrase):
    try:
        for item in items_list:
            if item in old_title:
                new_title = old_title.replace(item, alternative_phrase)
                print(f'asdasd {new_title}')
                return new_title
        return old_title
    except Exception as e:
        return old_title

def clean_title(ebay_title):
    
    title = ebay_title.lower()
    
    # items to delete
    terms_to_remove = ['sin cara id', 'manzana','iva incl.', 'incl. iva', '(gsm)', 'gsm', 'at&t', 'at&amp;t', 'feria', 'cdma', '()']
    title = remove_from_title(terms_to_remove, title)

    print(f'title remove {title}')
    
    #excelente estado
    l = ['a-ware', 'a (grado)', 'grado a']
    alt_phrase = 'estado excelente'
    title1 = substitute(l, title, alt_phrase)
    # avoid weird error that makes title = None
    
    # if not _title:
        # print('wtf')
        # _title = title
    # else:
        # title = _title
    
    print(f'title excele {title1}')

    # muy buen estado
    l = ['muy bien', 'muy bueno']
    alt_phrase = 'muy buen estado'
    title2 = substitute(l, title1, alt_phrase)
    # if not _title:
        # _title = title
    # else:
        # title = _title
    
    print(f'title muy buen {title2}')

    #estado aceptable
    l = ['b-ware', 'grado b', 'grado a/b', ' b ', 'akzeptabel']
    alt_phrase = 'estado aceptable'
    title3 = substitute(l, title2, alt_phrase)
    # if not _title:
        # _title = title
    # else:
        # title = _title
    
    print(f'title aceptable {title3}')

    # desbloqueado
    l = ['sin simlock', 'sin sim-lock', 'désimlocké', 'sin carrier']
    alt_phrase = 'desbloqueado'
    title4 = substitute(l, title3, alt_phrase)
    # if not _title:
    #     _title = title
    # else:
    #     title = _title
    
    return title4


title = 'telefono nuevo a-ware sin simlock'
title = clean_title(title)

# def f(title):
#     try:
#         title = title + 1
#     except:
#         print(title)
#         return title

# title = f('asdasdasd')
# title = f('as')


# INPUT_FILE   = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.json"
# INPUT_FILE_C2  = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output_C2.json"

# def process_price(price):
#     import funcs_currency

#     # sometimes price comes this way "USD580" being 580 the price
#     try:
#         if 'USD' in price:
#             price = price.replace('USD', '')
#             price = funcs_currency.convert_amount_toEUR(int(price), 'USD')
#     except TypeError:
#         pass
#     except Exception as e:
#         print(e)

#     price = price.split(',')[0]
#     price = price.replace('.', '') #like 1.256,44$
#     price = int(price)

   
#     return price


# with open(INPUT_FILE, encoding='utf8') as json_file:
#     scrapper_data = json.load(json_file)

#     prods_to_filter_price_by_median = []
#     for item in scrapper_data:  
#         # print(i)
        
#         # variables to filter:
#         price   = item[EBAY_PRICE_NAME]
#         ebay_id = item[EBAY_ID_NAME]
#         model   = item[TARGET_MODEL_NAME]
#         shipping_price = item[EBAY_SHIPPING_PRICE]
#         query_attr     = item[TARGET_ATTR_1_NAME]
#         import_taxes   = item[EBAY_IMPORT_TAXES_NAME]
        
#         price = process_price(price)
#         if 'local pick up' in shipping_price:
#             continue
#         shipping_price = process_shipping_price(shipping_price)
#         if shipping_price == 'error processing shipping price':
#             print(f'shipping price error with ebay_id: {ebay_id}')

#         if import_taxes:
#             tax_price = process_import_taxes(import_taxes)
#             price += tax_price
#         if shipping_price:
#             # print(price, shipping_price)
#             price += shipping_price
        
#         # from "iphone 12" to "iphone 12 256" (GB)
#         model += f' {query_attr}'
#         # check if model is already in prods_to_filter.., return False or IndexNumber
#         r_index = check_if_model_is_present(model, prods_to_filter_price_by_median)
#         # returned False = no entry -> create entry
#         if r_index:
#             r_index = int(r_index)
#             update_entry(r_index, price, prods_to_filter_price_by_median)
#         else:
#             create_entry(model, price, prods_to_filter_price_by_median)

# # for each item in list, get the median price from item's prices list
# for item in prods_to_filter_price_by_median:
#     prices_list = item.get('prices')

#     median_low = statistics.median_low(prices_list)
#     item['median_low'] = median_low
    
#     # median_high = statistics.median_high(prices_list)
#     # item['median_high'] =  median_high
#     # remove prices list, memory efficient
#     del item['prices']

# [print(item) for item in prods_to_filter_price_by_median]

# return prods_to_filter_price_by_median



##########################
# # filter output 1 xlsx
# EBAY_TITLE_COL      = 4
# SUBTITLE_COL        = 11
# EBAY_PROD_SPECS_COL = 25

# EBAY_SUBTITLE        = 'subtitle'
# EBAY_PROD_SPECS_NAME = 'prod_specs'
# EBAY_TITLE_NAME      = 'title'

# def copy_file():
#     import shutil
#     shutil.copy('crawler_output - Copy.json', 'crawler_output.json' )

# #########################
# def nlp_translate(text, target_language='es'):
#     import requests
#     import authentications #py file

#     translate_api_key = authentications.RapidAPI_Key

#     url = "https://nlp-translation.p.rapidapi.com/v1/translate"

#     # querystring = {"text":t,"to":"es","from":"de"}
#     querystring = {"text":text, "to":target_language}

#     headers = {
#         "X-RapidAPI-Host": "nlp-translation.p.rapidapi.com",
#         "X-RapidAPI-Key": translate_api_key
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring).json()
#     origin_language = response['from']
#     translated_text = response['translated_text']['es']

#     return translated_text, origin_language

# def translate_specs(specs):
    
#     # remove some parts we don't want, like "El articulo puede mostrar un deterioro"
#     # a part of the text is spanish already
#     # if you put into the translator it interprets it like spanish, so it won't translate
#     # split the not_spanish part with \n
#     # join in a string
#     # translate
#     # combine again translated with spanish
#     # add the phrase "Texto traducido automáticamente desde el Alemán:"

#     specs = specs.replace(' El artículo puede mostrar un deterioro ... ', '').replace('(en caso de ... ','')

#     phrase_to_add_german  = "Texto traducido automáticamente del Alemán:\n\n"
#     phrase_to_add_italian = "Texto traducido automáticamente del Italiano:\n\n"
#     phrase_to_add_english = "Texto traducido automáticamente del Inglés:\n\n"
#     phrase_to_add_french  = "Texto traducido automáticamente del Francés:\n\n"
    
#     if 'Estado: ' in specs:
#         splitted = specs.split('\n')
#         text_to_translate    = splitted[2:]
#         already_spanish_text = splitted[:1]

#         joined_to_translate = "\n".join(text_to_translate)
#         joined_spanish      = "\n".join(already_spanish_text)

#         r = nlp_translate(joined_to_translate)
#     else:
#         r = nlp_translate(specs)


#     translated, origin_lan = r
#     # print(translated) 

#     # avoid error 'joined_spanish' doesn't exist
#     if 'joined_spanish' not in locals():
#         joined_spanish = '' 

#     if origin_lan   == 'en':
#         combined = phrase_to_add_english + joined_spanish + "\n" + translated
#     elif origin_lan == 'fr':
#         combined = phrase_to_add_french + joined_spanish + "\n" + translated
#     elif origin_lan == 'de':
#         combined = phrase_to_add_german + joined_spanish + "\n" + translated
#     elif origin_lan == 'it':
#         # print(f'it: {joined_spanish}\n{translated}')
#         combined = phrase_to_add_italian + joined_spanish + "\n" + translated
#         # combined = phrase_to_add_italian + "\n" + translated
#         print(combined)
    
#     else: #for spanish 'es' and other languages
#         combined = joined_spanish + translated
#     # print(combined)
    
#     return combined

# t = """Marca: APPLE\nModello: Leggi Scheda Tecnica in Descrizione\nCapacità di memorizzazione: Leggi Scheda Tecnica in Descrizione\nDimensioni schermo: Leggi Scheda Tecnica in Descrizione\nMemoria RAM: Leggi Scheda Tecnica in Descrizione\nSistema operativo: Leggi Scheda Tecnica in Descrizione\nCaratteristiche: Leggi Scheda Tecnica in Descrizione\nNumero modello: Leggi Scheda Tecnica in Descrizione\nOperatore: Leggi Scheda Tecnica in Descrizione\nSlot scheda SIM: Leggi Scheda Tecnica in Descrizione\nTipo di scheda di memoria: Leggi Scheda Tecnica in Descrizione\nProcessore: Leggi Scheda Tecnica in Descrizione\nStato di blocco: Libero, può usare qualsiasi SIM\nFrequenza cellulare: Leggi Scheda Tecnica in Descrizione\nRisoluzione fotocamera: Leggi Scheda Tecnica in Descrizione\nMPN: Leggi Scheda Tecnica in Descrizione\nConnettività: Leggi Scheda Tecnica in Descrizione\nPaese di fabbricazione: Italia\nStile: Leggi Scheda Tecnica in Descrizione\nModello Chipset: Leggi Scheda Tecnica in Descrizione\nContratto: Nessuno\nGaranzia produttore: 3 mesi\nColore: Non applicabile"""

# import statistics
# import pandas as pd

# l = [num for num in range(0, 1000)]

# def f():
#     il = []
#     for i,item in enumerate(l):
#         if item > 500:
#             il.append(item)
#     return il

# i = f()
# for item in l[]:
#     print(item)

# data = pd.Series(l)
# print(data.describe())
# print('\n')
# a = data.describe()['25%']
# print(a)

# print(l)
# median_low  = statistics.median_low(l)
# median      = statistics.median(l)
# median_high = statistics.median_high(l)
# print(f'{median_low},   {median},   {median_high}')


