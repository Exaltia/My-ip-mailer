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
	my_ip = 'Hello this is Spaa...err, i mean ayumi, here is my new external address: %s',  extipaddr
	msg = MIMEText(my_ip)
	msg['Subject'] = 'You won! (ou pas...)' % today.strftime('%b %d %Y')
	msg['From'] = 'your@em.ail'
	msg['To'] = 'my.email'
	smtpserver.sendmail(gmail_user, [to], msg.as_string())
	smtpserver.quit()
# Change to your own account information
to = 'user@gmail.com'
gmail_user = 'your@em.ail'
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
assert splitextipaddr == 4, "External service is broken, try again later"
if int(splitextipaddr[0] not in range(0, 255) or int(splitextipaddr[1]) not in range(0, 255) or int(splitextipaddr[2]) not in range(0, 255) or int(splitextipaddr[3]) not in range(0, 255):
	print 'External service is broken, try again later'
	sys.exit(1)
try:
	with open('myip', r+) as file:
		lastipfromfile = file.read()
		splitlastipfromfile = lastipfromfile.split('.')
		assert len(splitlastipfromfile) == 4, "Ip lenght is wrong: %r" % splitlastipfromfile
		if int(splitlastipfromfile[0]) in range(0, 255) and int(splitlastipfromfile[1]) in range(0, 255) and int(splitlastipfromfile[2]) in range(0, 255) and int(splitlastipfromfile[3]) in range(0, 255):
			print 'last ip is ok'
			if lastipfromfile == extipaddr:
				print 'nothing to do'
				sys.exit(0)
			else:					
				file.seek(0)
				file.write(extipaddr)
				file.truncate()
				send_email(gmail_user, smtpserver, extipaddr)
		
		else:
			print 'This is not an IpV4!'
			file.seek(0)
			file.write(extipaddr)
			file.truncate()
			send_email()
		
except:
	print "something went wrong but i am  too lazy to give the real reason!"
