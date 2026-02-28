#designed to flip the updated bikes to the current model year

from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop,x_login
from mFunctions import *



newRelatedBikePath = '//*[@id="fields-bikeRelated"]/div[2]/button'
relatedPaths = ['//*[@id="fields-bikeRelated"]/div[1]/div[1]/div/span', '//*[@id="fields-bikeRelated"]/div[1]/div[2]/div/span', '//*[@id="fields-bikeRelated"]/div[1]/div[3]/div/span']
hasNoRelatedBikes = []

def updateRelatedBikes(bike):
    #
    #
    #
    SaveState = define_save_state()
    #
    #
    #
    NavBikes()
    #waitForTasks()

    print(f'    BEGIN updateRelatedBikes for {bike} \n')

    #search
    search(modelYear, bike)

    #Begin duplication
    print('     Entry Open: ' + bike)
    x_delay_click(bikePD['Related'])
    relatedBikesOld = []
    time.sleep(4)
    try:
        x_click(relatedPaths[0])
    except(NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
        hasNoRelatedBikes.append(bike)
        print(f'{bike} has no related bikes')
        SaveState = define_save_state()

    try:
        #bike 1 already confirmed but needs to be stored
        relatedBikesOld.append(x_get_text(relatedPaths[0]))
        numberOfRelatedBikes = 1

        #bike 2
        x_click(relatedPaths[1])
        relatedBikesOld.append(x_get_text(relatedPaths[1]))
        numberOfRelatedBikes = 2

        #bike 3
        x_click(relatedPaths[2])
        relatedBikesOld.append(x_get_text(relatedPaths[2]))
        numberOfRelatedBikes = 3

    except(NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
        notifyOfStall(f'updatedRelatedBikes failed accessing related bikes on bike: {bike} and has skipped this entry')
        return
    #delete entries
    for i in range(1, numberOfRelatedBikes + 1):
        x_delay_click('//*[@id="fields-bikeRelated"]/div[1]/div[1]/button')
        time.sleep(1)
    #refill entries
    for i in range(1, numberOfRelatedBikes + 1):
        #format new bike Name
        newBikeName = relatedBikesOld[i-1]
        newBikeName = newBikeName[4:len(newBikeName)]
        newBikeName = modelYear + newBikeName
        print(newBikeName)
        if(newBikeName == '2023 Rift Zone 29 3'):
            newBikeName = '2023 Rift Zone 29 XR'
        elif(newBikeName == '2023 Muirwoods RC'):
            continue
        if(newBikeName == '2023 Rift Zone 29" 3'):
            newBikeName = '2023 Rift Zone 29" XR'
        elif(newBikeName == '2023 Rift Zone 27.5 3'):
            newBikeName = '2023 Rift Zone 27.5 XR'
        elif(newBikeName == '2023 Gestalt 2.5'):
            newBikeName = '2023 Gestalt 2'
        elif(newBikeName == '2023 Rift Zone 27.5" 3'):
            newBikeName = '2023 Rift Zone 27.5" XR'
        elif(newBikeName == '2023 Gestalt X11'):
            newBikeName = '2023 Gestalt XR'
        elif(newBikeName == '2023 Rift Zone Jr 24'):
            newBikeName = '2023 Rift Zone Jr 24"'
        elif(newBikeName == '2023 San Quentin 20'):
            newBikeName = '2023 San Quentin 20"'
        elif(newBikeName == '2023 San Quentin 24'):
            newBikeName = '2023 San Quentin 24"'
        elif(newBikeName == '2023 Bayview Trail 24'):
            newBikeName = '2023 Bayview Trail 24"'
        elif(newBikeName == '2023 Hidden Canyon 20'):
            newBikeName = '2023 Hidden Canyon 20"' 
        try:
            x_click(newRelatedBikePath)
            #wait for search to load
            time.sleep(2)
            x_replace_field('/html/body/div[5]/div[1]/div/div[2]/div[1]/div[3]/input', newBikeName)
            time.sleep(2)
            x_double("//div[@data-label='" +newBikeName+"']")
            
        except(NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
            notifyOfStall(f'updaterelatedbikes Stalled on {bike} adding new related bike')
            print(f'add {newBikeName} below manually and press enter to continue script')
            input()

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


updateRelatedBikes('Alpine Trail Carbon 2')
updateRelatedBikes('Alpine Trail Carbon 1')
updateRelatedBikes('Alpine Trail XR')
updateRelatedBikes('Alpine Trail 7')
updateRelatedBikes('Alpine Trail Carbon 2 Frame Kit')
updateRelatedBikes('Alpine Trail E2')
#below has no related bikes
updateRelatedBikes('Alpine Trail E1')

updateRelatedBikes('Rift Zone 29" Carbon XR')
updateRelatedBikes('Rift Zone 29" Carbon 2')
updateRelatedBikes('Rift Zone 29" Carbon 1')
updateRelatedBikes('Rift Zone 29" Carbon XR Frame Kit')
updateRelatedBikes('Rift Zone 29" XR')
updateRelatedBikes('Rift Zone 29" 2')
updateRelatedBikes('Rift Zone 29" 1')

updateRelatedBikes('Rift Zone 27.5" XR')

updateRelatedBikes('Rift Zone 27.5" 2')
updateRelatedBikes('Rift Zone 27.5" 1')
updateRelatedBikes('San Quentin 3')
updateRelatedBikes('San Quentin 2')
updateRelatedBikes('San Quentin 1')
updateRelatedBikes('San Quentin 3 Frame Kit')
updateRelatedBikes('El Roy')
updateRelatedBikes('El Roy Frame Kit')
updateRelatedBikes('Bobcat Trail 5')
updateRelatedBikes('Bobcat Trail 4')
updateRelatedBikes('Bobcat Trail 3')
updateRelatedBikes('Bolinas Ridge 2')

updateRelatedBikes('Bolinas Ridge 1')
updateRelatedBikes('Wildcat Trail 3')
updateRelatedBikes('Wildcat Trail 1')
updateRelatedBikes('Team Marin 2')
updateRelatedBikes('Team Marin 1')
updateRelatedBikes('Pine Mountain 2')
updateRelatedBikes('Pine Mountain 1')
updateRelatedBikes('Alcatraz')
updateRelatedBikes('Alcatraz Frame Kit')
updateRelatedBikes('Headlands 2')
updateRelatedBikes('Headlands 1')
updateRelatedBikes('Headlands Frame Kit')
updateRelatedBikes('Gestalt XR')

updateRelatedBikes('Gestalt X10')
updateRelatedBikes('Gestalt 2')
updateRelatedBikes('Gestalt 1')

updateRelatedBikes('Gestalt')

updateRelatedBikes('Nicasio 2')

updateRelatedBikes('Nicasio+')
updateRelatedBikes('Nicasio')
updateRelatedBikes('Four Corners')
updateRelatedBikes('Lombard 1')
updateRelatedBikes('Fairfax 3')
updateRelatedBikes('Fairfax 2')
updateRelatedBikes('Fairfax ST 2')
updateRelatedBikes('Fairfax 1')
updateRelatedBikes('Fairfax ST 1')
updateRelatedBikes('Presidio 3')
updateRelatedBikes('Presidio 2')
updateRelatedBikes('Presidio 1')
updateRelatedBikes('Muirwoods')

updateRelatedBikes('Larkspur 2')

updateRelatedBikes('Larkspur 1')
updateRelatedBikes('San Rafael DS2')
updateRelatedBikes('San Rafael DS1')
updateRelatedBikes('San Anselmo DS2')
updateRelatedBikes('San Anselmo DS1')
updateRelatedBikes('DSX FS')
updateRelatedBikes('DSX 2')
updateRelatedBikes('DSX 1')
updateRelatedBikes('DSX')

updateRelatedBikes('Kentfield 2')
updateRelatedBikes('Kentfield ST 2')
updateRelatedBikes('Kentfield 1')
updateRelatedBikes('Kentfield ST 1')
updateRelatedBikes('Stinson 2')

updateRelatedBikes('Stinson ST 2')
updateRelatedBikes('Stinson 1')
updateRelatedBikes('Stinson ST 1')
updateRelatedBikes('Rift Zone 26')
updateRelatedBikes('Rift Zone JR 24"')

updateRelatedBikes('San Quentin 24"')

updateRelatedBikes('San Quentin 20"')
updateRelatedBikes('Bayview Trail 24"')
updateRelatedBikes('Hidden Canyon 20"')
updateRelatedBikes('Sausalito E2')
updateRelatedBikes('Sausalito ST E2')
updateRelatedBikes('Sausalito E1')
updateRelatedBikes('Sausalito ST E1')

updateRelatedBikes('Stinson Electric')
updateRelatedBikes('Stinson Electric ST')
"""

print('Below have no related bikes')
for i in hasNoRelatedBikes:
    print(i)