'''
By Kevin Song
31/10/2017
AA check
AE check
Commodity check
Fast check
All check
'''
from tkinter import *
from tkinter import scrolledtext

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
from datetime import datetime

import re
import threading

def login(username,password,url):
	console.insert(END,"Welcome to " + version + "|For I T S D")
	console.see(END)
	sleep(1)
	console.insert(END,'\n' + "Launching Web Browser Mozilla Firefox...")
	console.see(END)
	driver.get(str(url).strip())
	driver.set_window_size(1280,800)
	console.insert(END,'\n' + "Logining in as " + str(username) + "...")
	console.see(END)
	sleep(10)
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[1]/input").send_keys(str(username))
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[2]/input").send_keys(str(password))
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[3]/div/button").click()
	console.insert(END,'\n' + "Login successful.")
	console.see(END)
	sleep(15)
	driver.switch_to.frame("gsft_main")

def assign_to_me_comm(assign_after,assign_every):
	console.insert(END,'\n' + "Initiating GoalKeeper For Commodity")
	console.see(END)
	commodity = ['EMAS','SIMS','VPN','GWM','End User Services']
	QClear_Counter = 0
	AE_Counter = 0
	scan_time = 4
	assign_every_counter = int((int(assign_every) * 60) / (scan_time + 6) / 2)
	while True:
		sleep(scan_time)
		AE_Counter = AE_Counter + 1
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		incidents_numbers = len(incidents)
		if incidents_numbers == 0:#2
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Queue is cleared:)')
			console.see(END)
			QClear_Counter = QClear_Counter + 1
			if QClear_Counter == 31:
				console.insert(END,'\n' + "Q is cleared for a long time. Rebooting.")
				driver.close()
				break
			sleep(10)
		elif incidents_numbers == 1:# 12                                                         
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + '[1] ticket in Q')
			console.see(END)
			sleep(1)
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'\n' + 'This ticket just came in, less than 1 m.')
				console.see(END)
				sleep(9)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(assign_after)) or (AE_Counter >= assign_every_counter)):
					try:
						bus_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a").text
					except Exception as e:
						bus_single = 'Is Empty'
					prio_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[5]/span[2]/span")
					if(bus_single in commodity):
						if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
							#bus_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a")
							inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_with_flag_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_with_flag_single).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
						else:
							#bus_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a")
							inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_without_flag_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_without_flag_single).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
					else:
						console.insert(END,'\n' + 'This is not a Commodity Group Ticket')
						console.see(END)
						sleep(9)
				else:
					console.insert(END,'\n' + "This ticket isn't over " + str(assign_after) + "m, waiting..")
					console.see(END)
					sleep(9)
				#Assign Every code goes here
		else:
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + '[' + str(incidents_numbers) + ']' + ' tickets in Q')
			console.see(END)
			sleep(1)
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'\n' + 'This ticket just came in, less than 1 m.')
				console.see(END)
				sleep(9)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(assign_after)) or (AE_Counter >= assign_every_counter)):
					try:
						bus_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a").text
					except Exception as e:
						bus_muti = 'Is Empty'
					prio_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[5]/span[2]/span")
					if(bus_muti in commodity):
						if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'): 
							#bus_with_flag_muti =	driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a")
							inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_with_flag_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_with_flag_muti).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)									 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a
						else:													 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a
							#bus_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a")
							inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_without_flag_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_without_flag_muti).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
					else:
						console.insert(END,'\n' + 'This is not a Commodity Group Ticket')
						console.see(END)
						sleep(9)
				else:
					console.insert(END,'\n' + "These tickets aren't over " + str(assign_after) + "m, waiting..")
					console.see(END)
					sleep(9)
		sleep(scan_time)


