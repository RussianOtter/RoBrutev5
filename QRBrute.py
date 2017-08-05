import qrcode, random, hashlib, string, time, console, argparse

print "\n\t\t QR-Coupon Brute Force\n"
print " Hacking doesn't just pay, it saves\n"
time.sleep(5)

parser = argparse.ArgumentParser()
parser.add_argument("-r","--random",help="Generate Random Hex Length (Default 50)",default=50,type=int)
parser.add_argument("-p","--pattern",help="Generate Codes With a Base Pattern")
parser.add_argument("-n","--nohelp",help="Hides Help", action="store_true")
parser.add_argument("-a","--amount",help="Amount Of Attempts For Random", default=20, type=int)
parser.add_argument("-R","--Rate",help="Rate Of Show", default=0.5, type=float)
args = parser.parse_args()

if not args.nohelp:
	parser.print_help()
	print "\nPattern Format: Word&Range:Range\nExample: BestBuy&1000:2000\nOutput:\nBestBuy1000\nBestBuy1001\nBestBuy1002\n...\n"
	time.sleep(2)

def qr_ran(size=args.random,amount=args.amount,rate=args.Rate):
	for _ in range(amount):
		key = []
		for i in range(size):
			key.append(random.choice(list(string.hexdigits)))
		key = "".join(key)
		qr = qrcode.make(key)
		qr.show()
		time.sleep(rate)
		try:
			#console.clear()
			pass
		except:
			pass

qr_ran()
