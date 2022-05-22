# 

import json
import statistics
import funcs_currency
# import names used in json input file
from filter import TARGET_MODEL_NAME, EBAY_PRICE_NAME, EBAY_SHIPPING_PRICE, EBAY_IMPORT_TAXES_NAME, TARGET_ATTR_1_NAME, EBAY_ID_NAME
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
    for item in median_price_list:
        model = item.get('model')
        if model_attr == model:
            # median_high = item.get('median_high')
            median_low = item.get('median_low')
            # if item's price is lower than median_low price return True

            # 
            tolerance = set_tolerance(price)
            price_with_tolerance = price + (price * tolerance)
            # if price_with_tolerance < median_high:
            if price_with_tolerance < median_low:
                # print(f'ACCEPTED price {price} median_high {median_high}')
                print(f'ACCEPTED price {price} median_low {median_low}')
                return True
            else:
                print(f'FALSE not accepted price {price} median_low {median_low}')
                return False

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



def run(selected_input_file):

    with open(selected_input_file, encoding='utf8') as json_file:
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

        median_low = statistics.median_low(prices_list)
        item['median_low'] = median_low
        
        # median_high = statistics.median_high(prices_list)
        # item['median_high'] =  median_high
        # remove prices list, memory efficient
        del item['prices']

    [print(item) for item in prods_to_filter_price_by_median]

    return prods_to_filter_price_by_median


if __name__ == '__main__':
    run()