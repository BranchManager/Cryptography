import argparse
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from sys import getsizeof
BLOCK_SIZE = 16

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


def divide_into_blocks(message):
        print("hello")
        blocks = []
        #print("foor loop2")
        for i in range((len(message) // 16) + 1):
                #print(message[i * 16: (i +1) * 16])
                blocks.append(bytes(message[i * 16: (i +1) * 16]))
        return blocks

def cbcDec(blocks,outfile,key):	
	i = len(blocks)-1
	cText = []
	
		
	cipher = AES.new(key,AES.MODE_ECB)

	while i > 0:
		cNext = strxor(cipher.decrypt(blocks[i]),blocks[i-1])
		cText.prepend(cNext)
		i = i-1
	
	IV = cipher.encrypt(key)
	cText.prepend(strxor(cipher.decrypt(blocks[i]),IV))
	
	#remove padding

	file = open(outfile,"w")
	file.write(cText)


if __name__=="__main__":

	infile,outfile,key = parse_args()
	
	f = open(infile,'rb')
	inn = f.read()

	fkey = open(key,'r')
	keyinn = fkey.read()

	blockArr = divide_into_blocks(inn)
	
	CbcDec(blockArr,outfile,key)
