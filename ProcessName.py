import os

os.system("pip install pyfiglet")
os.system("pip install pyperclip")
os.system("pip install psutil")
os.system("pip install socket")


from pyfiglet import Figlet
f = Figlet()
print(f.renderText("ProcessNamer"))


import psutil

for proc in psutil.process_iter():
	try:
	
		processName = proc.name()
		processID = proc.pid
	
		
		
		import socket
		UDP_IP = "127.0.0.1"
		UDP_PORT = 8080
		MESSAGE = (processName)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
		
		
	except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
		pass
print("Complete")
exit()





		




