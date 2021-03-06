'''
By Kevin Song
31/10/2017
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

def assign_to_me_all():

	driver = webdriver.Firefox()
	actions = ActionChains(driver)

	driver.get("https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D")

	sleep(3)

	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[1]/input").send_keys('KEVISONG')
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[2]/input").send_keys('Schenker160503!10')
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[3]/div/button").click()
	sleep(10)
	driver.switch_to.frame("gsft_main")

	while True:		   
		sleep(60)

		print('[---------------------------------------------------------------------------]')
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		incidents_numbers = len(incidents)

		if incidents_numbers == 0:
			print(str(len(incidents)) + ' tickets in the Q, waiting...')
		elif incidents_numbers == 1:
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in.')
			else:
				time = int(re.sub("\D","",updated))
				if(time >= 20):
					print('This ticket is over 20 min, Waiting to be assigned in 3 seconds...')
					print('Assigning to Kevin Song')	
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
						ActionChains(driver).context_click(inc_with_flag_single).perform()
						sleep(5)														
						ActionChains(driver).move_by_offset(90,173).click().perform()
					else:
						inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
						ActionChains(driver).context_click(inc_without_flag_single).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
					print('Assignment complete')
				else:
					print("This ticket isn't over 20 mins, waiting...")
		else:
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in.')
			else:
				time = int(re.sub("\D","",updated))
				if(time >= 20):
					print('The first ticket is over 20 min, waiting to be assigned in 3 seconds...')
					print('Assigning to Kevin Song')				       
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
						ActionChains(driver).context_click(inc_with_flag_muti).perform()
						sleep(5)														
						ActionChains(driver).move_by_offset(90,173).click().perform()
					else:
						inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
						ActionChains(driver).context_click(inc_without_flag_muti).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
					print('Assignment complete')
				else:
					print('These tickets are not over 20 mins, waiting...')

assign_to_me_all()