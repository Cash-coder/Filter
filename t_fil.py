import random
import json 


INPUT_FILE = r"crawler_output.json"

# print(get_wp_shipping_time(t))

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


def nlp_translate(text, target_language='es'):
    import requests
    import authentications #py file

    translate_api_key = authentications.RapidAPI_Key

    url = "https://nlp-translation.p.rapidapi.com/v1/translate"

    # querystring = {"text":t,"to":"es","from":"de"}
    querystring = {"text":text, "to":target_language}

    headers = {
        "X-RapidAPI-Host": "nlp-translation.p.rapidapi.com",
        "X-RapidAPI-Key": translate_api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    origin_language = response['from']
    translated_text = response['translated_text']['es']

    return translated_text, origin_language

def translate_specs(specs):
    
    # remove some parts we don't want, like "El articulo puede mostrar un deterioro"
    # a part of the text is spanish already
    # if you put into the translator it interprets it like spanish, so it won't translate
    # split the not_spanish part with \n
    # join in a string
    # translate
    # combine again translated with spanish
    # add the phrase "Texto traducido automáticamente desde el Alemán:"

    specs = specs.replace(' El artículo puede mostrar un deterioro ... ', '').replace('(en caso de ... ','')

    phrase_to_add_german  = "Texto traducido automáticamente del Alemán:\n\n"
    phrase_to_add_italian = "Texto traducido automáticamente del Italiano:\n\n"
    phrase_to_add_english = "Texto traducido automáticamente del Inglés:\n\n"
    phrase_to_add_french  = "Texto traducido automáticamente del Francés:\n\n"
    
    if 'Estado: ' in specs:
        splitted = specs.split('\n')
        text_to_translate    = splitted[2:]
        already_spanish_text = splitted[:1]

        joined_to_translate = "\n".join(text_to_translate)
        joined_spanish      = "\n".join(already_spanish_text)

        r = nlp_translate(joined_to_translate)
    else:
        r = nlp_translate(specs)


    translated, origin_lan = r
    # print(translated) 

    # avoid error 'joined_spanish' doesn't exist
    if 'joined_spanish' not in locals():
        joined_spanish = '' 

    if origin_lan   == 'en':
        combined = phrase_to_add_english + joined_spanish + "\n" + translated
    elif origin_lan == 'fr':
        combined = phrase_to_add_french + joined_spanish + "\n" + translated
    elif origin_lan == 'de':
        combined = phrase_to_add_german + joined_spanish + "\n" + translated
    elif origin_lan == 'it':
        # print(f'it: {joined_spanish}\n{translated}')
        combined = phrase_to_add_italian + joined_spanish + "\n" + translated
        # combined = phrase_to_add_italian + "\n" + translated
        print(combined)
    
    else: #for spanish 'es' and other languages
        combined = joined_spanish + translated
    # print(combined)
    
    return combined


t = """Marca: APPLE\nModello: Leggi Scheda Tecnica in Descrizione\nCapacità di memorizzazione: Leggi Scheda Tecnica in Descrizione\nDimensioni schermo: Leggi Scheda Tecnica in Descrizione\nMemoria RAM: Leggi Scheda Tecnica in Descrizione\nSistema operativo: Leggi Scheda Tecnica in Descrizione\nCaratteristiche: Leggi Scheda Tecnica in Descrizione\nNumero modello: Leggi Scheda Tecnica in Descrizione\nOperatore: Leggi Scheda Tecnica in Descrizione\nSlot scheda SIM: Leggi Scheda Tecnica in Descrizione\nTipo di scheda di memoria: Leggi Scheda Tecnica in Descrizione\nProcessore: Leggi Scheda Tecnica in Descrizione\nStato di blocco: Libero, può usare qualsiasi SIM\nFrequenza cellulare: Leggi Scheda Tecnica in Descrizione\nRisoluzione fotocamera: Leggi Scheda Tecnica in Descrizione\nMPN: Leggi Scheda Tecnica in Descrizione\nConnettività: Leggi Scheda Tecnica in Descrizione\nPaese di fabbricazione: Italia\nStile: Leggi Scheda Tecnica in Descrizione\nModello Chipset: Leggi Scheda Tecnica in Descrizione\nContratto: Nessuno\nGaranzia produttore: 3 mesi\nColore: Non applicabile"""

translate_specs(t)

###############
# def write_response(r, n, data_row):

#     with open(INPUT_FILE, encoding='utf8') as f:
#         data = json.load(f)

#         splitted = r.split('[/]')
#         # print(f'r: {r}\nsplitted: {splitted}')

#         # reverse the list, avoid the last (empty) item
#         splitted = splitted[:-1]
#         for item in splitted[::-1]:
#             n -= 1
#             data[n][data_row] = item #.replace('[/]','')
#             print(f'written row {n}: item:{item[:35]}')
    
#     with open(INPUT_FILE, 'w',encoding='utf8') as f:
#         json.dump(data, f, indent=4)


# def combined_translation():

#     with open(INPUT_FILE, encoding='utf8') as f:
#         data = json.load(f)

#     resto = ''
#     combined_str = ""
#     n = 0
    
#     l = [EBAY_SUBTITLE, EBAY_PROD_SPECS_NAME, EBAY_TITLE_NAME]
#     data_row = EBAY_PROD_SPECS_NAME

#     for prod in data:
#         text = prod[data_row] 
#         text = str(text)

#         if resto != '':
#             combined_str += resto
#             resto = ''

#         if len(text) + len(combined_str) < 5000:
#             text += '[/]'
#             combined_str += text
#             n += 1
    
#         else:
#             r = nlp_translate(combined_str)
#             write_response(r, n, data_row)
#             n += 1
#             combined_str = ''
#             resto = text
            
#         # if the last grup is 2000 characters, but there no more later
#         # n+1 because json starts from 0 but len() starts from 1
#         if n == len(data): 
#             #avoid double activation 
#             if combined_str != '':
#                 r = nlp_translate(combined_str)
#                 write_response(r, n, data_row)


# # copy_file()
# # combined_translation()

# # t = '''"Marca: APPLE\nModello: Leggi Scheda Tecnica in Descrizione\nCapacità di memorizzazione: Leggi Scheda Tecnica in Descrizione\nDimensioni schermo: Leggi Scheda Tecnica in Descrizione\nMemoria RAM: Leggi Scheda Tecnica in Descrizione\nSistema operativo: Leggi Scheda Tecnica in Descrizione\nCaratteristiche: Leggi Scheda Tecnica in Descrizione\nNumero modello: Leggi Scheda Tecnica in Descrizione\nOperatore: Leggi Scheda Tecnica in Descrizione\nSlot scheda SIM: Leggi Scheda Tecnica in Descrizione\nTipo di scheda di memoria: Leggi Scheda Tecnica in Descrizione\nProcessore: Leggi Scheda Tecnica in Descrizione\nStato di blocco: Libero, può usare qualsiasi SIM\nFrequenza cellulare: Leggi Scheda Tecnica in Descrizione\nRisoluzione fotocamera: Leggi Scheda Tecnica in Descrizione\nMPN: Leggi Scheda Tecnica in Descrizione\nConnettività: Leggi Scheda Tecnica in Descrizione\nPaese di fabbricazione: Italia\nStile: Leggi Scheda Tecnica in Descrizione\nModello Chipset: Leggi Scheda Tecnica in Descrizione\nContratto: Nessuno\nGaranzia produttore: 3 mesi\nColore: Non applicabile"'''
# # e = "42384728374 asnkansd 1i23"
# # a,b = nlp_translate(e)
# # print(a,'\n',b)
