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
	m = c**d%N
	return m


if __name__ =="__main__":
    key,infile,outfile = parse_args()

	
    f = open(infile,'r')
    c = f.read()
	c = int(c)


    fkey = open(key,'r')
    key = fkey.readlines()

	f.close()

	LenN = int(key[0])
	r = k//2

	d = int(key[2])
	N = int(key[1])

	Clen = m.bit_length()
	
	if D%2 == 1:
		D+=1
	
	m = RSA_Dec(c,d,N)

	f.open(outfile,'w')
	f.write(m)
	f.close()

    print(type(key))
    print(key)
