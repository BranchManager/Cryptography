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
	print("LENGTH******** \n")
	print(len(blocks))

	#this foor loop basically getss the iv blocks and puts into tuple with key
	for i in range(0,(len(blocks))):
		print("first foor looop\n")
		print(blocks[i])
		ctr=intIV+(i+1)
		ctrbytes = long_to_bytes(ctr)
		ctr_arr.append((key,ctrbytes))
		print(ctr_arr[i])
	print("end first foor loop \n")
		
	#this runns multiprocessing for the blocks and puts htem in result list
	print(len(ctr_arr))
	p = Pool(5)
	result = p.starmap(encrypt,ctr_arr)
	print("RESLUT \n")
	print(result)
	

	print("BLOCK cipher part")
	for i in range(0,len(result)):
		print("SECOND foor looop\n")

		print("below we have the message blocks.hex()")
		print(blocks[i].hex())
		
		#exit()
		print("remember result is the iv run thorugh the block")
		print("Bellow we have reult length and the result [i]")
		print(len(result[i]))
		print(result[i])
		print("Bellow we have result length and the block [i]")
		print(len(blocks[i]))
		print(blocks[i])
		if(len(result[i])>len(blocks[i])):
			
			k = len(blocks[i])
			# print(blocks[i])
			# print(len(result[i])-k)
			# print(k)
			b = result[len(result)-1]
			result[i] = b[len(b)-k:]

			
			

		xored_string = strxor(result[i],blocks[i])

		result[i] = xored_string

		print("The below is the xored_string.hex()")
		print(xored_string.hex()+"\n")
	print("end SECOND foor loop \n")

	result.insert(0,IV)
	print(result[0])
	print(result)
	#exit()

	cipherstring = ""
	for i in range(0,len(result)):
		#the following line converts byte stirng to a hex string
		print("Cipher Block \n")
		cipherblock = result[i].hex()
		print(cipherblock)
		print(bytes.fromhex(cipherblock))
		cipherstring+=cipherblock
	exit()

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
	print(inn)
	

	fkey = open(key,'r')
	
	keyinn = fkey.read()
	
	keyinn = keyinn.rstrip('\t\r\n\0')

	bytekey = bytes.fromhex(keyinn)

	#paddedstring = padit(inn,1)
	

	blockArr = divide_into_blocks(inn)
	
	CTR(blockArr,outfile,bytekey)
