#!/usr/bin/python

import sys
import random
from keyGenerator import keyGenerator

class Encryption:
    def __init__(self):
        self.C1 = 0
        self.C2 = 0
        self.p = 0
        self.g = 2
        self.e2 = 0
        self.m = 0
        
    def readInput(self):
        ptext = open("ptext.txt","r")
        keyFile = open("pubkey.txt","r")
        keyString = keyFile.read()        
        keyList = keyString.split(',')
        self.p = int(keyList[0],2)
        self.e2 = int(keyList[2],2)
        
        text = ptext.read()
        charList = list(text)
        while (len(charList) % 4 != 0):
            charList.append('0')
        blocks = []
        i = 0
        for char in charList:
            if (i % 4 == 0):
                newBlock = []
            biChar = format(ord(char),"08b")
            print biChar
            newBlock.append(biChar)
            if (i % 4 == 3):
                blocks.append(newBlock)
            i = i+1    
        return blocks
    
    def encrypt(self):
        ctext = open("ctext.txt","w")
        totalBlocks = self.readInput()    
        for block in totalBlocks:
            self.m = int(''.join(block),2)
            myKeyGenerator = keyGenerator()
            k = random.randrange(self.p)
            self.C1 = myKeyGenerator.modExp(self.g, k, self.p)
            self.C2 = (myKeyGenerator.modExp(self.e2, k, self.p) * self.m) % self.p
            ctext.write(format(self.C1, "033b") + ","+ format(self.C2,"033b") + "\n")
            
            
            