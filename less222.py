from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id("input_value")
    
    x = input1.text
    y = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    button1 = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    input3 = browser.find_element_by_id("robotCheckbox")
    input3.click()
    input4 = browser.find_element_by_id("robotsRule")
    input4.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()