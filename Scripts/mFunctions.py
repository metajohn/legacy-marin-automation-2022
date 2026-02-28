"""
mFunctions
The main directory for Marin related functions

ALWAYS MAKE SURE TO UPDATE MODEL YEAR ANNUALLY 

INDEX

Dicts
    bikePD
    mainPD
    languagePD

TODO:
    Make sure all programs that reference this are using new model year variables
"""

from x_functions import *
from notificationbot import notifyOfStall
import login
import time
import os
import sys
import string
from selenium.webdriver.common.by import By

#MAIN URL
url_backstage = os.environ['MARIN_URL_LIVE_BACKSTAGE']

#ANNUAL UPDATE
modelYear = '2023'
lastModelYear = '2022'


#TESTING URL
"""
url = 'os.environ['MARIN_URL_TESTING_BACKSTAGE']'
"""

entryPath = '//*[@id="nav-entries"]/a/span[2]'
assetsPath = '//*[@id="nav-assets"]/a/span[2]'
bikePath = '//*[@id="sidebar"]/nav/ul/li[11]/a/span'

bikePD = {'Title': '//*[@id="title"]', 
            'Bike_Name': '//*[@id="fields-bikeName"]' ,
            'Price': '//*[@id="fields-bikePrice"]' ,
            'Slug': '//*[@id="slug"]',
            'Grid_Image': '//*[@id="fields-bikeGridImage"]/div[2]/button[1]' ,
            'Grid_Image_Search': '/html/body/div[4]/div[1]/div/div[2]/div[1]/div[1]/input',
            'DescriptionHTMLSwitch': '//*[@id="fields-bikeDescription-field"]/div[2]/div/div/div[1]/div/a[1]/i',
            'Description': '//*[@id="fields-bikeDescription"]',
            'Categories': '//*[@id="tab-tab-categories"]',
            'Model_Family': '//*[@id="fields-bikeModelFamily"]/div[2]/button',
            'Model_Year': '//*[@id="fields-bikeModelYear"]/div[2]/button',
            'Bike_Type': '//*[@id="fields-bikeTypes"]/div[2]/button',
            "Bike_Uses": '//*[@id="fields-bikeUses"]/div[2]/button',
            'Frame_Types': '//*[@id="fields-bikeFrameTypes"]/div[2]/button',
            'Frame_Material': '//*[@id="fields-bikeFrameMaterial"]/div[2]/button',
            'Wheel_Sizes': '//*[@id="fields-bikeWheelSizes"]/div[2]/button',
            'Bike_Status_Drop': '//*[@id="fields-bikeStatus"]',
            'Bike_Status_Active': '//*[@id="fields-bikeStatus"]/option[1]',
            'Bike_Status_Archive': '//*[@id="fields-bikeStatus"]/option[2]',
            'Save': '//*[@id="save-btn-container"]/button[1]',
            'Save_Drop': '//*[@id="save-btn-container"]/button[2]',
            'Save_Copy': '//*[@id="null-option-2"]',
            'Live_Toggle': '//*[@id="enabled"]/div/div',
            'Live_Drop': '//*[@id="expand-status-btn"]',
            'Spec': '//*[@id="tab-tab-specifications"]',
            'New_Spec': '//*[@id="fields-bikeSpecifications"]/div[2]/div/button',
            'Geo': '//*[@id="tab-tab-geometry"]',
            'New_Geo': '//*[@id="fields-bikeGeometryTable-field"]/div[3]/button',
            'Related': '//*[@id="tab-tab-related"]',
        }

mainPD = {'Language_Drop': '//*[@id="context-btn"]',
            'Search': '//*[@id="toolbar"]/div[2]/input',

}

languagePD = {
            'English': '//*[@id="null-option-0"]',
            'UK': '//*[@id="null-option-1"]',
            'Australia': '//*[@id="null-option-2"]',
            'Poland': '//*[@id="null-option-3"]',
            'Czech': '//*[@id="null-option-4"]',
            'Finland': '//*[@id="null-option-5"]',
            'Spain': '//*[@id="null-option-6"]',
            'Ecuador': '//*[@id="null-option-7"]',
            'Canada': '//*[@id="null-option-8"]',
            'International': '//*[@id="null-option-9"]',
            'Germany': '//*[@id="null-option-10"]',
            'Russia': '//*[@id="null-option-11"]',
            'France': '//*[@id="null-option-12"]',
            'Spanish': '//*[@id="null-option-13"]',
            'India': '//*[@id="null-option-14"]',
            'New Zealand': '//*[@id="null-option-15"]',
            'Ukraine': '//*[@id="null-option-16"]',
}

