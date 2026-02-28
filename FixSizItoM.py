#replaces family sizing - imperial with metric"

import os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop, x_get_value, x_print_time
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#
#what does subBlockList do? it exists nowhere else in code
#this may have been from an earlier attempt to find each size by subblock
subBlockList = [3, 4]

# newLocaleList = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]
newLocaleList = [ 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]

def ImperialToMetric(value):
    if value == '4\'10"':
        outValue = '146cm'
    elif value == '4\'11"':
        outValue = '150cm"'
    elif value == '5\'0"':
        outValue = '152cm'
    elif value == '5\'1"':
        outValue = '155cm'
    elif value == '5\'2"':
        outValue = '157cm'
    elif value == '5\'3"':
        outValue = '160cm'
    elif value == '5\'4"':
        outValue = '163cm'
    elif value == '5\'5"':
        outValue = '165cm'
    elif value == '5\'6"':
        outValue = '168cm'
    elif value == '5\'7"':
        outValue = '170cm'
    elif value == '5\'8"':
        outValue = '173cm'
    elif value == '5\'9"':
        outValue = '175cm'
    elif value == '5\'10"':
        outValue = '178cm'
    elif value == '5\'11"':
        outValue = '180cm'
    elif value == '6\'':
        outValue = '183cm'
    elif value == '6\'1"':
        outValue = '185cm'
    elif value == '6\'2"':
        outValue = '188cm'
    elif value == '6\'3"':
        outValue = '191cm'
    elif value == '6\'4"':
        outValue = '193cm'
    else:
        outValue = value
    return outValue

def replaceSizing(family):
    # waitForTasks()
    time.sleep(2)
    print(f'\n\n    BEGIN sizing fix for {family} Metric to Imperial\n')
    for language in newLocaleList:
        NavFamily()
        time.sleep(2)
        #set language from drop down
        x_delay_click(mainPD['Language_Drop'])
        #select language
        x_delay_click(f'//*[@id="null-option-{str(language)}"]')

        LoadSearch()

        search('', family)

        LoadBike(family)
        x_delay_click('//*[@id="tab-tab-size-guide"]')
        time.sleep(2)

        for i in range(8):
            try:
                x_click(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[{i}]/div[4]/div/div[3]/div[3]/input')
                sizeValue = x_get_value(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[{i}]/div[4]/div/div[3]/div[3]/input')
                iSizeValue = ImperialToMetric(sizeValue)
                x_replace_field('/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[' + str(i) + ']/div[4]/div/div[3]/div[3]/input', iSizeValue)
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[*THISVALUEINDICATESNEWBLOCK]/div[4]/div/div[3]/div[3]/input
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[*THISVALUEINDICATESNEWBLOCK]/div[4]/div/div[*THISVALUEPERBLOCK]/div[3]/input
            except(NoSuchElementException):
                print(f"size {i} does not exist")
            time.sleep(1)
            try:
                x_click(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[{i}]/div[4]/div/div[4]/div[3]/input')
                sizeValue = x_get_value(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[{i}]/div[4]/div/div[4]/div[3]/input')
                iSizeValue = ImperialToMetric(sizeValue)
                x_replace_field(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[' + str(i) + ']/div[4]/div/div[4]/div[3]/input', iSizeValue)
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[*THISVALUEINDICATESNEWBLOCK]/div[4]/div/div[3]/div[3]/input
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[1]/div[4]/div/div[*THISVALUEPERBLOCK]/div[3]/input
            except(NoSuchElementException):
                print(f"size {i} does not exist")
            time.sleep(1)


        SaveBike(family, SaveState, False, 200)
        x_print_time()

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


replaceSizing('Alpine Trail')
replaceSizing('Rift Zone')
replaceSizing('Rift Zone 27.5')
replaceSizing('San Quentin')
replaceSizing('El Roy')
replaceSizing('Bobcat Trail')
replaceSizing('Bolinas Ridge')
replaceSizing('Wildcat Trail')
replaceSizing('Team Marin')
replaceSizing('Pine Mountain')
"""
replaceSizing('Alcatraz')
"""
replaceSizing('Headlands')
replaceSizing('Gestalt X')
replaceSizing('Gestalt')
replaceSizing('Nicasio')
replaceSizing('Four Corners')
replaceSizing('Lombard')
replaceSizing('Fairfax')
replaceSizing('Terra Linda')
replaceSizing('Presidio')
replaceSizing('Muirwoods')
replaceSizing('Larkspur')
replaceSizing('Dual Sport')
replaceSizing('DSX')
replaceSizing('Kentfield')
replaceSizing('Stinson')
replaceSizing('San Quentin 24\"/20\"')
replaceSizing('Bayview Trail')
replaceSizing('Hidden Canyon')
replaceSizing('Donky Jr.')
replaceSizing('Alpine Trail E')
replaceSizing('Pine Mountain E')
replaceSizing('Sausalito')
replaceSizing('Rift Zone 26\"/Jr')
replaceSizing('Stinson E')
"""