#!/usr/bin/env python

"""
	https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
	
    'r' : use for reading
    'w' : use for writing
    'a' : use for appending to a file

"""

from collections import OrderedDict

fn = 'hostname.txt'
fi = open(fn,'r')
hostname = fi.readlines()
fi.close()

cisco_881_odict = OrderedDict([
        ('device_type','cisco_ios'),
        ('ip','10.30.26.227'),
        ('username','cisco'),
        ('password','cisco123')
])

print('Filename ' + fn + ' contains:')
print(hostname)

xfn = 'device_details.txt'
xfi = open(xfn,'w')

for i in cisco_881_odict:
	xfi.write(i + ':' + cisco_881_odict[i] + '\n')

xfi.close()
