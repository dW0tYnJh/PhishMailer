import smtplib
import os
import getpass
import sys
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email import encoders  
from email.mime.text import MIMEText
from .color import green, white, blue, start, alert, numbering

def CheckPerm():
	PermCheck = open("Permission.txt", "r")
	Check = PermCheck.read()
	PermCheck.close()
	if "No" in Check:
		os.system("clear")
	else:
		while True:
			if "Yes" in Check:
				os.system("clear")

def Gmail():
	MyMail = ("phishmailer@protonmail.com")
	os.system("clear")
	print(green)
	print("""
 __^__                                                        __^__
( ___ )------------------------------------------------------( ___ )
 | / |                                                        | \ |
 | / |+------------)PhishMailer BaitMailer V1.5(-------------+| \ |
 |___|                        Gmail                           |___|
(_____)------------------------------------------------------(_____) """)

	print(alert + "It Might Take A Few Minutes Until The Target Gets The Email" + alert)
	print(alert + "You Might Need To Allow Less Secure Apps On You Email Account" + alert)
	
	print("")
	fromaddr = input(start + " Enter Your Email-Address: ")
	password = getpass.getpass(start + " Enter Your Password (will not be shown): ")
	toaddr = input(start + " Enter Email-Address To Send To: ")
	subject = input(start + " Enter Subject: ")
	pathfile = input(start + " Enter Path To Html File: ")

	html = open(pathfile)
	msg = MIMEText(html.read(), 'html')
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject

	debug = False
	if debug:
		print(msg.as_string())
	else:
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(fromaddr, password)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print(alert + "Email Sent" + alert)
		
		PermCheck = open("Permission.txt", "r")
		Check = PermCheck.read()
		PermCheck.close()
		if "No" in Check:
			os.system("clear")
		else:
			while True:
				if "Yes" in Check:
					subject = "Phishmailer Sender"
					text = "Email Sent With PhishMailer"
					message = 'Subject: {}\n\n{}'.format(subject, text)
					
					server = smtplib.SMTP('smtp.gmail.com',587)
					server.starttls()
					server.login(fromaddr, password)
					server.sendmail(fromaddr, MyMail, message)
					server.quit()
					print(start + " Notice Sent To Me As Well, Thank You <3")
					sys.exit()
