#TODO update for 2023
#inputs VARIOUS INTERNATIONAL prices to relevant bikes
#copied from priceUS

"""
TODO

format into VARIABLE LANGUAGE pricing
"""

import openpyxl, os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop,x_login, x_get_value
from mFunctions import *

#
#
#
SaveState = define_save_state()
languageEntry = 'India'
#
#
#

def pricer(bike, priceCell):
    waitForTasks()
    print(f'\n\n    BEGIN price {languageEntry} for {bike} \n')
    NavBikes()
    
    price = (priceSheet.cell(row=priceCell, column=2).value)
    print(f'    sheet price: {price}')

    #format price
    price = '{:,}'.format(price)
    price = '$' + price + '.00'

    print(f'    format price: {price}')


    #use search to check for load  
    LoadSearch()
        
    search('2022', bike)
    
    #use title to check for load
    LoadBike(bike)
    originalprice = x_get_value(bikePD['Price'])
    print(f'field price: {originalprice}')
    if (originalprice == price):
        print('\n***price is the same, skipping entry***\n')
        breakpoint
    else:
        print('***new price entered***')
        x_replace_field(bikePD['Price'], price)

        SaveBike(bike, SaveState, False)


"""
Runtime
"""
runtime()

wb = openpyxl.load_workbook('Global MSRP-RRP 3-23-2021.xlsx')
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

pricer('Alpine Trail E2', 82)
pricer('Alpine Trail E1', 81)
pricer('Alpine Trail Carbon 2', 5)
pricer('Alpine Trail Carbon 1', 4)
pricer('Alpine Trail XR', 3)
pricer('Alpine Trail 7', 2)
pricer('Alpine Trail Carbon 2 Frame Kit', 97)
pricer('Rift Zone 29" Carbon XR', 11)
pricer('Rift Zone 29" Carbon 2', 10)
pricer('Rift Zone 29" Carbon 1', 9)
pricer('Rift Zone 29" 3', 8)
pricer('Rift Zone 29" 2', 7)
pricer('Rift Zone 29" 1', 6)
pricer('Rift Zone 29" Carbon XR Frame Kit', 96)
pricer('Rift Zone 27.5" 3', 14)
pricer('Rift Zone 27.5" 2', 13)
pricer('Rift Zone 27.5" 1', 12)
pricer('Rift Zone 26', 90)
pricer('El Roy', 32)
pricer('El Roy Frame Kit', 98)
pricer('San Quentin 3', 31)
pricer('San Quentin 2', 30)
pricer('San Quentin 1', 29)
pricer('San Quentin 3 Frame Kit', 94)
pricer('Alcatraz', 33)
pricer('Alcatraz Frame Kit', 93)
pricer('Bolinas Ridge 2', 28)
pricer('Bolinas Ridge 1', 26)
pricer('Bobcat Trail 5', 22)
pricer('Bobcat Trail 4', 20)
pricer('Bobcat Trail 3', 18)
pricer('Wildcat Trail 3', 24)
pricer('Wildcat Trail 1', 23)
pricer('Team Marin 2', 16)
pricer('Team Marin 1', 15)
pricer('Pine Mountain E2', 80)
pricer('Pine Mountain E1', 79)
pricer('Pine Mountain 2', 35)
pricer('Pine Mountain 1', 34)
pricer('Headlands 2', 43)
pricer('Headlands 1', 42)
pricer('Headlands Frame Kit', 95)
pricer('Gestalt X11', 41)
pricer('Gestalt X10', 40)
pricer('Gestalt 2.5', 39)
pricer('Gestalt 2', 38)
pricer('Gestalt 1', 37)
pricer('Gestalt', 36)
pricer('DSX FS', 58)
pricer('DSX 2', 57)
pricer('DSX 1', 56)
pricer('DSX', 55)
pricer('Nicasio 2', 45)
pricer('Nicasio 1', 44)
pricer('Nicasio +', 46)
pricer('Lombard 1', 47)
pricer('Four Corners', 48)
pricer('Muirwoods', 49)
pricer('Muirwoods RC', 50)
pricer('Presidio 3', 66)
pricer('Presidio 2', 65)
pricer('Presidio 1', 64)
pricer('Fairfax 3', 63)
pricer('Fairfax 2', 61)
pricer('Fairfax ST 2', 62)
pricer('Fairfax 1', 59)
pricer('Fairfax ST 1', 60)
pricer('San Rafael DS2', 52)
pricer('San Rafael DS1', 51)
pricer('San Anselmo DS2', 54)
pricer('San Anselmo DS1', 53)
pricer('Sausalito E2', 78)
pricer('Sausalito ST E2', 78)
pricer('Sausalito E1', 77)
pricer('Sausalito ST E1', 77)
pricer('Kentfield 2', 71)
pricer('Kentfield ST 2', 71)
pricer('Kentfield 1', 70)
pricer('Kentfield ST 1', 70)
pricer('Larkspur 2', 68)
pricer('Larkspur 1', 67)
pricer('Stinson 2', 75)
pricer('Stinson ST 2', 75)
pricer('Stinson 1', 73)
pricer('Stinson ST 1', 73)
pricer('Stinson Electric', 85)
pricer('Stinson Electric ST', 85)
pricer('Rift Zone Jr 24', 89)
pricer('Bayview Trail 24', 88)
pricer('Hidden Canyon 20', 87)
pricer('San Quentin 24', 92)
pricer('San Quentin 20', 91)