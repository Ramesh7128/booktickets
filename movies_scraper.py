from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
import json
from pyvirtualdisplay import Display
display = Display(visible=1)

display.start()
prof = webdriver.FirefoxProfile()

# for now check for 2 tickets in a sequence
def check_for_n_continous_tickets(tickets_list):
	for i in range(len(tickets_list)-1):
		print i
		first_number = int(tickets_list[i])
		next_number = int(tickets_list[i+1])
		if (next_number == first_number+1):
			return first_number, next_number
		else:
			continue
		

# driver = webdriver.Firefox(executable_path='/home/ramesh/Downloads/geckodriver')
driver = webdriver.Firefox(firefox_profile = prof)

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
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.user__name")))
movies_list_now_showing = []
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//div/dl/dt/a")))
movies_list = driver.find_elements_by_xpath('//div/dl/dt/a')
for i in range(len(movies_list)):
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//div/dl/dt/a")))
	movies_list = driver.find_elements_by_xpath('//div/dl/dt/a')
	if not movies_list[i].text in movies_list_now_showing:
		movies_list_now_showing.append(movies_list[i].text)
	
for i in range(len(movies_list_now_showing)):
	print i, ": ", movies_list_now_showing[i]

movie_code = raw_input('enter the movie code')
movie_name = movies_list_now_showing[int(movie_code)]
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, movie_name)))
element.click()

# add no of ticket selection and movie date selection


screen_show_list = []
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
shows_list = driver.find_elements_by_class_name('movie__show')
for i in range(len(shows_list)):
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
	shows_list = driver.find_elements_by_class_name('movie__show')
	try:
		driver.find_element_by_xpath('//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(i+2))
		theatre_list = driver.find_element_by_xpath('//div[%s]/div[1]/div/div[1]/span/span[1]' % str(i+2)).text
		screen_list = driver.find_element_by_xpath('//div[%s]/div[1]/div/div[1]/span/span[2]' % str(i+2)).text
		print theatre_list, screen_list
		screen_show_list.append((theatre_list, screen_list))
	except Exception as e:
		print e
		continue

for i in range(len(screen_show_list)):
	print i,": ", screen_show_list[i]

screen_selection = raw_input('enter the screen code')
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
shows_list = driver.find_elements_by_class_name('movie__show')
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))))
timings_list = driver.find_elements_by_xpath('//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))
show_availble_time = [] 
for i in range(len(timings_list)):
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))))
	timings_list = driver.find_elements_by_xpath('//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))
	show_availble_time.append(timings_list[i].text)


for i in range(len(show_availble_time)):
	print i, ": ", show_availble_time[i]


show_selection = int(raw_input('Enter the show code'))
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))))
timings_list = driver.find_elements_by_xpath('//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))
timings_list[show_selection].click()

WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div/ul/li/div[@class="seat available "]')))
seats_list = driver.find_elements_by_xpath('//div/ul/li/div[@class="seat available "]')
ticket_list_obj = {}
ticket_list = []
for seat in seats_list:
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div/ul/li/div[@class="available"]')))
	seats_list = driver.find_elements_by_xpath('//div/ul/li/div[@class="available"]')
	row_value_object = seat.find_element_by_xpath('..')
	row_value = row_value_object.get_attribute('data-row-number-id')
	row_div_id = row_value_object.get_attribute('data-seat-grid-row-id') 
	seat_no = seat.get_attribute("data-grid-seat-number")
	seat_no_user = seat.get_attribute("data-seat-number")

	if not row_div_id in ticket_list_obj.keys():
		ticket_list.append(ticket_list_obj)
		ticket_list_obj = {}
		ticket_list_obj[row_div_id] = []
		ticket_list_obj['row_value_id'] = row_div_id
	ticket_list_obj[row_div_id].append(seat_no_user)

	

print ticket_list
with open('tickets_list.txt', 'w') as f:
	f.write(json.dumps(ticket_list))

for i in range(len(ticket_list)):
	print i, ": ", ticket_list[i] 

print ticket_list
seat_selection = raw_input('enter the row and tickets code')
selected_ticket_obj = ticket_list[int(seat_selection)]

div_id = selected_ticket_obj['row_value_id']
if check_for_n_continous_tickets(selected_ticket_obj[div_id]):
	ticket_id_1, ticket_id_2 = check_for_n_continous_tickets(selected_ticket_obj[div_id])
print ticket_id_1, ticket_id_2
print div_id
xpath_ticket_1 = '//div/ul/li[%s]/div[%s]' % (str(div_id), str(ticket_id_1))
xpath_ticket_2 = '//div/ul/li[%s]/div[%s]' % (str(div_id), str(ticket_id_2))

print xpath_ticket_1
print xpath_ticket_2
element_ticket_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_ticket_1)))
element_ticket_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_ticket_2)))
element_ticket_1.click()
element_ticket_2.click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Next')))
element.click()

# add fuel cart payment option to finish booking




