
from cbc_modes import *

def CBC(blocks,outfile,key):
	
	i = 1
	
	cText = []
	
	cipher = AES.new(key,AES.MODE_ECB)
	
	reth = key

	IV = cipher.encrypt(reth[16:])
	

	cNext = cipher.encrypt(strxor(IV,blocks[0]))

	

	cText.append(cNext)

	while(i < len(blocks)-1):
		
		cNext = cipher.encrypt(strxor(cNext,blocks[i]))
		
		i = i+1	

		cText.append(cNext)
	
	file = open(outfile,"wb")
	for i in cText:
		file.write(i)


if __name__=="__main__":
	key,infile,outfile = parse_args()

	f = open(infile,'rb')
	inn = f.read()
	

	fkey = open(key,'r')
	
	keyinn = fkey.read()
	
	keyinn = keyinn.rstrip('\t\r\n\0')
	
	
	bytekey = bytes.fromhex(keyinn)
	
	print(len(keyinn))

	padText = padit(inn)
	
	blockArr = divide_into_blocks(padText)
	
	CBC(blockArr,outfile,bytekey)
