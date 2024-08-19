import os, sys, socket
from ftplib import FTP,error_perm

def fileftpcheck(ftpsrv, user, passwd) :
        try:
            ftp = FTP(ftpsrv)
            ftp.login(user, passwd)
            if len(ftp.nlst()) :
                print 'True'
                print(len(ftp.nlst()))
                for i in ftp.nlst():
                    print(i)
            else :
                print('No files')
                os._exit(1)
        except socket.error:
            print('Socket error')
        except error_perm:
            print('Login error')
        except socket.Timeouterror:
            print('Timeout')

try:
    if (len(sys.argv[1]) > 0) and (len(sys.argv[2]) > 0) and (len(sys.argv[3]) > 0):
            ftpsrv = sys.argv[1]
            user = sys.argv[2]
            passwd = sys.argv[3]
except IndexError:
    print("Wrong number of args")
    os._exit(1)

fileftpcheck(ftpsrv,user,passwd)