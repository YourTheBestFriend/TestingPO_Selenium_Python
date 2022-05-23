########################## 25.21503685571971
import math
from multiprocessing import Value
from selenium import webdriver
import time

var_link_num = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = 'http://suninjuly.github.io/find_link_text' # changed link

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # for task 3   
    link2 = browser.find_element_by_link_text(var_link_num) # find_element_by_partial_link_text --- если хотим найти элемент со ссылкой по подстроке
    link2.click() 

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys('Matthew')
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys('Goncharov')
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys('Minsk')
    input4 = browser.find_element_by_id("country")
    input4.send_keys('Belarus')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

# Для Unix or Linux систем оставить пустую строку