from Singel_LinkedList import Node, LinkedList


def middleValue(head: Node) -> int:
    midNode = head
    curdNode = head
    while curdNode:
        print(midNode.value, curdNode.value)
        if curdNode.next is None:
            break
        curdNode = curdNode.next.next
        midNode = midNode.next
    return midNode.value


ip = [1, 2, 3, 4, 5]
ll = LinkedList()
for i in ip:
    ll.append(i)

print(middleValue(ll.head))
