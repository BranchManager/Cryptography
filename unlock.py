import argparse
import sys
from datetime import datetime,timedelta
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa,ec

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--dir",help="Dir to Unlock")
    parser.add_argument("-p","--pubk",help="Action Public Key")
    parser.add_argument("-r","--prik",help="Action Private Key")
    parser.add_argument("-s","--sub",help="Who are we unlocking")
    args=parser.parse_args()

    if args.dir:
        Dir = args.dir
    if args.pubk:
        pubk = args.pubk
    if args.prik:
        prik = args.prik
    if args.sub:
        sub = args.sub

    return Dir,pubk,prik,sub


if __name__=="__main__":

    Dir,pubk,prik,sub = parse_args()