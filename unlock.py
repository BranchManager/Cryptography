import argparse
import sys
from datetime import datetime,timedelta
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils
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

def verify(signature, Public_ec_key):
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash, default_backend())
    hasher.update(b"data & ")
    hasher.update(b"more data")
    digest = hasher.finalize()
    Public_ec_key.verify(
        signature,
        digest,
        ec.ECDSA(utils.Prehashed())

    )
if __name__=="__main__":

    Dir,pubk,prik,sub = parse_args()

    publickey = open(pubk,'rb')
    pub = publickey.read()
    keysig = open('keyfile.sig','rb')
    signed = keysig.read()

    cert = x509.load_pem_x509_certificate(pub,default_backend())
    verify(signed, cert.public_key())
    print(signed)




    
