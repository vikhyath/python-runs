# Custom hashmap in python using a dict, TODO: change dict to a list to better reflect array
# SIZE is the max size of hashmap
# Collisions resolved using linear probing

class HashEntry:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def getKey(self):
        return self.key
    def getVal(self):
        return self.val

class HashMap:
    SIZE = 4
    # technically this is a dict, need to change to a list
    hashlist = {}
    def __init__(self):
        pass
    
    def put(self, key, val):
        index = self.getindex(key)
        if index == -1:
            return index
        
        # found an index to insert
        HashMap.hashlist[index] = HashEntry(key, val)
        return key

    def get(self, key):
        index = self.getindex(key)
        if (index not in HashMap.hashlist or index == -1):
            return -1

        # found the key, now get its value
        return HashMap.hashlist[index].getVal()

    def getindex(self, key):
        scaledkey = key % HashMap.SIZE
        # while key exists in hashmap's list and is valid, do "linear probing" for collision resolution
        index = scaledkey
        while (index in HashMap.hashlist and HashMap.hashlist[index].getKey() != key):
            # keep probing
            index = (index + 1) % HashMap.SIZE

            # went around, came back to where we started, i.e., key
            if (index == scaledkey):
                # hashmap is full
                return -1
        return index

def check(obj, key, val):
    op = obj.put(key, val)
    if op == -1:
        print 'Not enough space in hashmap to insert key,val: %d, %d'%(key, val)
    else:
        print 'inserted key, val: %d, %d'%(key,val)

def main():
    obj = HashMap()
    check(obj, 1, 10)
    check(obj, 2, 20)
    print obj.get(1)
    print obj.get(2)
    check(obj, 5, 30)
    print obj.get(5)
    print obj.get(1)
    print obj.get(2)
    print obj.get(4)
    check(obj, 1, 40)
    print obj.get(1)
    check(obj, 3, 60)
    print obj.get(3)
    check(obj, 4, 80)
    print obj.get(4)

if __name__ == '__main__':
    main()
