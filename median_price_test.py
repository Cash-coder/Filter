import pandas as pd
import traceback
import json
import statistics
import funcs_currency
# import names used in json input file


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
# EBAY_CATEGORY_NAME  = 'category'
EBAY_PAYMENT_NAME   = 'payment_methods'
EBAY_PROD_SPECS_NAME= 'prod_specs'
EBAY_PROD_STATE_NAME= 'product_state'
EBAY_PROD_DESCRIPTION_NAME = 'prod_description'
EBAY_SERVED_AREA_NAME='served_area'
EBAY_REVIEWS_NAME   = 'reviews'
EBAY_PROD_SOLD_OUT_NAME = 'product_sold_out_text'
EBAY_IMPORT_TAXES_NAME  = 'import_taxes'
TARGET_CATEGORY_NAME    = 'target_category' #used later in importer, if smartphone, import to smartphones
TARGET_ATTR_1_NAME   = 'query_attribute_1'
TARGET_ATTR_2_NAME   = 'query_attribute_2'
TARGET_MODEL_NAME    = 'query_model'
TARGET_PROD_STATE    = 'query_prod_state'
EBAY_PICS_URLS       = 'ebay_pics'
EBAY_SUBTITLE        = 'subtitle'
EBAY_IFRAME          = 'iframe_description_url'
mean_price_NAME= 'mean_price'
SUBTITLE_NAME        = 'subtitle'


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


def process_shipping_price(ebay_shipping_price):
   
    if ebay_shipping_price == []:
        ebay_shipping_price = 0
        return ebay_shipping_price

    try:
        # used to debug
        original = ebay_shipping_price 

        if 'GRATIS' in ebay_shipping_price or 'gratis' in ebay_shipping_price:
            ebay_shipping_price = 0
            return ebay_shipping_price
        
        try:
            ebay_shipping_price = ebay_shipping_price.replace('EUR','').replace('GBP','').replace('USD','').replace(',','.').replace('aprox.','').replace('(','').replace(')','').replace('de gastos de envío','').strip()
            ebay_shipping_price = float(ebay_shipping_price)
        except Exception as e:
            print(f'Exception with ebay shipping price: original: {original}\nprocessed: <{ebay_shipping_price}>\nError: {e}')
            return 'error processing shipping price'
        
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
            
            
        return ebay_shipping_price
    
    except Exception as e:
        print(e)
        traceback.print_exc
        return 'error processing shipping price'


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
    for item in median_price_list:
        model = item.get('model')
        if model_attr == model:
            # median_high = item.get('median_high')
            median_low = item.get('median_low')
            median_low = int(median_low)

            # admit some tolerance for the low prices
            tolerance_percentage = set_tolerance(price)
            median_low_price_with_tolerance = median_low + (price * tolerance_percentage)

            print(f'ebay_model_attr: {model_attr}, median_model_attr:{model}\nprice {price} median_low_tolerance:{median_low_price_with_tolerance}, median_low:{median_low}')
            # if price_with_tolerance < median_high:
            if price < median_low_price_with_tolerance:
                # print(f'ACCEPTED price {price} median_high {median_high}')
                print(f'ACCEPTED price {price} median_low_tolerance {median_low_price_with_tolerance}')
                return True
            else:
                print(f'FALSE not accepted price {price} median_low {median_low_price_with_tolerance}')
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


def check_defective_prod(ebay_title, prod_state):
    try:
        ebay_title_lower = ebay_title.lower()
        
        #if the prod is broken
        if 'Para desguace' in prod_state: 
            # print(f'broken item {ebay_title, prod_state}')
            return True
        
        if 'placa madre' in ebay_title_lower or 'placa base' in ebay_title_lower or 'motherboard' in ebay_title_lower or 'logic card' in ebay_title_lower or 'defectuoso' in ebay_title_lower or ' bad' in ebay_title_lower:
            # print(f'broken item {ebay_title, prod_state}')
            return True
        elif 'piezas' in ebay_title_lower or 'parts' in ebay_title_lower or 'mal estado' in ebay_title_lower:
            # print(f'broken item {ebay_title, prod_state}')
            return True
        # icloud locked notice the white space to differentiate "unlocked" and " locked"
        elif ' bloqueado' in ebay_title_lower or ' locked' in ebay_title_lower:
            # print(f'broken item {ebay_title, prod_state}')
            return True
    
    except Exception as e:
        print(e)       
        traceback.print_exc()
        
        return True 


def run():

    with open(INPUT_FILE, encoding='utf8') as json_file:
        scrapper_data = json.load(json_file)

        prods_to_filter_price_by_median = []
        for item in scrapper_data:  
            # print(i)
            
            # variables to filter:
            price   = item[EBAY_PRICE_NAME]
            ebay_id = item[EBAY_ID_NAME]
            model   = item[TARGET_MODEL_NAME]
            shipping_price = item[EBAY_SHIPPING_PRICE]
            query_attr     = item[TARGET_ATTR_1_NAME]
            import_taxes   = item[EBAY_IMPORT_TAXES_NAME]
            ebay_title   =  item[EBAY_TITLE_NAME]
            prod_state   =  item[EBAY_PROD_STATE_NAME]

            
            price = process_price(price)
            if 'local pick up' in shipping_price:
                continue
            
            is_defective =  check_defective_prod(ebay_title, prod_state)
            
            if is_defective:
                # print(f'faulty item {ebay_title, prod_state}')
                continue
            

            shipping_price = process_shipping_price(shipping_price)
            # if shipping_price == 'error processing shipping price':
                # print(f'shipping price error with ebay_id: {ebay_id}')


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

    #print for each model_attr, all the median prices with number of prods in each.
    # median_low  = 125€ , 50 prods
    # median_high = 200€ , 35 prods

    # for each item in list, get the median price from item's prices list
    for item in prods_to_filter_price_by_median:
        prices_list = item.get('prices')
        prices_list.sort()

        model = item.get('model')
        
        pd_serialization = pd.Series(prices_list)
        bottom_25_percentage = pd_serialization.describe()['25%']

        l = len(prices_list)
        _05_percent = sum(prices_list) / len(prices_list) * 0.05
        bottom_30_percent = bottom_25_percentage + _05_percent

        print(pd_serialization.describe())
        print(f'{model}     {bottom_25_percentage}  {bottom_30_percent} \n{prices_list}\n\n\n')
        
        item['median_low'] = bottom_25_percentage
        
        # median_high = statistics.median_high(prices_list)
        # item['median_high'] =  median_high
        # remove prices list, memory efficient
        del item['prices']

        

    # return prods_to_filter_price_by_median

    # for each model_attr
        # print(median_low,n_items median,n_items high,n_items)


if __name__ == '__main__':
    run()