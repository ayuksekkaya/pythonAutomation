from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import yaml
import os
from selenium.webdriver.chrome.service import Service


DAILY_HEALTH_LINK = 'https://slate.brandeis.edu/portal/brandeis_covid19'


def daily_health():
    # To make it run without the browser popping up.
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    driver = webdriver.Chrome(options=opt)
    driver.refresh()
    driver.get(DAILY_HEALTH_LINK)
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//*[@id='username']")
    passphrase_enter = driver.find_element(By.XPATH, "//*[@id='password']")
    
    a_yaml_file = open(os.path.dirname(__file__) + "/credentials.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    username.send_keys(parsed_yaml_file['login']['username'])
    passphrase_enter.send_keys(parsed_yaml_file['login']['password'])
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[6]/button').click()
    a_yaml_file.close()
    time.sleep(2)
    WebDriverWait(driver, 200).until(
            EC.title_contains("COVID-19")
            
        )
        
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td/div/div[5]/form/div/span/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="form_febaa6cf-a91c-4512-9a62-1b4d9fc76087_10"]').click()
    driver.find_element(By.XPATH, '//*[@id="form_d18b4fe3-24e1-48fa-8275-eac56f2485fc_2"]').click()
    driver.find_element(By.XPATH, '//*[@id="form_7621d269-5d6c-4104-90c4-ea21e5c0a953_1"]').click()
    driver.find_element(By.XPATH, '//*[@id="form_718644d8-2fac-43e8-9ee4-b292aafe4f45_1"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/form/div[4]/button').click()

    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Return to Portal"))
        )
    except:
        print("unsuccesful")

    print("succesful")


daily_health()






