class MyHashMap:

    def __init__(self):
        #initialize a list
        self.map = [-1] * 1000001 #map is the variable name assigned to hold the list.

    def put(self, key: int, value: int) -> None:
        #inserts a (key, value) pair
        self.map[key] = value

    def get(self, key: int) -> int:
        #return the value of the key
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)