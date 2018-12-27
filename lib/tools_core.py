#!/usr/bin/python2
import os, platform, time, random
sembarang = random.randint(1,3)

err_keyint = "[!] Keyboard Interrupted by User !!!"
err_invld = "[!] Error: Invalid number selected !"
err_invalid = "[!] Error: Invalid option !"
err_blank = "[!] Error: Don't leave it blank !"
err_cantcon = "[!] Error: Can't connect with Target !"
err_cantconp = '''[!] Error: Can't connect to Target's Port !
	Are You sure that Port is opened and allow connection ?
	Try to scan it with Nmap'''
err_cantfind = '''[!] Error: Can't reach Target ! Are You sure Your Target
	is Online ? Are the URL is correct ? Are You Online ?'''
err_cantbck = "[!] Error: Can't go back ! this is the main Modules !"
err_notavai = '''[!] Sorry: This Modules is currently not available right now...
	This Modules maybe Unlocked in the next Version of M-Evil Tools :)
	so...stay with Me :)'''
err_bukalst = '''[!] Error: Can't open List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
err_bacalst = '''[!] Error: Can't read List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
banner1 = '''
          ________      ________     _______ 
          ___  __ \_______  ___/     ___    |
          __  / / /  __ \____ \________  /| |
          _  /_/ // /_/ /___/ //_____/  ___ |
          /_____/ \____//____/       /_/  |_|

        { DoS-A v1 }==={ Coded by M-XacT-666 }
'''
banner2 = '''
       _____        ______      _______ 
      (____ \      / _____)    (_______)
       _   \ \ ___( (____ _____ _______ 
      | |   | / _ \ ____ (_____)  ___  |
      | |__/ / |_| |____) )    | |   | |
      |_____/ \___(______/     |_|   |_|

    { DoS-A v1 }==={ Coded by M-XacT-666 }
'''
banner3 = '''
        dBBBBb  dBBBBP.dBBBBP        dBBBBBb
           dB' dBP.BP BP                  BB
      dBP dB' dBP.BP  `BBBBb          dBP BB
     dBP dB' dBP.BP      dBP dBBBBP  dBP  BB
    dBBBBB' dBBBBP  dBBBBP'         dBBBBBBB

     { DoS-A v1 }==={ Coded by M-XacT-666 }
'''
def clearscreen(x):
	if x == "Windows":
		os.system('CLS')
	else:
		os.system('clear')
def tidur(x):
	time.sleep(x)
def keluar():
	print ""
	print "[*] Closing Tools..."
	tidur(1)
	print "[^] Thanks for using My Tools !"
	exit()
def banner(x):
	if x == 1:
		print banner1
	elif x == 2:
		print banner2
	elif x == 3:
		print banner3
def judul():
	banner(sembarang)