#!/usr/bin/env python
'''
Script connects to any router you specify and extracts sysName and sysDescr
'''

import snmp_helper
import getpass
SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
	ip_address = raw_input("Provide the IP address: ")
	#ip_address = ip.addr.strip()
	comm_string = getpass.getpass(prompt="Provide the Community string: ")
	rtr1 = (ip_address, comm_string, 7961)
	rtr2 = (ip_address, comm_string, 8061)

	for device in (rtr1, rtr2):
		for each_oid in (SYS_NAME, SYS_DESCR):
			snmp_data = snmp_helper.snmp_get_oid(device, oid=each_oid)
			output = snmp_helper.snmp_extract(snmp_data)
			print output

	print

if __name__ == "__main__":
	main()