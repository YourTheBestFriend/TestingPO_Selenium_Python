########################## 22.32466393652502

from multiprocessing import Value
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys('Matthew')
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys('Goncharov')
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys('Minsk')
    input4 = browser.find_element_by_id("country")
    input4.send_keys('Belarus')

    # button = browser.find_element_by_css_selector("button.btn")
    # Из задания 5 сделал через xpath
    button = browser.find_element_by_xpath("//button[contains(@class,'btn-default')]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# Для Unix or Linux систем оставить пустую строку