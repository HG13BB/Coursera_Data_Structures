#Python 3
#Author: Henry Greeley
#Coursera Data Structures Class

# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]



class hashtable:
    #ratio_expand = .99
    min_size = 5
    _multiplier = 263
    _prime = 1000000007
         
    def __init__(self,size):
        self._size = size
        self._buckets = [None] * self._size
        self._list = None
        self._count = 0
    
    def read_query(self):
        return Query(input().split())
    
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

    def write_chain(self, chain):
        print(' '.join(chain))

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(self.check(query.ind))
        else:
            if query.type == 'find':
                print(self.finditem(query.s))
            elif query.type == 'add':
                self.setitem(query.s)
            else:
                self.delitem(query.s)

    
    def hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % len(self._buckets)        

    def setitem(self, word):
        loc = self.hash_func(word)
        if self._buckets[loc]:
            if word in self._buckets[loc]:
                return
            else:
                self._buckets[loc].append(word)
        else:
            self._buckets[loc] = [word]
            
        #self._count += 1
        #self._ensure_capacity()
        #return self._buckets
        
    def resetitem(self, word):
        loc = self.hash_func(word)
        if self._buckets[loc]:
            if word in self._buckets[loc]:
                return
            else:
                self._buckets[loc].append(word)
        else:
            self._buckets[loc] = [word]
    
    def delitem(self, word):
        loc = self.hash_func(word)
        if self._buckets[loc]:
            if word not in self._buckets[loc]:
                return
            if word in self._buckets[loc]:
                wordloc = self._buckets[loc].index(word)
                self._buckets[loc].pop(wordloc)
            
            #self._count -= 1
            #self._ensure_capacity()
        
        #return self._buckets   
    
    def finditem(self, word):
        loc = self.hash_func(word)
        if self._buckets[loc]:
            if word not in self._buckets[loc]:
                return 'no'
            if word in self._buckets[loc]:
                return 'yes'
        else:
            return 'no'
            
    def _ensure_capacity(self):
        fill = self._count / self._size
        
        # expand or shrink?
        if fill > self.ratio_expand:
            self._size = self._size * 2 + 1
        else:
            return
        # reallocate buckets
        temp = self._buckets.copy()
        self._buckets = [None] * self._size
        # store entries into new buckets
        for i in temp:
            if i:
                [self.resetitem(j) for j in i]
                
    def check(self,n):
        if self._buckets[n]:
            return reversed(self._buckets[n])
        else:
            return '' 
            
if __name__ == '__main__':
    bucket_count = int(input())
    proc = hashtable(bucket_count)
    proc.process_queries()


