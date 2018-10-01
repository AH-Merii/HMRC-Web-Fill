import os
import sys
import time
import xlrd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def runtest():
    driver.get(
        """https://www.tax.service.gov.uk/gg/sign-in?
        continue=%2Foauth%2Fgrantscope%3Fauth_id%3D5bb150d92500000b002d9e6f
        %26state%3DinitialContact789708&origin=oauth-frontend"""
    )
    # time.sleep(1)  # Let the user actually see something!
    """ Initialize HTML Elements """
    userId = driver.find_element_by_id("userId")
    password = driver.find_element_by_id("password")
    signinButton = driver.find_element_by_id("signin")

    userId.send_keys("O KK Trial")
    password.send_keys("Om12345")
    signinButton.click()

    # search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()
    sys.exit(0)  # Exit script


def edgeSession():
    # create new Edge session
    dir = os.path.dirname(__file__)
    edge_path = dir + r"\MicrosoftWebDriver.exe"
    print(edge_path)
    driver = webdriver.Edge(edge_path)
    return driver


try:
    driver = edgeSession()
    runtest()
except NoSuchElementException:
    driver.quit()
    sys.exit("No element found, try again")  # Exit script & Notify failiure
