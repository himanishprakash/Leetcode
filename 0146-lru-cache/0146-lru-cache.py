class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.diction = OrderedDict()

    def get(self, key: int) -> int:

        if key not in self.diction:
            return -1

        self.diction.move_to_end(key)

        return self.diction[key]

    def put(self, key: int, value: int) -> None:
        if key in self.diction:
            self.diction.move_to_end(key)
        
        self.diction[key] = value

        if len(self.diction) > self.capacity:
            self.diction.popitem(False)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)