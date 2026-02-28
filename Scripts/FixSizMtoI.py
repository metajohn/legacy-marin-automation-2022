#replaces family sizing - metric with imperial"

import os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop, x_login, x_get_value, x_print_time
import login
from mFunctions import *

#
#
#
SaveState = define_save_state()
x_print_time('Start Time: ')
#
#
#
subBlockList = [3, 4]

newLocaleList = [1, 8]

def MetricToImperial(value):
    if value == '146cm':
        outValue = '4\'10"'
    elif value == '150cm':
        outValue = '4\'11"'
    elif value == '152cm':
        outValue = '5\''
    elif value == '155cm':
        outValue = '5\'1"'
    elif value == '157cm':
        outValue = '5\'2"'
    elif value == '160cm':
        outValue = '5\'3"'
    elif value == '163cm':
        outValue = '5\'4"'
    elif value == '165cm':
        outValue = '5\'5"'
    elif value == '168cm':
        outValue = '5\'6"'
    elif value == '170cm':
        outValue = '5\'7"'
    elif value == '173cm':
        outValue = '5\'8"'
    elif value == '175cm':
        outValue = '5\'9"'
    elif value == '178cm':
        outValue = '5\'10"'
    elif value == '180cm':
        outValue = '5\'11"'
    elif value == '183cm':
        outValue = '6\''
    elif value == '185cm':
        outValue = '6\'1"'
    elif value == '188cm':
        outValue = '6\'2"'
    elif value == '191cm':
        outValue = '6\'4"'
    elif value == '193cm':
        outValue = '6\'5"'
    else:
        outValue = value
    return outValue

def replaceSizing(family):
    waitForTasks()
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
                iSizeValue = MetricToImperial(sizeValue)
                x_replace_field('/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[' + str(i) + ']/div[4]/div/div[3]/div[3]/input', iSizeValue)
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[*THISVALUEINDICATESNEWBLOCK]/div[4]/div/div[3]/div[3]/input
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[*THISVALUEINDICATESNEWBLOCK]/div[4]/div/div[*THISVALUEPERBLOCK]/div[3]/input
            except(NoSuchElementException):
                print(f"size {i} does not exist")
            try:
                x_click(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[{i}]/div[4]/div/div[4]/div[3]/input')
                sizeValue = x_get_value(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[{i}]/div[4]/div/div[4]/div[3]/input')
                iSizeValue = MetricToImperial(sizeValue)
                x_replace_field(f'/html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[' + str(i) + ']/div[4]/div/div[4]/div[3]/input', iSizeValue)
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[*THISVALUEINDICATESNEWBLOCK]/div[4]/div/div[3]/div[3]/input
                # /html/body/div[1]/div/div[3]/main/form/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/div/div[1]/div[1]/div[4]/div/div[*THISVALUEPERBLOCK]/div[3]/input
            except(NoSuchElementException):
                print(f"size {i} does not exist")


        SaveBike(family, SaveState, False)
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
"""
replaceSizing('San Quentin')
replaceSizing('El Roy')
replaceSizing('Bobcat Trail')
replaceSizing('Bolinas Ridge')
replaceSizing('Wildcat Trail')
replaceSizing('Team Marin')
replaceSizing('Pine Mountain')
replaceSizing('Alcatraz')
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