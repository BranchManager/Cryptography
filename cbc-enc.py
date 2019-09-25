import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input",help="input file")
	parser.add_argument("-o","--output",help="output file")
	parser.add_argument("-k","--key",help="key file")
	args=parser.parse_args()

	if args.input:
		inputf = args.input
	if args.output:
		outputf = args.output
	if args.key:
		keyf = args.key
	return inputf, outputf, keyf


if __name__=="__main__":

	infile,outfile,key = parse_args()
	
	f = open(infile,'r')
	inn = f.read()

	fkey = open(key,'r')
	keyinn = fkey.read()
