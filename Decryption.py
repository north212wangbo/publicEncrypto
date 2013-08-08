#!/usr/bin/python

import sys
from keyGenerator import keyGenerator

class Decryption:
    def __init__(self):
        self.C1 = 0
        self.C2 = 0
        self.p = 0
        self.g = 2
        self.d = 0
        self.m = 0
        
    def decrypt(self):
        decrypted = open("dtext.txt","w")
        ctext = open("ctext.txt","r")
        keyFile = open("prikey.txt","r")
        keyString = keyFile.read()
        keyList = keyString.split(',')
        self.p = int(keyList[0],2)
        self.d = int(keyList[2],2)
        message = ''
        
        for line in ctext:
             cipherList = line.split(',')
             self.C1 = int(cipherList[0],2)
             self.C2 = int(cipherList[1],2)
             myKeyGenerator = keyGenerator()
             temp = myKeyGenerator.modExp(self.C1, self.p-1-self.d , self.p)
             self.m = (temp * self.C2) % self.p             
             message += format(self.m,"08x").decode("hex")
             decrypted.write(format(self.m,"08x").decode("hex"))
        print 'Message: \n', message, '\n'