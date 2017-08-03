#!/usr/bin/env python
# modified from http://elinux.org/RPi_Email_IP_On_Boot_Debian
# this is currently only supporting ipv4!
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import urllib2
import sys
def send_email(gmail_user, smtpserver, extipaddr):
    my_ip = 'Hello this is Spaa...err, i mean halfus, here is my new external address: %s' % extipaddr
    print type(my_ip)
    msg = MIMEText(my_ip)
    msg['Subject'] = 'You won! (ou pas...) %s' % today.strftime('%b %d %Y')
    msg['From'] = 'you@em.ail'
    msg['To'] = 'you@em.ail'
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()
# Change to your own account information
to = 'you@em.ail'
gmail_user = 'you@em.ail'
gmail_password = 'password' #Yourpasswordhere
assert gmail_password != 'password', "Try again, your password is not password!"
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
extipaddr = urllib2.urlopen("http://icanhazip.com").read()
splitextipaddr = extipaddr.split('.')
splitextipaddr[3] = splitextipaddr[3].strip('\n') #Line end with \n , who anger the assert
assert len(splitextipaddr) == 4, "External service is broken, try again later"
myrange = range(0,255)
if int(splitextipaddr[0]) not in myrange or int(splitextipaddr[1]) not in myrange or int(splitextipaddr[2]) not in myrange or int(splitextipaddr[3]) not in myrange:
    print 'External service is broken, try again later'
    sys.exit(1)

try:
    with open('myip', 'r+') as fichier:
        lastipfromfile = fichier.read()
        print lastipfromfile
        try:
            splitlastipfromfile = lastipfromfile.split('.')
            #assert len(splitlastipfromfile) == 4, "Ip lenght is wrong: %r" % splitlastipfromfile
            if int(splitlastipfromfile[0]) in myrange and int(splitlastipfromfile[1]) in myrange and int(splitlastipfromfile[2]) in myrange and int(splitlastipfromfile[3]) in myrange:
                print 'last ip is ok'
                if lastipfromfile == extipaddr:
                    print 'nothing to do'
                    sys.exit(0)
                else:
                    print "ecrase ip"
                    fichier.seek(0)
                    fichier.write(extipaddr)
                    fichier.truncate()
                    send_email(gmail_user, smtpserver, extipaddr)
                    sys.exit(0)
    
            else:
                print 'This is not an IpV4!'
                fichier.write(extipaddr)
                fichier.truncate()
                fichier.seek(0)
                send_email(gmail_user, smtpserver, extipaddr)
        except:
            fichier.write(extipaddr)
            fichier.truncate()
            fichier.seek(0)
            send_email(gmail_user, smtpserver, extipaddr)
except:
    print "something went wrong but i am  too lazy to give the real reason!"
    print type(extipaddr)
    print sys.exc_info()
