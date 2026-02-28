#launches 2023 bikes and archives 2022 version"

import openpyxl, os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop,x_login, x_get_value, x_print_time
from mFunctions import *

"""
make sure to activate the 2022 year and set 2021 to archive first
before running this script
"""

#
#
#
SaveState = define_save_state()
#
#
#

def flipNew(bikeNew):
    try:
        print(f'    START Launch Flip for new {bikeNew}\n')
        #load 2022 bike
        LoadSearch()
        search('2023', bikeNew)
        LoadBike(bikeNew)

        #enable 2022 bike
        x_delay_click(bikePD['Live_Drop'])
        x_delay_click(bikePD['Live_Toggle'])
        print('bike set to Enabled')
        time.sleep(5)
        
        SaveBike(bikeNew, SaveState, False)
        print(f'    END Launch Flip for new {bikeNew}\n')
        print('waiting for 200 seconds')
        time.sleep(200)
    except(NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException) as e:
        notifyOfStall(f'launchFlip failed on flipNew: {bikeNew} and the program has stopped: {e}')
        quit()

def flipOld(bikeOld):
    try:

        print(f'    START Launch Flip for old {bikeOld}\n')
        #load 2021 bike
        LoadSearch()
        search('2022', bikeOld)
        LoadBike(bikeOld)
        x_delay_click(bikePD['Categories'])
        x_delay_click(bikePD['Bike_Status_Drop'])
        x_delay_click(bikePD['Bike_Status_Archive'])

        SaveBike(bikeOld, SaveState, False)
        
        print(f'    END Launch Flip for old {bikeOld}\n')
        

    except(NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException) as e:
        notifyOfStall(f'launchFlip failed on flipOld: {bikeOld} and the program has stopped: {e}')
        quit()


"""
Runtime
"""
runtime()

x_print_time('Start Time: ')

"""
Site Navigation
"""

backstage_login()

NavBikes()

LoadSearch()

"""
Function Calls

flipOld('Alcatraz')
flipNew('Alcatraz')


flipOld('Alcatraz Frame Kit')

flipNew('Alcatraz Frame Kit')
flipOld('Alpine Trail 7')
flipNew('Alpine Trail 7')
flipOld('Alpine Trail Carbon 1')
flipNew('Alpine Trail Carbon 1')
flipOld('Alpine Trail Carbon 2')
flipNew('Alpine Trail Carbon 2')
flipOld('Alpine Trail Carbon 2 Frame Kit')
flipNew('Alpine Trail Carbon 2 Frame Kit')

flipOld('Bayview Trail 24')
flipNew('Bayview Trail 24\"')
flipOld('Bobcat Trail 3')
flipNew('Bobcat Trail 3')
flipOld('Bobcat Trail 4')
flipNew('Bobcat Trail 4')
flipOld('Bobcat Trail 5')
flipNew('Bobcat Trail 5')
flipOld('Bolinas Ridge 1')
flipNew('Bolinas Ridge 1')
flipOld('Bolinas Ridge 2')
flipNew('Bolinas Ridge 2')
flipOld('DSX')
flipNew('DSX')
flipOld('DSX 1')
flipNew('DSX 1')
flipOld('DSX 2')
flipNew('DSX 2')
flipOld('DSX FS')
flipNew('DSX FS')
flipOld('Fairfax 1')
flipNew('Fairfax 1')
flipOld('Fairfax 2')
flipNew('Fairfax 2')
flipOld('Fairfax 3')
flipNew('Fairfax 3')
flipOld('Fairfax ST 1')
flipNew('Fairfax ST 1')
flipOld('Fairfax ST 2')
flipNew('Fairfax ST 2')
flipOld('Four Corners')
flipNew('Four Corners')
flipOld('Headlands 1')
flipNew('Headlands 1')
flipOld('Headlands 2')
flipNew('Headlands 2')
flipOld('Headlands Frame Kit')
flipNew('Headlands Frame Kit')

flipOld('Hidden Canyon 20')
flipNew('Hidden Canyon 20\"')
flipOld('Kentfield 1')
flipNew('Kentfield 1')
flipOld('Kentfield 2')
flipNew('Kentfield 2')
flipOld('Kentfield ST 1')
flipNew('Kentfield ST 1')
flipOld('Kentfield ST 2')
flipNew('Kentfield ST 2')
flipOld('Larkspur 1')
flipNew('Larkspur 1')
flipOld('Larkspur 2')
flipNew('Larkspur 2')
flipOld('Lombard 1')
flipNew('Lombard 1')
flipOld('Muirwoods')
flipNew('Muirwoods')
flipOld('Nicasio')
flipNew('Nicasio')
flipOld('Nicasio 2')
flipNew('Nicasio 2')
flipOld('Nicasio+')
flipNew('Nicasio+')
flipOld('Presidio 1')
flipNew('Presidio 1')
flipOld('Presidio 2')
flipNew('Presidio 2')
flipOld('Presidio 3')
flipNew('Presidio 3')
flipOld('Rift Zone 29" Carbon 1')
flipNew('Rift Zone 29" Carbon 1')
flipOld('Rift Zone 29" Carbon 2')
flipNew('Rift Zone 29" Carbon 2')
flipOld('Rift Zone 29" Carbon XR')
flipNew('Rift Zone 29" Carbon XR Frame Kit')
flipOld('San Anselmo DS1')
flipNew('San Anselmo DS1')
flipOld('San Anselmo DS2')
flipNew('San Anselmo DS2')

flipOld('San Quentin 20')
flipNew('San Quentin 20"')
flipOld('San Quentin 24')
flipNew('San Quentin 24"')
flipOld('San Rafael DS1')
flipNew('San Rafael DS1')
flipOld('San Rafael DS2')
flipNew('San Rafael DS2')
flipOld('Sausalito E1')
flipNew('Sausalito E1')
flipOld('Sausalito ST E1')
flipNew('Sausalito ST E1')

flipOld('Stinson 1')
flipNew('Stinson 1')
flipOld('Stinson 2')
flipNew('Stinson 2')

flipOld('Stinson Electric')
flipNew('Stinson E')
"""
flipOld('Stinson Electric ST')
flipNew('Stinson E ST')
flipOld('Stinson ST 1')
flipNew('Stinson ST 1')
flipOld('Stinson ST 2')
flipNew('Stinson ST 2')
flipOld('Team Marin 1')
flipNew('Team Marin 1')
flipOld('Wildcat Trail 1')
flipNew('Wildcat Trail 1')
flipOld('Wildcat Trail 3')
flipNew('Wildcat Trail 3')