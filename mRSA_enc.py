import math
import argparse
import random
import sys
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
		fe = (r-24)-mesBitLen
		mee = mes.zfill(fe)

	chk = 0


	while chk != 1:
		ctr = 0

		rpad = bin(random.getrandbits(r))[2:]

		rpad = bytearray(rpad,'utf-8')

		for i in rpad:
			if i == b'0x00':
				ctr+=1

		if ctr == 0:
			chk = 1


	st = b'00000000'
	ed = b'00000010'
	mee = bytearray(mee,'utf-8')

	paddedm = st+ed+rpad+st+mee
	print(paddedm)	
	print("above is paddedm")
	#m = int.from_bytes(paddedm,"big")
	m = int(paddedm,2)
	print(m)
	print("welll")
	print(bin(m))
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

	print (c)
	print(type(key))
	print(key)
