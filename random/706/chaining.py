class MyHashMap:

    def __init__(self):
        self.array = []
        for i in range(10):
            self.array.append([])

    def put(self, key: int, value: int) -> None:
        new_key = key % 10

        for pair in self.array[new_key]:
            if pair[0] == key:
                pair[1] = value
                return None

        self.array[new_key].append([key, value])

    def get(self, key: int) -> int:
        new_key = key % 10

        for pair in self.array[new_key]:
            if pair[0] == key:
                print(f"Returning {pair}")
                return pair[1]

        print(f"Returning -1")
        return -1

    def remove(self, key: int) -> None:
        new_key = key % 10

        for i in range(len(self.array[new_key])):
            if self.array[new_key][i][0] == key:
                self.array[new_key].pop(i)

                break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)