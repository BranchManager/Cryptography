import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
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

def padit(data_to_pad):
        #print("TRY PAD")
        length = len(data_to_pad)
        #print(length)
        pad = b'\x78'
        if(length%BLOCK_SIZE)==0:
                return data_to_pad
        elif length < BLOCK_SIZE:
                #print(length)
                pad_len = BLOCK_SIZE - length
                padded_data = data_to_pad + pad *pad_len
                #print(data_to_pad)
                return padded_data
        elif (length>BLOCK_SIZE)!=0:
                pad_len = BLOCK_SIZE-(length%BLOCK_SIZE)
                #padded_data=data_to_pad + bytes(pad_len,"x")
                padded_data = data_to_pad + pad * pad_len
                # print(type(padded_data))
                # print(padded_data)
                # print("RETURN TYPE")
                return padded_data



def divide_into_blocks(message):
        print("hello")
        blocks = []
        #print("foor loop2")
        for i in range((len(message) // 16) + 1):
                #print(message[i * 16: (i +1) * 16])
                blocks.append(bytes(message[i * 16: (i +1) * 16]))
        return blocks

def CBC(blocks,outfile,key):	
	i = 1
	cText = []
	

	cipher = AES.new(key,AES.MODE_ECB)
	IV = cipher.encrypt(key)
	
	cNext = cipher.encrypt(strxor(IV,blocks[0])
	cText.append(cNext)

	while(i < sizeof(blocks)):
		cNext = cipher.encrypt(strxor(cNext,blocks[i]))
		i = i+1
		cText.append(cNext)
	file = open(outfile,"w")
	file.write(cText)


if __name__=="__main__":

	infile,outfile,key = parse_args()
	
	f = open(infile,'r')
	inn = f.read()
	
	fkey = open(key,'r')
	keyinn = fkey.read()
	
	padText = padit(inn)

	blockArr = divide_into_blocks(padText)
	
	CBC(blockArr,outfile,key)
