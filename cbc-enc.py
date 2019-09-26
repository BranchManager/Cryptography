from cbc_modes import *

def CBC(blocks,outfile,key):	
	i = 1
	
	cText = []
	
	
	cipher = AES.new(key,AES.MODE_ECB)
	IV = cipher.encrypt(key)
	
	cNext = cipher.encrypt(strxor(IV,blocks[0])
	cText.append(cNext)
	print("wer")

	while(i < len(blocks)):
		print("dalsdkfakf")
		cNext = cipher.encrypt(strxor(cNext,blocks[i]))
		i = i+1
	
		print(type(cNext))
		
		cText.append(cNext)
	
	file = open(outfile,"w")
	file.write(cText)


if __name__=="__main__":

	infile,outfile,key = parse_args()
	print("h")
	f = open(infile,'r')
	inn = f.read()
	
	fkey = open(key,'r')
	keyinn = fkey.read()
	
	padText = padit(inn)

	blockArr = divide_into_blocks(padText)
	
	CBC(blockArr,outfile,key)
