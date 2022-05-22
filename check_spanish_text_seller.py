import collections
import json
import csv


# open scrapper_output
# row by row, get seller
# print how many times a seller appeared

#if seller is new:
# append seller to a list
# elif seller already appended, += 1 to quantity
# print seller and qunatity (prods they have)
# now you can check manually seller with lots of prods and mark them as spanish_text_seller

INPUT_FILE   = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.json"

# with open(INPUT_FILE, encoding='utf8') as json_file:
#     scrapper_data = json.load(json_file)

# vendors_list = []
# for item in scrapper_data:        
#     seller = item.get('ebay_vendor')
#     vendors_list.append(seller)

# ocurrences = collections.Counter(vendors_list)
# print(ocurrences)
# [print(ocurrence, n) for ocurrence, n in ocurrences]


WEB_PICS_DB    = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\WEB_PICS_DB.xlsx"
INPUT_FILE     = r"C:\Us  ers\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output.json"
INPUT_FILE_C2  = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\crawler_output_C2.json"
OUTPUT_FILE    = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\FILTER_OUTPUT.xlsx" 
OUTPUT_FILE_C2 = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\FILTER_OUTPUT_CHANNEL2.xlsx" 
LOGS_FOLDER    = r"C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\sm_sys_folder\logs_folder"


def get_args():
    import sys
        # first arg  resume filtering in case of crush, specify as a parameter when calling from terminal
    # you have to manually save the output file because this will remove all old entries. So it will start from index x, but all processed data will be removed
    # or you can find the file in the logs folder
    
    # arg1 = resume_index in case of crush restart at index x
    try:
        first_arg = sys.argv[1]
        if first_arg != '-':
            resume_from_index_n = int(first_arg)
        else:
            resume_from_index_n = 0
    except IndexError: # if not specified start from the beginning
        resume_from_index_n = 0

    # arg2 = c2 = channel_2 use input and output files of channel 2
    try:
        second_arg = sys.argv[2]
        if second_arg == 'c2':
            selected_input_file  = INPUT_FILE_C2
            selected_output_file = OUTPUT_FILE_C2
    except IndexError:
        selected_input_file  = INPUT_FILE
        selected_output_file = OUTPUT_FILE
    
    print(f'selected_input_file: {selected_input_file}\n selected_output_file: {selected_output_file}\n resume_from_index_n: {resume_from_index_n}\n')
    return selected_input_file, selected_output_file, resume_from_index_n

# selected_input_file ,selected_output_file ,resume_from_index_n = get_args()
selected_input_file, \
selected_output_file, \
resume_from_index_n = get_args()
