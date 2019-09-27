from cbc_modes import *

print("hello here")
if __name__=="__main__":
	messagef,tagf,keyf = parse_args_mac()

	omessagf=open(messagef,'rb')
	message = omessagf.read()

	okeyf = open(keyf)
	key = okeyf.read()

	padded_message = padit(message)
	print(len(message))
	print(len(padded_message))
	print(type(padded_message))

	blocks=divide_into_blocks(padded_message)

	
	
	print(key)
	bytekey = bytes.fromhex(key)
	print(len(bytekey))
	#exit()
	the_tag,cipherblocks,iv = cbcmac(bytekey,blocks,1)

	hextag = the_tag.hex()
	print(hextag)

	otagf = open(tagf,'rb')
	tag_to_check = otagf.read()

	#notice we can compare strings to 
	#the_tag is byte string of hextag (hex string)
	if tag_to_check == the_tag:
		print("True")
	else:
		print("False")

