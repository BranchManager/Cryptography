from cbc_modes import *

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

	pBlock = cText[len(cText)-1]
	rem = pBlock[len(pBlock)-1]

	while rem > 0:
		pBlock.remove(pBlock[len(pByte)-1])
		rem--

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
