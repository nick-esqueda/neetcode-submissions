class ListNode:
    def __init__(self, key=None, value=None, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt
    
    def __repr__(self):
        return f"<{self.value}>"

class LRUCache:
    """
    Explanation:
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 10);  // cache: {1=10}
    lRUCache.get(1);      // return 10
    lRUCache.put(2, 20);  // cache: {1=10, 2=20}
    lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
    lRUCache.get(2);      // returns 20 
    lRUCache.get(1);      // return -1 (not found)


    {
        1: 10
        2: 20
    }
    would have to loop through keys to find what was LRU
    can you maintain recency in another data structure?
    - each time get/put is called, have to update key as the most recently used

    [ 1, 2 ]


    h -> 2 <-> 3 <-> 4 -> n
    LRU   ------------ MRU
    """
    def __init__(self, capacity: int):
        # Initialize the cache of size 'capacity'
        self.capacity = capacity
        self.size = 0

        # Initialize head and tail nodes
        self.head = ListNode() # LRU
        self.tail = ListNode() # MRU
        self.head.nxt = self.tail
        self.tail.prev = self.head
 
        # Initialize the map for O(1) lookup
        self.nodeMap = dict()
        
    def removeListNode(self, node) -> None:
        """
        Remove the given node from the list

        Qs:
        Do you need to remove from the map here too? Or separate member func?
        Keep separate, Call both from evictNode() or updateMRU

        """
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

        node.nxt = None
        node.prev = None
 
    def appendListNode(self, node) -> None:
        """
           >node<\
        h</      >t 
        """
        last = self.tail.prev
 
        last.nxt = node
        node.prev = last

        node.nxt = self.tail
        self.tail.prev = node
    
    def updateMRU(self, key) -> None:
        """
        For use when key already exists (not adding a new node)
        """
        node = self.nodeMap[key]
        self.removeListNode(node)
        self.appendListNode(node)
    
    def addToMap(self, key, node):
        self.nodeMap[key] = node
    
    def evictLRU(self):
        # Guard clause in case there are no nodes
        if self.size == 0:
            return
        
        lruNode = self.head.nxt
        self.removeListNode(lruNode)
        del self.nodeMap[lruNode.key]
        self.size -= 1
 
    def get(self, key: int) -> int:
        """
        return the value for key
        -1 if not exists

        mark as "used"

        hash map for O(1) lookup?
        """
        if key not in self.nodeMap:
            return -1

        # Mark the node as the most recently used
        self.updateMRU(key)
        return self.nodeMap[key].value
        
    def put(self, key: int, value: int) -> None:
        """
        Update or add if not exists
        Remove last recently used if over capacity
 
        mark as "used"

        increment capacity if not evicting
        """
        # Update the node, if exists
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.removeListNode(node)
            self.appendListNode(node)
            return
        
        # Evict the LRU if we are over capacity
        if self.size >= self.capacity:
            self.evictLRU()

        # Add a new node
        node = ListNode(key, value)
        self.appendListNode(node)
        self.addToMap(key, node)

        self.size += 1
