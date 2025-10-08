class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self) -> str:
        curdNode = self.top
        vals = []
        while curdNode:
            vals.append(str(curdNode.data))
            curdNode = curdNode.next

        return ", ".join(vals)

    def push(self, data) -> None:
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def pop(self):
        if self.top is None:
            raise ValueError('Stack is Empty')
        value = self.top.data
        self.top = self.top.next
        return value
        self.size -= 1

    def peer(self):
        if self.top is None:
            raise ValueError('Stack is Empty')
        return self.top.data

arr = stack()
arr.push(11)
arr.push(12)
arr.push(13)
arr.push(14)
print(arr.pop())
print(arr.peer())
print(len(arr))
print(arr)
