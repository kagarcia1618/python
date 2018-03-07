#!/usr/bin/env python

from datetime import datetime
from collections import OrderedDict
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException

def extract(filename):
	fi = open(filename,'r') #Opens the file
	data_raw = fi.readlines() #Reads the file and store it to data_raw per line data
	fi.close() #Closes the file
	return (data_raw)

current_time = datetime.now().strftime("%d%b%Y")

node_db_filename = "node_database.txt" #File that contains the nodes database
node_login_filename = "login_credential.txt" #File that contains the login credential
cli_commands_filename = "cli_commands.txt" #File that contains the cli commands

node_db_raw = extract(node_db_filename) #Temporary storage of the raw data of the nodes database
node_login_raw = extract(node_login_filename) #Temporary storage of the raw data of login credential
cli_commands_raw = extract(cli_commands_filename) #Temporary storage of the raw data of cli commands

node_db = OrderedDict() #Variable that will contain node details
node_login = OrderedDict() #Variable that will contain login credentials
cli_commands = OrderedDict() #Variable that will contain cli commands

for i in range(len(node_db_raw)):
	node_db[str(i)] = node_db_raw[i].split(',')
	for j in range(len(node_db[str(i)])):
		if j == (len(node_db[str(i)])-1):
			node_db[str(i)][j] = node_db[str(i)][j].strip('\r\n' or '\n')

for i in range(len(node_login_raw)):
	node_login[str(i)] = node_login_raw[i].split(',')

for i in range(len(cli_commands_raw)):
	cli_commands[str(i)] = cli_commands_raw[i].strip('\r\n' or '\n')

device_params = OrderedDict()
netmiko_params = ['device_type','ip','username','password']

for i in range(len(node_db)):
	device_params[str(i)] = OrderedDict()
	for j in netmiko_params:
		if j == 'device_type':
			device_params[str(i)][str(j)] = node_db[str(i)][2]
		if j == 'ip':
			device_params[str(i)][str(j)] = node_db[str(i)][1]
		if j == 'username':
			device_params[str(i)][str(j)] = node_login['0'][0]
		if j == 'password':
			device_params[str(i)][str(j)] = node_login['0'][1]

for i in range(len(device_params)):
	try:
		net_connect = ConnectHandler(**device_params[str(i)])
		wr_file = open(node_db[str(i)][0] + '_' + node_db[str(i)][1] + '_' + current_time +'.txt','w')
		for j in range(len(cli_commands)):
			output = net_connect.send_command(cli_commands[str(j)])
			x = len(cli_commands[str(j)])
			y = ''
			for k in range(66-x):
				y += '<'
			wr_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + cli_commands[str(j)] + y + '\n' + output + '\n')
			print('[' + node_db[str(i)][0] + ']' + '>>>>>>>>>>>>>>>>>>>>' + cli_commands[str(j)] + y + '\n' + output + '\n')
		wr_file.close()
	except (NetMikoAuthenticationException, NetMikoTimeoutException) as z:
		wr_file = open(node_db[str(i)][0] + '_' + node_db[str(i)][1] + '_' + current_time +'.txt','w')
		wr_file.write(str(z))
		print(z)
		wr_file.close()