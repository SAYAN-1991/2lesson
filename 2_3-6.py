from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    br1 = browser.find_element(By.CLASS_NAME, "btn").click()
    #confirm = browser.switch_to.alert
    #confirm.accept()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_tap1 = browser.find_element(By.ID, "input_value")
    x_tap1_chacked = int(x_tap1.text)
    x = x_tap1_chacked
    y = calc(x)
    pole = browser.find_element(By.ID, "answer")
    pole.send_keys(y)

    bt = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true)", bt)
    bt.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
