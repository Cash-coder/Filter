import sys
import random
import json


# INPUT_FILE = r"crawler_output.json"
INPUT_FILE     = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.json"


# with open(INPUT_FILE, encoding='utf8') as json_file:
#     scrapper_data = json.load(json_file)

#     for item in scrapper_data:
#         ebay_id = item['ebay_article_id']
#         # print(ebay_id)

#         if ebay_id == '275310573205':
#             shipping = item['shipping_price']
#             print(shipping)

def set_tolerance(input_price):
    
    if input_price < 200:
        tolerance = 0.18
    elif input_price < 400:
        tolerance = 0.12
    elif input_price < 600:
        tolerance = 0.10
    elif input_price < 800:
        tolerance = 0.10
    elif input_price < 1000:
        tolerance = 0.07
    else: 
        tolerance = 0.05
   
    
    return tolerance

p = [150, 240, 280, 350,380,400,450,500,550,600,650,750,800,900,1000,1050, 1100,1150, 1200,1250, 1300, 1350,1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 2500]
for price in p:
    tolerance = set_tolerance(price)
    price_with_tolerance = price + (price * tolerance)
    print(price, '    ',price_with_tolerance)






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

