from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://intranet.raiffeisen.ru/grandprix/form.aspx')
# inputElement = driver.find_element_by_id("gp_company_user")
# inputElement.send_keys('Карпова Ирина Евгеньевна')
# time.sleep(5)
# inputElement.send_keys(Keys.ARROW_DOWN, Keys.ENTER) 

# driver.find_element_by_id("gp_notes").send_keys('Проффесионал своего дела, который помогает в любой ситуации')
# driver.find_element_by_id("gp_for_quality").click()
# driver.find_element_by_id("gp_post_user_form").click()