import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

fname = browser.find_element(By.NAME, "firstname")
fname.send_keys("Name")
lname = browser.find_element(By.NAME, "lastname").send_keys("Last")
email = browser.find_element(By.NAME, "email").send_keys("s@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
print(file_path)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
bt = browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(10)
browser.quit()
