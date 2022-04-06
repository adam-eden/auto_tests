from selenium import webdriver
import math

# ввод вычесленной функции, проверка на капчу
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# используем get_attribute
link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector("#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input_text = browser.find_element_by_css_selector("#answer")
input_text.send_keys(y)

click_radiobutton = browser.find_element_by_css_selector("#robotsRule")
click_radiobutton.click()

click_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
click_checkbox.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
