from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_tap1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_tap1.text
    y = calc(x)
    pole = browser.find_element(By.ID, "answer")
    pole.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]").click()
    radioB = browser.find_element(By.CSS_SELECTOR, "[value=robots]")
    radioB.click()
    bt = browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
