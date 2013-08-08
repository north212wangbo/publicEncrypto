#!/usr/bin/python

import binascii
import sys
import random

class keyGenerator:
    generator = 2
    
    
    def __init__(self):
        self.p = 0
        self.d = 0
        self.e2 = 0

    
    def findPrime(self):
        while True:
            q = random.randrange(2**31,2**32)
            while (q % 12 != 5):
                q = random.randrange(2**31,2**32)            
            if not self.RabinMiller(q):
                continue
            elif not self.RabinMiller(2*q+1):
                continue
            else:
                break
        return 2*q+1
        
    def RabinMiller(self,n):
        d = n - 1 #assume n > 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
        for i in range(20):
            a = 0
            while a == 0:
                a = random.randrange(n)
            if not self.passMillerRobin(a,s,d,n):
                return False
        return True
        
    def passMillerRobin(self,a,s,d,n):
        a_to_d_mod_n = self.modExp(a,d,n)
        if a_to_d_mod_n == 1:
            return True
        for i in range(s):
            if a_to_d_mod_n == n - 1:
                return True
            a_to_d_mod_n = (a_to_d_mod_n * a_to_d_mod_n) % n
        return False
    
    def modExp(self,a,d,n):
        if (d == 0):
            return 1
        if (d % 2 == 0):
            return ((self.modExp(a,d/2,n) % n)**2) % n
        else:
            return (self.modExp(a,d-1,n) * a) % n
    
    def genRandomPriKey(self):
        self.p = self.findPrime()
        self.d = random.randrange(self.p)
        return 
        
    def genPubKey(self):       
        self.e2 = self.modExp(2,self.d,self.p)
        return
    
    def keyGen(self):
        self.genRandomPriKey()
        self.genPubKey()
        priKey = open("prikey.txt","w")
        pubKey = open("pubkey.txt","w")
        priKey.write(format(self.p,"033b")+ "," + format(keyGenerator.generator,"02b") + "," + format(self.d,"033b"))
        pubKey.write(format(self.p,"033b") + "," + format(keyGenerator.generator,"02b") + "," + format(self.e2,"033b"))
        return
    
    