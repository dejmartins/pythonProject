class CustomList(list):

    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds bro")
        return super().__getitem__(index - 1)

    def __setitem__(self, key, value):
        if key <= 0:
            raise IndexError("Index out of bounds")
        return super().__setitem__(key - 1, value)


l = CustomList()
l.append(3)
l.append(5)

l[1] = 10
print(l)
print(l[1])
