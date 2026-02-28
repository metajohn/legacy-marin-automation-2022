"""
DelSap

Deletes SAP on chosen bikes
"""

#TODO add pagename to the geo function and manually enter the page for each function call
#in addition to the yStart and yEned

import os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop, x_login
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#

def DelSap(bike):
    NavBikes()

    search(modelYear, bike)

    x_delay_click('/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[1]/div[4]/div[3]/div/div[1]/div[1]/div[4]/div/div[2]/div[3]/input')
    x_replace_field('/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[1]/div[4]/div[3]/div/div[1]/div[1]/div[4]/div/div[2]/div[3]/input', '')

    try:
        x_click('/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[1]/div[4]/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/div[3]/input')
        x_replace_field('/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[1]/div[4]/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/div[3]/input','')
    except(NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
        print('No Second Color')

    SaveBike(bike, SaveState, False, 200)

"""
Begin
"""

runtime()

"""
                Site Navigation
"""


backstage_login()

NavBikes()


"""
            Call Functions
"""

"""
COMPLETED
"""

DelSap('Alpine Trail Carbon 2')
DelSap('Alpine Trail Carbon 1')
DelSap('Alpine Trail XR')
DelSap('Alpine Trail 7')
DelSap('Alpine Trail Carbon 2 Frame Kit')
DelSap('Alpine Trail E2')
DelSap('Alpine Trail E1')
DelSap('Rift Zone 29" Carbon XR')
DelSap('Rift Zone 29" Carbon 2')
DelSap('Rift Zone 29" Carbon 1')
DelSap('Rift Zone 29" Carbon XR Frame Kit')
DelSap('Rift Zone 29" XR')
DelSap('Rift Zone 29" 2')
DelSap('Rift Zone 29" 1')
DelSap('Rift Zone 27.5" XR')
DelSap('Rift Zone 27.5" 2')
DelSap('Rift Zone 27.5" 1')
DelSap('San Quentin 3')
DelSap('San Quentin 2')
DelSap('San Quentin 1')
DelSap('San Quentin 3 Frame Kit')
DelSap('El Roy')
DelSap('El Roy Frame Kit')
DelSap('Bobcat Trail 5')
DelSap('Bobcat Trail 4')
DelSap('Bobcat Trail 3')
DelSap('Bolinas Ridge 2')
DelSap('Bolinas Ridge 1')
DelSap('Wildcat Trail 3')
DelSap('Wildcat Trail 1')
DelSap('Team Marin 2')
DelSap('Team Marin 1')
DelSap('Pine Mountain 2')
DelSap('Pine Mountain 1')
DelSap('Alcatraz')
DelSap('Alcatraz Frame Kit')
DelSap('Headlands 2')
DelSap('Headlands 1')
DelSap('Headlands Frame Kit')
DelSap('Gestalt XR')
DelSap('Gestalt X10')
DelSap('Gestalt 2')
DelSap('Gestalt 1')
DelSap('Gestalt')
DelSap('Nicasio 2')
DelSap('Nicasio+')
DelSap('Nicasio')
DelSap('Four Corners')
DelSap('Lombard 1')
DelSap('Fairfax 3')
DelSap('Fairfax 2')
DelSap('Fairfax 2 ST')
DelSap('Fairfax 1')
DelSap('Fairfax 1 ST')
DelSap('Presidio 3')
DelSap('Presidio 2')
DelSap('Presidio 1')
DelSap('Muirwoods')
DelSap('Larkspur 2')
DelSap('Larkspur 1')
DelSap('San Rafael DS2')
DelSap('San Rafael DS1')
DelSap('San Anselmo DS2')
DelSap('San Anselmo DS1')
DelSap('DSX FS')
DelSap('DSX 2')
DelSap('DSX 1')
DelSap('DSX')
DelSap('Kentfield 2')
DelSap('Kentfield ST 2')
DelSap('Kentfield 1')
DelSap('Kentfield ST 1')
DelSap('Stinson 2')
DelSap('Stinson ST 2')
DelSap('Stinson 1')
DelSap('Stinson ST 1')
DelSap('Rift Zone 26')
DelSap('Rift Zone JR 24"')
DelSap('San Quentin 24"')
DelSap('San Quentin 20"')
DelSap('Bayview Trail 24"')
DelSap('Hidden Canyon 20"')
DelSap('Sausalito E2')
DelSap('Sausalito ST E2')
DelSap('Sausalito E1')
DelSap('Sausalito ST E1')
