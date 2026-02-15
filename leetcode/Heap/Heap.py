import heapq


class Heap:
    def __init__(self) -> None:
        pass

    # NOTE: O(logN) Time Complexity and O(1) Space Complexity
    def heapPushMin(self, heapList: list, value: int) -> None:
        """
        Push value to heap list and modify into MinHeap accordingly
        Args:
        - (heapList: list) : Get Min heapify list
        - (value: int): Pust value fot heap list
        Return:
        - None
        """
        heapList.append(value)
        chileIdx = len(heapList) - 1
        parentIdx = (chileIdx - 1) // 2

        while parentIdx >= 0 and heapList[parentIdx] > heapList[chileIdx]:
            heapList[parentIdx], heapList[chileIdx] = (
                heapList[chileIdx],
                heapList[parentIdx],
            )
            chileIdx = parentIdx
            parentIdx = (chileIdx - 1) // 2

    # NOTE: O(logN) Time Complexity and O(1) Space Complexity
    def heapPushMax(self, heapList: list, value: int) -> None:
        """
        Push value to heap list and modify into MaxHeap accordingly
        Args:
        - (heapList: list) : Get Max heapify list
        - (value: int): Pust value fot heap list
        Return:
        - None
        """
        heapList.append(value)
        chileIdx = len(heapList) - 1
        parentIdx = (chileIdx - 1) // 2

        while parentIdx >= 0 and heapList[parentIdx] < heapList[chileIdx]:
            heapList[parentIdx], heapList[chileIdx] = (
                heapList[chileIdx],
                heapList[parentIdx],
            )
            chileIdx = parentIdx
            parentIdx = (chileIdx - 1) // 2

    def heapify(self, heapList: list) -> None:
        parentIdx = len(heapList) - 1

        while parentIdx >= 0:
            leftIdx = (parentIdx * 2) + 1
            rightIdx = (parentIdx * 2) + 2
            childIdx = parentIdx

            if leftIdx < len(heapList) and heapList[childIdx] > heapList[leftIdx]:
                childIdx = leftIdx

            if rightIdx < len(heapList) and heapList[childIdx] > heapList[rightIdx]:
                childIdx = rightIdx

            if childIdx != parentIdx:
                heapList[parentIdx], heapList[childIdx] = (
                    heapList[childIdx],
                    heapList[parentIdx],
                )
            print(heapList)

            parentIdx = parentIdx - 1


ip = [5, 4]
heap = Heap()
heap.heapPushMin(ip, 1)
heap.heapPushMax(ip, 10)
print(ip)
# heap.heapify(ip)
heapq.heapify(ip)
print(ip)
