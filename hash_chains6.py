# python3

#import sys
from collections import deque

class Solver:
    prime1 = 1000000007
    prime2 = 1000000009
    multiplier = 39

    
    def __init__(self, s):
        self.s = s
        self.hash1 = deque()
        self.hash2 = deque()
        
    def ask(self, a, b, l):
        self.hashtable(self.s,l)
        return self.hash1[a] == self.hash2[b]

    def hashtable(self,string,length):
        
        [self.hash1.append(self.hashfunc1(string[i:i+length])) for i in range(len(string)-length+1)]
        
        [self.hash2.append(self.hashfunc2(string[i:i+length])) for i in range(len(string)-length+1)]
        
    def hashfunc1(self,string):
        return hash(string)

        #ans = 0
        #for c in reversed(string):
        #    ans = (ans * self.multiplier + ord(c)) % self.prime1
        #return ans
    
    def hashfunc2(self,string):
        return hash(string)
        #ans = 0
        #for c in reversed(string):
        #    ans = (ans * self.multiplier + ord(c)) % self.prime2
        #return ans 

sh = Solver('trololo')

#sh.hashtable('trololo',3)

sh.ask(2,4,3)