def assign_to_me_fast(assign_after,assign_every):
	console.insert(END,'\n' + "Initiating GoalKeeper For Fast Group")
	console.see(END)
	commodity = ['EMAS','SIMS','VPN','GWM','End User Services']
	QClear_Counter = 0
	AE_Counter = 0
	scan_time = 4
	assign_every_counter = int((int(assign_every) * 60) / (scan_time + 6) / 2)
	while True:
		sleep(scan_time)
		AE_Counter = AE_Counter + 1
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		incidents_numbers = len(incidents)
		if incidents_numbers == 0:
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Queue is cleared:)')
			console.see(END)
			QClear_Counter = QClear_Counter + 1
			if QClear_Counter == 31:
				console.insert(END,'\n' + "Q is cleared for a long time. Rebooting.")
				driver.close()
				break
			sleep(10)
		elif incidents_numbers == 1:                                                          
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + '[1] ticket in Q')
			console.see(END)
			sleep(1)
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'\n' + 'This ticket just came in, less than 1 m.')
				console.see(END)
				sleep(9)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(assign_after)) or (AE_Counter >= assign_every_counter)):
					try:
						bus_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a").text
					except Exception as e:
						bus_single = 'Is Empty'
					prio_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[5]/span[2]/span")
					if(bus_single not in commodity):
						if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
							#bus_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a")
							inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_with_flag_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_with_flag_single).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
						else:
							#bus_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a")
							inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_without_flag_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_without_flag_single).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
					else:
						console.insert(END,'\n' + 'This is not a Fast Group Ticket')
						console.see(END)
						sleep(9)
				else:
					console.insert(END,'\n' + "This ticket isn't over " + str(assign_after) + "m, waiting..")
					console.see(END)
					sleep(9)
				#Assign Every code goes here
		else:
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + '[' + str(incidents_numbers) + ']' + ' tickets in Q')
			console.see(END)
			sleep(1)
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'\n' + 'This ticket just came in, less than 1 m.')
				console.see(END)
				sleep(9)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(assign_after)) or (AE_Counter >= assign_every_counter)):
					try:
						bus_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a").text
					except Exception as e:
						bus_muti = 'Is Empty'
					prio_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[5]/span[2]/span")
					if(bus_muti not in commodity):
						if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'): 
							#bus_with_flag_muti =	driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a")
							inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_with_flag_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_with_flag_muti).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)									 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a
						else:													 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a
							#bus_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a")
							inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_without_flag_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_without_flag_muti).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
					else:
						console.insert(END,'\n' + 'This is not a Fast Group Ticket')
						console.see(END)
						sleep(9)
				else:
					console.insert(END,'\n' + "These tickets aren't over " + str(assign_after) + "m, waiting..")
					console.see(END)
					sleep(9)
		sleep(scan_time)

