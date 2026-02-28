"""
techTranslate

Translates the changes on the technology Frame Materials pages to the other nationalities

Currently only needs to translate two boxes on the mountain frame materials page.
"""

import openpyxl, os, time
from selenium import webdriver
from bikeList import bikeList
from x_functions import x_click, x_delay_click, x_drop,x_login, x_replace_field
from mFunctions import *

#
#
#
SaveState = define_save_state()
#
#
#

backstage_login()

BeginEntry()

waitForTasks()


for language in languagePD.keys():

    #selecting correct language
    x_delay_click(mainPD['Language_Drop'])
    SetLanguage(languagePD[language])
    #checking for load
    LoadSearch()
    #navigating by click to pages section
    x_delay_click('//*[@id="sidebar"]/nav/ul/li[19]/a/span')
    #navigate by click to Mountain Frame Materials Copy
    x_delay_click('/html/body/div/li/div[3]/main/div[2]/div[3]/div/div[1]/div[1]/div/table/tbody/tr[12]/th/div/div/span/a')

    print(f' begin tech page translate for language : {language} ')
    #checking load with title
    LoadBike('Pavement Frame Materials')

    #the fields to be replaced
    x_replace_field('//*[@id="title"]', 'Pavement Frame Materials 2022')

    x_replace_field('//*[@id="slug"]', 'pavement-frame-materials-2022')


    #Save Page
    SaveBike('Pavement Frame Materials', SaveState, False)

    waitForTasks()

