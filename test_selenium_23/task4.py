######################## 21.226053607547385
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html' # changed link

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input") # complete
    for element in elements:
        element.send_keys("1234")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
finally:
    time.sleep(30)
    browser.quit()

# Для Unix or Linux систем оставить пустую строку