#!/usr/bin/python3

import platform #To get OS Version
import subprocess #For Private, public IP, default gateway
import shutil # to check free/used space
import time # for free space and CPU usage time indicator
import os # to get directory listing and measure folder size
from time import sleep # To refresh functions and create a slowed down effect
import psutil # For CPU usage
import datetime # For timestamp to monitor CPU usage refresh

def taskbanner():
	print('')
	sleep(1)
	print('Student Name          : Fransiskus Asisi Bhismobroto')
	print('Student Code          : s10')
	print('Unit                  : CFC090423')
	print('Intiate XE105 Project : Python Fundamental')
	print('')
	sleep(2)	

def task1():
	print('Initiating Task 1/5')
	sleep(1.5)
	print('--------------------Task 1--------------------')
	sleep(1.5)
	platsys=platform.system()
	print("The Operating System is:          :",platsys)
	platplat=platform.platform()
	print("The Version of Operating System is:",platplat)
	print('----------------------------------------------')
	sleep(1.5)
		
def task2():
	print('')
	print('Initiating Task 2/5')
	sleep(1.5)
	print('--------------------Task 2--------------------')
	sleep(1.5)
	#Task 2.1: Display Private IP Address
	ifconfig_result=subprocess.run(['ifconfig'], capture_output= True, text=True)
	output=ifconfig_result.stdout
	private_ip=output.split(' ')
	output_list=output.split(' ')
	print('Private IP Address is        :',output_list[13]) #From the result of output (in list form), Internal IP is the 14th item (index 13)
	print('')
	#Task 2.2: Display Default Gateway IP Address: call up another portion of output list	
	print('Default Gateway Address is   :',output_list[19])#From the result of output (in list form), default gateway IP is the 20th item (index 19)
	#Task 2.3: Display Public IP Address
	ifconfig_io_result=subprocess.run(['curl','ifconfig.io'], capture_output= True, text=True)
	public_ip=ifconfig_io_result.stdout
	print('Public IP Address is         :',public_ip)
	print('----------------------------------------------')
	sleep(1.5)

def task3():
	print('')
	print('Initiating Task 3/5')
	sleep(1.5)
	print('--------------------Task 3--------------------')
	a,b,c=shutil.disk_usage('/') 
		# This function retrieve total, used and free harddisk space in order as a,b,c
		# As path is necessary, for this project, the total harddisk space in root level is taken (hence '/' as path)
	print('Total Hard Disk Size  :  ',int(a/2**30),'GB')
	sleep(0.5)
	print('Used Hard Disk Size   :  ',int(b/2**30),'GB')
	sleep(0.5)
	print('Free Hards Disk Size  :  ',int(c/2**30),'GB')
	print('----------------------------------------------')
	sleep(1.5)
	sleep(1.5)

def task4():
	print('')
	print('Initiating Task 4/5')
	sleep(1.5)
	print('--------------------Task 4--------------------')
	sleep(1.5)
	#Step 4.1: Get listing of all files/directory names via os.listdir method under list called 'names' (of files or dictionaries)
	names=os.listdir()
	#Step 4.2: Create empty list (to sort and get top 5 size) and dictionary (to call up file/directory name), will be appended under for loop condition
	dictionary={}
	size_list=[]
	#Step 4.3: Check if items identified are directory or files
	#Step 4.4: Under the for loop, append list for values (to be sorted), another is dictionary (to call up item based on file size)
	for item in names:
		if os.path.isdir(item) == True: #If items is a directory, get the current location of directory, use os.scandir() function
			location=os.getcwd()
			dirpath=str(location+'/'+item)
			item_size= 0
			for x in os.scandir(dirpath):
				item_size=item_size+os.path.getsize(x)
			dictionary.update({item_size:item})
			size_list.append(item_size)
		elif os.path.isfile(item) == True: #If items is a file, get the size by os.path.getsize(item)
			item_size=os.path.getsize(item)
			dictionary.update({item_size:item})
			size_list.append(item_size)
		else:
			print(item,'is weirdly neither a file or directory')
	#Step 4.5: Get the 5 item with the largest size, by sorting and shortening the list such that only the top 5 size values remain
	size_list.sort()
	size_list.reverse()
	while len(size_list) > 5:
		size_list.pop()
	#Step 4.6: Call up the relevant file/directories name based on the size	
	print('The Top 5 Directories (or Files) and their respective sizes are:')
	print(' ')
	sleep(2)
	number=0
	#Step 4.7: Print the top 5 directories, with name, size and order number, with an indication if it is a file or directory
	for i in size_list:
		name_name=dictionary[i]
		if os.path.isdir(name_name) == True:
			type_type="is a Directory with size of "
		else:
			type_type='is a File with size of'
		number=number+1
		print(number,'. ',name_name,type_type,i,'bytes')
		sleep(1.5)
	print('----------------------------------------------')
	sleep(1.5)	

def task5():
	print('')
	print('Initiating Task 5/5')
	sleep(1.5)
	print('--------------------Task 5--------------------')
	sleep(0.5)
	print('CPU Usage will be refreshed every 10 seconds')
	print('To terminate the process, please press [Ctrl + c]')
	sleep(1.5)
	while True:
		cpu_use=psutil.cpu_percent()
		print('The CPU Usage is: ',cpu_use,'%','As at: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
		sleep(10)

#CALL THE FUNCTIONS!
taskbanner()
task1()
task2()
task3()
task4()
task5()



