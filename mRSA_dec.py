import math
import argparse

import sys
sys.path.insert(1,"../PyPl/PyPl")
import random


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

def RSA_Dec(c,d,N):

	print(c)


	n = N//2
	r = n//2

	#c = bin(c)
	#c = c[2:]


#N = 256
#n = 128
#r = 64

#0x00,0x02,(0x01,0x02,0x06,0x05,0x03),0x00,m

	mbit = r-24

	#The below function is the same as the above 

	m = pow(c,d,N)

	print(bin(m))

	m = remove_padding(m,n)
	return m

def remove_padding(padded_m,n):
	zre = 0
	bin_mess = bin(padded_m)[2:]
	ctr = 0

	for i in bin_mess:
		print(zre)
		if i == '0':
			zre+=1
		elif i == '1':
			zre = 0
		if zre == 8:
			bin_mess = bin_mess[ctr:]
			break
		ctr+=1
	
	message = int(bin_mess,2)
	print(message)
	return message

if __name__ =="__main__":
	key,infile,outfile = parse_args()


	f = open(infile,'r')
	c = f.read()
	c = int(c)


	fkey = open(key,'r')
	key = fkey.readlines()
	
	f.close()

	LenN = int(key[0])
	#r = k//2

	d = int(key[2])
	N = int(key[1])

	Clen = c.bit_length()

	if Clen%2 == 1:
		Clen+=1

	m = RSA_Dec(c,d,N)
	

	f = open(outfile,'w')
	f.write(str(m))
	f.close()

print(key)
