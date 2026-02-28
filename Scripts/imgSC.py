#imgSC checks the image size of every image and creates lists of the bikes that are not correctly sized


"""
TODO
get the correct sizes by url
get every url of relevant categories

check every item entry by xpath
wait for load
pull image size string
compare string to page correct size string"1000 x 540"

if size is not correct store on a list
cycle through the entire page until it fails
check multiple times to be sure that the page has actually loaded

if entry cannot be found check if there is another page
click on new page
reset entry cycle variable
repeat


"""

import os, time
from selenium import webdriver
from x_functions import x_click, x_delay_click, x_drop,x_login, x_get_value
from mFunctions import *

def openTabs():
    print('open all tabs and press enter')
    input()

def newPage(page):
    page = page - 1
    for i in range(0, page):
        x_delay_click('//*[@id="count-container"]/div/div[2]')
        x_delay_click('/html/body/div/div/div[3]/main/div[2]/div[3]/div/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/span')

def imgSC(categoryName, assetXPath, sizeString):
    print(f'Beginning {categoryName} Search')
    endpages = False
    page = 1
    incorrectNameList = []
    incorrectSizeList = [] 
    while(endpages == False):
        entryI = 0
        x_click(assetXPath)
        #check first entry for load
        x_delay_click('/html/body/div/div/div[3]/main/div[2]/div[3]/div/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/span')
        time.sleep(1)
        for entryI in range(1, 102):
            try:
                if page == 2:
                    newPage(2)
                elif page == 3:
                    newPage(3)
                elif page == 4:
                    newPage(4)
                elif page == 5:
                    newPage(5)
                elif page == 6:
                    newPage(6)
                elif page == 7:
                    newPage(7)
                elif page == 8:
                    newPage(8)
                elif page == 9:
                    newPage(9)
                elif page == 10:
                    newPage(10)
                elif page == 11:
                    newPage(11)
                elif page == 12:
                    newPage(12)
                elif page == 13:
                    newPage(13)
                    
                #open Entry
                x_click(f'//*[@id="content"]/div[1]/div[1]/div/table/tbody/tr[{entryI}]/th/div/div[2]/span/a')
                #check for Load
                x_delay_click('//*[@id="title"]')
                name = x_get_value('//*[@id="title"]')
                print()
                print(name)
                imageSize = x_get_text('//*[@id="dimensions-value"]')
                print(f'--{imageSize}--')
                time.sleep(1)
                if (sizeString != imageSize):
                    print(imageSize)
                    print(sizeString)
                    print('added to list')
                    incorrectNameList.append(name)
                    incorrectSizeList.append(imageSize)
                click_Assets()
                #check first entry for load
                x_delay_click('/html/body/div/div/div[3]/main/div[2]/div[3]/div/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/span')
                x_click(assetXPath)
                x_delay_click('/html/body/div/div/div[3]/main/div[2]/div[3]/div/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/span')


            except(NoSuchElementException, AttributeError, ElementClickInterceptedException):
                print('cant locate next entry')
                print('trying next page')
                try:
                    time.sleep(1)
                    page += 1
                    if page >= 14:
                        endpages = True
                except(NoSuchElementException, AttributeError, ElementClickInterceptedException):
                    print('no new page')
                    endpages = True
                    for i in range(len(incorrectSizeList)):
                        print(incorrectNameList[i])
                        print(incorrectSizeList[i])
        
    endpages = True
    print()
    print(f'-----------------------{categoryName} List Complete--------------------------')
    for i in range(len(incorrectNameList)):
        print()
        print(incorrectNameList[i])
        print(incorrectSizeList[i])
    print()
    print('--------------------------End List----------------------------')
    x_print_time()
            

"""
Runtime
"""
runtime()

"""
Site Navigation
"""

backstage_login()
click_Assets()
openTabs()

"""
Function Calls
"""

"""
FINISHED



imgSC('Bikes-Category-Header', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[2]/ul/li[1]/ul', '1680×950')



imgSC('Bikes-Gallery', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[2]/ul/li[3]', '1456×752')


imgSC('Bikes-Grid', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[2]/ul/li[5]', '1000×540')


"""
imgSC('Bikes-Hero', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[2]/ul/li[6]', '2920×1800')
"""


imgSC('Bikes-Technology', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[2]/ul/li[7]', '970×770')

imgSC('Bikes-Mod-Gallery', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[1]', '1440×940')
imgSC('Bikes-Mod-HeroSidebySide', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[2]', '1680×950')
imgSC('Bikes-Mod-Hero-Image', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[3]/ul/li[1]', '3200×1500')
#category below represents a minor problem as the constraints are - 1456 x any height
imgSC('Bikes-Hightlight', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[4]', '1456×1000')
imgSC('Bikes-Mod-Image', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[5]', '1940×1000')
imgSC('Bikes-MediaRow42_58', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[6]', '1680×950')
imgSC('Bikes-MediaRow50_50', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[7]', '1456×1220')
imgSC('Bikes-MediaRow66_33', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[8]', '970×770')
imgSC('Bikes-Media2Col', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[9]', '1456×687')
imgSC('Bikes-Media3Col', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[4]/ul/li[10]', '968×535')
imgSC('NewsReviews-Grid', '//*[@id="sidebar"]/nav/ul/li[1]/ul/li[6]/ul/li', '968×538')
"""