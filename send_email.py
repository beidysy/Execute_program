#!/usr/bin/env python
import subprocess
import smtplib


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


# Write any windows or unix command to execute it!
command = ''
subprocess.Popen(command, shell=True)

send_mail("Put your google email address",
          "Get a google app password", "The message that should be print")
