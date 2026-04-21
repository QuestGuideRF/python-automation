import smtplib
import csv
from string import Template
from email .mime .multipart import MIMEMultipart
from email .mime .text import MIMEText
gmail_user ="test@gmail.com"
gmail_pwd ="demo"
TO ='test1@gmail.com'
SUBJECT ="Тестирование отправки с помощью Gmail"
TEXT ="Тестирование отправки почты с использованием серверов Gmail"
server =smtplib .SMTP ('smtp.gmail.com',587 )
server .ehlo ()
server .starttls ()
server .login (gmail_user ,gmail_pwd )
BODY ='\r\n'.join (['Кому: %s'%TO ,
'От: %s'%gmail_user ,
'Тема: %s'%SUBJECT ,
'',TEXT ])
server .sendmail (gmail_user ,[TO ],BODY )
print ('электронное письмо отправлено')