def check_for_n_continous_tickets(tickets_list, no_of_tickets=2):
	tickets_list = [int(x) for x in tickets_list]
	tickets_list.sort()
	continous_grouping_list = []
	grouping_index_list = []
	temp_list = []
	for number in tickets_list:
		if temp_list:
			if number == temp_list[-1]+1:
				temp_list.append(number)
			else:
				continous_grouping_list.append(temp_list)
				grouping_index_list.append(len(temp_list))
				temp_list = []
				temp_list.append(number)
		else:
			temp_list.append(number)


	continous_grouping_list.append(temp_list)
	grouping_index_list.append(len(temp_list))

	for i in range(len(grouping_index_list)):
		if no_of_tickets <= grouping_index_list[i]:
			return continous_grouping_list[i]




# tickets_list = [1,2,3,5,6,8,9,10,11,12,15,16,18,19,20,22,23,24,25,26]
# value = check_for_n_continous_tickets(tickets_list)


"""
Earlier logic for 2 tickets
"""
# if check_for_n_continous_tickets(selected_ticket_obj[div_id]):
# 	ticket_id_1, ticket_id_2 = check_for_n_continous_tickets(selected_ticket_obj[div_id])
# print ticket_id_1, ticket_id_2
# print div_id
# xpath_ticket_1 = '//div/ul/li[%s]/div[@data-seat-number="%s"]' % (str(div_id), str(ticket_id_1))
# xpath_ticket_2 = '//div/ul/li[%s]/div[@data-seat-number="%s"]' % (str(div_id), str(ticket_id_2))

# print xpath_ticket_1
# print xpath_ticket_2
# element_ticket_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_ticket_1)))
# element_ticket_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_ticket_2)))
# element_ticket_1.click()
# element_ticket_2.click()


# for now check for 2 tickets in a sequence
# def check_for_n_continous_tickets(tickets_list):
# 	for i in range(len(tickets_list)-1):
# 		print i
# 		first_number = int(tickets_list[i])
# 		next_number = int(tickets_list[i+1])
# 		print first_number, next_number
# 		if (next_number == first_number+1) or (first_number == next_number+1):
# 			return first_number, next_number
# 		else:
# 			continue
		
