from cbc_modes import *

def CTR(blocks,outfile,key):	
	i = 0
	x = 1
	cText = []
	
	cipher = AES.new(key,AES.MODE_ECB)
	reth = key
	IV = cipher.encrypt(reth[16:])

	print(type(IV[0]))
	while(i < len(blocks)-1):

		cNext = strxor(cipher.encrypt(IV),blocks[i])			 

		if IV[len(IV)-1] < 16:
			bytes = IV.replace(IV[len(IV)-x],bytes([IV[len(IV)-x] + 1]))
		else:
			x = x+1
			bytes = IV.replace(IV[len(IV)-x],bytes([IV[len(IV)-x] + 1]))
		
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

	blockArr = divide_into_blocks(inn)
	
	CTR(blockArr,outfile,bytekey)
