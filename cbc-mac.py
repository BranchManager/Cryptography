import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor
from sys import getsizeof
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
	return messagef,tagf, keyf
#paddit takes a binary string so of format (b'Iam the string to pad)
def padit(data_to_pad):
	#print("TRY PAD")
	length = len(data_to_pad)
	#print(length)
	pad = b'\x78'
	if(length%BLOCK_SIZE)==0:
		return data_to_pad
	elif length < BLOCK_SIZE:
		#print(length)
		pad_len = BLOCK_SIZE - length
		padded_data = data_to_pad + pad *pad_len
		#print(data_to_pad)
		return padded_data
	elif (length>BLOCK_SIZE)!=0:
		pad_len = BLOCK_SIZE-(length%BLOCK_SIZE)
		#padded_data=data_to_pad + bytes(pad_len,"x")
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
#def encrypt(key,block)

def cbcmac(key,message_blocks):
	cipher = b'0'
	for i in range(message_blocks):
		xored_string = strxor(cipher,message_blocks[i])
		cipher = encrypt(key,xored_string)

#def tag_it(key):
print("hello here")
if __name__=="__main__":
	messagef,tagf,keyf = parse_args_mac()

	omessagf=open(messagef,'rb')
	message = omessagf.read()

	okeyf = open(keyf, 'rb')
	key = omessagf.read()

	padded_message = padit(message)
	print(len(message))
	print(len(padded_message))
	print(type(padded_message))

	blocks=divide_into_blocks(padded_message)

	tag=cbcmac(key,blocks)
	

	
	#exit()

	#divide_into_blocks(padded_message)
