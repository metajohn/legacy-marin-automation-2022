"""
Duplicate Bikes
This particular script is based around duplicating 2021 carry forward bikes into 2022 bikes

This program is generally run after init on a new model year

----------------------

has annual updates

RETOUR MUST BE DISABLED BEFORE DOING THIS

MUST BE FOLLOWED BY slugT
"""

import openpyxl, os, time
from selenium import webdriver
from bikeList_2023 import bikeList
from x_functions import x_click, x_delay_click, x_drop, x_login
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#

def db(bike, oldBike, slug):
    NavBikes()
    'waitForTasks()'
    
    print(f'    BEGIN db for {bike} \n')
    """
    Tab Navigation
    """
    #search
    search(lastModelYear, oldBike)
    
    #Begin duplication
    print('     Entry Open: ' + oldBike)

    #replace title with correct year and new name if applicable
    x_replace_field(bikePD['Title'], modelYear + ' ' + bike)

    #replace name just to be safe
    x_replace_field(bikePD['Bike_Name'], bike)

    #replace slug
    x_replace_field(bikePD['Slug'], modelYear + '-' + slug)

    #Navigate to Categories Tab
    x_click(bikePD['Categories'])

    #cancel year assignement
    
    x_click('//*[@id="fields-bikeModelYear"]/div[1]/div/button')
    #Change year to 2022
    #ANNUAL UPDATE
    x_drop(bikePD['Model_Year'], "//div[@data-label=\'2023\']")

    time.sleep(5)
    #Disable

    x_delay_click(bikePD['Live_Drop'])
    #switch the enabled/disabeld radio switch multiple times to make sure all nationalities all have the same state
    x_delay_click(bikePD['Live_Toggle'])
    x_delay_click(bikePD['Live_Toggle'])
    x_delay_click(bikePD['Live_Toggle'])
    print('\n')
    time.sleep(1)
    #TODO turn this into an xfunction that returns true or false
    isLiveElement = browser.find_element(By.XPATH, '//*[@id="enabled"]')
    isLive = isLiveElement.get_attribute('aria-checked')
    print(isLive)
    if (isLive == 'true'):
        time.sleep(1)
        x_delay_click(bikePD['Live_Toggle'])

    print('bike set to Disabled')


    SaveBike_Copy(bike, SaveState, False)

"""
Runtime
"""
runtime()

"""
Site Navigation
"""

backstage_login()

"""
Function Calls
"""

