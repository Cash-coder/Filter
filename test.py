from datetime import date
import datetime
import calendar 

date_a = "vie. 10 jul. y el lun. 12 jul."
date_b = "vie. 2 agos. y el lun. 6 agosto."
date_c = "vie. 12 jul."
date_d = "vie. 1 ago."


def get_wp_shipping_time(ebay_shipping_time):

    #split ebay dates "vie. 9 jul. y el lun. 12 jul."
    ebay_date = ebay_shipping_time.split('.')
    ##get today's current day and month number
    current_day = str(date.today()).split('-')[2]
    current_month = str(date.today()).split('-')[1]
    current_month = int(current_month)
    current_month_name = calendar.month_name[current_month].lower()
    current_month_letters = current_month_name[0:3]

    

    
    # it can be one date(jul 12) or a range between 2 days (jul. 12 and jul. 16)
    #if it's a range of 2 dates:
    if len(ebay_date) == 5: 
        #select chunk like (9 jul)
        ebay_first_date = ebay_date[1]
        #select the number (9)
        ebay_first_day = ebay_first_date.split(' ')[1]
        #select the month name (jul)
        ebay_first_month = ebay_first_date.split(' ')[2]
        #second_date = ebay_date[3]
        #second_day = second_date.split(' ')[1]
        #ebay_second_month = second_date.split(' ')[2]
        
        #first letters from current month name to compare with ebay's
        # if it's the same month: jul == jul        
        if current_month_letters == ebay_first_month:
            print("detecte same month")
            shipping_days = int(ebay_first_day) - int(current_day)

            if shipping_days == 1:
                wp_shipping_text = "Envío en 24h"
            elif shipping_days == 2:
                wp_shipping_text = "Envío en 48h"
            elif shipping_days == 3:
                wp_shipping_text = "Envío en 72h"
            elif shipping_days > 3: #if thre's more than 3 days return just the number of days
                return shipping_days
            return wp_shipping_text, shipping_days

        #if it's a different month, like jul-aug
        elif current_month_letters != ebay_first_month:
            print("detecte new month")
            #sample date: today's 27 jul, shipping arrival on 2 aug = 6 days
            # (from today's number to the end month) + ebay 1º day
            # (31-27)+2
            now = datetime.datetime.now()
            current_month_total_days = calendar.monthrange(now.year,now.month)[1]        
            daysto_end_month = current_month_total_days - now.month
            wp_shipping_days = daysto_end_month + int(ebay_first_day)

            return wp_shipping_days
   
    elif len(ebay_date) == 3: #there's only one date, like in "vie. 12 jul."
        ebay_day_number = ebay_shipping_time.split('.')[1]
        ebay_day_number = ebay_day_number.split(' ')[1]
        ebay_month_name = ebay_shipping_time.split('.')[1].split(' ')[2]

        #if it's the same month
        if current_month_letters == ebay_month_name:
            
            shipping_days = int(ebay_day_number) - int(current_day)

            if shipping_days == 1:
                wp_shipping_text = "Envío en 24h"
            elif shipping_days == 2:
                wp_shipping_text = "Envío en 48h"
            elif shipping_days == 3:
                wp_shipping_text = "Envío en 72h"
            elif shipping_days > 3: #if thre's more than 3 days return just the number of days
                return shipping_days
            return wp_shipping_text, shipping_days
        
        #if it's a different month
        elif current_month_letters != ebay_month_name:

            now = datetime.datetime.now()
            current_month_total_days = calendar.monthrange(now.year,now.month)[1]        
            daysto_end_month = current_month_total_days - now.month
            shipping_days = daysto_end_month + int(ebay_day_number)

            if shipping_days == 1:
                wp_shipping_text = "Envío en 24h"
            elif shipping_days == 2:
                wp_shipping_text = "Envío en 48h"
            elif shipping_days == 3:
                wp_shipping_text = "Envío en 72h"
            elif shipping_days > 3: #if thre's more than 3 days return just the number of days
                return shipping_days
            return wp_shipping_text, shipping_days
            


get_wp_shipping_time(date_d)
#get_wp_shipping_time(date_c)
