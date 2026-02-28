#inputs ALL LANGUAGES with unique formatting

import openpyxl, os, time
from selenium import webdriver
from notificationbot import notifyOfCompletion
from x_functions import x_click, x_delay_click, x_drop,x_login, x_get_value
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#

def pricer(bike, priceCell):
    for language in languagePD.items():
        print(f'\n\n    BEGIN price {language[0]} for {bike} \n')
        NavBikes()

        SetLanguage(language[1])
        
        price = (priceSheet.cell(row=priceCell, column=2).value)
        print(f'    sheet price: {price}')

        #format price
        price = '{:,}'.format(price)
        price = '$' + price + '.00 (USD)'

        print(f'    format price: {price}')


        #use search to check for load  
        LoadSearch()
            
        search(modelYear, bike)
        
        #use title to check for load
        LoadBike(bike)
        originalprice = x_get_value(bikePD['Price'])
        print(f'field price: {originalprice}')
        if originalprice != price:
            x_replace_field(bikePD['Price'], price)
            SaveBike(bike, SaveState)
            print(f'\n new price entered: {price}')
        else:
            print('***price is the same***')


"""
Runtime
"""
runtime()

wb = openpyxl.load_workbook('Marin Global MSRP - July 2022.xlsx')
print(wb, 'open')
priceSheet = wb['Sheet1']
print(priceSheet, 'acquired')

"""
Site Navigation
"""

backstage_login()

click_Entries()

LoadSearch()

"""
Function Calls
"""

"""
FINISHED
"""

pricer('Rift Zone E (base) (JAN-FEB 2023)', 78)
pricer('Rift Zone E1 (JAN-FEB 2023)', 79)
pricer('Rift Zone E2 (JAN-FEB 2023)', 80)

notifyOfCompletion(f'price empty has completed @ {datetime.datetime.now()}')