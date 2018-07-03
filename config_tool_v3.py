#!/usr/bin/env python

from datetime import datetime
from collections import OrderedDict
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from collections import namedtuple

def extract(a):
	"""
	a - exact filename of the data to be extracted
	"""
	with open(a,'r') as i:
		return(i.read())

def ssh_login(a,b,c,d):
	'''
	a - filtered device detail in netmiko format
	b - filtered device detail with hostname
	c - filtered device command line
	d - file format of the log file
	'''
	for i in range(len(a)):
		try:
			net_connect = ConnectHandler(**a[i])
			wr_file = open( b[i][0] + '_' + b[i][1] + '_' + current_time + '.' + d, 'w' )
			for j in c:
				output = net_connect.send_command(j)
				wr_file.write( j + '\n' + output + '\n')
				print('[' + b[i][0] + '] ' + j + '\n' + output + '\n')
			wr_file.close()
		except (NetMikoAuthenticationException, NetMikoTimeoutException) as z:
			wr_file = open(b[i][0] + '_' + b[i][1] + '_' + current_time + '.' + d, 'w' )
			wr_file.write(str(z))
			print(z)
			wr_file.close()
	return

def cisco_ios(a,b,c):
	'''
	a - all devices parameter detail in netmiko format
	b - all devices parameter detail with hostname
	c - all devices command lines
	'''
	params_filter = [ a[i] for i in a if a[i]['device_type'] == 'cisco_ios' ]
	node_filter = [ b[i] for i in range(len(b)) if b[i].device_type == 'cisco_ios' ]
	cfg_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_ios' and c[i][1] == 'cfg']
	log_filter = [ c[i][2] for i in range(len(c)) if c[i][0] == 'cisco_ios' and c[i][1] == 'log']
	
	ssh_login(params_filter,node_filter,cfg_filter,'cfg')
	ssh_login(params_filter,node_filter,log_filter,'log')

	return [params_filter,node_filter,cfg_filter,log_filter]

current_time = datetime.now().strftime("%d%b%Y")

node_db_raw = extract('node_database.txt') #Temporary storage of the raw data of the nodes database
node_login_raw = extract('login_credential.txt') #Temporary storage of the raw data of login credential
cli_commands_raw = extract('cli_commands.txt') #Temporary storage of the raw data of cli commands

Node = namedtuple('Node',['hostname', 'ip', 'device_type'])
Login = namedtuple('Login', ['username', 'password'])
Node_db = namedtuple('Node_db',['ip', 'device_type', 'username', 'password'])

Command_details = [ i.split(',') for i in cli_commands_raw.splitlines() ]

Node_details = [Node(*i.split(',')) for i in node_db_raw.splitlines()]
Login_details = [Login(*i.split(',')) for i in node_login_raw.splitlines()]
Node_db_details = [Node_db(Node_details[i].ip, \
	Node_details[i].device_type, Login_details[0].username, \
	Login_details[0].password) for i in range(len(Node_details))]

device_params = OrderedDict()
netmiko_params = ['ip', 'device_type', 'username', 'password']

for i in range(len(Node_db_details)):
	device_params[i] = OrderedDict()
	for j in range(len(Node_db_details[i])):
		device_params[i][netmiko_params[j]] = Node_db_details[i][j]
		
# for i in range(len(device_params)):
# 	try:
# 		net_connect = ConnectHandler(**device_params[i])
# 		wr_file = open(Node_details[i][0] + '_' + Node_details[i][1] + '_' + current_time +'.txt','w')
# 		for j in cli_commands_raw.splitlines():
# 			output = net_connect.send_command(j)
# 			x = len(j)
# 			y = ''
# 			for k in range(66-x):
# 				y += '<'
# 			wr_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + j + y + '\n' + output + '\n')
# 			print('[' + Node_details[i][0] + ']' + '>>>>>>>>>>>>>>>>>>>>' + j + y + '\n' + output + '\n')
# 		wr_file.close()
# 	except (NetMikoAuthenticationException, NetMikoTimeoutException) as z:
# 		wr_file = open(Node_details[i][0] + '_' + Node_details[i][1] + '_' + current_time +'.txt','w')
# 		wr_file.write(str(z))
# 		print(z)
# 		wr_file.close()