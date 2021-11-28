# from ebaysdk.finding import Connection
# from ebaysdk.shopping import Connection as Shopping
# from openpyxl import load_workbook

# FILTER_OUTPUT_PATH =r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\FILTER_OUTPUT.xlsx"
# LOGS_FOLDER        =r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\logs_folder"

# def copy_move_file(src_dir, dst_dir, mode='time'):
#     '''file_name, src_dir, dst_dir, mode=time or no_time // absolute paths'''
#     #if mode=time -> include time on file title, elif normal -> not include time
#     import os
#     import shutil
#     import datetime

#     #detect file_name and file_format
#     file = src_dir.split('\\')[-1]
#     file_name = file.split('.')[0]
#     file_format = file.split('.')[1]
#     file_format = '.' + file_format

#     #create time id to rename the file
#     now = str(datetime.datetime.now())[:16]
#     now = now.replace(' ', '_')
#     now = now.replace(':', '-')

#     #include time or not based on specified mode
#     if mode == 'time':
#         abs_path = file_name + str(now) + file_format
#     elif mode == 'no_time':
#         abs_path = file_name + file_format

#     dst_path = dst_dir + '\\' + abs_path

#     shutil.copy(src_dir, dst_path)
#     print(f'file {file} moved to {dst_path}')

# def clean_excel(EXCEL_FILE):
#     from openpyxl import load_workbook
#     import logging

#     wb = load_workbook(EXCEL_FILE)
#     ws = wb.active

#     #starting at 2, delete all rows
#     ws.delete_rows(2, ws.max_row+1)
#     wb.save(EXCEL_FILE)

#     logging.info(f'cleaned set_prod_db  and gaps_file to begin fresh writing')

# copy_move_file(FILTER_OUTPUT_PATH, LOGS_FOLDER)
# clean_excel(FILTER_OUTPUT_PATH)


deepl_auth_key = 'ea826f71-83b5-f5aa-231f-aad69f95aec2:fx'
import deepl
text = 'Der Endverbraucher ist verpflichtet Batterien ordnungsgemäß bei keiner Verwendung mehr zu entsorgen. Denn Batterien gehören nicht in den Hausmüll! Gerne helfen wir Ihnen bei Informationen zu Standorten in Ihrer Nähe. Detaillierte Informationen finden Sie in unseren AGB."'
target_language = 'ES'
translator = deepl.Translator(deepl_auth_key) 
result = translator.translate_text(text, target_lang=target_language) 
translated_text = result.text
print(translated_text)

# api = Connection(appid='VadymKoz-find-PRD-0a5a8fca7-7fbfe1d0', config_file=None)
# api = Connection(config_file='ebay.yaml')
# response = api.execute('findItemsAdvanced', {'keywords': 'legos'})
# print(response)


# ebay_prod_id = 114974576186
# # api = Shopping(config_file='ebay.yaml')
# api = Shopping(appid='VadymKoz-find-PRD-0a5a8fca7-7fbfe1d0', config_file=None)
# request = {'ItemID':ebay_prod_id}
# response = api.execute('GetSingleItem', request)
# print(response)

# api = Shopping(config_file='ebay.yaml')
# response = api.execute('FindPopularItems', {'QueryKeywords': 'Python'})
# print(response.dict())


# id="icImg"
# class="img img500 vi-img-gallery-vertical-align "

# from requests_html import HTMLSession
# session = HTMLSession()
# r = session.get('https://i.ebayimg.com/images/g/70QAAOSwz29hHOKL/')
# print(r.text)