'''
By Kevin Song
31/10/2017
AA check
AE check
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
	console.insert(END,"Welcome to GoalKeeper v0.8 | For I T S D"+'\n')
	console.see(END)
	sleep(1)
	console.insert(END,"Launching Web Browser Mozilla Firefox..."+'\n')
	console.see(END)
	driver.get(str(url).strip())
	console.insert(END,"Logining as " + str(username) + "..."+'\n')
	console.see(END)
	sleep(10)
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[1]/input").send_keys(str(username))
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[1]/fieldset/div[2]/input").send_keys(str(password))
	driver.find_element_by_xpath("/html/body/article/div[2]/div/form/div[3]/div/button").click()
	console.insert(END,"Login successful."+'\n')
	console.see(END)
	sleep(15)
	driver.switch_to.frame("gsft_main")

def assign_to_me_all(time):
	console.insert(END,"Initiating GoalKeeper"+'\n')
	console.see(END)
	QClear_Counter = 0
	AE_Counter = 0
	while True:
		sleep(5)
		AE_Counter = AE_Counter + 1
		incidents = driver.find_elements_by_xpath(".//*[@class='ng-scope ng-isolate-scope data_row']"+'\n')
		incidents_numbers = len(incidents)
		if incidents_numbers == 0:
			console.insert(END,'----------------------------------------'+'\n')
			console.see(END)
			sleep(1)
			console.insert(END,"[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue'+'\n')
			console.see(END)
			sleep(1)
			console.insert(END,"[" + str(datetime.now())[:19] + "] " + 'Queue is cleared:)'+'\n')
			console.see(END)
			QClear_Counter = QClear_Counter + 1
			if QClear_Counter == 3:
				console.insert(END,"Q is cleared for a long time. Rebooting."+'\n')
				driver.close()
				break
			sleep(1)
		elif incidents_numbers == 1:
			console.insert(END,'----------------------------------------'+'\n')
			console.see(END)
			sleep(1)
			console.insert(END,"[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue'+'\n')
			console.see(END)
			sleep(1)
			console.insert(END,"[" + str(datetime.now())[:19] + "] " + '[1] ticket in Q'+'\n')
			console.see(END)
			sleep(1)
			#updated = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[9]/span/span/div[3]/sn-time-ago/time").text
			updated = driver.find_elements_by_tag_name('time')   
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'This ticket just came in, less than 1 m.'+'\n')
				console.see(END)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(time)) or (AE_Counter == 10)):
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_single =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span[2]")#####
						console.insert(END,'Incident:' + '\t\t' + inc_with_flag_single.text+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Updated:' + '\t\t' + str(updated_time) +'m'+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Assigning:' + '\t\t' + 'To '+ str(username)+'\n')
						console.see(END)
						sleep(1)
						ActionChains(driver).context_click(inc_with_flag_single).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						console.insert(END,'Assignment Complete'+'\n')
						console.see(END)
					else:
						inc_without_flag_single = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr/td[3]/span")########
						console.insert(END,'Incident:' + '\t\t' + inc_without_flag_single.text+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Updated:' + '\t\t' + str(updated_time) +'m'+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Assigning:' + '\t\t' + 'To '+ str(username)+'\n')
						console.see(END)
						sleep(1)
						ActionChains(driver).context_click(inc_without_flag_single).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						console.insert(END,'Assignment Complete'+'\n')
						console.see(END)
				else:
					console.insert(END,"This ticket isn't over " + str(time) + "m, waiting.." +'\n')
					console.see(END)
				#Assign Every code goes here
		else:
			console.insert(END,'----------------------------------------'+'\n')
			console.see(END)
			sleep(1)
			console.insert(END,"[" + str(datetime.now())[:19] + "] " + 'Scanning the Queue'+'\n')
			console.see(END)
			sleep(1)
			console.insert(END,"[" + str(datetime.now())[:19] + "] " + '[' + str(incidents_numbers) + ']' + ' tickets in Q'+'\n')
			console.see(END)
			sleep(1)
			updated = driver.find_elements_by_tag_name('time')
			if updated[0].text.startswith('j') or updated[0].text.startswith('a'):
				console.insert(END,'This ticket just came in, less than 1 m.'+'\n')
				console.see(END)
			else:
				updated_time = int(re.sub("\D","",updated[0].text))
				if((updated_time >= int(time)) or (AE_Counter == 10)):
					if(driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[12]/span/span").text == 'true'):
						inc_with_flag_muti =    driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span[2]")#####
						console.insert(END,'Incident:' + '\t\t' + inc_with_flag_muti.text+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Updated:' + '\t\t' + str(updated_time) +'m'+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Assigning:' + '\t\t' + 'To '+ str(username)+'\n')
						console.see(END)
						sleep(1)
						ActionChains(driver).context_click(inc_with_flag_muti).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						console.insert(END,'Assignment Complete'+'\n')
						console.see(END)
					else:
						inc_without_flag_muti = driver.find_element_by_xpath("/html/body/sn-list-parent/sn-list/div/div/div/div[2]/div/div[3]/table[1]/tbody/tr[1]/td[3]/span")########
						console.insert(END,'Incident:' + '\t\t' + inc_without_flag_muti.text+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Updated:' + '\t\t' + str(updated_time) +'m'+'\n')
						console.see(END)
						sleep(1)
						console.insert(END,'Assigning:' + '\t\t' + 'To '+ str(username)+'\n')
						console.see(END)
						sleep(1)
						ActionChains(driver).context_click(inc_without_flag_muti).perform()
						sleep(5)
						ActionChains(driver).move_by_offset(90,173).click().perform()
						console.insert(END,'Assignment Complete'+'\n')
						console.see(END)
				else:
					console.insert(END,"These tickets aren't over " + str(time) + "m, waiting.." +'\n')
					console.see(END)
		sleep(5)


def run(username,password,url,time):
	#url = "https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D"
	while True:
		try:
			global driver
			driver = webdriver.Firefox()
			login(username,password,url)
			assign_to_me_all(time)
		except Exception as e:
			console.insert(END,'An error occurred, rebooting GoalKeeper.'+'\n')
			console.see(END)
			driver.close()
			pass

def run_multi(username,password,url,time):
	th = threading.Thread(target=run,args=(username,password,url,time))  
	#th.setDaemon(True)守护线程  
	th.start()
		
def stop():
	try:
		console.insert(END,'Stopping...'+'\n')
		driver.close()
	except Exception as e:
		console.insert(END,'GoalKeeper is not running.'+'\n')

def stop_multi():
	th2=threading.Thread(target=stop)  
	#th.setDaemon(True)守护线程  
	th2.start()

username = 'KEVISONG'
password = 'Schenker160503!10'
url = 'https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3Dassignment_group%253Dc299e951dbfd7e001529f3571d961913%255Eassigned_to%253D%255EstateNOT%2520IN6,7,8%26sysparm_fixed_query%3D'
url_test_assign = 'https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3DGOTOnumber%253DINC000497402%26sysparm_fixed_query%3D'
url_test_clear ='https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_fixed_query%3D%26sysparm_query%3Dnumber%253DINC000497402%255Enumber!%253DINC000497402%26sysparm_clear_stack%3Dtrue'
url_test_wrong = 'This is wrong url'
time = 1


#GUI
root = Tk()
root.title("GoalKeeper v0.8")
root.resizable(width = False, height = False)
Label(root, font=('Consolas',12),fg = 'gold',bg='grey', width=31, height=2, text="Enter Information").grid(row=0,columnspan=2,sticky = W + E + N + S)
Label(root, font=('Consolas',12),fg = 'white',bg='grey', width=17, text="SIMS ID").grid(row=1,sticky = W + E + N + S,pady=2)
Label(root, font=('Consolas',12),fg = 'white',bg='grey', width=17, text="Password").grid(row=2,sticky = W + E + N + S)
Label(root, font=('Consolas',12),fg = 'white',bg='grey', width=17, text="ServiceNow URL").grid(row=3,sticky = W + E + N + S,pady=2)
Label(root, font=('Consolas',12),fg = 'white',bg='grey', width=17, text="Time").grid(row=4, sticky = W + E + N + S)

x = StringVar()
y = StringVar()
z = StringVar()
n = StringVar()

e1 = Entry(root, font=('Consolas',12),fg = 'grey',width=20, textvariable = x)
e2 = Entry(root, font=('Consolas',12),fg = 'grey',width=20, textvariable = y)
e3 = Entry(root, font=('Consolas',12),fg = 'grey',width=20, textvariable = z)
e4 = Entry(root, font=('Consolas',12),fg = 'grey',width=20, textvariable = n)

x.set(username)
y.set(password)
z.set(url_test_clear)
n.set(time)

e1.grid(row=1, column=1,sticky = W + E + N + S,pady=2)
e2.grid(row=2, column=1,sticky = W + E + N + S)
e3.grid(row=3, column=1,sticky = W + E + N + S,pady=2)
e4.grid(row=4, column=1,sticky = W + E + N + S)


button_start = Button(root,text = "S T A R T", font=('Consolas',12),fg = 'white',bg='grey',command = lambda:run_multi(e1.get(),e2.get(),e3.get(),e4.get()))
#button_stop = Button(root, text = "Stop", font=('Consolas',10),command = stop_multi)
button_start.grid(row = 150, column = 0, rowspan = 100, columnspan = 2, sticky = W + E + N + S)
#button_stop.grid(row = 12, column = 0, rowspan = 3, columnspan = 2, padx = 10, pady = 10, sticky = W + E + N + S)

console = scrolledtext.ScrolledText(root, font=('Consolas',12),fg='white',bg='black',width=40, height=25, wrap=WORD)
console.grid(row = 0, column=2, rowspan = 200, sticky = W + E + N + S)

if __name__=='__main__':
	mainloop()