languageKD = ['English,' ,'UK' ,'Australia' ,'Poland' ,'Czech' ,'Finland' ,'Spain' ,'Ecuador' ,'Canada' ,'International' ,'Germany' ,'Russia' ,'France', '']

"""
Functions
"""

def backstage_login():
    x_login(url_backstage, login.marin_backstage_username, login.marin_backstage_password)

def define_save_state():
    try:
        SaveStateDefinition = sys.argv[1]
        print(f'***SaveState is {SaveStateDefinition}***\n\n' )
    except(IndexError):
        SaveStateDefinition = 'test'
        print(f'***SaveState is {SaveStateDefinition}***\n\n' )
    return SaveStateDefinition

def xCheckStillExists(xpath, loadingString):
    animation = "|/-\\"
    exists = True
    while(exists):
        try:
            browser.find_element(By.XPATH, xpath)
            exists = True
            for i in range(30):
                time.sleep(0.1)
                sys.stdout.write(loadingString + "\r" + animation[i % len(animation)])
                sys.stdout.flush()
            LoadSearch()
            click_Entries_Silent()
            LoadSearch()
        except Exception:
            exists = False

def runtime():
    os.chdir(os.environ['WEBDRIVER'])

def NavBikes():
    click_Entries()

    url_Bikes()

def NavFamily():
    click_Entries()

    url_Family()

def BeginEntry():
    click_Entries()

def LoadBike(bike):
    #use title to check for load
    x_delay_click(bikePD['Title'])
    print('     Entry Open: ' + bike)

def LoadSearch():
    x_delay_click(mainPD['Search'])

def SetLanguage(languagePath):
    """needs the xpath of the language, not the language string"""
    #set language from drop down
    x_delay_click(mainPD['Language_Drop'])
    time.sleep(1)
    #select language
    x_click(languagePath)

#Save wait time value for functions

#Save functions
def SaveBike(bike, test, waitForTasksBool = False, timeToWaitForSave = 200):
    #Save Entry
    if (test == 'live' or test == 'cycle' or test == 'save'):
        print('debug is false')
    else:
        print('\n\n***testmode WILL NOT SAVE...\n type \'y\' to SAVE \n type \'skip\' to continue without saving \n type any other to QUIT***\n\n')
        u = input()
        u = u.lower()
        if u == 'y':
            x_click(bikePD['Save'])
            print('\n     Saved: ' + bike + '\n\n')
            if(waitForTasksBool == True):
                waitForTasks()
            else:
                print('ignoring tasks queue')
        elif u == 'skip':
            print('Save function set to cycle')
            print('continuing without saving')
        else:
            quit()
    if (test == 'live' or test == 'save'):
        x_click(bikePD['Save'])
        print('\n     Saved: ' + bike + '\n\n')
        if(waitForTasksBool == True):
            waitForTasks()
        else:
            print('ignoring tasks queue')
            x_wait(timeToWaitForSave)
    elif (test == 'cycle'):
        print('Save function set to cycle')
        print('continuing without saving')

def SaveBike_Copy(bike, test, waitForTasksBool = False):
    #Save Entry as copy
    if (test == 'live' or test == 'cycle' or test == 'save'):
        print('SaveBike_Copy - function is NOT TEST')
    else:
        print('\n\n***testmode WILL NOT SAVE...\n type \'y\' to SAVE \n type \'skip\' to continue without saving \n type any other to QUIT***\n\n')
        u = input()
        u = u.lower()
        if u == 'y':
            x_click(bikePD['Save_Drop'])
            x_delay_click(bikePD['Save_Copy'])
            print('     Saved: ' + bike + '\n')
            if(waitForTasksBool == True):
                waitForTasks()
            else:
                print('ignoring tasks queue')
        elif u == 'skip':
            print('Save function set to cycle')
            print('continuing without saving')
        else:
            quit()
    if (test == 'live' or test == 'save'):
        x_click(bikePD['Save_Drop'])
        x_delay_click(bikePD['Save_Copy'])
        print('     Saved: ' + bike + '\n')
        x_print_time()
        if(waitForTasksBool == True):
            waitForTasks()
        else:
            print('ignoring tasks queue')
    elif (test == 'cycle'):
        print('SaveBike_Copy - function set to cycle')
        print('continuing without saving')


