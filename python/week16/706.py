class MyHashMap:

    def __init__(self):
        self._myMap = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.remove(key)
        self._myMap.append([key, value])

    def get(self, key: int) -> int:
        for i in self._myMap:
            if i[0] == key:
                return i[1]
        return -1 

    def remove(self, key: int) -> None:
        val = self.get(key)
        if val != -1:
            self._myMap.remove([key, val])

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)