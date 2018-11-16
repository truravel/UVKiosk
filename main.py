#NOTICE: All information contained herein is, and remains the property of IT of United States and its suppliers, if any.  The intellectual and technical concepts contained herein are proprietary to IT of United States and its suppliers and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or copyright law. Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained from IT of United States.
#v2.181115
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from files.config import Unifi_Config

import re
import requests
import time
import json
import platform

import ssl
import re
import os
import errno
import random

import win32com.client as comctl
wsh = comctl.Dispatch("WScript.Shell")


def set_input(driver, input_user_id='userid', user="", time=2):
        band = False
        try:
            if time >= 0 and user != "":
                username_element = WebDriverWait(driver, time).until(
                    EC.presence_of_element_located((By.ID, input_user_id)))
                username_element.send_keys(user)
                band = True
        except TimeoutException as toe:
            error = "set_input TimeoutException {0} >> {1}".format(input_user_id, toe)
            print(error)
        except NoSuchElementException as nsee:
            error = "set_input NoSuchElementException {0} >> {1}".format(input_user_id, nsee)
            print(error)
        except Exception as ex:
            error = "set_input {0} >> {1}".format(input_user_id, ex)
            print(error)
        return band


if __name__ == "__main__":
    if "Darwin" in platform.platform():
        driver = './files/chromedriver_mac'
    elif "Linux" in platform.platform():
        driver = './files/chromedriver_linux'
    else:
        driver  = './files/chromedriver_win'

    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_argument("disable-infobars")
    browser = webdriver.Chrome(driver, chrome_options=options)

    browser.get("https://"+ Unifi_Config['host'] + ":7443/login")
    time.sleep(10)
    set_input(browser,'ember1696', Unifi_Config['user'])
    time.sleep(.5)
    set_input(browser,'ember1697', Unifi_Config['password'])
    time.sleep(1)
    browser.execute_script("$('#loginForm').submit()")
    time.sleep(10)
    browser.execute_script("$(location).attr('href','/live-view');")
    time.sleep(12)
    browser.execute_script("$('body').addClass('fullscreen'); ")
    browser.execute_script(' $("div.ember-view.appGlobalSideNav.appGlobalSideNav--withHeader").css("display","none"); ')
    browser.find_element_by_tag_name("body").send_keys(Keys.F11)
    wsh.SendKeys("{F11}")
    time.sleep(0.5)
    browser.find_element_by_tag_name("body").send_keys(Keys.F11)
    wsh.SendKeys("{F11}")
        
    

    
