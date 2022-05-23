import time
from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")

time.sleep(5)

driver.get("http://bga.by/contacts")
time.sleep(5)

username = driver.find_element_by_id("124158159")
username.send_keys("Матвей")
time. sleep(5)

emailbox = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[1]/form/div/div[2]/input")
emailbox.send_keys("matveygoncharov77@gmail.com")
time. sleep(5)

textarea = driver.find_element_by_tag_name("textarea")
textarea.send_keys("Мой первый тест через Selenium")

submit_button = driver.find_element_by_css_selector("#submitFormcontacts")
# submit_button.click()

time. sleep(5)
driver.quit()