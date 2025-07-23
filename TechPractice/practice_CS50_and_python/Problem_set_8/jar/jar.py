class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Jar exceeded limit")
        elif n > self.capacity:
            raise ValueError("Jar exceeded limit")
        self._size = self.size + n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Withdrawing extra cookies")
        self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()