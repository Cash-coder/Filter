from datetime import date
import calendar 

date_a = "vie. 16 jul. y el lun. 12 jul."
date_b = "vie. 27 jul. y el lun. 1 agosto."
date_c = "vie. 12 jul."


def get_wp_shipping_time(ebay_shipping_time):

    #split ebay dates "vie. 9 jul. y el lun. 12 jul."
    ebay_date = ebay_shipping_time.split('.')
    #select chunks like (9 jul)
    ebay_first_date = ebay_date[1]
    second_date = ebay_date[3]
    #select the number (9)
    ebay_first_day = ebay_first_date.split(' ')[1]
    #select the month name (jul)
    ebay_first_month = ebay_first_date.split(' ')[2]
    #second_day = second_date.split(' ')[1]
    #ebay_second_month = second_date.split(' ')[2]


    current_day = str(date.today()).split('-')[2]
    current_month = str(date.today()).split('-')[1]
    current_month = int(current_month)
    # print("this month is",calendar.month_name[current_month])
    # print(f"arrives in {wp_shipping_time_days} days")
    
    current_month_name = calendar.month_name[current_month].lower()
    first_month_letters = current_month_name[0:3]

    print(first_month_letters)

    if first_month_letters == ebay_first_month:
        shipping_days = int(ebay_first_day) - int(current_day)
        print(shipping_days)

        if shipping_days == 1:
            wp_shipping_time = "Envío en 24h"
        if shipping_days == 2:
            wp_shipping_time = "Envío en 48h"
        if shipping_days == 3:
            wp_shipping_time = "Envío en 72h"

        print(wp_shipping_time)
        return wp_shipping_time


get_wp_shipping_time(date_a)


# #is it's the same month
# if ebay_first_month == ebay_second_month:
#     wp_shipping_time_days = int(second_day) - int(first_day)
# #if it's different month
# else:
#     daysto_end_month = 31 - int(first_day)
#     wp_shipping_time_days = daysto_end_month + int(second_day)        

# if wp_shipping_time_days == 1:
#     wp_shipping_time_days = "Envío en 24h"
# elif wp_shipping_time_days == 2:
#     wp_shipping_time_days = "Envío en 48h"
# elif wp_shipping_time_days == 3:
#     wp_shipping_time_days = "Envío en 72h"