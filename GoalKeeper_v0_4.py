'''
By Kevin Song
31/10/2017
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import re

driver = webdriver.Firefox()

def initiate(username,password,url):
	print("Welcome to GoalKeeper v0.4 | A Kevin Song Production")
	sleep(2)

	print("Launching Web Browser Mozilla Firefox...")
	
	actions = ActionChains(driver)

	driver.get(str(url))
	print("Logining as " + str(username) + "...")

	sleep(3)

	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[1]/input").send_keys(str(username))
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[2]/input").send_keys(str(password))
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[3]/div/button").click()
	print("Login successful.")
	sleep(20)

	# try-except needed here...
	driver.switch_to.frame("gsft_main")


def assign_to_me_all(time):

	print("Initiating GoalKeeper")
	#counter = 0
	while True:
		'''
		counter = counter + 1
		
		if counter == 3:
			driver.refresh()
			sleep(5)
			counter = 0
		'''
		sleep(10)

		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		incidents_numbers = len(incidents)
		if incidents_numbers == 0:
			print('----------------------------------------')
			sleep(2)
			print("[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			sleep(2)
			print("[" + str(datetime.now())[:19] + "] " + 'Queue is cleared:)')
			sleep(2)
		elif incidents_numbers == 1:
			print('----------------------------------------')
			sleep(2)
			print("[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			sleep(2)
			print("[" + str(datetime.now())[:19] + "] " + '1  ticket in the Q')
			sleep(2)
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j'):
				print('This ticket just came in, less than 1 m.')
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if(updated_time >= int(time)):
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
						print('Incident:' + '\t' + inc_with_flag_single.text)
						print('Updated:' + '\t' + str(updated_time) +'m')
						print('Assigning:' + '\t' + 'To '+ str(username))
						ActionChains(driver).context_click(inc_with_flag_single).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						print('Assignment Complete')
					else:
						inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
						print('Incident:' + '\t' + inc_without_flag_single.text)
						print('Updated:' + '\t' + str(updated_time) +'m')
						print('Assigning:' + '\t' + 'To '+ str(username))
						ActionChains(driver).context_click(inc_without_flag_single).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						print('Assignment Complete')
				else:
					print("This ticket isn't over " + str(time) + "m, waiting.." )
		else:
			print('----------------------------------------')
			sleep(2)
			print("[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			sleep(2)
			print("[" + str(datetime.now())[:19] + "] " + str(incidents_numbers) + ' tickets in the Q')
			sleep(2)
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j'):
				print('This ticket just came in, less than 1 m.')
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if(updated_time >= int(time)):
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
						print('Incident:' + '\t' + inc_with_flag_muti.text)
						print('Updated:' + '\t' + str(updated_time) +'m')
						print('Assigning:' + '\t' + 'To '+ str(username))
						ActionChains(driver).context_click(inc_with_flag_muti).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						print('Assignment Complete')
					else:
						inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
						print('Incident:' + '\t' + inc_without_flag_muti.text)
						print('Updated:' + '\t' + str(updated_time) +'m')
						print('Assigning:' + '\t' + 'To '+ str(username))
						ActionChains(driver).context_click(inc_without_flag_muti).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						print('Assignment Complete')
				else:
					print("These tickets aren't over " + str(time) + "m, waiting.." )


url = "https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D"

initiate('KEVISONG','Schenker160503!10',url)

assign_to_me_all(25)