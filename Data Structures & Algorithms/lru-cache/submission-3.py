class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.time = 0
        self.capacity = capacity
        self.cache = dict() 

        self.head = Node(-1,-1) #starting and ending with dummy nodes
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

    def move_front(self, node):
        node.prev = self.head
        node.next = self.head.next
            
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        self.time += 1

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.move_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        self.time += 1
        node = None

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            
        else:
            if len(self.cache) >= self.capacity:
                #evict the least recently used key
                replacement = self.tail.prev.key

            
                self.remove(self.cache[replacement])
                self.cache.pop(replacement)
                
     
            node = Node(key, value)
            self.cache[key] = node

        self.move_front(node)
           
            
        
            



