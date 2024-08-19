#!/usr/bin/python
import os, signal, sys
from ftplib import FTP 


def fileftpcheck():
	try:
		ftp = FTP('samba')
		ftp.login('boba', 'q1q1q1')
		where      = ''
		folderName = 'test01'

		if folderName in ftp.nlst(where) :
		    print('Monitoring file exists')
		else:
			print('No monitoring file')

def filemntcheck( argpath ):
	try:
		print(os.path.isfile(argpath))
	finally:
		print(signal.alarm(0))


filemntcheck(sys.argv[1])
