#!/usr/bin/env python
import argparse
import netaddr
import sys

HOST = 'ios-xe-mgmt.cisco.com'
PORT = 10000
USER = 'root'
PASS = 'C!sc0123'
BASE = 'GigabitEthernet'
INT_ID = '3'
FILE = 'create_subinterface.xml'
TEMPLATE = 'create_subinterface.j2'

def main():
    """Main method to configure a subinterface."""
    parser = argparse.ArgumentParser()
    parser.add_argument('vlan', help="VLAN number (1-4094)", type=int)
    parser.add_argument('prefix', help="IPv4 or IPv6 prefix")
    parser.add_argument('--template', '-t', default=TEMPLATE, help="Jinja2 template file name")
    parser.add_argument('--config', '-c', default=FILE, help="XML config file name")
    parser.add_argument('--interface', '-i', default=BASE, help="interface name to use")
    parser.add_argument('--id', '-d', default=INT_ID, help="interface ID to use")
    parser.add_argument('--user', '-u', default=USER, help="user name on remote host")
    parser.add_argument('--password', '-p', default=PASS, help="password on remote host")
    parser.add_argument('--port', '-P', default=PORT, help="port on remote host")
    parser.add_argument('--host', '-H', default=HOST, help="remote host")
    args = parser.parse_args()

    # check for valid VLAN ID
    if args.vlan < 1 or args.vlan > 4094:
        parser.print_usage()
        print("invalid VLAN ID %s" % str(args.vlan))
        sys.exit()

    # check for valid prefix
    try:
		ip = netaddr.IPNetwork(args.prefix)
		print(str(args.vlan))
    except netaddr.core.AddrFormatError as e:
		parser.print_usage()
		print(e)
		sys.exit()
		
	

if __name__ == '__main__':
	sys.exit(main())