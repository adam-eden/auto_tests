from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("[name = firstname]")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("[name = lastname]")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("[name = email]")
input3.send_keys("test@email.com")

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'download.text')

download = browser.find_element_by_css_selector("#file")
download.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
