import traceback
import pandas as pd
import json
import funcs_currency
# import names used in json input file
from filter import TARGET_MODEL_NAME, EBAY_PRICE_NAME, EBAY_SHIPPING_PRICE, EBAY_IMPORT_TAXES_NAME, TARGET_ATTR_1_NAME, EBAY_ID_NAME, EBAY_TITLE_NAME, EBAY_PROD_STATE_NAME, EBAY_PROD_DESCRIPTION_NAME, EBAY_SUBTITLE
from filter import process_shipping_price


INPUT_FILE   = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.json"
INPUT_FILE_C2  = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output_C2.json"


# ALL THIS IN ANOTHER FILE (median_lower_price_filter.py), BUT IMPORTED AS FUNCTIONS AND EXECUTED HERE
# fitler by median_low()
#   create list of dicts: prods_to_filter_price_by_median {prod: [prices list]}
#   for prod in data: 
        # create final_price with price + shipping + import_taxes
#       if prod exist in prods_to_filter.., add price, else create entry
# for prod in prods_to_filter...
    #get the median_low
    # add median low [{prod, price_list, median_low}]
# create a new list filtering prices by median low
# for prod in prods_to_filter..
    # if prod_price > median_low: continue
    # else: append to prods_filtered_by_median_low
# return list


def process_import_taxes(import_taxes):
    if '£' in import_taxes:
        amount = import_taxes.replace('£','')
        import_taxes = funcs_currency.convert_amount_toEUR(amount, 'GBP')
    elif 'US $' in import_taxes:
        amount = import_taxes.replace('US $','')
        import_taxes = funcs_currency.convert_amount_toEUR(amount, 'USD')
    else:
        import_taxes = 0

    return int(import_taxes)


def check_if_model_is_present(model, prods_to_filter_price_by_median):
    for index, item in enumerate(prods_to_filter_price_by_median):
        item_model = item.get('model')
        if model == item_model:
            return str(index) # return string because if index == 0 == False == dones't work
    
    # if no matches
    return False


def update_entry(index, new_price, prices_list):
    prices = prices_list[index]['prices']
    prices.append(new_price)

def create_entry(model, price, prods_to_filter_price_by_median ):
    entry = {'model':model, 'prices':[price]}
    prods_to_filter_price_by_median.append(entry)

def process_price(price):
    import funcs_currency

    # sometimes price comes this way "USD580" being 580 the price
    try:
        if 'USD' in price:
            price = price.replace('USD', '')
            price = funcs_currency.convert_amount_toEUR(int(price), 'USD')
    except TypeError:
        pass
    except Exception as e:
        print(e)

    price = price.split(',')[0]
    price = price.replace('.', '') #like 1.256,44$
    price = int(price)

    return price

# used in filter.py
def filter_median_high_price(model_attr, price, median_price_list):
    price = int(price)

    for item in median_price_list:
        model = item.get('model')
        if model_attr == model:
            # median_high = item.get('median_high')
            bottom_30_percent = item.get('bottom_percent')
            bottom_30_percent = int(bottom_30_percent)

            # admit some tolerance for the low prices
            # tolerance_percentage = set_tolerance(price)
            # median_low_price_with_tolerance = median_low + (price * tolerance_percentage)

            print(f'ebay_model_attr: {model_attr}, median_model_attr:{model}\nprice {price} bottom_30_percent:{bottom_30_percent}')
            # if price_with_tolerance < median_high:
            if price < bottom_30_percent:
                # print(f'ACCEPTED price {price} median_high {median_high}')
                print(f'ACCEPTED price {price} median_low_tolerance {bottom_30_percent}')
                return True
            else:
                print(f'FALSE not accepted price {price} median_low {bottom_30_percent}')
                return False

def set_tolerance(input_price):
    
    if input_price < 200:
        tolerance = 0.15
    elif input_price < 400:
        tolerance = 0.10
    elif input_price < 600:
        tolerance = 0.08
    elif input_price < 800:
        tolerance = 0.065
    elif input_price < 1000:
        tolerance = 0.06
    else: 
        tolerance = 0.05
    
    return tolerance

