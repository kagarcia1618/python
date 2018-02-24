#!/usr/bin/env pdata_splitthon

from collections import OrderedDict
from pprint import pprint

data_parsed = OrderedDict()
tmp_data = OrderedDict()
final_data = {}
a = 0
b = 0

data_raw = 'Gi0/0                          up             up       Block 12 Holland Avenue, 272012'
data_split = data_raw.split(' ')

for i in range(len(data_split)):
	if data_split[i] != '':
		data_parsed[a] = data_split[i]
		a += 1
		
pprint(data_parsed)

for i in range(len(data_parsed)):
	if i < 3:
		final_data[b] = data_parsed[i]
		b += 1
	else:
		for i in range(len(data_parsed)-3):
			tmp_data[data_parsed[b]] = i
			b += 1
		final_data[3] = " ".join(tmp_data)
		break;

print(final_data)