
JSON_FILE = 'new.json'
# JSON_FILE = 'short_scrapper_output.json'
EXCEL_FILE = 'scrapper_output.xlsx'

def json_to_excel(json_file, excel_file='json_to_excel.xlsx'):
    import pandas
    pandas.read_json(json_file).to_excel(excel_file)

json_to_excel(JSON_FILE, EXCEL_FILE)
