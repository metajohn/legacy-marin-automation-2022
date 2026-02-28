#TODO update for 2023
#inputs VARIOUS IEURO prices to relevant bikes
#copied from priceUS

"""
TODO

format into EU pricing
"""

import openpyxl, os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop,x_login, x_get_value
from mFunctions import *
from notificationbot import notifyOfCompletion

#
#
#
SaveState = define_save_state()
languageEntry = 'France'
price_difference_list = []
#
#
#

def pricer(bike, priceCell):
    print(f'\n\n    BEGIN price {languageEntry} for {bike} \n')
    NavBikes()
    
    price = (priceSheet.cell(row=priceCell, column=4).value)
    print(f'    sheet price: {price}')

    #format price
    price = '{:,}'.format(price)
    price = price + '.00 ' + '€'

    print(f'    format price: {price}')


    #use search to check for load  
    LoadSearch()
        
    search(modelYear, bike)
    
    #use title to check for load
    LoadBike(bike)
    originalprice = x_get_value(bikePD['Price'])
    print(f'field price: {originalprice}')
    if (originalprice == price):
        print('\n***price is the same, skipping entry***\n')
    else:
        print('***new price entered***')
        x_replace_field(bikePD['Price'], price)

        if(SaveState == 'cycle'):
            price_difference_list.append(f'{bike} siteprice: {originalprice} sheetprice: {price}')

        SaveBike(bike, SaveState, False, 200)


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

SetLanguage(languagePD[languageEntry])
LoadSearch()

"""
Function Calls
"""

"""
FINISHED
"""

pricer('Alcatraz', 34)
pricer('Alcatraz Frame Kit', 92)
pricer('Alpine Trail 7', 2)
pricer('Alpine Trail Carbon 1', 4)
pricer('Alpine Trail Carbon 2', 5)

pricer('Alpine Trail Carbon 2 Frame Kit', 96)
pricer('Alpine Trail E (NOV 1)', 81)
pricer('Alpine Trail E1 (NOV 1)', 82)
pricer('Alpine Trail E2 (NOV 1)', 83)
pricer('Alpine Trail XR (OCT 1)', 3)

pricer('Bayview Trail 24\"', 87)
pricer('Bobcat Trail 3', 18)
pricer('Bobcat Trail 4', 20)

pricer('Bobcat Trail 5', 22)
pricer('Bolinas Ridge 1', 26)
pricer('Bolinas Ridge 2', 28)
pricer('DSX', 54)
pricer('DSX 1', 55)
pricer('DSX 2', 56)
pricer('DSX FS', 57)
pricer('El Roy', 33)
pricer('El Roy Frame Kit', 97)
pricer('Fairfax 1', 58)
pricer('Fairfax 2', 60)
pricer('Fairfax 3', 62)
pricer('Fairfax ST 1', 59)
pricer('Fairfax ST 2', 61)
pricer('Four Corners', 48)
pricer('Gestalt (AUG 15)', 37)
pricer('Gestalt 1 (SEP 1)', 38)

pricer('Gestalt 2  (SEP 1)', 39)
pricer('Gestalt X10 (AUG 15)', 40)
pricer('Gestalt XR (NOV 15)', 41)

pricer('Headlands 1', 42)
pricer('Headlands 2', 43)
pricer('Headlands Frame Kit', 94)
pricer('Hidden Canyon 20\"', 86)
pricer('Kentfield 1', 68)
pricer('Kentfield 2', 70)
pricer('Kentfield ST 1', 69)
pricer('Kentfield ST 2', 71)
pricer('Larkspur 1', 66)
pricer('Larkspur 2', 67)
pricer('Lombard 1', 47)
pricer('Muirwoods', 49)
pricer('Nicasio', 45)
pricer('Nicasio 2', 46)

pricer('Nicasio+', 44)
pricer('Pine Mountain 1 (SEP 15)', 35)
pricer('Pine Mountain 2 (FEB 1)', 36)
pricer('Presidio 1', 63)
pricer('Presidio 2', 64)
pricer('Presidio 3', 65)
pricer('Rift Zone 26\" (OCT 19)', 89)
pricer('Rift Zone 27.5" 1 (OCT 19)', 12)
pricer('Rift Zone 27.5" 2 (OCT 19)', 13)
pricer('Rift Zone 27.5" XR (OCT 19)', 14)
pricer('Rift Zone 29" 1 (OCT 19)', 6)
pricer('Rift Zone 29" 2 (OCT 19)', 7)
pricer('Rift Zone 29" Carbon 1', 9)
pricer('Rift Zone 29" Carbon 2', 10)
pricer('Rift Zone 29" Carbon XR', 11)
pricer('Rift Zone 29" Carbon XR Frame Kit', 95)
pricer('Rift Zone 29" XR (OCT 19)', 8)

pricer('Rift Zone E (base) (JAN-FEB 2023)', 78)
pricer('Rift Zone E1 (JAN-FEB 2023)', 79)
pricer('Rift Zone E2 (JAN-FEB 2023)', 80)
pricer('Rift Zone Jr 24\" (OCT 19)', 88)
pricer('San Anselmo DS1', 52)
pricer('San Anselmo DS2', 53)
pricer('San Quentin 1 (OCT 3)', 30)
pricer('San Quentin 2 (DEC 1)', 31)
pricer('San Quentin 24\"', 91)
pricer('San Quentin 20\"', 90)
pricer('San Quentin 3 (DEC 1)', 32)
pricer('San Quentin 3 Frame Kit (DEC 1)', 93)
pricer('San Rafael DS1', 50)
pricer('San Rafael DS2', 51)
pricer('Sausalito E1', 76)
pricer('Sausalito E2 ROW spec (SEP 15)', 77)
pricer('Sausalito E2 USA/Australia spec (SEP 15)', 77)

pricer('Sausalito ST E1', 76)
pricer('Sausalito ST E2 ROW spec (SEP 15)', 77)
pricer('Sausalito ST E2 USA/Australia spec (SEP 15)', 77)
pricer('Stinson 1', 72)
pricer('Stinson 2', 74)
pricer('Stinson E', 84)
pricer('Stinson E ST', 85)
pricer('Stinson ST 1', 73)
pricer('Stinson ST 2', 75)
pricer('Team Marin 1', 15)
pricer('Team Marin 2', 16)
pricer('Wildcat Trail 1', 23)
pricer('Wildcat Trail 2 (SEP 1)', 24)
pricer('Wildcat Trail 3', 25)

notifyOfCompletion(f'price cad has completed @ {datetime.datetime.now()}')

for item in price_difference_list:
    print(item)