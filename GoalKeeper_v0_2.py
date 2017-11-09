'''
By Kevin Song
31/10/2017
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import re
#print()
#print("[" + str(datetime.now())[:19] + "]")
def assign_to_me_all():
	print("Welcome to GoalKeeper v0.1 | A Kevin Song Production")
	sleep(2)
	print("Launching Web Browser Mozilla Firefox...")
	
	driver = webdriver.Firefox()
	actions = ActionChains(driver)

	driver.get("https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D")
	print("Logining as KEVISONG...")

	sleep(3)

	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[1]/input").send_keys('KEVISONG')
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[2]/input").send_keys('Schenker160503!10')
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[3]/div/button").click()
	print("Login successful.")
	sleep(10)
	driver.switch_to.frame("gsft_main")
	
	print("Initiating GoalKeeper")

	while True:		   
		sleep(30)
		
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		incidents_numbers = len(incidents)
		if incidents_numbers == 0:
			print('----------------------------------------')
			print("[" + str(datetime.now())[:19] + "] " + 'Q is cleared   :-)')
			sleep(1)
		elif incidents_numbers == 1:
			print('----------------------------------------')
			print("[" + str(datetime.now())[:19] + "] " + '1  ticket in the Q')
			sleep(1)
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in, less than 1 m.')
				'''
				if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
					inc_with_flag_single_j_text = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]/a").text
					print('Incident:' + '\t' + inc_with_flag_single_j_text)
					print('Updated:' + '\t' + 'just now')
					print('Assigning:' + '\t' + 'No')
				else:
					inc_without_flag_single_j_text = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span/a").text
					print('Incident:' + '\t' + inc_without_flag_single_j_text)
					print('Updated:' + '\t' + 'just now')
					print('Assigning:' + '\t' + 'No')
				'''
			else:
				time = int(re.sub("\D","",updated))
				if(time >= 25):
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
						print('Incident:' + '\t' + inc_with_flag_single.text)
						print('Updated:' + '\t' + str(time) +'m')
						print('Assigning:' + '\t' + 'To Kevin Song')
						ActionChains(driver).context_click(inc_with_flag_single).perform()
						sleep(5)														
						ActionChains(driver).move_by_offset(90,173).click().perform()
					else:
						inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
						print('Incident:' + '\t' + inc_without_flag_single.text)
						print('Updated:' + '\t' + str(time) +'m')
						print('Assigning:' + '\t' + 'To Kevin Song')
						ActionChains(driver).context_click(inc_without_flag_single).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
				else:
					print("This ticket isn't over 25m, waiting.....")
		else:
			print('----------------------------------------')
			print("[" + str(datetime.now())[:19] + "] " + str(incidents_numbers) + ' tickets in the Q')
			sleep(1)
			updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[9]/span/span/div[3]/sn-time-ago/time").text
			if updated.startswith('j'):
				print('This ticket just came in, less than 1 m.')
			else:
				time = int(re.sub("\D","",updated))
				if(time >= 25):			       
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
						print('Incident:' + '\t' + inc_with_flag_muti.text)
						print('Updated:' + '\t' + str(time) +'m')
						print('Assigning:' + '\t' + 'To Kevin Song')
						ActionChains(driver).context_click(inc_with_flag_muti).perform()
						sleep(5)														
						ActionChains(driver).move_by_offset(90,173).click().perform()
					else:
						inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
						print('Incident:' + '\t' + inc_without_flag_muti.text)
						print('Updated:' + '\t' + str(time) +'m')
						print('Assigning:' + '\t' + 'To Kevin Song')
						ActionChains(driver).context_click(inc_without_flag_muti).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
				else:
					print("These tickets aren't over 25m, waiting..")

assign_to_me_all()