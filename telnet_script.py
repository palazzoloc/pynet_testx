#!/usr/bin/env python

import telnetlib
import time
import socket
import sys
import pysnmp
TELNET_PORT = 23
TELNET_TIMEOUT = 6

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed out!")


def initial_login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def enable_login(remote_conn, password):
    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    # Telnet to the router
    remote_conn = telnet_connect(ip_addr)

    # Send commands to the router - username and password
    output = initial_login(remote_conn, username, password)
    print output

    # See the login prompt
    time.sleep(1)
    output = remote_conn.read_very_eager()
	
    # Set the terminal length to 0 and show the running version
    output = send_command(remote_conn, 'terminal length 0')
    # output = send_command(remote_conn, 'show version')
    output = send_command(remote_conn, 'show ip int brief')
    #output = send_command(remote_conn, 'enable')
    #output = enable_login(remote_conn, password)
    #output = send_command(remote_conn, 'conf t')
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()