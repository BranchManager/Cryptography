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

  
def sign_orverify_it(enc_AES_key_to_sign, private_signing_key,):  #Noah function
  if isinstance(private_signing_key, rsa.RSAPrivateKey):
      print("now")
      #now we start the signing process
def encrypt_key(RSA_key, AES_key):   #Noah Function
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
    return


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
    
    
    x509c.close()
    
    cert = x509.load_pem_x509_certificate(data,default_backend())

    #with open(prik,'rb') as keyf:
    
    priv_key = serialization.load_pem_private_key(key_file.read(),password=None, backend=default_backend())
    
    #signed_key = sign_it(aes_key,priv_key)

    print(priv_key)
    print("testing")
    print(cert.public_key())

    aes_key = b"bily"
    encrypt_key(cert.public_key(),aes_key)

    exit()
    for i in cert.subject:
        if i.value != sub:
            print("Incorrect Subject.")
            exit()
    
    print(cert.public_key())

    key = AESGCM.generate_key(bit_length=128)
    
    print(key)
    

    aesgcm = AESGCM(key)

    nonce = os.urandom(11)

	#sign_it()
    
    for subdir, dirs, files in os.walk(Dir):
        for file in files:
            tmp = os.path.join(subdir, file)
            f = open(tmp,'rb')
            
            
            
  #key = get_random_bytes(32)
	#cipher = AES.new(key, AES.MODE_GCM)
	#ciphertext, tag = cipher.encrypt_and_digest(data)
            