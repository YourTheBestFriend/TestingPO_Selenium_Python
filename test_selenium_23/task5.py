######################## 25.269106145549635
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_xpath_form' # changed link

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

    button = browser.find_element_by_xpath("//button[contains(@type,'submit')]")
    button.click()
   
finally:
    time.sleep(10)
    browser.quit()

# Для Unix or Linux систем оставить пустую строку

''' 
22.32466393652502 + 25.21503685571971 + 21.226053607547385 + 25.269106145549635
94.03486054534176
'''