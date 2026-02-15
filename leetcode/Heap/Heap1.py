class Heap:
    def __init__(self) -> None:
        pass

    # NOTE: O(log N) Time Complexity and O(1) Space Complexity
    def heapPush(self, heapList: list, val: int, heapType: str) -> list:
        """
        Insert top node of the heap and adjust the child nodes accordingly.
        Args:
        - [val: int]: Insert val of the Heap
        - [heapType: str]: 'min' or 'max' Heap
        - [heapList: list]: If you have heaplist, assign here
        return:
            None
        """
        # 1. Add to the end
        heapList.append(val)
        # 2. Restore heap property
        if heapType == "min":
            self._min_bubble_up(heapList, len(heapList) - 1)
        elif heapType == "max":
            self._max_bubble_up(heapList, len(heapList) - 1)

        return heapList

    def _max_bubble_up(self, heapList: list, index: int):
        parentIdx = (index - 1) // 2

        # If aren't at the root and the current value is less than its parent
        if index > 0 and heapList[index] > heapList[parentIdx]:
            heapList[index], heapList[parentIdx] = (
                heapList[parentIdx],
                heapList[index],
            )
            self._max_bubble_up(heapList, parentIdx)

    def _min_bubble_up(self, heapList: list, index: int):
        parentIdx = (index - 1) // 2

        # If aren't at the root and the current value is less than its parent
        if index > 0 and heapList[index] < heapList[parentIdx]:
            heapList[index], heapList[parentIdx] = (
                heapList[parentIdx],
                heapList[index],
            )
            self._min_bubble_up(heapList, parentIdx)

    def heapPop(self) -> None:
        if not heapList:
            return None
        if len(heapList) == 1:
            return heapList.pop()

        # 1. Stored the root and return it later
        root = heapList[0]

        # 2. Move the last element to the root
        heapList[0] = heapList.pop()

        # Restore the heap property
        self._sift_down(0)

        return root

    def _sift_down(self, heapList: list, parent: int):
        index = parent
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(heapList)

        # check if left child exits and is smaller than current
        if left < size and heapList[left] > heapList[index]:
            index = left

        # check if right child exits and is smaller than the current value
        if right < size and heapList[right] > heapList[index]:
            index = right

        # If the smallers isn't the parent, swap and continue sifthing
        if index != parent:
            heapList[parent], heapList[index] = (
                heapList[index],
                heapList[parent],
            )
            self._sift_down(index)

    # NOTE: O(N) Time Complexity and O(1) Space Complexity
    def heapify(self, valList: list, heapType: str) -> None:
        """
        Convert List DS to Heap DS
        Args:
        - [vallist: list] : values in List format
        - [heapType: str]: 'min' or 'max' Heap
        Return:
        - [: list] : Return the Heap List
        """
        heapList = []
        for v in valList:
            self.heapPush(heapList=heapList, val=v, heapType=heapType)

        valList = heapList

    # NOTE: O(1) Time Complexity and O(1) Space Complexity
    def heapPeer(self) -> int:
        """
        Return the top value in the heap
        Args:
        - None
        Return:
        - [: int] : return the top value
        """

        return heapList[0]

    def heapSort(self) -> list:
        tempList = heapList
        sortList = []
        while heapList:
            sortList.append(self.heapPop())

        heapList = tempList
        return sortList


ip = [7, 3, 5, 0, 3, 9, 6, 7]
heap = Heap()
heap.heapify(valList=ip, heapType="min")
print(ip)
