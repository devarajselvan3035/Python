class HashMap:
    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.buckets = [None for _ in range(self.capacity)]
        self.size = 0

    def _hash_function(self, key) -> int:
        index = 0
        str_key = str(key)
        for s in str_key:
            index += ord(s)
        return index % self.capacity

    """
    put(key, value): Insert a key-value pair into the map. I the key already exists,
    its associated value is updated.
    """

    def put(self, key, value) -> None:
        idx = self._hash_function(key)
        if self.buckets[idx] is None:
            self.buckets[idx] = [[key, value]]
        else:
            for pair in self.buckets[idx]:
                if pair[0] == key:
                    pair[1] = value
                    return self.buckets
            self.buckets[idx].append([key, value])
        return self.buckets

    """
    get(key): Retrieves the value associated with the spicified key. It return
    null if the key is not found in the Hashmap.
    """

    def get(self, key):
        idx = self._hash_function(key)
        if self.buckets[idx]:
            sub_bucket = self.buckets[idx]
            for pair in sub_bucket:
                if pair[0] == key:
                    return pair[1]
        raise ValueError("key not find in HashMap")


if __name__ == "__main__":
    hash = HashMap()
    print(hash.put("name", "devaraj"))
    print(hash.put("eman", "devaraj"))
    print(hash.put("name", "kaviraj"))
    print(hash.get("name"))
    print(hash.get("age"))
