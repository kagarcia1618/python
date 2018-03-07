#!/usr/bin/env python

import logging
from ncclient import manager
import sys

router = {"ip": "10.30.26.227", 
          "port": 22, 
          "user": "zibmkenneth", 
"pass": "cisco123"}

def main():
 	"""Main method that prints NETCONF capabilities of remote device."""

	m = manager.connect(host=router["ip"], port=router["port"], username=router["user"], password=router["pass"], hostkey_verify=False)

        print('***Here are the Remote Devices Capabilities***')
        for capability in m.server_capabilities:
		print(capability)

if __name__ == '__main__':
	sys.exit(main())
