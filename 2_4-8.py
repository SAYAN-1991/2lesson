from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button2 = browser.find_element(By.ID, "book").click()


x_tap1 = browser.find_element(By.ID, "input_value")
x_tap1_chacked = int(x_tap1.text)
x = x_tap1_chacked
y = calc(x)
pole = browser.find_element(By.ID, "answer")
pole.send_keys(y)

bt = browser.find_element(By.ID, "solve").click()
#browser.execute_script("return arguments[0].scrollIntoView(true)", bt)
