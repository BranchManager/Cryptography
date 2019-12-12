import math
import argparse
import random
import sys
import struct
from textwrap import wrap
sys.path.insert(1,"PyPl/PyPl")


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
		fe = (r-24)
		print(fe)

		mee = mes.zfill(fe)
		print(mee)
	chk = 0


	while chk != 1:
		ctr = 0
		
		rpad = random.getrandbits(r)
		rpad = bin(rpad)[2:].zfill(r)
		print(rpad)
		print(len(rpad))
		print(r)
		curByte = 0
		
		Ctr = 0

		for i in rpad:
			
			if i == 0:
				curByte+=1
			if curByte == 8:
				break
			
			if ctr == 8:
				curByte=0
				ctr = 0
			
			ctr+=1
		
		if curByte != 8:
			chk = 1




	st = '00000000'
	ed = '00000010'
	print(type(rpad))
	print(type(mes))
	
	paddedm = st+ed+rpad+st+mee
	print(paddedm)	
	print("above is paddedm")
	#m = int.from_bytes(paddedm,"big")
	test = wrap(paddedm,8)
	m = int(paddedm,2)
	print(test)
	#print(m)
	#print("welll")
	#print(bin(m))
	#exit()
	
	c = pow(m,e)%N
	
	print("cipher is")
	print(c)
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
	r = r//2

	e = int(key[2])
	N = int(key[1])

	D = m.bit_length()

	if D%2 == 1:
		D+=1

	s = bin(m)[2:]
	
	c = RSA_ENC(r,D,s,e,N)

	f = open(outfile,'w')
	f.write(str(c))
	f.close()

#	print (c)
#	print(type(key))
#	print(key)
