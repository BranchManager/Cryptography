import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input",help="input file")
	parser.add_argument("-o","--output",help="output file")
	parser.add_argument("-k","--key",help="key file")
	args=parser.parse_args()

	if args.input:
		inputf = args.input
	if args.output:
		outputf = args.output
	if args.key:
		keyf = args.key
	return inputf, outputf, keyf
def key_bits(keyinn):
	#print(keyinn)
	#AES_KEY = int(keyinn, 16).to_bytes(len(key) // 2, 'little')
	r = bytearray.fromhex(keyinn)
	print(r)
	iv = b'1234512345kilifq'

	data = b'hello to all of you young niggas I hope all is well'
	cipher = AES.new(r, AES.MODE_CBC,iv)
	ciphertext = cipher.encrypt(pad(data,16))
	print(ciphertext)

	cipher2 = AES.new(r,AES.MODE_CBC,iv)
	print(type(ciphertext))
	plaintext = cipher2.decrypt(ciphertext)
	print("Plaintext \n")
	print(plaintext)
	#print(AES_KEY.bit_length())
if __name__=="__main__":

	infile,outfile,key = parse_args()
	
	f = open(infile,'rb')
	inn = f.read()

	fkey = open(key,'r')
	keyinn = fkey.read()
	
	key_bits(keyinn)
