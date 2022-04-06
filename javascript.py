from selenium import webdriver
import math

# с прокруткой страницы (если поля перекрыты другими элементами страницы)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value.nowrap")
x = x_element.text
y = calc(x)

input_text = browser.find_element_by_css_selector("#answer")
input_text.send_keys(y)

button = browser.find_element_by_tag_name("button")
browser.execute_script("button = document.getElementsByTagName('button')[0]; button.scrollIntoView(true);", button)
button.click()

click_radiobutton = browser.find_element_by_css_selector("#robotsRule")
click_radiobutton.click()

click_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
click_checkbox.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
