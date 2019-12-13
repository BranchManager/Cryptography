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

# def RSA_ENC(N,e,m):

# return
def convert_lines(lines,m):
	bits_in_N = int(lines[0]) #& 0xFF
	N_itself = int(lines[1]) #& 0xFF
	eORd = int(lines[2]) #& 0xFF
	message = int(m) #& 0xFF

	return bits_in_N, N_itself, eORd, message


def pad_message(Nbits,m):
	n = Nbits//2

	bits_n_r = n//2
	bits_n_m = bits_n_r - 24
	#generate r
	r = number.getRandomInteger(bits_n_r)
	print(bin(r))
	print(r)

	m_n_bits = bin(m)[2:].zfill(bits_n_m)
	print(m_n_bits)
	exit()
	


	
	
	m_bytes = m.to_bytes(m_byte_len, byteorder='big')

	print(m_bytes)
	print(m_bits)
	exit()

	

	#r_bytes = int_to_bytes
	message_bytes = (12).to_bytes(Nbits//8, byteorder='little')

	#print(r_bytes)
	print(message_bytes)

	
	

if __name__ =="__main__":
    key,infile,outfile = parse_args()

    f = open(infile,'r')
    m = f.readline()

    print(type(m))
    

    fkey = open(key,'r')
    key = fkey.readlines()

    Nbits,N,eORd,mess = convert_lines(key,m)
   
    pad_message(Nbits,mess)

	

    print(Nbits)
    print(N)
    print(eORd)
    print(mess)

