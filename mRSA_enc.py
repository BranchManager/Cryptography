import math
import argparse

import sys
sys.path.insert(1,"PyPl/PyPl")

from Crypto.Cipher import AES
from multiprocessing import Pool
from Crypto.Util.strxor import strxor
from sys import getsizeof
from Crypto.Random import get_random_bytes
from Crypto.Util import number
from Crypto.Util.number import long_to_bytes

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-k","--key",help="key")
	parser.add_argument("-i","--input",help="input file")
	parser.add_argument("-o","--output",help="output file")
	args=parser.parse_args()

	if args.key:
		key = args.key
	if args.input:
		infile = args.input
	if args.output:
		outfile = args.output
	return key,infile,outfile

def RSA_ENC(r,mesBitLen,mes,e,N):
	
	if r-24 < 0:
		print("n is too small")
		return -1

	if mesBitLen > r-24:
		print("Error Message is too Large")
		return -1
	elif mesBitLen < r-24:
		
	
	
	chk = 1

	while chk != 1:
		ctr = 0

		rpad = random.getrandbits(r)
		rpad = rpad.to_bytes()
		
		for i in rpad:
			if i == b'0x00':
				ctr+=1
		
		if ctr == 0:
			chk = 0


	st = b'0x00'
	ed = b'0x02'
	mes = mes.to_bytes()
	paddedm = st+ed+rpad+st+mes

	m = paddedm.to_int()
	c = m**e%N
	
	return c
	

if __name__ =="__main__":
    key,infile,outfile = parse_args()

	
    f = open(infile,'r')
    m = f.read()
	m = int(m)


    fkey = open(key,'r')
    key = fkey.readlines()

	f.close()
	k = int(key[0])
	r = k//2

	e = int(key[2])
	N = int(key[1])

	D = m.bit_length()
	
	if D%2 == 1:
		D+=1
	

	c = RSA_ENC(r,D,m,e,N)
	f.open(outfile,'w')
	f.write(c)
	f.close()

	print (c)
    print(type(key))
    print(key)
