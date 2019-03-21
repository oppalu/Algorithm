# LRU cache O(1)
# Design and implement a data structure for LRU cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.data:
            # 把该节点放到队列最后
            node = self.data.get(key)
            self.dequeue(node)
            self.enqueue(node)
            return node.v
        return -1
        

    def put(self, key, value):
        if key in self.data:
            self.dequeue(self.data[key])
        node = Node(key, value)
        self.data[key] = node
        self.enqueue(node)
        if len(self.data) > self.capacity:
            temp = self.head.next
            self.dequeue(temp)
            self.data.pop(temp.k)
    
    def enqueue(self, node):
        # 加到末尾
        p = self.tail.pre
        p.next = node
        node.pre = p
        node.next = self.tail
        self.tail.pre = node


    def dequeue(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1)) #return 1
obj.put(3,3) # remove key2
print(obj.get(2)) # return -1
obj.put(4, 4)  #remove key 1
print(obj.get(1)) # return -1
print(obj.get(3)) # return 3
print(obj.get(4)) # return 4