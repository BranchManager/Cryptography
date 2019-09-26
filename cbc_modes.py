import argparse

import sys
sys.path.insert("./PyPl")

from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor
from sys import getsizeof
from Crypto.Random import get_random_bytes
BLOCK_SIZE = 16

def parse_args_mac():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--tag",help="input file")
	parser.add_argument("-m","--message",help="output file")
	parser.add_argument("-k","--key",help="key file")
	args=parser.parse_args()

	if args.tag:
		tagf = args.tag
	if args.message:
		messagef = args.message
	if args.key:
		keyf = args.key
	return messagef,tagf,keyf
#paddit takes a binary string so of format (b'Iam the string to pad)
def padit(data_to_pad):
	#print("TRY PAD")
	length = len(data_to_pad)
	#print(length)
	pad = b'\x78'
	if(length%BLOCK_SIZE)==0:
		return data_to_pad + b'\x10'*length
	elif length < BLOCK_SIZE:
		#print(length)
		pad_len = BLOCK_SIZE - length
		pad = bytes(chr(pad_len),'utf-8')
		print(pad)
		padded_data = data_to_pad + pad *pad_len
		#print(data_to_pad)
		return padded_data
	elif (length>BLOCK_SIZE)!=0:
		pad_len = BLOCK_SIZE-(length%BLOCK_SIZE)

		#padded_data=data_to_pad + bytes(pad_len,"x")
		pad = bytes(chr(pad_len),'utf-8')
		print(pad_len)
		print(pad)
		
		#exit()
		padded_data = data_to_pad + pad * pad_len
		# print(type(padded_data))
		# print(padded_data)
		# print("RETURN TYPE")
		return padded_data

		

def divide_into_blocks(message):
	print("hello")
	blocks = []
	#print("foor loop2")
	for i in range((len(message) // 16) + 1):
		#print(message[i * 16: (i +1) * 16])
		blocks.append(bytes(message[i * 16: (i +1) * 16]))
	return blocks
#def block(key,XoredMessage):
	# print('for loop')
	# for i in INPUT:
	# 	print(i)
def encrypt(key,block):
	Fk= AES.new(key,AES.MODE_ECB)
	ciphertext = Fk.encrypt(block)
	return ciphertext

def cbcmac(key,message_blocks,cbcmac_flag):
	print(len(key))
	exit()
	#exit()
	iv = 0
	cipherblocks=[]
	if cbcmac_flag == 1:
		cipherblock = b'\x00'*16
	else:
		cipherblock = get_random_bytes(16)
		iv = cipherblock
	# for i in range(message_blocks):
	print(len(message_blocks[0]))
	print(len(cipherblock))
	print(len(message_blocks))
	for i in range(0,(len(message_blocks)-1)):
		print(i)
		print("xor length")
		print(len(cipherblock))
		print(message_blocks[i])
		print(len(message_blocks[i]))
		xored_string = strxor(cipherblock,message_blocks[i])
		print("xor length AFTER xor")
		print(len(cipherblock))
		print(len(message_blocks[i]))
		cipherblock = encrypt(key,xored_string)
		print("LENGTH")
		print(len(cipherblock))
		cipherblocks.append(cipherblock)
	return cipherblocks[-1],cipherblocks,iv
	

#def tag_it(key):
# print("hello here")
# if __name__=="__main__":
# 	messagef,tagf,keyf = parse_args_mac()

# 	omessagf=open(messagef,'rb')
# 	message = omessagf.read()

# 	okeyf = open(keyf)
# 	key = okeyf.read()

# 	padded_message = padit(message)
# 	print(len(message))
# 	print(len(padded_message))
# 	print(type(padded_message))

# 	blocks=divide_into_blocks(padded_message)

	
	
# 	print(key)
# 	bytekey = bytes.fromhex(key)
# 	print(len(bytekey))
# 	#exit()
# 	the_tag,cipherblocks,iv = cbcmac(bytekey,blocks,1)

# 	hextag = the_tag.hex()
# 	print(hextag)

# 	otagf = open(tagf,'w')
# 	otagf.write(hextag)
	
	
	
	

	
	#exit()

	#divide_into_blocks(padded_message)
