from cbc_modes import *

def CTRdec(blocks,outfile,key):	

	

	IV = blocks[0]
	intIV = int.from_bytes(IV,byteorder='big')
	print(intIV)
	print(blocks)
	
	ctr_arr = []
	for i in range(1,len(blocks)):
		print("Cipher Block in dec \n")
		print(blocks[i].hex())
		ctr=intIV+i
		print(ctr)
		print(ctr)
		ctrbytes = long_to_bytes(ctr)
		ctr_arr.append((key,ctrbytes))
		
	
	p = Pool(5)
	result = p.starmap(encrypt,ctr_arr)
	print("RESLUT \n")
	print(result)

	print(len(result))
	
	decypherblock = []
	for i in range(1,len(blocks)):
		print("decrypted blocks")
		print(blocks[i].hex())
		xored_string = strxor(result[i-1],blocks[i])
		result[i-1] = xored_string
		decypherblock.append(result[i-1])

		print(decypherblock)

	
	plaintext = ""
	
	for i in decypherblock:
		plaintext+=i.hex()
	print(plaintext)
		
		


	
	cipherstring = ""
	

	file = open(outfile,"wb")
	for i in decypherblock:
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
	del blockArr[-1]
	
	
	
	CTRdec(blockArr,outfile,bytekey)

