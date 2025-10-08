class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.lenght = 0

    """
        push(item): This method adds an item to the top of the stack.
        This operation increase the size of the stack.
    """

    # O(1) - Constant time complexity
    def push(self, item) -> None:
        newNode = Node(item)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.lenght += 1

    """
        pop(): this method removes and returns the element at the top of the stack.
        This operation decreases the size of the stack. If the stack is empty, an error
        or exception may be raised (eg "stack underflow")
    """

    # O(1) -> constant time complexity
    def pop(self):
        return_value = self.head
        if self.head is None:
            raise ValueError("Stack is Empty")
        else:
            self.head = self.head.next
        self.lenght -= 1
        return return_value.data

    """
    peek(): This method returns the element at the top of the stack without removing it.
    """

    # O(1) -> constant time complexity
    def peek(self):
        if self.head is None:
            raise ValueError("Stack is Empty")
        else:
            return self.head.data

    """
    isEmpty(): This method checks whether the stack is empty. In typically returns 
    a boolean value True or False.
    """

    # O(1) -> constant time complexity
    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    """
    size(): this method reutrns the number of elements in stack
    """

    # O(1) - constant time complexity
    def size(self) -> int:
        return self.lenght

    """
    show(): This method print all elements inside the stack.
    """

    # O(1) -> constant time complexity
    def show(self) -> None:
        curdNode = self.head
        while curdNode:
            print(curdNode.data, end=",")
            curdNode = curdNode.next


if __name__ == "__main__":
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.pop()
    stk.pop()
    print(stk.peek())
    stk.show()
