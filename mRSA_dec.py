import math
import argparse
import textwrap
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

def RSA_Dec(c,d,N,lenN):

	#print(c)


	n = lenN//2
	r = n//2

	#c = bin(c)
	#c = c[2:]


#N = 256
#n = 128
#r = 64

#0x00,0x02,(0x01,0x02,0x06,0x05,0x03),0x00,m
	buf = '00000000000000'
	mbit = r-24
	mbit = n - mbit
	#The below function is the same as the above
	print("n and Index where message should start:")
	print(n)
	print(mbit)
	
	m = pow(c,d,N)
	
	e = buf+(bin(m)[2:])
	
	print("padded message, and length of padded message:")
	print(e)
	#print(bin(m))
	print(len(e))
	#m = remove_padding(m,nna)
	
	oye = textwrap.wrap(e,8)
	padr = 0
	ctr = 0
	print(oye)
	for i in oye:
		if i == '00000000':
			padr += 1
		if padr == 2:
			e = e[ctr:]
			break
		ctr+=8	
		
	print(e)
	return int(e,2)

def remove_padding(padded_m,n):
	r = n//2 
	lenM = r-12
	print(lenM)
	print(n)
	zre = 0
	print("Padded Message")
	print(bin(padded_m))
	bin_mess = bin(padded_m)[4:]
	ctr = 0
	oye = textwrap.wrap(bin_mess,8)
	
	print(oye)
	for i in bin_mess:
		if i == '0':
			zre+=1
		elif i == '1':
			zre = 0
		if zre == 8:
			bin_mess = bin_mess[ctr:]
			break
		ctr+=1
	
	message = int(bin_mess,2)
	print(bin(message))
	return message

if __name__ =="__main__":
	key,infile,outfile = parse_args()


	f = open(infile,'r')
	c = f.read()
	c = int(c)


	fkey = open(key,'r')
	key = fkey.readlines()
	
	f.close()

	lenN = int(key[0])
	#r = k//2

	d = int(key[2])
	N = int(key[1])

	Clen = c.bit_length()

	if Clen%2 == 1:
		Clen+=1

	m = RSA_Dec(c,d,N,lenN)
	
	print(m)
	f = open(outfile,'w')
	f.write(str(m))
	f.close()

	#print(key)
