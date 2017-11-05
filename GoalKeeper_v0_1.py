'''
By Kevin Song

31/10/2017
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import GoalKeeperGUI
'''
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D")
sleep(3)
'''
#incidents = driver.find_elements_by_class_name("ng-scope ng-isolate-scope data_row")

def go():

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
		sleep(5)			  #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr   /td[9]/span/span/div[3]/sn-time-ago/time
		#if (is_element_exist("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time")):
		'''
		if (is_element_exist(xpath)):
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_xpath(xpath)[0].text
			print('Updated time is :' + updated)
		'''
		#incidents = driver.find_elements_by_class_name("ng-scope ng-isolate-scope data_row")
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		if len(incidents) == 0:
			print(str(len(incidents)) + ' tickets in the Q, refreshing page...')
			actions.key_down(Keys.F5)
			actions.key_up(Keys.F5)
			#sleep(3)
		elif len(incidents) == 1:
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in.')
			else:
				if(int(re.sub("\D","",updated)) >= 15):
					print('This ticket is over 15 min, Waiting to be assigned...')
					actions.context_click(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]/a"))
					#actions.move_by_offset(90,173).click()
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
				if(int(re.sub("\D","",updated)) >= 15):
					print('The first ticket is over 15 min, waiting to be assigned...')
					actions.context_click(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]/a"))
					#actions.move_by_offset(90,173).click()
				else:
					print('These tickets are not over 15 mins, waiting...')
					#sleep(10)
					actions.key_down(Keys.F5)
					actions.key_up(Keys.F5)

go()