from cbc_modes import *

print("hello here")
if __name__=="__main__":
	messagef,tagf,keyf = parse_args_mac()

	omessagf=open(messagef,'rb')
	message = omessagf.read()

	okeyf = open(keyf,'r')
	key = okeyf.read()
	
	padded_message = padit(message)
	print(len(message))
	print(len(padded_message))
	print(type(padded_message))

	blocks=divide_into_blocks(padded_message)

	
	
	print(key)
	print(len(key))
	bytekey = bytes.fromhex(key)
	print(len(bytekey))
	#exit()
	the_tag,cipherblocks,iv = cbcmac(bytekey,blocks,1)

	hextag = the_tag.hex()
	print(hextag)

	otagf = open(tagf,'w')
	otagf.write(hextag)