"""
x_Functions
Human Readable selenium package
Deals exclusively with xpaths

If it doesn't "delay forever" it can fail

Index

x_click
x_delay_click
x_double
x_drop
xKeys
x_replace_field
login
x_get_value
various problematic print times

TODO
Wait for xpath to not exist?
    CheckLoading
        while loading = true
        try
            loading = false
            loading = true
        except()
def xPathExists(xpath):
    try:
        self.browser.find_element_by_xpath(xpath)
        return True
    except:
        return False
        


"""
import sys
import time
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException

os.chdir(os.environ[WEBDRIVER])
browser = webdriver.Firefox()

StartTime = datetime.datetime.now()

"""
#this was moved to mfunctions to add load_search so that it does not stall the website and wait forever
#it became too specific to Marin to justify an xFunction
def xCheckStillExists(xpath, loadType):
    animation = "|/-\\"
    exists = True
    while(exists):
        try:
            browser.find_element_by_xpath(xpath)
            exists = True
            for i in range(30):
                time.sleep(0.1)
                sys.stdout.write(loadType + "\r" + animation[i % len(animation)])
                sys.stdout.flush()
        except:
            exists = False
"""

#x_click clicks on an xpath, can fail
def x_click(xpath):
    browser.find_element(By.XPATH, xpath).click()

#x_delay_click delays until xpath can be click on, can delay forever
#TODO fix weird formatting
def x_delay_click(xpath):
    loaded = False
    while(loaded is False):
        try:
            browser.find_element(By.XPATH, xpath).click()
            time.sleep(1)
            loaded = True
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
            animation = "|/-\\"
            for i in range(30):
                time.sleep(0.1)
                sys.stdout.write(f"xD_click->checking for {xpath}")
                sys.stdout.write("checking for " + xpath + "load" + "\r" + animation[i % len(animation)])
                sys.stdout.flush()

#xCheckIfExists delays until a path exists, x_delay_click without click, can delay forever
#TODO fix weird formatting   
def xCheckIfExists(xpath, loadingString):
    animation = "|/-\\"
    exists = False
    while(not exists):
        try:
            browser.find_element(By.XPATH, xpath)
            exists = False
            for i in range(30):
                time.sleep(0.1)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.write(loadingString)
                sys.stdout.flush()
        except Exception:
            exists = True


def x_double(xpath):
    """
    x_double simulates a double click (technically triple clicks)
    can delay forever
    """
    x_delay_click(xpath)
    x_click(xpath)
    x_click(xpath)


def x_drop(xpath, selector_xpath):

    """
    x_drop opens xpath dropdown
    it mercilessly attempts to click on the selector_xpath
    can delay forever
    """

    x_delay_click(xpath)
    x_delay_click(selector_xpath)
    x_double(selector_xpath)


def xKeys(xpath, keys_to_send):

    """x_keys sends keys to an xpath"""

    browser.find_element(By.XPATH, xpath).send_keys(keys_to_send)

def x_replace_field(xpath, replacement_text):

    """
    replace_field replaces text in a field-xpath with replacementText
    doesn't seem to support formatted strings for some reason
    """

    field_to_replace = browser.find_element(By.XPATH, xpath)
    field_to_replace.clear()
    xKeys(xpath, replacement_text)

def x_login(url, username, password):

    """login is a generic login function, url is for login page"""

    browser.get(url + 'login')
    username_element = browser.find_element(By.ID, 'loginName')
    username_element.send_keys(username)
    password_element = browser.find_element(By.ID, 'password')
    password_element.send_keys(password)
    password_element.submit()

#gets the value of an xpath
def x_get_value(xpath):

    """gets the value at an x path"""

    field = browser.find_element(By.XPATH, xpath)
    fieldvalue = field.get_attribute('Value')
    return fieldvalue

#gets the text of an xpath
def x_get_text(xpath):
    """gets the text at an xpath"""
    field = browser.find_element(By.XPATH, xpath).text
    return field

def x_print_time(relevance = 'The time is: '):
    """
    x_print_time() prints the time and can include a string that displays the relevance of printing the time
    """
    current_time = datetime.datetime.now()
    print(f'{relevance} {current_time}')


def x_wait(wait_time):

    """x_wait sleeps for waitTime after printing a notification of its intended sleep time"""

    print(f'x_wait called, waiting for {wait_time} seconds')
    time.sleep(wait_time)