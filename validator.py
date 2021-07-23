import requests
import os
from multiprocessing.dummy import Pool
import sys
r = '\033[31m'
g = '\033[32m'
w = '\033[37m'
y = '\033[33m'
Ex = """

         Usage : python Validator.py list.txt 12

         list.txt = You'r Email List

         12 = threads You Stupid

"""
Usro = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
def main(email):
	url = ("https://verify.gmass.co/verify?email={}&key=52d5d6dd-cd2b-4e5a-a76a-1667aea3a6fc").format(email)
	get_url = requests.get(url, headers=Usro)
	text = (get_url.text)
	if "\"Valid\":true,\"Status\":\"Valid\"" in text:
		print((g+'Email : {} is True '+w).format(email))
	else:
		print((r+'Email : {} is Shit '+w).format(email))
try:
	try:
		emails = sys.argv[1]
		thread = int(sys.argv[2])
		emailsList = open(emails, 'r').read().splitlines()
		p = Pool(12)
		p.map(main, emailsList)
	except IndexError:
		print (y+Ex+w)
except  KeyboardInterrupt:
	print(' L9lawi La7bst ')