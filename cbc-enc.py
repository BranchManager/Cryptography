print("asdfjqwer")

from cbc_modes import *

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



def CBC(blocks,outfile,key):
	i = 1
	
	cText = []
	
	cipher = AES.new(key,AES.MODE_ECB)
	
	IV = cipher.encrypt(key)
	
	cNext = cipher.encrypt(strxor(IV,blocks[0]))

	cText.append(cNext)

	while(i < len(blocks)):
		
		print("dalsdkfakf")
		cNext = cipher.encrypt(strxor(cNext,blocks[i]))
	
	i = i+1	
	
	print(type(cNext))
	cText.append(cNext)
	
	file = open(outfile,"w")
	file.write(cText)


if __name__=="__main__":
	key,infile,outfile = parse_args()
	print("h")

	f = open(infile,'rb')
	inn = f.read()
	
	fkey = open(key,'rb')
	keyinn = fkey.read()
	
	print(keyinn)
	padText = padit(inn)
	
	blockArr = divide_into_blocks(padText)
	
	CBC(blockArr,outfile,keyinn)
