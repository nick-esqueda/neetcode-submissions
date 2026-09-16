from collections import defaultdict

class TimeMapNode:
    def __init__(self, key, value, timestamp):
        self.key = key
        self.value = value
        self.timestamp = timestamp
    
    def __repr__(self):
        return f"({self.key}|{self.value}|{self.timestamp})"
 
class TimeMap:
    """
    return the latest value for key (closest to passed in timestamp)

    {
      "alice": [ { "alice", "hi", 3 }, { "alice", "hi", 5 } ]
      "bob": [ { "bob", "hi", 3 } ]
    }

    set():
    all timestamps passed are strictly increasing, so don't need insertion logic. just append() 

    get():
    return the closest  value to timestamp (upper bound)
    if there are no timestamp_prevs earlier than timestamp, return ""

    [ T, T, T, F, F, F ]
            ^   
    looking for the last timestamp_prev that is <= timestamp

    the first one underneath it

    condition = mid <= t
    t = 6
    [ 1, 3, 5, 8 ]
            l
            m      
            r   
    
    [ { "happy", 1 }, { "sad" 3 } ]
                          l             
                          r
                          m
    """

    def __init__(self):
        self.data = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append(TimeMapNode(key, value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]

        if not len(data) or timestamp < data[0].timestamp:
            return ""

        l, r = 0, len(data) - 1
        i = 0 
        while l < r:
            mid = l + (r - l + 1) // 2

            if data[mid].timestamp <= timestamp:
                # Might be the answer - include
                l = mid
            else:
                # Cannot be the answer - exclude
                r = mid - 1
            
        return data[l].value
