"""
Init
This program creates New Bike Entries from bikeListNew in bikeList

Should be used only for bikes that are NEW and not carry forward
This program runs first generally in a model year
"""

import openpyxl, os, time
from selenium import webdriver
from bikeList_2023 import bikeList, bikeListNew, familyDict, typeDict
from x_functions import x_click, x_delay_click,x_login, x_drop
from mFunctions import *

"""
os.chdir(os.environ[MARIN_URL_TESTING_BACKSTAGE])
browser = webdriver.Firefox()
"""

#
#
#
SaveState = define_save_state()
#
#
#

#Change this on ERROR to start on correct bike
start=0
i=start

def init(bike, typeName, familyName):

    print(f'    BEGIN init |{i}| for {bike} \n')
    yearPrefix = modelYear

    NavBikes()

    click_NewBike()
    """
    Begin NEW BIKE
    """
    
    #check title for load
    x_delay_click(bikePD['Title'])

    #enter title field
    xKeys(bikePD['Title'], f'{yearPrefix} {bike}')
    print('title entered')

    #enter name field
    xKeys(bikePD['Bike_Name'], f'{bike}')
    print('name entered')

    #Default Image Drop Down
    x_drop(bikePD['Grid_Image'], '/html/body/div[4]/div[1]/div/div[2]/div[2]/div/table/tbody/tr[1]/th')
    print('default grid image selected')
        #categories TAB
    x_delay_click(bikePD['Categories'])
    print('switch to Categories Tab')

    #Model Family Drop Down
    x_drop(bikePD['Model_Family'], f"//div[@data-label='{familyName}']")
    print('model family selected')

    #Model Year Drop Down
    #ANNUAL UPDATE
    x_drop(bikePD['Model_Year'], "//div[@data-label=\'2023\']")
    print('model year selected')

    #Bike Type Drop Down
    x_drop(bikePD['Bike_Type'], f"//div[@data-label='{typeName}']")
    print('bike type selected')

    #Disable
    x_delay_click(bikePD['Live_Drop'])
    x_delay_click(bikePD['Live_Toggle'])
    print('bike set to Disabled')
    time.sleep(5)
    
    SaveBike(bike, SaveState, False)
    
    print(f'    END init |{i}| for {bike}\n')
    waitForTasks()
    

#Runtime

backstage_login()

#Programatic bike creation via bikeListNew
"""
for item in bikeListNew[start:]:

    init(item)
    i += 1
"""

#Individual bike creation via custom function calls
"""
init('Rift Zone 29\" XR', 'Mountain', 'Rift Zone 29')
init('Rift Zone 27.5\" XR', 'Mountain', 'Rift Zone 27.5')
init('San Quentin Frame Kit', 'Mountain', 'San Quentin')
init('Wildcat Trail 2', 'Mountain', 'Wildcat Trail')
init('Gestalt XR', 'Drop Bar', 'Gestalt')
"""
init('Rift Zone 26\"', 'Youth/Kids', 'Rift Zone 26\"/Jr')
init('Alpine Trail E', 'eBikes', 'Alpine Trail E')