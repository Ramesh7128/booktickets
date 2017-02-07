from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os


driver = webdriver.Firefox(executable_path='/home/ramesh/Downloads/geckodriver')
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://www.spicinemas.in/chennai/now-showing')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'selectCity')))
driver.find_element_by_id("selectCity").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-topbar"]/a')))
driver.find_element_by_xpath('//*[@id="login-topbar"]/a').click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('ramesh7128@gmail.com')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userPassword"]')))
driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('findout5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_submit"]')))
driver.find_element_by_xpath('//*[@id="login_submit"]').click()

WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//div/dl/dt/a")))
movies_list_now_showing = []
movies_list = driver.find_elements_by_xpath('//div/dl/dt/a')
for i in range(len(movies_list)):
	movies_list = driver.find_elements_by_xpath('//div/dl/dt/a')
	if not movies_list[i].text in movies_list_now_showing:
		movies_list_now_showing.append(movies_list[i].text)
	
for i in range(len(movies_list_now_showing)):
	print i, ": ", movies_list_now_showing[i]

movie_code = raw_input('enter the movie code')
movie_name = movies_list_now_showing[int(movie_code)]
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, movie_name)))
element.click()


# # time.sleep(5)

# for movie in movies_list:
# 	print movie.text
# 	# try:
# 	# 	element = movie.find_element_by_xpath('.//div/dl/dt/a')
# 	# 	if element.text == 'XXX RETURN OF XANDER CAGE':
# 	# 		element.click()
# 	# 		break
# 	# except StaleElementReferenceException as e:
# 	# 	print e
# 	# 	break


# text_to_be_present	# 
	

