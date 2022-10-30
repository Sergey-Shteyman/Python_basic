class MyDict(dict):

    def get(self, key):
        if key in self.keys():
            return self[key]
        else:
            return 0


my_dict = MyDict({1: "a", 2: "b"})
print(my_dict.get(1))
print(my_dict.get(3))
