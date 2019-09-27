from cbc_modes import *

def CTR(blocks,outfile,key):	
	print("BLOCK START")
	print(blocks)
	
	i = 0
	x = 1
	cText = []
	
	
	num_of_blocks_arr = range(0,len(blocks))
	print(num_of_blocks_arr)
	
	reth = key
	IV = encrypt(key,reth[16:])

	print("IV information ")
	print(type(IV[0]))
	print(IV[0])
	print(type(IV))
	print(IV)
	print("\n")
	intIV = int.from_bytes(IV,byteorder='big')
	print(intIV)
	ctr_arr = []
	print("LENGTH********")
	print(len(blocks))
	for i in range(0,(len(blocks))):
		print(blocks[i])
		ctr=intIV+i
		ctrbytes = long_to_bytes(ctr)
		ctr_arr.append((key,ctrbytes))
		print(ctr_arr[i])
	
		
	
	p = Pool(5)
	result = p.starmap(encrypt,ctr_arr)
	print("RESLUT \n")
	print(result)
	for i in range(0,len(result)-1):
		print("BLOCK cipher part")
		print(blocks[i].hex())
		
		#exit()
		print(len(result[i]))
		print(result[i])
		print(len(blocks[i]))
		print(blocks[i])
		xored_string = strxor(result[i],blocks[i])

		result[i] = xored_string
		print(xored_string.hex()+"\n")

	result.insert(0,IV)
	print(result)

	cipherstring = ""
	for i in range(0,len(result)):
		#the following line converts byte stirng to a hex string
		print("Cipher Block \n")
		cipherblock = result[i].hex()
		print(cipherblock)
		cipherstring+=cipherblock

	print("\n")
	print("THE FINAL CIPHER IS:")
	print(cipherstring)
	
	
	
	file = open(outfile,"wb")
	file.write(bytes.fromhex(cipherstring))
	# for i in cText:
	# 	file.write(i)


if __name__=="__main__":

	key,infile,outfile = parse_args()
	
	f = open(infile,'rb')
	inn = f.read()

	fkey = open(key,'r')
	
	keyinn = fkey.read()
	
	keyinn = keyinn.rstrip('\t\r\n\0')

	bytekey = bytes.fromhex(keyinn)

	paddedstring = padit(inn,1)
	

	blockArr = divide_into_blocks(paddedstring)
	
	CTR(blockArr,outfile,bytekey)
