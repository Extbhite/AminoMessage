#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# // copyright
# // Script by: whoname00
# // telegram — @thisDominus
# // discord — whoname00#8684

import amino
import time
import pyfiglet
import getpass
from colorama import Fore, Style
from os import _exit

print(Fore.GREEN + Style.NORMAL + '''
Script by whoname00
telegram - @thisDominus
''')
print(pyfiglet.figlet_format("AminoMessage", font="contessa"))
print('''
1. Send message
2. List of working msgType
3. Exit from script
''')
selectnum = str(input("> Choose number: "))

def listmsg():
    print("""
    Working msgType:
    109

    Restart this script -  to back choosing!
    """)
    _exit(1)

    # // List msgType.

def exitscript():
    print("""
    Done!
    You're successfully exited from script!

    Restart this script -  to back choosing!
    """)
    _exit(1)

    # // Exit function.

# // Selection

if selectnum == "1":
    # // Login

    email = str(input("> Your email: "))
    time.sleep(3)
    password = getpass.getpass("> Your password: ")

    # // Login

    client = amino.Client()
    try:
        client.login(email=email, password=password)
    except:
        print("Incorrent password, try again!")
        _exit(1)
    clients = client.sub_clients(size=100)
    for x, name in enumerate(clients.name, 1):
        print(f"{x}.{name}")
        communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
        sub_client = amino.SubClient(comId=communityid, profile=client.profile)
        chats = sub_client.get_chat_threads(size=150)
        for z, title in enumerate(chats.title, 1):
            print(f"{z}.{title}")
            chatx = chats.chatId[int(input("Выберите чат/Select the chat: "))-1]
            msgtype = str(input("> Type msgType: "))
            while True:
                try:
                    msg = input("> Type your message: ")
                    sub_client.send_message(message=msg, chatId=chatx, messageType=msgtype)
                except:
                    pass
elif selectnum == "2":
    listmsg()

elif selectnum == "3":
    exitscript()
