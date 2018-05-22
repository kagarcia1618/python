#!/usr/bin/env python

from datetime import datetime
from collections import OrderedDict
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from collections import namedtuple

def extract(filename):
	with open(filename,'r') as fi:
		return(fi.read())

current_time = datetime.now().strftime("%d%b%Y")

node_db_raw = extract('node_database.txt') #Temporary storage of the raw data of the nodes database
node_login_raw = extract('login_credential.txt') #Temporary storage of the raw data of login credential
cli_commands_raw = extract('cli_commands.txt') #Temporary storage of the raw data of cli commands

Node = namedtuple('Node',['hostname', 'ip', 'device_type'])
Login = namedtuple('Login', ['username', 'password'])
Node_db = namedtuple('Node_db',['ip', 'device_type', 'username', 'password'])

Node_details = [Node(*i.split(',')) for i in node_db_raw.splitlines()]
Login_details = [Login(*i.split(',')) for i in node_login_raw.splitlines()]
Node_db_details = [Node_db(Node_details[i].ip, Node_details[i].device_type, Login_details[0].username, Login_details[0].password) for i in range(len(Node_details))]

device_params = OrderedDict()
netmiko_params = ['ip', 'device_type', 'username', 'password']

for i in range(len(Node_db_details)):
	device_params[i] = OrderedDict()
	for j in range(len(Node_db_details[i])):
		device_params[i][netmiko_params[j]] = Node_db_details[i][j]
		
for i in range(len(device_params)):
	try:
		net_connect = ConnectHandler(**device_params[i])
		wr_file = open(Node_details[i][0] + '_' + Node_details[i][1] + '_' + current_time +'.txt','w')
		for j in cli_commands_raw.splitlines():
			output = net_connect.send_command(j)
			x = len(j)
			y = ''
			for k in range(66-x):
				y += '<'
			wr_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + j + y + '\n' + output + '\n')
			print('[' + Node_details[i][0] + ']' + '>>>>>>>>>>>>>>>>>>>>' + j + y + '\n' + output + '\n')
		wr_file.close()
	except (NetMikoAuthenticationException, NetMikoTimeoutException) as z:
		wr_file = open(Node_details[i][0] + '_' + Node_details[i][1] + '_' + current_time +'.txt','w')
		wr_file.write(str(z))
		print(z)
		wr_file.close()
