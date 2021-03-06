#!/usr/bin/env python
'''
Author: Kenneth A. Garcia
'''

from collections import OrderedDict

def parse_cisco_ios_int_desc (node_int_data):
	data_split = OrderedDict() #Contains the split parsed data from data_raw
	data_parsed = OrderedDict() #Contains the multiple split parsed data from data_split
	tmp_data = OrderedDict() #Holds the multiple description values of data_parsed prior joining/concatenating the contents and storing it to final_data
	final_data = OrderedDict() #Contains the final parsed data values
	
	a = 0 #Integer index value for storing container of data_split to data_parsed
	b = 0 #Integer index value for storing container of data_parsed to final_data
	c = 0 #Integer index value for storing leaf data of data_split to data_parsed
	d = 0 #Integer index value for storing leaf data of data_parsed to final_data
	
	data_raw = node_int_data.split('\n')
	
	for i in range(len(data_raw)): #Itirates the line contents of data_raw
		if i != 0: #Omits the first line of the data_raw
			#data_raw[i]=data_raw[i].strip('\n') #Removes the new line character of the line
			data_split[i] = data_raw[i].split(' ') #Split the line based on ' ' character delimiter & stores it to data_split
			data_parsed[a] = OrderedDict() #Stores an ordered dict to the first container of data_parsed
			for j in range(len(data_split[i])): #Itirates the values of data_split
				if data_split[i][j] != '': #Checks the values of data_split if not equal to ' ' character
					data_parsed[a][c] = data_split[i][j] #Stores the values of data_split if not equal to ' ' character
					c += 1 #Increases index value for storing leaf data of data_split to data_parsed
			c = 0 #Resets the index value
			a += 1
	
	for i in range(len(data_parsed)):
		final_data[str(i)] = OrderedDict()
		for j in range(len(data_parsed[d])):
			if j < 3:
				final_data[str(d)][str(b)] = data_parsed[d][j]
				b += 1
				if j == 2:
					if len(data_parsed[d]) == 3:
						final_data[str(d)]['3'] = 'NO_DATA'
				if j == 1:
					if final_data[str(d)][str(j)] == 'admin':
						final_data[str(d)][str(j)] = 'admin_down'
			else:
				if data_parsed[d][j] == 'down':
					if len(data_parsed[d]) == 4:
						final_data[str(d)]['3'] = 'NO_DATA'
				else:
					for k in range(len(data_parsed[d])-3): #Itirates the description values if more than one & stores into tmp_data
						if data_parsed[d][1] != 'admin': #Checks if the status equals 'admin' due to extra space that will be added if this is the value
							tmp_data[data_parsed[d][b]] = k
						else:
							if k != 0: #Skips the first value if Status equals 'admin'
								tmp_data[data_parsed[d][b]] = k
						b += 1	
					final_data[str(d)]['3'] = " ".join(tmp_data)
					tmp_data = OrderedDict()
					break
		b = 0
		d += 1
	return (final_data)