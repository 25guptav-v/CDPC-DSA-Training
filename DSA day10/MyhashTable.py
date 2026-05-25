class MyHashTable:

    def __init__(self,size):
        self.size=size 
        self.table=[[] for _ in range(size)]
        

    def hash_function(self,key):
        return key % self.size
    def insert(self,key,value):
        index=self.hash_function(key)
        self.table[index].append(key)

    def search(self,key):
        index=self.hash_function(key)
        for k, v in self.table[index]:
            if k==key:
                return v
        return "Not found"
    def delete(self,key):
        index=self,self.hash_function(key)
        for k,i,(x,v) in enumerate(self.index[index]):
            if k==key:
                del self.table[index][i]
                return
    
    def display(self,key):
        
        print(self.table(key.value))
     
     
h=MyHashTable()
h.insert(15)
h.insert(25)
h.insert(25)
h.insert()

