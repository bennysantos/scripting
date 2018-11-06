import os, sys, socket

os.system("clear")

def check_adm():
	if os.getuid() == 0:
		main()
	else:
		print("You need to have root privileges to run this script!")
		sys.exit(1)

def menu_ports():
	print("1 - Ports range 0-1023")
	print("2 - Ports range 0-65535")
	print("3 - Custom ports range")

def check_ports_IP(IP):
	while true:
		os.system("clear")
		menu_ports()
		opt = input(" > ")
		if opt == 1:
			cp_1_IP(IP) #
		elif opt == 2:
			cp_2_IP(IP) #
		elif opt == 3:
			while true:
				custom_cp_1 = input("First port > ")
				custom_cp_2 = input("Last port > ")
				print("\n\n")
				print(custom_cp_1+"-"+custom_cp_2)
				print("First port > " + custom_cp_1)
				print("Last port > " + custom_cp_2)
				opt = input("y/n?")
				if opt == "y":
					cp_3_IP(IP, custom_cp_1, custom_cp_2) #
				else:
					os.system("clear")
		else:
			pass

def start_scan_IP(IP):
	temp = 0
	os.system("clear")
	print("Checking if " + IP + " is up!")
	while temp <= 3:
		response = os.system("ping -c 1 " + IP )
		if response == 0:
			print("Host UP!")
		else:
			temp += 1
	if temp >= 3:
		print(IP + " host not UP!")
		# menu de log
	else:
		check_ports_IP(IP)

#def start_scan_IPR(IP):

def main():
	IP = input("IP (10.0.0.1) or Network (10.0.0.0/24) > ")
	if IP.count(".") == 3:
		start_scan_IP(IP)
	elif IP.count(".") == 3 and "/24" in IP:
		start_scan_IPR(IP)
	else:
		os.system("clear")
		print("Enter correct IP or Network!")
		sys.exit(1)

check_adm()
