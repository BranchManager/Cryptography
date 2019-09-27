from cbc_modes import *

def CTRdec(blocks,outfile,key):	

	
	print(blocks)
	
	IV = blocks[0]
	intIV = int.from_bytes(IV,byteorder='big')
	print(intIV)
	print(IV)
	
	print(blocks)
	
	ctr_arr = []
	print("block Len")
	print(blocks)
	print(len(blocks))
	
	for i in range(1,len(blocks)):
		print(i)
		print("Cipher Block in dec \n")
		print(blocks[i].hex())
		ctr=intIV+i
		print(ctr)
		print(ctr)
		ctrbytes = long_to_bytes(ctr)
		ctr_arr.append((key,ctrbytes))
		
	print(len(ctr_arr))
	p = Pool(5)
	result = p.starmap(encrypt,ctr_arr)
	print("RESLUT \n")
	print(result)
	

	print(len(result))
	
	print(blocks)
	
	decypherblock = []
	for i in range(1,len(blocks)):
		print("decrypted blocks")
		print(blocks[i].hex())
		if(len(result[i-1])>len(blocks[i])):
			
			k = len(blocks[i])
			# print(blocks[i])
			# print(len(result[i])-k)
			# print(k)
			b = result[len(result)-1]
			result[i-1] = b[len(b)-k:]
			

		xored_string = strxor(result[i-1],blocks[i])
		result[i-1] = xored_string
		decypherblock.append(result[i-1])

		# print("results -1 ")
		# print(result[i-1])
		# print(result[i-1].hex())
		# print(decypherblock)
		print(result)

	plaintext = ""
	plaintexthex=''
	for i in decypherblock:
		plaintext += i.decode('utf-8')
		plaintexthex+=i.hex()
	print(plaintext)
	
	file = open(outfile,"wb")
	file.write(bytes.fromhex(plaintexthex))
		
		


	
	cipherstring = ""
	

	# file = open(outfile,"w")
	# file.write(cText)



if __name__=="__main__":


	key,infile,outfile = parse_args()

	
	f = open(infile,'rb')
	inn = f.read()



	fkey = open(key,'r')
	keyinn = fkey.read()

	keyinn = keyinn.rstrip('\t\r\n\0')

	bytekey = bytes.fromhex(keyinn)
	
	print(inn.hex())
	blockArr = divide_into_blocks(inn)
	#del blockArr[-1]
	
	
	print(blockArr)
	
	CTRdec(blockArr,outfile,bytekey)

