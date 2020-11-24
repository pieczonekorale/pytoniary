class Bug:
    counter = 0

    def __init__(self):
        Bug.counter += 1
        self.id=Bug.counter
        print(self.id)

    def print(self):
        print(self.id)

    def __str__(self):
        return '{self.id}, {self.counter}'.format(self=self)

    def __del__(self):
        print("destruktor:")
        print("licznik:")
        Bug.counter -= 1
        print(Bug.counter)
        print("id usuniete:")
        print(self.id)


bugs = []
for i in range(10):
    bugs.append(Bug())
    print(bugs[i])

