import settings, login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, datetime
from pyvirtualdisplay import Display

display = Display(visible=0, use_xauth=True, size=(800, 600))
display.start()

login.initialize_browser()
login.login()

print("Successful Login")

# Switch to main body frame..
time.sleep(4)
settings.driver.switch_to_frame('unitFrame')

# html = settings.driver.page_source
# print(html)

# Open the first timesheet available in the table
xpath = '/html/body/form[10]/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/span'
settings.driver.find_element_by_xpath(xpath).click()

time.sleep(3)

print("Opened Timesheet")

# Flip back to the default frame
settings.driver.switch_to.default_content()

# And then drill back in to the timesheet frame
settings.driver.switch_to_frame('unitFrame')

# Find todays date
date_num = datetime.datetime.today().weekday() + 1

# Select todays cell for the first row in the timesheet 
xpath = '//*[@id="hrs0_' + str(date_num) + '"]'
date_cell = settings.driver.find_element_by_xpath(xpath)
settings.driver.execute_script("arguments[0].click();", date_cell)

# Edit the cell and slap in 8 hours.
xpath = '//*[@id="editor"]'
settings.driver.find_element_by_xpath(xpath).send_keys('8')

# Click out of the box
xpath = '//*[@id="hrs1_' + str(date_num) + '"]'
date_cell = settings.driver.find_element_by_xpath(xpath)
settings.driver.execute_script("arguments[0].click();", date_cell)

# Save TS
xpath = '//*[@id="appOptionsDivsaveTS"]'
settings.driver.find_element_by_xpath(xpath).click()

# close browser after 3 seconds to wait for save

time.sleep(3)
settings.driver.quit()

display.stop()
