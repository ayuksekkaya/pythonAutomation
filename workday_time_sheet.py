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

WORKDAY_LINK = "https://wd5.myworkday.com/wday/authgwy/brandeis/login.htmld"
PATH_TO_YAML_FILES = "/home/asyuksek/Brandeis_Undergrad/guru/automation"
JOB_NAME_FILES = ['Computer Science - Guru (Jr DevOps Engineer)', 'TA - COSI 131a (+)']


def time_sheet():
    opt = webdriver.ChromeOptions()
    # opt.add_argument('headless')
    driver = webdriver.Chrome(options=opt)
    driver.get(WORKDAY_LINK)
    time.sleep(5)
    driver = log_in(driver)
    driver = naivgate_to_to_time(driver)
    time.sleep(5)
    
    for job in JOB_NAME_FILES:
        job_file = open(os.path.join(PATH_TO_YAML_FILES, job + '.yaml'))
        job_hours = yaml.load(job_file, Loader=yaml.FullLoader)

        for day, hours in job_hours.items():
            driver = navigate_to_menu(driver, job)
            driver = enter_time(driver, day, hours)
        job_file.close()
    time.sleep(10)
    print("Success")


def log_in(driver):
    username = driver.find_element(By.XPATH, "//*[@id='username']")
    passphrase_enter = driver.find_element(By.XPATH, "//*[@id='password']")

    a_yaml_file = open(os.path.join(PATH_TO_YAML_FILES,"credentials.yaml" ))
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    username.send_keys(parsed_yaml_file["login"]["username"])
    passphrase_enter.send_keys(parsed_yaml_file["login"]["password"])
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/div/form/div[6]/button"
    ).click()
    a_yaml_file.close()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.title_contains("Home"))
    time.sleep(2)

    return driver


def naivgate_to_to_time(driver):
    time.sleep(5)

    navigation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//button[@data-automation-id="globalNavButton"]')
        )
    )
    navigation.click()
    time.sleep(5)
    shortcut = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//button[@data-automation-id="globalNavShortcutsTab"]')
        )
    )
    shortcut.click()
    time_entry = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@data-automation-id="globalNavShortcutItemLabel"]')
        )
    )
    time_entry.click()
    time.sleep(5)

    return driver


def navigate_to_menu(driver, job_name):
    action = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[@title="Actions"]'))
    )
    action.click()
    time.sleep(15)
    day = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@data-automation-label="Quick Add"]')
        )
    )
    day.click()
    time.sleep(5)
    show_all = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@data-automation-id="selectShowAll"]')
        )
    )
    show_all.click()
    time.sleep(5)
    guru = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, f'//div[@title="{job_name}"]')
        )
    )
    guru.click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@title="Next"]').click()
    time.sleep(5)
    return driver


def enter_time(driver, day, hours):
    time.sleep(2)
    driver.find_element(By.XPATH, f'//div[@data-automation-id="checkbox" and @data-uxi-form-item-child-list-index="{day}"]').click()
    time.sleep(5)
    start, end = driver.find_elements(
        By.XPATH, '//div[@data-automation-id="standaloneTimeWidget"]/input'
    )
    start.send_keys(hours["start"])
    end.send_keys(hours["end"])
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@title="OK"]').click()

    return driver


time_sheet()
