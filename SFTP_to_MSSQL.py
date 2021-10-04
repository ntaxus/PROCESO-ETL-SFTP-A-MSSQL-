##!/bin/bash

import os
import datetime
import paramiko
import openpyxl
import time
import numpy as np
import pandas as pd
import getpass
from paramiko import transport

from paramiko.transport import Transport

def getTransport():
    while True:
        host = input('Add a host: ')
        port = int(input('Add a port: '))
        try: 
            transport = paramiko.Transport((host,port))
            return transport
            break
        except Exception as e:
            print('We could not connect to the host. Please review your credentials. ', e)

def getCredentials(transport):
    username = input('Add the username: ')
    password = input('Add your password: ')
    try: 
        transport.connect(None, username, password)
        try: 
            sftp = paramiko.SFTPClient.from_transport(transport)
            print('You are connected to the host, please have fun.')
        except Exception as e:
            print(e,'.'+ 'Something went wrong. Please, retry...')
    except Exception as e: 
        print('Error, please review your credentials. ',e)


if __name__=='__main__':
    #Connect to SFTP
    paramiko.util.log_to_file("paramiko.log")
    # Open Connection
    transport = getTransport()
    # Connect to sftp with credentials
    sftp = getCredentials(transport)


