from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block div.form-group.first_class > input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block div.form-group.second_class > input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block div.form-group.third_class > input")
    input3.send_keys("Smolensk@mail.ru")
    input4 = browser.find_element_by_css_selector("div.second_block div.form-group.first_class > input")
    input4.send_keys("32222332")
    input5 = browser.find_element_by_css_selector("div.second_block div.form-group.second_class > input")
    input5.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

