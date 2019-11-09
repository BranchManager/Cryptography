import math
import argparse

import sys
sys.path.insert(1,"../PyPl/PyPl")

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

def RSA_ENC(N,e,m):



if __name__ =="__main__":
    key,infile,outfile = parse_args()

    f = open(infile,'r')
    m = f.read()

    fkey = open(key,'r')
    key = fkey.read()

    print(type(key))
    print(key)