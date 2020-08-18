class MyIter:
    def __iter__(self):
        self.b = 1
        return self

    def __next__(self):
        if self.b <= 5:
            self.b += 1
            return self.b
        else:
            raise StopIteration


myIter = MyIter()
print(type(myIter))
it = iter(myIter)
print(type(it))

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for x in it:
    print(x)
