# // Скрипт был основан на AminoLab
# // Для его установки, прописываем следующее: pip install AminoLab
# !! Если у вас версия 1.3, и ничего работает кроме ошибок: pip install --upgrade AminoLab

import os
os.system("cls")

try:
	import AminoLab
except ModuleNotFoundError:
	os.system("pip install AminoLab")
	import AminoLab
try:
  import pyfiglet
except ModuleNotFoundError:
  os.system("pip install pyfiglet") 
  import pyfiglet
try:
  from colored import fore, back, style, attr
except ModuleNotFoundError:
  os.system("pip install colored")
  from colored import fore, back, style, attr
attr(0)

# * ///
# Оформление внутри скрипта.
print(fore.DARK_GREEN_SEA + style.BOLD)
ver = "1.2.1"
telegramtag = "@none"
print(f"""
Script by whoname00
telegram — {telegramtag}(none — without tag)
""")
print(pyfiglet.figlet_format("AminoMsg", font="bublhead"))
print(f"Version the script : {ver}\n")
# * ///

client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
msgtype = input("Message Type >> ")
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
ndcId = clients.ndc_Id[int(input("Select the community >> "))-1]
print("""
>>> Selected the community.
""")
chats = client.my_chat_threads(ndc_Id=ndcId, size=100)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
threadId = chats.thread_Id[int(input("Select The Chat >> "))-1]
print("""
>>> Selected the chat.
""")
while True:
	mess = input("Message >> ")
	client.send_message(ndc_Id=ndcId, thread_Id=threadId, message=mess, message_type=msgtype)
	
  # ndc_Id = comId
	# thread_Id = chatId
	# message = content. 
	# message_type = type of the content. (0, 51, 107)