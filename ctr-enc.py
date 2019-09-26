from cbc_modes import *

def CTR(blocks,outfile,key):	
	i = 1
	cText = []
	
	cipher = AES.new(key,AES.MODE_ECB)
	IV = cipher.encrypt(key)
	
	cNext = strxor(cipher.encrypt(IV),blocks[0])
	cText.append(cNext)

	while(i < len(blocks)):
		IV = IV+1
		cNext = strxor(cipher.encrypt(IV),blocks[i])
		i = i+1
		cText.append(cNext)
	
	file = open(outfile,"w")
	file.write(cText)


if __name__=="__main__":

	infile,outfile,key = parse_args()
	
	f = open(infile,'rb')
	inn = f.read()

	fkey = open(key,'r')
	keyinn = fkey.read()

	blockArr = divide_into_blocks(inn)
	
	CTR(blockArr,outfile,key)
