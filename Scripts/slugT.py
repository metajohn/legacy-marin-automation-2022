#translates slugs from english bike to all other sites
#this is necessary after duplicating bikes (running  dupe.py) that were previously a different year.

"""
TODO
"""

import openpyxl, os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop,x_login
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#


#localelist
#All Languages
newLocaleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""
#Selected Languages
newLocaleList = [0]
"""
slugprefix = modelYear + '-'


def slugT(bike, slug):

    for i in newLocaleList:
        NavBikes()
        #set language from drop down
        x_delay_click(mainPD['Language_Drop'])
        #select language
        x_click(f'//*[@id="null-option-{str(i)}"]')

        print(f'\nStarting slug translation for language {i}')
        print(f'Bike == {bike}\n')
        
        #use search to check for load
        x_delay_click(mainPD['Search'])
        
        search(modelYear, bike)
        #replace slug
        LoadBike(bike)
        x_replace_field(bikePD['Slug'], (slugprefix + slug))

        SaveBike(bike, SaveState, False)

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



slugT('Alpine Trail Carbon 2', 'alpine-trail-carbon-2')
slugT('Alpine Trail Carbon 1', 'alpine-trail-carbon-1')
slugT('Alpine Trail XR', 'alpine-trail-xr')
slugT('Alpine Trail 7', 'alpine-trail-7')
slugT('Alpine Trail Carbon 2 Frame Kit', 'alpine-trail-carbon-2-frame-kit')
slugT('Alpine Trail E2', 'alpine-trail-e2')
slugT('Alpine Trail E1', 'alpine-trail-e1')
slugT('Rift Zone 29" Carbon XR', 'rift-zone-29-carbon-xr')
slugT('Rift Zone 29" Carbon 2', 'rift-zone-29-carbon-2')
slugT('Rift Zone 29" Carbon 1', 'rift-zone-29-carbon-1')
slugT('Rift Zone 29" Carbon XR Frame Kit', 'rift-zone-29-carbon-xr-frame-kit')
slugT('Rift Zone 29" XR', 'rift-zone-29-xr')
slugT('Rift Zone 29" 2', 'rift-zone-29-2')
slugT('Rift Zone 29" 1', 'rift-zone-29-1')
slugT('Rift Zone 27.5" XR', 'rift-zone-275-xr')
slugT('Rift Zone 27.5" 2', 'rift-zone-275-2')
slugT('Rift Zone 27.5" 1', 'rift-zone-275-1')
slugT('San Quentin 3', 'san-quentin-3')
slugT('San Quentin 2', 'san-quentin-2')
slugT('San Quentin 1', 'san-quentin-1')

slugT('San Quentin 3 Frame Kit', 'san-quentin-3-frame-kit')
slugT('El Roy', 'el-roy')
slugT('El Roy Frame Kit', 'el-roy-frame-kit')
slugT('Bobcat Trail 5', 'bobcat-trail-5')
slugT('Bobcat Trail 4', 'bobcat-trail-4')
slugT('Bobcat Trail 3', 'bobcat-trail-3')
slugT('Bolinas Ridge 2', 'bolinas-ridge-2')
slugT('Bolinas Ridge 1', 'bolinas-ridge-1')
slugT('Wildcat Trail 3', 'wildcat-trail-3')
slugT('Wildcat Trail 1', 'wildcat-trail-1')
slugT('Team Marin 2', 'team-marin-2')
slugT('Team Marin 1', 'team-marin-1')
slugT('Pine Mountain 2', 'pine-mountain-2')
slugT('Pine Mountain 1', 'pine-mountain-1')
slugT('Alcatraz', 'alcatraz')
slugT('Alcatraz Frame Kit', 'alcatraz-frame-kit')
slugT('Headlands 2', 'headlands-2')
slugT('Headlands 1', 'headlands-1')
slugT('Headlands Frame Kit', 'headlands-frame-kit')
slugT('Gestalt XR', 'gestalt-xr')
slugT('Gestalt X10', 'gestalt-x10')
slugT('Gestalt 2', 'gestalt-2')
slugT('Gestalt 1', 'gestalt-1')
slugT('Gestalt', 'gestalt')
slugT('Nicasio 2', 'nicasio-2')
slugT('Nicasio+', 'nicasio-plus')
slugT('Nicasio', 'nicasio')
slugT('Four Corners', 'four-corners')
slugT('Lombard 1', 'lombard-1')
slugT('Fairfax 3', 'fairfax-3')
slugT('Fairfax 2', 'fairfax-2')
slugT('Fairfax ST 2', 'fairfax-st-2')
slugT('Fairfax 1', 'fairfax-1')
slugT('Fairfax ST 1', 'fairfax-st-1')
slugT('Presidio 3', 'presidio-3')
slugT('Presidio 2', 'presidio-2')
slugT('Presidio 1', 'presidio-1')
slugT('Muirwoods', 'muirwoods')
slugT('Larkspur 2', 'larkspur-2')
slugT('Larkspur 1', 'larkspur-1')
slugT('San Rafael DS2', 'san-rafael-ds2')
slugT('San Rafael DS1', 'san-rafael-ds1')
slugT('San Anselmo DS2', 'san-anselmo-ds2')
slugT('San Anselmo DS1', 'san-anselmo-ds1')
slugT('DSX FS', 'dsx-fs')
slugT('DSX 2', 'dsx-2')
slugT('DSX 1', 'dsx-1')

slugT('DSX', 'dsx')
slugT('Kentfield 2', 'kentfield-2')
slugT('Kentfield ST 2', 'kentfield-st-2')
slugT('Kentfield 1', 'kentfield-1')
slugT('Kentfield ST 1', 'kentfield-st-1')
slugT('Stinson 2', 'stinson-2')
slugT('Stinson ST 2', 'stinson-st-2')
slugT('Stinson 1', 'stinson-1')
slugT('Stinson ST 1', 'stinson-st-1')

slugT('Rift Zone 26"', 'rift-zone-26')
"""
slugT('Rift Zone Jr 24"', 'rift-zone-jr-24')
slugT('San Quentin 24"', 'san-quentin-24')
slugT('San Quentin 20"', 'san-quentin-20')
slugT('Bayview Trail 24"', 'bayview-trail-24')
slugT('Hidden Canyon 20"', 'hidden-canyon-20')
slugT('Sausalito E2', 'sausalito-e2')
slugT('Sausalito ST E2', 'sausalito-st-e2')
slugT('Sausalito E1', 'sausalito-e1')
slugT('Sausalito ST E1', 'sausalito-st-e1')

