import settings, login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

login.initialize_browser()
login.login()

time.sleep(4)
settings.driver.switch_to_frame('unitFrame')

print("Waited for ever...")

html = settings.driver.page_source
print(html)

xpath = '/html/body/form[10]/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/span'
settings.driver.find_element_by_xpath(xpath).click()

time.sleep(3)

settings.driver.switch_to.default_content()

settings.driver.switch_to_frame('unitFrame')

xpath = '//*[@id="hrs0_3"]'
date_cell = settings.driver.find_element_by_xpath(xpath)
settings.driver.execute_script("arguments[0].click();", date_cell)

xpath = '//*[@id="editor"]'
settings.driver.find_element_by_xpath(xpath).send_keys('8')