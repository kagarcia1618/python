#!/usr/bin/env python

from collections import OrderedDict
from netmiko import ConnectHandler
from parser_module import parse_cisco_ios_int_desc
from pprint import pprint
import xmltodict

def extract(filename):
	fi = open(filename,'r') #Opens the file
	data_raw = fi.readlines() #Reads the file and store it to data_raw per line data
	fi.close() #Closes the file
	return (data_raw)

node_db_filename = "node_database.txt"
node_login_filename = "login_credential.txt"
node_db = OrderedDict() #Contains node details
node_login = OrderedDict() #Contains login credentials
node_db_raw = extract(node_db_filename)
node_login_raw = extract(node_login_filename)

for i in range(len(node_db_raw)):
	node_db[str(i)] = node_db_raw[i].split(',')
	for j in range(len(node_db[str(i)])):
		if j == (len(node_db[str(i)])-1):
			node_db[str(i)][j] = node_db[str(i)][j].strip('\r\n' or '\n')

for i in range(len(node_login_raw)):
	node_login[str(i)] = node_login_raw[i].split(',')

device_params = OrderedDict()
output = OrderedDict()
parsed_data = OrderedDict()
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
	net_connect = ConnectHandler(**device_params[str(i)])
	output[str(i)] = net_connect.send_command("show int desc")
	parsed_data[str(i)] = parse_cisco_ios_int_desc(output[str(i)])

for i in range(len(parsed_data)):
	print('Device ' + node_db[str(i)][0] + ' has the following interface description :\n')
	for j in range(len(parsed_data[str(i)])):
		print('\tInterface : ' + parsed_data[str(i)][str(j)]['0'] + '\n\tDescription : ' +  parsed_data[str(i)][str(j)]['3'] + '\n')
	print('')

pprint(str(xmltodict.unparse({'Cisco':parsed_data})))