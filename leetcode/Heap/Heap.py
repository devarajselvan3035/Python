class Heap:
    def __init__(self) -> None:
        self.values = []
        self.idx = 1

    # NOTE: O(log N) Time Complexity and O(1) Space Complexity
    def heapPush(self, val: int, heapType: str, heapList: list = None) -> list:
        """
        Insert top node of the heap and adjust the child nodes accordingly.
        Args:
        - [val: int]: Insert val of the Heap
        - [heapType: str]: 'min' or 'max' Heap
        - [heapList: list]: If you have heaplist, assign here
        return:
            None
        """
        if heapList:
            self.values = heapList

        # 1. Add to the end
        self.values.append(val)
        # 2. Restore heap property
        if heapType == "min":
            self._min_bubble_up(len(self.values) - 1)
        elif heapType == "max":
            self._max_bubble_up(len(self.values) - 1)

        return self.values

    def _max_bubble_up(self, index):
        parentIdx = (index - 1) // 2

        # If aren't at the root and the current value is less than its parent
        if index > 0 and self.values[index] > self.values[parentIdx]:
            self.values[index], self.values[parentIdx] = (
                self.values[parentIdx],
                self.values[index],
            )
            self._max_bubble_up(parentIdx)

    def _min_bubble_up(self, index):
        parentIdx = (index - 1) // 2

        # If aren't at the root and the current value is less than its parent
        if index > 0 and self.values[index] < self.values[parentIdx]:
            self.values[index], self.values[parentIdx] = (
                self.values[parentIdx],
                self.values[index],
            )
            self._min_bubble_up(parentIdx)

    def heapPop(self) -> None:
        if not self.values:
            return None
        if len(self.values) == 1:
            return self.values.pop()

        # 1. Stored the root and return it later
        root = self.values[0]

        # 2. Move the last element to the root
        self.values[0] = self.values.pop()

        # Restore the heap property
        self._sift_down(0)

        return root

    def _sift_down(self, parent: int):
        index = parent
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.values)

        # check if left child exits and is smaller than current
        if left < size and self.values[left] > self.values[index]:
            index = left

        # check if right child exits and is smaller than the current value
        if right < size and self.values[right] > self.values[index]:
            index = right

        # If the smallers isn't the parent, swap and continue sifthing
        if index != parent:
            self.values[parent], self.values[index] = (
                self.values[index],
                self.values[parent],
            )
            self._sift_down(index)

    # NOTE: O(N) Time Complexity and O(1) Space Complexity
    def heapify(self, valList: list, heapType: str) -> list:
        """
        Convert List DS to Heap DS
        Args:
        - [vallist: list] : values in List format
        - [heapType: str]: 'min' or 'max' Heap
        Return:
        - [: list] : Return the Heap List
        """
        for v in valList:
            self.heapPush(v, heapType=heapType)

        return self.values

    # NOTE: O(1) Time Complexity and O(1) Space Complexity
    def heapPeer(self) -> int:
        """
        Return the top value in the heap
        Args:
        - None
        Return:
        - [: int] : return the top value
        """

        return self.values[0]

    def heapSort(self) -> list:
        tempList = self.values
        sortList = []
        while self.values:
            sortList.append(self.heapPop())

        self.values = tempList
        return sortList


ip = [7, 3, 5, 0, 3, 9, 6, 7]
# ip = [1, 3, 6]
# for i in ip:
#     heap.heapPush(i)
# print(heap.values)
