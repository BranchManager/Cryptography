import argparse
import sys
import math
sys.path.insert(1,"PyPl/PyPl")
from Crypto.Util import number 

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--PublicKeyFile",help="Public Key File name")
	parser.add_argument("-s","--PrivateKeyFile",help="Private Key File name")
	parser.add_argument("-n","--NumberOfBits",help="Number of Bits")
	args = parser.parse_args()
	if args.PublicKeyFile:
		PublicKeyFile = args.PublicKeyFile
	if args.PrivateKeyFile:
		PrivateKeyFile = args.PrivateKeyFile
	if args.NumberOfBits:
		NBits = args.NumberOfBits
	return PublicKeyFile,PrivateKeyFile,NBits

def PrimeNumbers(n):
	p = number.getPrime(n)
	q = number.getPrime(n)

	return p,q

def EEA(p,q):
	t = 0
	r = q
	newt = 1
	newr = p

	while newr != 0:
		qt = r//newr
		t,newt = newt,t-qt*newt
		r,newr = newr,r-qt*newr
	
	if r > 1:
		return -1
	if t < 0:
		t = t+q
	return t
\
def CoPrime(o):
	for i in range(2,o):
		if math.gcd(i,o) == 1:
			return i
	return -1

def FileMaker(x,y,z,F):
	f = open(F,'w')
	f.write(str(x)+"\n")
	f.write(str(y)+"\n")
	f.write(str(z)+"\n")
	f.close()


if __name__=="__main__":
	Pub,Pri,N = parse_args()

	N = int(N)
	
	e = -1
	d = -1

	while e == -1 or d == -1:
		p,q = PrimeNumbers(N)
		
		o = (p-1)*(q-1)
		e = CoPrime(o)
		d = EEA(e,o)
		n = p*q
		Bitlength = n.bit_length()

	
	FileMaker(Bitlength,n,e,Pub)
	FileMaker(Bitlength,n,d,Pri)
