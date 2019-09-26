import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def parse_args_mac():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--tag",help="input file")
	parser.add_argument("-m","--message",help="output file")
	parser.add_argument("-k","--key",help="key file")
	args=parser.parse_args()

	if args.input:
		tagf = args.tag
	if args.output:
		messagef = args.message
	if args.key:
		keyf = args.key
	return tagf, messagef, keyf

    
def divide_into_blocks(message):

def block(key,XoredMessage):


def tag_it(key):

if __name__=="__name__":
    messagef,tagf,key = parse_args_mac()

    omessagf=open(messagef,'rb')
    message = omessagf.read()

    divide_into_blocks(message)