def assign_to_me_all(assign_after,assign_every):
	console.insert(END,'\n' + "Initiating GoalKeeper For All Tickets")
	console.see(END)
	commodity = ['EMAS','SIMS','VPN','GWM','End User Services']
	QClear_Counter = 0
	AE_Counter = 0
	scan_time = 4
	assign_every_counter = int((int(assign_every) * 60) / (scan_time + 6) / 2)
	while True:
		sleep(scan_time)
		AE_Counter = AE_Counter + 1
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']")
		incidents_numbers = len(incidents)
		if incidents_numbers == 0:
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Queue is cleared:)')
			console.see(END)
			QClear_Counter = QClear_Counter + 1
			if QClear_Counter == 31:
				console.insert(END,'\n' + "Q is cleared for a long time. Rebooting.")
				driver.close()
				break
			sleep(10)
		elif incidents_numbers == 1:                                                          
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + '[1] ticket in Q')
			console.see(END)
			sleep(1)
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'\n' + 'This ticket just came in, less than 1 m.')
				console.see(END)
				sleep(9)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(assign_after)) or (AE_Counter >= assign_every_counter)):
					try:
						bus_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a").text
					except Exception as e:
						bus_single = 'Is Empty'
					prio_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[5]/span[2]/span")
					if True:
						if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
							#bus_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a")
							inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_with_flag_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_with_flag_single).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
						else:
							#bus_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a")
							inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_without_flag_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_single.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_without_flag_single).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
							sleep(9)
				else:
					console.insert(END,'\n' + "This ticket isn't over " + str(assign_after) + "m, waiting..")
					console.see(END)
					sleep(9)
				#Assign Every code goes here
		else:
			console.insert(END,'\n' + '----------------------------------------')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue')
			console.see(END)
			sleep(1)
			console.insert(END,'\n' + "[" + str(datetime.now())[:19] + "] " + '[' + str(incidents_numbers) + ']' + ' tickets in Q')
			console.see(END)
			sleep(1)
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'\n' + 'This ticket just came in, less than 1 m.')
				console.see(END)
				sleep(9)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(assign_after)) or (AE_Counter >= assign_every_counter)):
					try:
						bus_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a").text
					except Exception as e:
						bus_muti = 'Is Empty'
					prio_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[5]/span[2]/span")
					if True:
						if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'): 
							#bus_with_flag_muti =	driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a")
							inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_with_flag_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_with_flag_muti).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)									 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[6]/span/a
						else:													 #/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a
							#bus_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[6]/span/a")
							inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
							console.insert(END,'\n' + 'Incident:' + '\t\t' + inc_without_flag_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Updated:' + '\t\t' + str(updated_time) +'m')
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Priority:' + '\t\t' + prio_muti.text)
							console.see(END)
							sleep(1)
							console.insert(END,'\n' + 'Assigning to:' + '\t\t' + str(username))
							console.see(END)
							sleep(1)
							ActionChains(driver).context_click(inc_without_flag_muti).perform()
							sleep(5)
							ActionChains(driver).move_by_offset(90,173).click().perform()
							if AE_Counter >= assign_every_counter:
								AE_Counter = 0
							console.insert(END,'\n' + 'Assignment:' + '\t\t' + 'Complete')
							console.see(END)
							sleep(9)
				else:
					console.insert(END,'\n' + "These tickets aren't over " + str(assign_after) + "m, waiting..")
					console.see(END)
					sleep(9)
		sleep(scan_time)

def assign_to_me_comm_init(username,password,url,assign_after,assign_every):
	#url = "https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D"
	while True:
		try:
			global driver
			driver = webdriver.Firefox()
			login(username,password,url)
			assign_to_me_comm(assign_after,assign_every)
		except Exception as e:
			try:
				driver.close()
			except WebDriverException as e2:
				console.insert(END,'\n' + 'GoalKeeper Stopped Manually.' + '\n')
				console.see(END)
				break
			console.insert(END, '\n' + 'An error occurred, rebooting GoalKeeper.' + '\n')
			console.see(END)
			print("[" + str(datetime.now())[:19] + "] ")
			print(e)
			pass

def assign_to_me_fast_init(username,password,url,assign_after,assign_every):
	while True:
		try:
			global driver
			driver = webdriver.Firefox()
			login(username,password,url)
			assign_to_me_fast(assign_after,assign_every)
		except Exception as e:
			try:
				driver.close()
			except WebDriverException as e2:
				console.insert(END,'\n' + 'GoalKeeper Stopped Manually.' + '\n')
				console.see(END)
				break
			console.insert(END, '\n' + 'An error occurred, rebooting GoalKeeper.' + '\n')
			console.see(END)
			print("[" + str(datetime.now())[:19] + "] ")
			print(e)
			pass

def assign_to_me_all_init(username,password,url,assign_after,assign_every):
	while True:
		try:
			global driver
			driver = webdriver.Firefox()
			login(username,password,url)
			assign_to_me_all(assign_after,assign_every)
		except Exception as e:
			try:
				driver.close()
			except WebDriverException as e2:
				console.insert(END,'\n' + 'GoalKeeper Stopped Manually.' + '\n')
				console.see(END)
				break
			console.insert(END, '\n' + 'An error occurred, rebooting GoalKeeper.' + '\n')
			console.see(END)
			print("[" + str(datetime.now())[:19] + "] ")
			print(e)
			pass

def assign_to_me_comm_muti(username,password,url,assign_after,assign_every):
	th = threading.Thread(target=assign_to_me_comm_init,args=(username,password,url,assign_after,assign_every))  
	#th.setDaemon(True)守护线程  
	th.start()

def assign_to_me_fast_muti(username,password,url,assign_after,assign_every):
	th2 = threading.Thread(target=assign_to_me_fast_init,args=(username,password,url,assign_after,assign_every))  
	#th.setDaemon(True)守护线程  
	th2.start()

def assign_to_me_all_muti(username,password,url,assign_after,assign_every):
	th3 = threading.Thread(target=assign_to_me_all_init,args=(username,password,url,assign_after,assign_every))  
	#th.setDaemon(True)守护线程  
	th3.start()


def stop():
	try:
		console.insert(END,'\n' + 'Stopping...')
		driver.close()
	except Exception as e:
		console.insert(END,'\n' + 'GoalKeeper is not running.')

def stop_multi():
	th2=threading.Thread(target=stop)  
	#th.setDaemon(True)守护线程  
	th2.start()
'''
username = 'KEVISONG'
password = 'Schenker160503!10'
url = 'https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_fixed_query%3D%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255EORassignment_group%253D35d1fca1db2ab6001529f3571d96191f%255EORassignment_group%253Da7b5f56fdb79f240b809f1c41d961904%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_clear_stack%3Dtrue'
url_test_assign = 'https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3DGOTOnumber%253DINC000497402%26sysparm_fixed_query%3D'
url_test_clear ='https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_fixed_query%3D%26sysparm_query%3Dnumber%253DINC000497402%255Enumber!%253DINC000497402%26sysparm_clear_stack%3Dtrue'
url_test_wrong = 'This is wrong url'
url_jia = ''
url_leo = ''
assign_after = 1
assign_every = 20
'''
version = 'GoalKeeper v0.9.3'
with open('Settings.ini', 'r') as f:
    username = f.readline().strip()
    password = f.readline().strip()
    url = f.readline().strip()
    assign_after = f.readline().strip()
    assign_every = f.readline().strip()


#GUI
root = Tk()
root.title(version)
root.resizable(width = False, height = False)


Label(root, font=('Consolas',10),fg = '#EEB422',bg='#191926', width=31, height=2, text="GoalKeeper | ITSD").grid(row=0,columnspan=2,sticky = W + E + N + S)
Label(root, font=('Consolas',10),fg = 'white',bg='#191970', width=17, height=1, text="SIMS ID").grid(row=1,sticky = W + E + N + S,pady=1)
Label(root, font=('Consolas',10),fg = 'white',bg='#191970', width=17, height=1, text="Password").grid(row=2,sticky = W + E + N + S)
Label(root, font=('Consolas',10),fg = 'white',bg='#191970', width=17, height=1, text="ServiceNow URL").grid(row=3,sticky = W + E + N + S,pady=1)
Label(root, font=('Consolas',10),fg = 'white',bg='#191970', width=17, height=1, text="Assign After").grid(row=4, sticky = W + E + N + S)
Label(root, font=('Consolas',10),fg = 'white',bg='#191970', width=17, height=1, text="Assign Every").grid(row=5, sticky = W + E + N + S,pady=1)

x = StringVar()
y = StringVar()
z = StringVar()
n = StringVar()
m = StringVar()

e1 = Entry(root, font=('Consolas',10),fg = 'black',width=20, textvariable = x)
e2 = Entry(root, show='*', font=('Consolas',10),fg = 'black',width=20, textvariable = y)
e3 = Entry(root, font=('Consolas',10),fg = 'black',width=20, textvariable = z)
e4 = Entry(root, font=('Consolas',10),fg = 'black',width=20, textvariable = n)
e5 = Entry(root, font=('Consolas',10),fg = 'black',width=20, textvariable = m)

x.set(username)
y.set(password)
z.set(url)
n.set(assign_after)
m.set(assign_every)

e1.grid(row=1, column=1,sticky = W + E + N + S,pady=1)
e2.grid(row=2, column=1,sticky = W + E + N + S)
e3.grid(row=3, column=1,sticky = W + E + N + S,pady=1)
e4.grid(row=4, column=1,sticky = W + E + N + S)
e5.grid(row=5, column=1,sticky = W + E + N + S,pady=1)

button_start_comm = Button(root,text = "Start as Commodity",relief=FLAT, font=('Consolas',10),fg = 'white',bg='#191930',command = lambda:assign_to_me_comm_muti(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
button_start_fast = Button(root,text = "Start as Fast",relief=FLAT, font=('Consolas',10),fg = 'white',bg='#191930',command = lambda:assign_to_me_fast_muti(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
button_start_all = Button(root,text = "Start as All",relief=FLAT, font=('Consolas',10),fg = 'white',bg='#191930',command = lambda:assign_to_me_all_muti(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
button_start_comm.grid(row = 6, column = 0, columnspan = 2, sticky = W + E + N + S)
button_start_fast.grid(row = 7, column = 0, columnspan = 2, sticky = W + E + N + S,pady=1)
button_start_all.grid(row = 8, column = 0, columnspan = 2, sticky = W + E + N + S)
#button_stop.grid(row = 12, column = 0, rowspan = 3, columnspan = 2, padx = 10, pady = 10, sticky = W + E + N + S)

console = scrolledtext.ScrolledText(root, font=('Consolas',10),fg='white',bg='black',width=40, height=30, wrap=WORD)
console.grid(row = 0, column=2, rowspan = 9, sticky = W + E + N + S)

if __name__=='__main__':
	mainloop()