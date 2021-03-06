#!/usr/bin/python3
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
    parser.add_argument("-t","--Typek",help="rsa or ec")
    parser.add_argument("-s","--subject",help="subject of keypair")
    parser.add_argument("-pub","--publickey",help="Public key file name")
    parser.add_argument("-priv","--privatekey",help="Private key file name")
    args=parser.parse_args()

    if args.Typek:
        Type = args.Typek
    if args.subject:
        subject = args.subject
    if args.publickey:
        PubF = args.publickey
    if args.privatekey:
        PrivF = args.privatekey

    return Type,subject,PubF,PrivF


#paddit takes a binary string so of format (b'Iam the string to pad)


if __name__=="__main__":

    Type,subject,PubF,PrivF = parse_args()

    if Type == "ec":
        private_key = ec.generate_private_key(ec.SECP384R1(),default_backend())

    if Type == "rsa":
        private_key = rsa.generate_private_key(public_exponent=65537,key_size = 2048,backend=default_backend())
    
    now = datetime.utcnow()
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, subject)])    
    csr = x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(private_key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(now).not_valid_after(now + timedelta(days=365)).sign(private_key,hashes.SHA256(),default_backend())    
    with open(PubF,"wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))
    with open(PrivF, "wb") as f:
        f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption(),))#BestAvailableEncryption(b"yoyo"),))
    

