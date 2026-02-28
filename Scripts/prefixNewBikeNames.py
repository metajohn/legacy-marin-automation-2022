"""
prefixNewBikeTitles

adds current model year to the displayed title

Honestly I'm not sure what this does..

This may be intended for bikes that have been updated for the current year,
and does not apply to unchanged carry forwards
the name is not new, thus the need for a distinction.
"""

import login, os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click,x_login, x_drop, x_print_time
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#

def prefix(bike):
    waitForTasks()

    LoadSearch()

    search('2022', bike)

    print(f'    BEGIN prefixNewBikeTitles for {bike} \n')

    LoadBike(bike)

    x_replace_field(bikePD['Bike_Name'], f'2022 {bike}')
    print('name prefixed')

    SaveBike(bike, SaveState, False)
    print(f'    END prefixNewBikeTitles for {bike} \n')


"""
Runtime
"""
runtime()

"""
Site Navigation
"""

backstage_login()

waitForTasks()

NavBikes()

LoadSearch()

"""
Function Calls
"""

"""
FINISHED
"""

prefix('Rift Zone 29" Carbon XR Frame Kit')
prefix('Rift Zone 29" Carbon XR')
prefix('Rift Zone 29" Carbon 2')
prefix('Rift Zone 29" Carbon 1')
prefix('Alcatraz - SEP 1')
prefix('Alcatraz Frame Kit')
prefix('Bolinas Ridge 2 - Jul 1')
prefix('Wildcat Trail 3')
prefix('Wildcat Trail 1')
prefix('Bobcat Trail 5')
prefix('Bobcat Trail 4 - JUN 1')
prefix('DSX 2 FS')
prefix('DSX 2')
prefix('Muirwoods - JUN 1')
prefix('Stinson Electric')
prefix('Stinson Electric ST')
prefix('Fairfax 3')
prefix('Fairfax 2')
prefix('Fairfax ST 2')
prefix('Fairfax 1')
prefix('Fairfax ST 1')
prefix('Bayview Trail 24')
prefix('Hidden Canyon 20')

"""
End Calls
"""

x_print_time()
