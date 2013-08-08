#!/usr/bin/python

import sys
from keyGenerator import keyGenerator
from Encryption import Encryption
from Decryption import Decryption


def main():
    while True:
        print "Choose from job"
        print "1.Key Generation"
        print "2.Encrytion"
        print "3.Decryption"
        print "4.Exit"
        choice = sys.stdin.readline()
 
        if (choice == '1\n'): 
            myKeyGenerator = keyGenerator()
            myKeyGenerator.keyGen()
            print "Key Generation Finished\n"
        elif (choice  == '2\n'):
            encryptor = Encryption()
            encryptor.encrypt()
            print "Encryption Finished\n"
        elif (choice == '3\n'):
            decryptor = Decryption()
            decryptor.decrypt()
            print "Decryption Finished\n"
        elif (choice == '4\n'):
            break;
        else: 
            print "invalid input"
            choice = sys.stdin.readline()
    
if __name__== '__main__':
    main()