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
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

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

def verify(signature, Public_ec_key,enckey):
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash, default_backend())
    #hasher.update(b"data & ")
    #hasher.update(b"more data")
    digest = hasher.finalize()
    Public_ec_key.verify(
        signature,
        enckey,
        ec.ECDSA(hashes.SHA256())

    )
    
def dec_key(cipherkey,privkey):
    print("cipher key \n")
    print(cipherkey)
    print(privkey)
    aes_key = privkey.decrypt(
        cipherkey,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
                
        )
         
    )
    print("the final real aes key")
    print(aes_key)
    return aes_key

if __name__=="__main__":

    Dir,pubk,prik,sub = parse_args()

    publickey = open(pubk,'rb')
    pub = publickey.read()
    keyfile = open('keyfile','rb')
    keysig = open('keyfile.sig','rb')
    priv = open(prik,'rb')

    privkey = priv.read()
    signed = keysig.read()
    key = keyfile.read()

    print("key in unlock \n")
    print(key)

    cert = x509.load_pem_x509_certificate(pub,default_backend())
    priv_keyRSA = serialization.load_pem_private_key(privkey,password=None, backend=default_backend())
    #this try catch calls the verify function to verify the signature
    #if it does not verify we will get a messag stating invalid sig and exit the program
    try:
        verify(signed, cert.public_key(),key)
    except InvalidSignature:
        print("Invalid Signature.....Exiting")
        exit()

    aes_key = dec_key(key,priv_keyRSA)
    print(aes_key)




    
