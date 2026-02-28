"""
BikeDescriptionTranslate
Used for applying translations en masse to same bikes

descriptionlist[] stores descriptions captured from the page of the bike parameter
these are added to the pages of the bikes in applylist[]
"""

"""
Pseudo

Go to original bike

for languages
    open bike
    switch to html
    copy html description

    manually create list to apply translations
    for item in list
        switch language
        open bike
        switch html
        paste translation
        save
        wait
"""

import openpyxl, os, time
from selenium import webdriver
from bikeList import bikeList
from x_functions import x_click, x_delay_click, x_drop, x_login
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#
#Source
"""
newLocaleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""
#Mod
newLocaleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def translateDescription(bike):
    descriptionList = []
    for i in newLocaleList:
        waitForTasks()
        NavBikes()
        #set language from drop down
        x_delay_click(mainPD['Language_Drop'])
        #select language
        x_click(f'//*[@id="null-option-{str(i)}"]')
        LoadSearch()
        search('2022', bike)

        x_delay_click(bikePD['DescriptionHTMLSwitch'])
        time.sleep(2)
        description = x_get_text(bikePD['Description'])
        descriptionList.append(description)
        
    for x in descriptionList:
            print(x)
    applyList = ['Fairfax 2', 'Fairfax ST 2', 'Fairfax 1', 'Fairfax ST 1',]

    for b in applyList:
        for i in newLocaleList:
            print(f'\n\nentering description for {b} language {i}')
            NavBikes()
            waitForTasks()
            #set language from drop down
            x_delay_click(mainPD['Language_Drop'])
            #select language
            x_click(f'//*[@id="null-option-{str(i)}"]')
            LoadSearch()
            search('2022', b)

            x_delay_click(bikePD['DescriptionHTMLSwitch'])
            time.sleep(2)
            x_replace_field(bikePD['Description'], descriptionList[i])
            SaveBike(b, SaveState, False, 200)
    
    

"""
Runtime
"""
runtime()

"""
Site Navigation
"""

backstage_login()

click_Entries()
"""
SetLanguage(languagePD[languageEntry])
"""
LoadSearch()

"""
Function Calls
"""

"""
FINISHED
"""

translateDescription('Fairfax 3')


