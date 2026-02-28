#launches 2022 bikes and archives 2021 version"
import time
from x_functions import x_click, x_delay_click, x_drop, x_login, x_get_value, x_print_time, startTime
from mFunctions import *

"""
"""

#
#
#
SaveState = define_save_state()
#
#
#

def regionCheck(bike, UK, Australia, Poland, Czech, Finland, Spain, Ecuador, Canada, International, Germany, Russia, France, Spanish, India, NZ, Ukraine):
    waitForTasks()
    print(f'    START Region Set for {bike}\n')
    #load 2022 bike
    LoadSearch()
    search('2022', bike)
    LoadBike(bike)

    #enable 2022 bike
    x_delay_click(bikePD['Live_Drop'])
    time.sleep(2)
    if UK != 'UK':
        x_click('//*[@id="enabledForSite-2"]/div/div')
    if Australia != 'Australia':
        x_click('//*[@id="enabledForSite-3"]/div/div')
    if Poland != 'Poland':
        x_click('//*[@id="enabledForSite-4"]/div/div')
    if Czech != 'Czech':
        x_click('//*[@id="enabledForSite-5"]/div/div')
    if Finland != 'Finland':
        x_click('//*[@id="enabledForSite-6"]/div/div')
    if Spain != 'Spain':
        x_click('//*[@id="enabledForSite-7"]/div/div')
    if Ecuador != 'Ecuador':
        x_click('//*[@id="enabledForSite-8"]/div/div')
    if Canada != 'Canada':
        x_click('//*[@id="enabledForSite-9"]/div/div')
    if International != 'International':
        x_click('//*[@id="enabledForSite-10"]/div/div')
    if Germany != 'Germany':
        x_click('//*[@id="enabledForSite-11"]/div/div')
    if Russia != 'Russia':
        x_click('//*[@id="enabledForSite-12"]/div/div')
    if France != 'France':
        x_click('//*[@id="enabledForSite-13"]/div/div')
    if Spanish != 'Spanish':
        x_click('//*[@id="enabledForSite-14"]/div/div')
    if India != 'India':
        x_click('//*[@id="enabledForSite-15"]/div/div')
    if NZ != 'NZ':
        x_click('//*[@id="enabledForSite-16"]/div/div')
    if Ukraine != 'Ukraine':
        x_click('//*[@id="enabledForSite-17"]/div/div')
    print(f'{bike} regions set')
    time.sleep(5)

    SaveBike(bike, SaveState)

    print(f'    END Region Set for {bike}\n')

"""
Runtime
"""
runtime()

startTime()

"""
Site Navigation
"""

backstage_login()

waitForTasks()

NavBikes()

LoadSearch()


"""
FINISHED


regionCheck('Bobcat Trail 4', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Muirwoods', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail E2', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail E1', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail Carbon 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', '_DIS_', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail Carbon 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail XR', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail 7', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Alpine Trail Carbon 2 Frame Kit', 'UK', 'Australia', 'Poland', '_DIS_', '_DIS_', '_DIS_', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', '_DIS_', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 29" 3', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 29" 2', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 29" 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 27.5" 3', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 27.5" 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 27.5" 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone 26"', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('El Roy', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('El Roy Frame Kit', 'UK', 'Australia', '_DIS_', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Quentin 3', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Quentin 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Quentin 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Quentin 3 Frame Kit', 'UK', 'Australia', '_DIS_', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Bolinas Ridge 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Bobcat Trail 3', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Team Marin 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Team Marin 1', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Pine Mountain E2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Pine Mountain E1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Pine Mountain 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Pine Mountain 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Headlands 1', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Headlands Frame Kit', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Gestalt X11', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Gestalt X10', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Gestalt 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Gestalt 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Gestalt', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('DSX 2', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('DSX 1', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Nicasio 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Nicasio', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Nicasio +', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Lombard 1', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Four Corners', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Muirwoods RC', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Presidio 3', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Presidio 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Presidio 1', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Rafael DS2', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Rafael DS1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Anselmo DS2', 'UK', 'Australia', 'Poland', 'Czech', 'Finland', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Anselmo DS1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Sausalito E2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Sausalito ST E2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Sausalito E1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Sausalito ST E1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Kentfield 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Kentfield ST 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Kentfield 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Kentfield ST 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Larkspur 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Larkspur 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Stinson 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Stinson ST 2', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Stinson 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Stinson ST 1', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', '_DIS_', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('Rift Zone Jr 24', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', 'NZ', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Quentin 24', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regionCheck('San Quentin 20', 'UK', 'Australia', 'Poland', 'Czech', '_DIS_', 'Spain', 'Ecuador', 'Canada', 'International', 'Germany', 'Russia', 'France', 'Spanish', 'India', '_DIS_', 'Ukraine')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
End Calls
"""
startTime()
x_print_time()