class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = dict()
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        tmp = self.head.next
        self.head.next = node
        tmp.prev = node
        node.prev = self.head
        node.next = tmp
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def update(self, node):
        self.remove(node)
        self.add(node)


    def get(self, key: int) -> int:
        if key in self.vals:
            node = self.vals[key]
            self.update(node)
            return node.val
        else:
            return -1
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            node = self.vals[key]
            node.val = value
            self.update(node)
            return
        node = Node(key, value)
        self.add(node)
        self.vals[key] = node
        if len(self.vals) > self.cap:
            node = self.tail.prev
            self.remove(node)
            del self.vals[node.key]
        return
        

        
        
