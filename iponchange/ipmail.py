#! /usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import argparse
import subprocess

class EmailSender:
    def __init__(self, user, pwd, tosend):
        self._user = user
        self._pwd = pwd
        self._tosend = tosend

    def SetSmtpServer(self, smtpserver, smtpserver_port):
        self._smtpserver = smtpserver
        self._smtpserver_port = smtpserver_port

    def sendmail(self, title, message):
        msg = MIMEText(message)
        msg["Subject"] = title
        msg["From"] = self._user
        msg["To"] = self._tosend
        try:
            s = smtplib.SMTP_SSL(self._smtpserver, self._smtpserver_port)
            s.login(self._user, self._pwd)
            s.sendmail(self._user, self._tosend, msg.as_string())
            s.quit()
            print("Success!")
        except smtplib.SMTPException as e:
            print("Falied,%s" % e)
paser=argparse.ArgumentParser()
paser.add_argument("-m","--msg",help="about the msg you wanted to send")

emailsender=EmailSender("from_eamil","key","to_email")
emailsender.SetSmtpServer("smtp.exmail.qq.com", 465)

args=paser.parse_args()

if args.msg:
    emailsender.sendmail("nodename:crontab info",args.msg)
else:
    info = subprocess.Popen("machine reboot", shell=True, stdout=subprocess.PIPE).stdout.read()
    emailsender.sendmail("nodename:ip addr alter", info.decode())

"""
@author:raymond
@file:ipmail.py
@time:2018/3/1813:52
"""