"""
FINISHED

db('Alpine Trail Carbon 2', 'Alpine Trail Carbon 2', 'alpine-trail-carbon-2')

db('Alpine Trail Carbon 1', 'Alpine Trail Carbon 1', 'alpine-trail-carbon-1')

db('Alpine Trail XR', 'Alpine Trail XR', 'alpine-trail-xr')
db('Alpine Trail 7', 'Alpine Trail 7', 'alpine-trail-7')
db('Alpine Trail Carbon 2 Frame Kit', 'Alpine Trail Carbon 2 Frame Kit', 'alpine-trail-carbon-2-frame-kit')
db('Alpine Trail E2', 'Alpine Trail E2', 'alpine-trail-e2')
db('Alpine Trail E1', 'Alpine Trail E1', 'alpine-trail-e1')
db('Rift Zone 29" Carbon XR', 'Rift Zone 29" Carbon XR', 'rift-zone-29-carbon-xr')
db('Rift Zone 29" Carbon 2', 'Rift Zone 29" Carbon 2', 'rift-zone-29-carbon-2')

db('Rift Zone 29" Carbon 1', 'Rift Zone 29" Carbon 1', 'rift-zone-29-carbon-1')
db('Rift Zone 29" Carbon XR Frame Kit', 'Rift Zone 29" Carbon XR Frame Kit', 'rift-zone-29-carbon-xr-frame-kit')
db('Rift Zone 29" XR', 'Rift Zone 29" 3', 'rift-zone-29-xr')
db('Rift Zone 29" 2', 'Rift Zone 29" 2', 'rift-zone-29-2')
db('Rift Zone 29" 1', 'Rift Zone 29" 1', 'rift-zone-29-1')
db('Rift Zone 27.5" XR', 'Rift Zone 27.5" 3', 'rift-zone-27.5-xr')
db('Rift Zone 27.5" 2', 'Rift Zone 27.5" 2', 'rift-zone-27.5-2')
db('Rift Zone 27.5" 1', 'Rift Zone 27.5" 1', 'rift-zone-27.5-1')
db('San Quentin 3', 'San Quentin 3', 'san-quentin-3')
db('San Quentin 2', 'San Quentin 2', 'san-quentin-2')
db('San Quentin 1', 'San Quentin 1', 'san-quentin-1')
db('San Quentin 3 Frame Kit', 'San Quentin 3 Frame Kit', 'san-quentin-3-frame-kit')
db('El Roy', 'El Roy', 'el-roy')

db('El Roy Frame Kit', 'El Roy Frame Kit', 'el-roy-frame-kit')
db('Bobcat Trail 5', 'Bobcat Trail 5', 'bobcat-trail-5')
db('Bobcat Trail 4', 'Bobcat Trail 4', 'bobcat-trail-4')
db('Bobcat Trail 3', 'Bobcat Trail 3', 'bobcat-trail-3')
db('Bolinas Ridge 2', 'Bolinas Ridge 2', 'bolinas-ridge-2')
db('Bolinas Ridge 1', 'Bolinas Ridge 1', 'bolinas-ridge-1')
db('Wildcat Trail 3', 'Wildcat Trail 3', 'wildcat-trail-3')
db('Wildcat Trail 1', 'Wildcat Trail 1', 'wildcat-trail-1')
db('Team Marin 2', 'Team Marin 2', 'team-marin-2')
db('Team Marin 1', 'Team Marin 1', 'team-marin-1')
db('Pine Mountain 2', 'Pine Mountain 2', 'pine-mountain-2')
db('Pine Mountain 1', 'Pine Mountain 1', 'pine-mountain-1')
db('Alcatraz', 'Alcatraz', 'alcatraz')
db('Alcatraz Frame Kit', 'Alcatraz Frame Kit', 'alcatraz-frame-kit')
db('Headlands 2', 'Headlands 2', 'headlands-2')
db('Headlands 1', 'Headlands 1', 'headlands-1')
db('Headlands Frame Kit', 'Headlands Frame Kit', 'headlands-frame-kit')
db('Gestalt XR', 'Gestalt X11', 'gestalt-xr')
db('Gestalt X10', 'Gestalt X10', 'gestalt-x10')

db('Gestalt 2', 'Gestalt 2', 'gestalt-2')
db('Gestalt 1', 'Gestalt 1', 'gestalt-1')
db('Gestalt', 'Gestalt', 'gestalt')
db('Nicasio 2', 'Nicasio 2', 'nicasio-2')

db('Nicasio+', 'Nicasio+', 'nicasio-plus')
db('Nicasio', 'Nicasio', 'nicasio')
db('Four Corners', 'Four Corners', 'four-corners')
db('Lombard 1', 'Lombard 1', 'lombard-1')
db('Fairfax 3', 'Fairfax 3', 'fairfax-3')
db('Fairfax 2', 'Fairfax 2', 'fairfax-2')

db('Fairfax ST 2', 'Fairfax ST 2', 'fairfax-st-2')
db('Fairfax 1', 'Fairfax 1', 'fairfax-1')
db('Fairfax ST 1', 'Fairfax ST 1', 'fairfax-st-1')
db('Presidio 3', 'Presidio 3', 'presidio-3')
db('Presidio 2', 'Presidio 2', 'presidio-2')
db('Presidio 1', 'Presidio 1', 'presidio-1')
db('Muirwoods', 'Muirwoods', 'muirwoods')
db('Larkspur 2', 'Larkspur 2', 'larkspur-2')
db('Larkspur 1', 'Larkspur 1', 'larkspur-1')
db('San Rafael DS2', 'San Rafael DS2', 'san-rafael-ds2')

db('San Rafael DS1', 'San Rafael DS1', 'san-rafael-ds1')

db('San Anselmo DS2', 'San Anselmo DS2', 'san-anselmo-ds2')

db('San Anselmo DS1', 'San Anselmo DS1', 'san-anselmo-ds1')

db('DSX FS', 'DSX FS', 'dsx-fs')
db('DSX 2', 'DSX 2', 'dsx-2')

db('DSX 1', 'DSX 1', 'dsx-1')
db('DSX', 'DSX', 'dsx')
db('Kentfield 2', 'Kentfield 2', 'kentfield-2')
db('Kentfield ST 2', 'Kentfield ST 2', 'kentfield-st-2')
db('Kentfield 1', 'Kentfield 1', 'kentfield-1')
db('Kentfield ST 1', 'Kentfield ST 1', 'kentfield-st-1')
db('Stinson 2', 'Stinson 2', 'stinson-2')
db('Stinson ST 2', 'Stinson ST 2', 'stinson-st-2')
db('Stinson 1', 'Stinson 1', 'stinson-1')
db('Stinson ST 1', 'Stinson ST 1', 'stinson-st-1')
db('Rift Zone 26"', 'Rift Zone 26', 'rift-zone-26')
db('Rift Zone Jr 24"', 'Rift Zone Jr 24', 'rift-zone-jr-24')
db('San Quentin 24"', 'San Quentin 24', 'san-quentin-24')
db('San Quentin 20"', 'San Quentin 20', 'san-quentin-20')
db('Bayview Trail 24"', 'Bayview Trail 24', 'bayview-trail-24')
db('Hidden Canyon 20"', 'Hidden Canyon 20', 'hidden-canyon-20')
db('Sausalito E2', 'Sausalito E2', 'sausalito-e2')
db('Sausalito ST E2', 'Sausalito ST E2', 'sausalito-st-e2')
db('Sausalito E1', 'Sausalito E1', 'sausalito-e1')
db('Sausalito ST E1', 'Sausalito ST E1', 'sausalito-st-e1')
"""
db('Stinson Electric', 'Stinson Electric', 'stinson-electric')
db('Stinson Electric ST', 'Stinson Electric ST', 'stinson-electric-st')