def check_defective_prod(ebay_title, prod_state, item_description, subtitle):
    try:

        ebay_title_lower = ebay_title.lower()
        
        #check if bad prod_state
        if 'Para desguace' in prod_state: 
            print(f'broken item {ebay_title, prod_state}')
            return True

        # check bad stuff in title
        # items grade d considered bad state
        bad_stuff_signs = [
            'repuesto', 'pantalla rota', 'roto', 'pantalla rajada', 'pantalla dañada', 'daños', 'desmontaje'
            'placa madre', 'placa base', 'tarjeta madre', 'motherboard',  'logic card', 'placa lógica', 'defectuoso', 'defectuosa',
            ' bad', 'piezas','mal estado',' bloqueado',' locked', 'cracked back glass', 'agrietado espalda',
            'leer descripción', 'por favor leer', 'incompleto', 'destrozada', 'destrozado' , ' bloqueo icloud',
            'sin cámara trasera', 'grado d', ' d ', 'no funciona', 'agrietado', 'caja vacía', 'desmontaje',
            # airpods
            'sólo', 'solo lado', 'sólo lado','solamente', 'izquierdo' ,'izquierda', 'derecho', 'reemplazo', 'caso sólo'
            # macbooks | para macbook
            'montaje', 'ensamblaje', 'para', 'reposamanos', 'reposamuñecas', 'pantalla completa', 'pieza original', 'conjunto de pantalla', 'conjunto pantalla', 'pantalla conjunto'
            'barra superior', 'topcase', 'top case'
            ]
        
         # o2,xfinity, t-mobile are phone carriers
        carriers = ['o2', 'xfinity' , 't-mobile', 'at&amp;t', 'verizon', 'cricket','sprint']

        # title bad signs 
        r = _check(bad_stuff_signs, ebay_title_lower)
        if r: 
            return True
        # title carriers 
        r = _check(carriers, ebay_title_lower)
        if r: 
            return True


        # for sign in bad_stuff_signs:
        #     if sign in ebay_title_lower:
        #         print(f'broken item {ebay_title, prod_state}')
        #         return True

        # check bad stuff in description
        r = _check(bad_stuff_signs, item_description)
        if r: 
            return True
        
        # subtitle bad_signs 
        if subtitle:
            r = _check(bad_stuff_signs, subtitle)
            if r: 
                return True
        # subtitle carriers
        if subtitle:
            r = _check(carriers, subtitle)
            if r: 
                return True


    except Exception as e:
        print(e)       
        traceback.print_exc()
        
        return True # if filter fails, avoid this prod

def _check(items_list, text):
    text = text.lower()

    for item in items_list:
        if item in text:
            print(f'found bad sign: {item} in text: {text}')
            return True
    

def run(selected_input_file):

    with open(selected_input_file, encoding='utf8') as json_file:
        scrapper_data = json.load(json_file)

        prods_to_filter_price_by_median = []
        for item in scrapper_data:  
            
            # variables to filter:
            price       = item[EBAY_PRICE_NAME]
            ebay_id     = item[EBAY_ID_NAME]
            model       = item[TARGET_MODEL_NAME]
            ebay_title  = item[EBAY_TITLE_NAME]
            subtitle    = item[EBAY_SUBTITLE]
            query_attr  = item[TARGET_ATTR_1_NAME]
            import_taxes     = item[EBAY_IMPORT_TAXES_NAME]
            prod_state       = item[EBAY_PROD_STATE_NAME]
            shipping_price   = item[EBAY_SHIPPING_PRICE]
            prod_description = item[EBAY_PROD_DESCRIPTION_NAME]
            prod_description = "\n".join(prod_description)

            is_defective = check_defective_prod(ebay_title, prod_state, prod_description, subtitle)
            
            if is_defective:
                #delete_item ?
                # enumerate add index to list, in filter.py remove all indexes from json
                continue

            # avoid prods from australia
            if 'AUD' in price:
                continue

            price = process_price(price)
            
            if 'local pick up' in shipping_price:
                continue
            shipping_price = process_shipping_price(shipping_price)
            if shipping_price == 'error processing shipping price':
                print(f'shipping price error with ebay_id: {ebay_id}')

            if import_taxes:
                tax_price = process_import_taxes(import_taxes)
                price += tax_price
            if shipping_price:
                # print(price, shipping_price)
                price += shipping_price
            
            # from "iphone 12" to "iphone 12 256" (GB)
            model += f' {query_attr}'
            # check if model is already in prods_to_filter.., return False or IndexNumber
            r_index = check_if_model_is_present(model, prods_to_filter_price_by_median)
            # returned False = no entry -> create entry
            if r_index:
                r_index = int(r_index)
                update_entry(r_index, price, prods_to_filter_price_by_median)
            else:
                create_entry(model, price, prods_to_filter_price_by_median)
            

    # for each item in list, get the median price from item's prices list
    for item in prods_to_filter_price_by_median:
        prices_list = item.get('prices')

        # median_low = statistics.median_low(prices_list)
        
        # get the bottom 25% of prices
        pd_serialization = pd.Series(prices_list)
        bottom_25_percentage = pd_serialization.describe()['25%']

        # get the 5% of prices and sum to 25 to get 30% or prices
        _10_percent = sum(prices_list) / len(prices_list) * 0.1
        bottom_35_percent = bottom_25_percentage + _10_percent

        item['bottom_percent'] = bottom_35_percent
        
        del item['prices']

    # print model_attr, bottom_30 price
    [print(item) for item in prods_to_filter_price_by_median]

    return prods_to_filter_price_by_median


if __name__ == '__main__':
    run()