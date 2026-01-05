"""
599. Minimum Index Sum of Two Lists
===================================
Given two arrays of strings list1 and list2, find the commom strings with the least index Sum

A common string is a string is a string that appeared in both list1 and list2.

A common string with the lease index sum is a common string such that if it appeared at list[i]
and list2[j] then i+j should be the minimum value among all the other common strings

Return all the common strings with the leaset index sum. Return the answer in any order.
"""

from typing import List


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    id_sum = float("inf")
    word_dict = {}
    for idx, string in enumerate(list1):
        if string in list2:
            idy = list2.index(string)
            word_dict[string] = idx + idy

    min_val = min(word_dict.values())

    return [k for k, v in word_dict.items() if v == min_val]


# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
print(findRestaurant(list1, list2))
