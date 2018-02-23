#!/usr/bin/env python
 
from netmiko import ConnectHandler
from pprint import pprint
from collections import OrderedDict
 
cisco_881_odict = OrderedDict([
	('device_type','cisco_ios'),
	('ip','10.30.26.227'),
	('username','zibmkenneth'),
	('password','Nuh$@1bm022018')
])

cisco_881_dict = {
	'device_type': 'cisco_ios',
	'ip': '10.30.26.227',
	'username': 'zibmkenneth',
	'password': 'Nuh$@1bm022018'
}

print ("***Regular Dictionary Format***")
pprint(cisco_881_dict)
print ("")

print ("***Ordered Dictionary Format***")
pprint(cisco_881_odict)
print ("")

x = 0
y = {}

for i in  cisco_881_dict:
	y[x] = i
	x += 1
	
x = 0
z = {}

for j in y:
	z[x] = cisco_881_dict[y[x]]
	x += 1

print("***Parsed Dictionary - Data Name***")
pprint(y)
print ("")

print("***Parsed Dictionary - Data Value***")
pprint(z)
print ("")

x = 0
y = {}

for i in  cisco_881_odict:
	y[x] = i
	x += 1
	
x = 0
z = {}

for j in y:
	z[x] = cisco_881_odict[y[x]]
	x += 1

print("***Parsed Ordered Dictionary - Data Name***")
pprint(y)
print ("")

print("***Parsed Ordered Dictionary - Data Value***")
pprint(z)
