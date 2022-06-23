from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("alert('Robots at work');")
    time.sleep(5)

    num1 = browser.find_element(By.ID, "num1")
    num1_n = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    num2_n = int(num2.text)
    sum = num1_n + num2_n
    print(sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    bt = browser.find_element(By.CLASS_NAME, "btn").click()

    '''
    select = Select(browser.find_element((By.TAG_NAME, "select")))
    select.select_by_value("1")

    x_tap1 = browser.find_element(By.CSS_SELECTOR, "img")
    x_tap1_chacked = int(x_tap1.get_attribute("valuex"))
    print(x_tap1_chacked)
    x = x_tap1_chacked
    y = calc(x)
    pole = browser.find_element(By.ID, "answer")
    pole.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]").click()
    radioB = browser.find_element(By.CSS_SELECTOR, "[value=robots]")
    radioB.click()
    bt = browser.find_element(By.CLASS_NAME, "btn").click()
    '''

finally:
    time.sleep(10)
    browser.quit()
