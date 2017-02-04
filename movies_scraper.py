from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path='/home/ramesh/Downloads/geckodriver')
driver.get('https://www.spicinemas.in/')

# elem.send_keys(Keys.RETURN)
# assert "No results found" not in driver.page_source
elem = driver.find_element_by_id("selectCity").click()
driver.find_element_by_xpath('//*[@id="login-topbar"]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('ramesh7128@gmail.com')
driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('findout5')
driver.find_element_by_xpath('//*[@id="login_submit"]').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/article/section[2]/div/div/section/section[1]/nav/section/ul/li[2]/a').click()
time.sleep(10)
movies_list = driver.find_elements_by_class_name("movie__item")
for movie in movies_list:
    movie.find_element_by_xpath("//a/img[title()='ATHEY KANGAL']").click()
