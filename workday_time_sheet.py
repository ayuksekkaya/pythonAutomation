from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import os
from selenium.webdriver.chrome.service import Service

WORKDAY_LINK = 'https://wd5.myworkday.com/wday/authgwy/brandeis/login.htmld'

def time_sheet():
    driver = webdriver.Chrome()
    driver.get(WORKDAY_LINK)
    time.sleep(5)
    driver = log_in(driver)
    driver = naivgate_to_to_time(driver)
    time.sleep(5)
    driver = navigate_to_menu(driver)
    driver = enter_time(driver, "0")
    time.sleep(5)
    driver = navigate_to_menu(driver)
    driver = enter_time(driver, "1")
    time.sleep(5)
    driver = navigate_to_menu(driver)
    driver = enter_time(driver, "3")
    time.sleep(5)
    driver = navigate_to_menu(driver)
    driver = enter_time(driver, "4")
    time.sleep(10)
    print("Success")


def log_in(driver):
    username = driver.find_element(By.XPATH, "//*[@id='username']")
    passphrase_enter = driver.find_element(By.XPATH, "//*[@id='password']")

    print(os.path.dirname(__file__) + "credentials.yaml")
    a_yaml_file = open(os.path.dirname(__file__) + "credentials.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    username.send_keys(parsed_yaml_file['login']['username'])
    passphrase_enter.send_keys(parsed_yaml_file['login']['password'])
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[6]/button').click()
    a_yaml_file.close()
    time.sleep(2)
    WebDriverWait(driver, 20).until(
        EC.title_contains("Home")
    )
    time.sleep(2)

    return driver

def naivgate_to_to_time(driver):
    time.sleep(5)
    time_bttn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@title="Time"]'))
    )
    time_bttn.click()
    time.sleep(5)
    this_week = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-automation-id="dropDownCommandButton"]'))
    )
    this_week.click()
    time.sleep(5)

    return driver

def navigate_to_menu(driver):
    action = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[@title="Actions"]'))
    )
    action.click()
    time.sleep(15)
    day = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@data-automation-label="Quick Add"]'))
    )
    day.click()
    time.sleep(5)
    show_all = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@data-automation-id="selectShowAll"]'))
    )
    show_all.click()
    time.sleep(5)
    guru = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@title="COSI Department - Guru (+)"]'))
    )
    guru.click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@title="Next"]').click()
    time.sleep(5)
    return driver

def enter_time(driver, day):
    time.sleep(2)
    driver.execute_script('document.getElementsByClassName("WLLF")[' + day + '].click();')
    time.sleep(5)
    start, end = driver.find_elements(By.XPATH, '//div[@data-automation-id="standaloneTimeWidget"]/input')
    yaml_file = open(os.path.dirname(__file__) + "hours.yaml")
    hours = yaml.load(yaml_file, Loader=yaml.FullLoader)
    start.send_keys(hours[day]["start"])
    end.send_keys(hours[day]["end"])
    yaml_file.close()
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@title="OK"]').click()
    return driver

time_sheet()