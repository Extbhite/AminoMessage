#!/usr/bin/env python
# -*- coding: utf-8 -*-
# // copyright
# // Script by: whoname00
# // telegram — @thisDominus
# // discord — whoname00#8684

from os import _exit
import amino
import time

print("~ ============================== ~")
print("|        Message Amino Bot       |")
print("|          by whoname00          |")
print("|     telegram — @thisDominus    |")
print("~ ============================== ~")
print("")
email = input("Email: ")
time.sleep(.25)
password = input("Password: ")
print("")
client = amino.Client()
try:
  client.login(email=email, password=password)
except:
  print("\n\nIncorrect account or email, password.\nPlease re-login or check password and email account.\n\n")
subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
	comId = input("Type community id: ")
	subclient = amino.SubClient(comId=comId, profile=client.profile)
	for chatName, chatid in zip(subclient.get_chat_threads().title, subclient.get_chat_threads().chatId):
	  chatId = input("Type chatId: ")
	  print("MessageType: 1, 50, 58, 51, 100, 110, 115")
	  msgtype = input("Type message type: ")
	  while True:
	    try:
	      msg = input("Type message: ")
	      subclient.send_message(message=msg, chatId=chatId, messageType=msgtype)
	    except:
	      pass