def endp():
    print('-----------------------------------')

def waitForTasks():
        click_Entries_Silent()
        LoadSearch()
        xCheckStillExists('//*[@id="job-icon"]/span[1]', 'waiting for tasks to complete')
        print('-----------------------------------')

"""
Navigation
"""



def url_Entries():
    print("-> Navigating via URL : Entries ")
    browser.get(url_backstage + 'entries')

def click_Entries():
    print("-> Navigating via x_delay_click : Entries ")
    x_delay_click(entryPath)

def click_Entries_Silent():
    x_delay_click(entryPath)

def url_Assets():
    print("-> Navigating via URL : Assets ")
    browser.get(url_backstage + 'assets')

def click_Assets():
    print("-> Navigating via x_delay_click : Assets ")
    x_delay_click(assetsPath)
    
def url_Bikes():
    print("-> Navigating via URL : Bikes ")
    browser.get(url_backstage + 'entries/bikes')

def url_Family():
    print("-> Navigating via URL : Bike Family ")
    browser.get(url_backstage + 'entries/modelFamilies')

def click_Bikes():
    print("-> Navigating via x_delay_click : Bikes ")
    x_delay_click(bikePath)

def click_NewBike():
    print("-> Navigating via x_delay_click : NEW Bike ")
    x_delay_click('//*[@id="action-button"]/div/a')

def click_SaveEntry():
    print("+ Saving via x_delay_click")
    x_delay_click('/html/body/div[1]/li/div[3]/main/form/div[1]/header/div[2]/div[2]/button[1]')

"""
Utilities
"""



def dictFormat(item):
    itemFormat = item.replace(' ', '')
    itemFormat = itemFormat.replace('"', '')
    itemFormat = itemFormat.replace('.', '')
    itemFormat = itemFormat.replace('+', 'plus')
    return itemFormat

"""
Search
"""

#TODO improve search to avoid occasional hiccups
#TODO write test function that continuously searches to see where it hangs up
def search(yearPrefix, bikeTitle):
    
    #declare variables before engaging in pseudo-endless search loop
    repeatCheck = 0
    entryFound = False
    textBoxPath = '//*[@id="toolbar"]/div[2]/input'
    textBox = browser.find_element(By.XPATH, '//*[@id="toolbar"]/div[2]/input')

    """
    TODO
    take name and if it fails, strip the symbols and check again.
    use symbolcheck to flag for condition, use i to save position of cursed ' " '
    """
    symbolCheck = False

    while(entryFound == False):
        time.sleep(1)
        if bikeTitle == 'Four Corners':
            textBox.send_keys(yearPrefix + ' ' + 'Corners')
        else:
            textBox.send_keys(yearPrefix + ' ' + bikeTitle)
        time.sleep(3)
        if (repeatCheck < 2):
            # Click on Entry
            try:
                time.sleep(1)
                x_click("//div[@data-label='" +
                       yearPrefix + ' ' + bikeTitle + "']")
                entryFound = True
            except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
                    x_replace_field(textBoxPath, '')
            repeatCheck += 1
        else:
            # Click on Entry
            try:
                x_click("//div[@data-label='" + yearPrefix + bikeTitle + "']")
                entryFound = True
            except (NoSuchElementException, AttributeError, ElementClickInterceptedException) as e:
                notifyOfStall(f'Search->could not locate entry:\n{yearPrefix} {bikeTitle} \n {datetime.datetime.now()} \n {e}')
                print()
                print('============Could not locate entry - ' +
                      yearPrefix + bikeTitle)
                print('Open entry manually and press ENTER ===========')
                x_print_time('Search stalled: ')
                input()
                entryFound = True
                time.sleep(1)