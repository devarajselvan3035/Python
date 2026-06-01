class HashSet:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.buget = [0] * self.capacity

    def _hash(self, key) -> int:
        return hash(key) % self.capacity

    def add(self, value) -> None:
        idx = self._hash(value)
        self.buget[idx] = value

    def remove(self, value) -> None:
        idx = self._hash(value)
        self.buget[idx] = 0

    def contains(self, value) -> bool:
        return value in self.buget

    def show(self) -> None:
        print([v for v in self.buget if v != 0])


hs = HashSet(10)
hs.add(1)
hs.add(100)
hs.add(2)
hs.add(2)
hs.show()
