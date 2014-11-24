#!/usr/bin/python
#
# Author: Travis Zajkowski [ travis@travisz.com ]
#
# A class for sending metrics to a carbon-cache server
# using the plaintext protocol. See README.md for an example.

import sys
import time
import socket

class CarbonClient():
    def __init__(self, host, port):
        self.host = str(host)
        self.port = int(port)

    def sendcarbon(self, name, metric):
        try:
            sock = socket.socket()
            sock.connect((self.host, self.port))
        except socket.error as msg:
            print(msg)
            print('Could not open socket to carbon: ' + self.host + ':' +str(self.port))
            sys.exit(1)
        
        carbon_data = "%s %s %s \n" % (name, metric, int(time.time()))
        sock.sendall(carbon_data.encode())
        sock.close()
