from cbc_modes import *

#print("hello here")
if __name__=="__main__":
	messagef,tagf,keyf = parse_args_mac()

	omessagf=open(messagef,'rb')
	message = omessagf.read()

	okeyf = open(keyf,'r')
	key = okeyf.read()
	
	padded_message = padit(message)
	#print(len(message))
	#print(len(padded_message))
	#print(type(padded_message))

	blocks=divide_into_blocks(padded_message)

	
	
	#print(key)
	#print(len(key))
	#the following string converts hex string to byte string
	bytekey = bytes.fromhex(key)
	#print(len(bytekey))
	#exit()
	the_tag,cipherblocks,iv = cbcmac(bytekey,blocks,1)

	# test=int.from_bytes(the_tag,byteorder='big')
	# print("TEST")
	# print(test)
	# print(long_to_bytes(test))


	#print("real deal")
	#print(the_tag)

	#the following line converts b stirng to a hex string
	#hextag = the_tag.hex()
	#print(hextag)

	otagf = open(tagf,'wb')
	otagf.write(the_tag)