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
from check import check_for_n_continous_tickets
import urlparse

display.start()
prof = webdriver.FirefoxProfile()


# driver = webdriver.Firefox(executable_path='/home/ramesh/Downloads/geckodriver')
driver = webdriver.Firefox(firefox_profile = prof)

driver.get('https://www.spicinemas.in/chennai/now-showing')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'selectCity')))
driver.find_element_by_id("selectCity").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-topbar"]/a')))
driver.find_element_by_xpath('//*[@id="login-topbar"]/a').click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('ramesh7128@gmail.com')
# driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('venki1989@gmail.com')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userPassword"]')))
driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('findout5')
# driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('united1')
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

movie_code = raw_input('Enter the movie code :')
movie_name = movies_list_now_showing[int(movie_code)]
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, movie_name)))
element.click()

# date selection need to be added
date_list_available = []
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bookTicket"]/section[1]/div/div[2]/div')))
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="bookTicket"]/section[1]/div/div[2]/div/ul/li[@class="filter__list__item available"]')))
date_list_elements = driver.find_elements_by_xpath('//*[@id="bookTicket"]/section[1]/div/div[2]/div/ul/li[@class="filter__list__item available"]')
for date_element in date_list_elements:
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="bookTicket"]/section[1]/div/div[2]/div/ul/li[@class="filter__list__item available"]')))
	date_list_elements = driver.find_elements_by_xpath('//*[@id="bookTicket"]/section[1]/div/div[2]/div/ul/li[@class="filter__list__item available"]')
	date_list_available.append(date_element.get_attribute('data-date-value'))

for i in range(len(date_list_available)):
	print i, ": ", date_list_available[i]

date_choice = raw_input("Enter the date: ")
date_value = str(date_list_available[int(date_choice)])
url = driver.current_url
new_url = urlparse.urljoin(url, "%s?seats=2" % date_value) 
driver.get("%s" % new_url);

# ticket selection
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
ticket_drop_down = driver.find_element_by_xpath('//*[@id="bookTicket"]/section[1]/div/div[1]/div/a')
ticket_drop_down.click()
no_of_tickets_selected = str(raw_input('No of tickets :'))

WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bookTicket"]/section[1]/div/div[1]/div/ul/li[%s]' % no_of_tickets_selected)))
no_tickets_list = driver.find_element_by_xpath('//*[@id="bookTicket"]/section[1]/div/div[1]/div/ul/li[%s]' % no_of_tickets_selected)
no_tickets_list.click()




screen_show_list = []
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
shows_list = driver.find_elements_by_class_name('movie__show')
for i in range(len(shows_list)):
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
	shows_list = driver.find_elements_by_class_name('movie__show')
	try:
		WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bookTicket"]/section[2]/div/div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(i+2)))))
		driver.find_element_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(i+2))
		theatre_list = driver.find_element_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[1]/div/div[1]/span/span[1]' % str(i+2)).text
		screen_list = driver.find_element_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[1]/div/div[1]/span/span[2]' % str(i+2)).text
		screen_show_list.append((theatre_list, screen_list))
	except Exception as e:
		theatre_list = driver.find_element_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[1]/div/div[1]/span/span[1]' % str(i+2)).text
		screen_list = driver.find_element_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[1]/div/div[1]/span/span[2]' % str(i+2)).text
		screen_show_list.append((theatre_list, screen_list, "not-available"))
		continue

for i in range(len(screen_show_list)):
	print i,": ", screen_show_list[i]

screen_selection = raw_input('Enter the screen code :')
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "movie__show")))
shows_list = driver.find_elements_by_class_name('movie__show')
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="bookTicket"]/section[2]/div/div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))))
timings_list = driver.find_elements_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))
show_availble_time = [] 
for i in range(len(timings_list)):
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="bookTicket"]/section[2]/div/div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))))
	timings_list = driver.find_elements_by_xpath('//*[@id="bookTicket"]/section[2]/div/div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))
	show_availble_time.append(timings_list[i].text)

for i in range(len(show_availble_time)):
	print i, ": ", show_availble_time[i]

show_selection = int(raw_input('Enter the show code'))
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))))
timings_list = driver.find_elements_by_xpath('//div[%s]/div[2]/div/ul/li[@class="session  indicate-busy show available"]' % str(int(screen_selection)+2))
timings_list[show_selection].click()

# if A certificate
try:
	WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="certification_a"]/div/a[1]')))
	element_a_popup = driver.find_element_by_xpath('//*[@id="certification_a"]/div/a[1]')
	element_a_popup.click()
except:
	pass


WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div/ul/li/div[@class="seat available "]')))
seats_list = driver.find_elements_by_xpath('//div/ul/li/div[@class="seat available "]')
ticket_list_obj = {}
ticket_list = []


# write a logic to book tickets when displaying itself
for seat in seats_list:
	WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div/ul/li/div[@class="seat available "]')))
	seats_list = driver.find_elements_by_xpath('//div/ul/li/div[@class="seat available "]')
	row_value_object = seat.find_element_by_xpath('..')
	row_value = row_value_object.get_attribute('data-row-number-id')
	row_div_id = row_value_object.get_attribute('data-seat-grid-row-id') 
	seat_no = seat.get_attribute("data-grid-seat-number")
	seat_no_user = seat.get_attribute("data-seat-number")

	if not row_div_id in ticket_list_obj.keys():
		ticket_list.append(ticket_list_obj)
		index_value = len(ticket_list)-1 
		print index_value, ":", ticket_list_obj
		ticket_list_obj = {}
		ticket_list_obj[row_div_id] = []
		ticket_list_obj['row_value_id'] = row_div_id
	ticket_list_obj[row_div_id].append(seat_no_user)


seat_selection = raw_input('enter the row and tickets code')
selected_ticket_obj = ticket_list[int(seat_selection)]

div_id = selected_ticket_obj['row_value_id']

"""
logic for n tickets
"""
if check_for_n_continous_tickets(selected_ticket_obj[div_id], int(no_of_tickets_selected)):
	tickets_numbers_list = check_for_n_continous_tickets(selected_ticket_obj[div_id], int(no_of_tickets_selected))
	for ticket in tickets_numbers_list:
		xpath_ticket = '//div/ul/li[%s]/div[@data-seat-number="%s"]' % (str(div_id), str(ticket))
		element_ticket = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_ticket)))
		element_ticket.click()
		no_of_tickets_selected = int(no_of_tickets_selected)-1
		if not no_of_tickets_selected:
			break

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="actions"]')))
# element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="actions"]/a')))
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/article/div/div/section/div/section[2]/div[2]/div/div[2]/a')))
element.click()

# fuel wallet
# payment = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="instant-pay"]')))
# payment.click()

# card payment
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/article/div/div/section/div/section[3]/div/div[2]/div[2]/div[2]/a[2]')))
element.click()