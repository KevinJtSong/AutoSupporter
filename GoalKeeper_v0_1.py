'''
By Kevin Song
31/10/2017
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
#driver.find_element_by_xpath('/html/body/div[3]/ul/li[8]/a')
def go():

	driver = webdriver.Firefox()
	actions = ActionChains(driver)

	driver.get("https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D")

	sleep(3)

	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[1]/input").send_keys('KEVISONG')
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[2]/input").send_keys('Schenker160503!10')
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[3]/div/button").click()
	sleep(10)
	sleep(60)

	driver.switch_to.frame("gsft_main")

	while True:		   
		sleep(20)			  #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr   /td[9]/span/span/div[3]/sn-time-ago/time
		#if (is_element_exist("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time")):
		'''
		if (is_element_exist(xpath)):
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_xpath(xpath)[0].text
			print('Updated time is :' + updated)
		'''
		#incidents = driver.find_elements_by_class_name("ng-scope ng-isolate-scope data_row")
		print('[---------------------------------------------------------------------------]')
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		if len(incidents) == 0:
			print(str(len(incidents)) + ' tickets in the Q, waiting...')
			actions.key_down(Keys.F5)
			actions.key_up(Keys.F5)
			#sleep(3)
		elif len(incidents) == 1:
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in.')
			else:
				time = int(re.sub("\D","",updated))
				if(time >= 1):
					print('This ticket is over 15 min, Waiting to be assigned in 3 seconds...')
					print('Assigning to Kevin Song')	
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						#actions.context_click(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]/a"))
																	           #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]/a
						inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
						actions.context_click(inc_with_flag_single).perform()#.move_by_offset(90,173).click()
						sleep(10)														
						actions.move_by_offset(90,173).perform().click()
						#driver.find_element_by_xpath('/html/body/div[3]/ul/li[8]/a').click()
					else:												       
						#actions.context_click(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span/a")
																			   #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span/a
						inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
						actions.context_click(inc_without_flag_single).perform()#.move_by_offset(90,173).click()
						sleep(10)
						actions.move_by_offset(90,173).perform().click()
						#driver.find_element_by_xpath('/html/body/div[3]/ul/li[8]/a').click()
					print('Assignment complete')
				else:
					print("This ticket isn't over 15 mins, waiting...")
					#sleep(10)
					actions.key_down(Keys.F5)
					actions.key_up(Keys.F5)
		else:
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in.')
			else:
				time = int(re.sub("\D","",updated))
				if(time >= 1):
					print('The first ticket is over 15 min, waiting to be assigned in 3 seconds...')
					print('Assigning to Kevin Song')				       
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						#actions.context_click(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]/a"))
																		     #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]/a
						inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
						actions.context_click(inc_with_flag_muti).perform()#.move_by_offset(90,173).click()
						sleep(10)														
						actions.move_by_offset(90,173).perform().click()
						#driver.find_element_by_xpath('/html/body/div[3]/ul/li[8]/a').click()
					else:												    
						#actions.context_click(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span/a")
																			 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span/a
						inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
						actions.context_click(inc_without_flag_muti).perform()#.move_by_offset(90,173).click()
						sleep(10)
						actions.move_by_offset(90,173).perform().click()
						#driver.find_element_by_xpath('/html/body/div[3]/ul/li[8]/a').click()
					print('Assignment complete')
				else:
					print('These tickets are not over 15 mins, waiting...')
					#sleep(10)
					actions.key_down(Keys.F5)
					actions.key_up(Keys.F5)
		print('[---------------------------------------------------------------------------]')

go()