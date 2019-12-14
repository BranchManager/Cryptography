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

  
def verify_it(pub_key, key):  
    
    #checking key vs public key to make sure it works
    validate = pub_key.verify(key,ec.ECDSA(hashes.SHA256()))

    if (validate == key):
        return True

    else:
        return False
    

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

def del_keyfile():
    os.remove("keyfile")
    os.remove("keyfile.sig")

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
    
    x509c.close()
    
    cert = x509.load_pem_x509_certificate(data,default_backend())
    
    for i in cert.subject:
        if i.value != sub:
            print("Incorrect Subject.")
            exit()
   
   #to open the keyfile and read in keyfile
    with open(some_key, 'rb') as keyfile:
        key = keyfile.read()

    #to open the keyfile.sig and read in keyfile.sig
    with open(some_key, 'rb') as keyfile:
        pub_key = keyfile.read()

    #key will be the decrypted keyfile.sig, pub_key will be the key in just keyfile
    check = verify_it(pub_key, key)
    
    if (check != True)
        exit ()

    
    #fetch aes key from keyfile // I don't know how to so I'm commenting this here

    
    #put the delete keyfile, and keyfile.sig in a function to make debugging easier
    del_keyfile()
    
    for subdir, dirs, files in os.walk(Dir):
        for file in files:
            tmp = os.path.join(subdir, file)
            f = open(tmp,'rb')
            ct = aesgcm.decrypt(nonce,f.read(),None)
            print(ct)
            f.close()
            wf = open(tmp,"wb")
            wf.write(ct)
            wf.close()