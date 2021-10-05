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

def getFile(sftp, localpath, filepath):
    #sftp.get(filepath, localpath)
    pass
def closeConnection(sftp, transport):
    try:
        if sftp:
            sftp.close()
        if transport:
            transport.close()
    except Exception as e:
        print('Error. The sftp or transport service are not working well. Please, retry...', e)


if __name__=='__main__':
    #Extract part
    
    #Connect to SFTP
    paramiko.util.log_to_file("paramiko.log")
    # Open Connection
    transport = getTransport()
    # Connect to sftp with credentials
    sftp = getCredentials(transport)
    #Download a file from a SFTP connection with a filepath and a localpath 
    filepath = "/coto/upload/TEMPLATECOTO.xlsx"
    localpath = "./templateCoto.xlsx"
    getFile(sftp, filepath, localpath)
    # Close the connection
    closeConnection(sftp, transport)

    #Transformation part

    #We extract this from a SFTP but in this project we'll use an example xlsx file.
    df = pd.read_excel('datasets/templateCoto.xlsx', engine = 'openpyxl')
    df = df.rename(columns = {'idmorodo':'IDMOROSO', 'idcliente':'IDCLIENTE', 'Telefono':'TELEFONO',
    'estado':'endpoint'})
    df['fecha_carga'] = time.strftime("%Y-%d-%m %H:%M:%S", time.localtime())
    df['estado_inicial'] = np.nan
    df['tipo_bot'] = 'Coto'
    df['fecha_interaccion'] = np.nan
    df = df[['IDMOROSO', 'IDCLIENTE', 'TELEFONO','Saldo Minimo', 'Saldo Total', 'tipo_bot' ,'endpoint','fecha_carga']]




