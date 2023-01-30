'''
Code description: A recursive implementation of Merge Sort.
Author: gz All rights reserved.
Date: 1/26/23
'''

from typing import List


def myMergeSort(mylist: List[int]) -> List[int]:
    if len(mylist) == 1:
        return mylist
    pos = len(mylist) // 2
    left = myMergeSort(mylist[:pos])
    right = myMergeSort(mylist[pos:])

    return mySorted(left, right, 0, 0, [])

# i: index of the left list. j: index of the right list
def mySorted(left: List[int], right: List[int], i: int, j: int, mysorted: List[int]) -> List[int]:
    if i == len(left):  # exhaust the list
        return mysorted + right[j:]
    if j == len(right):
        return mysorted + left[i:]
    if left[i] < right[j]:
        return mySorted(left, right, i + 1, j, mysorted + [left[i]])
    else:
        return mySorted(left, right, i, j + 1, mysorted + [right[j]])

# Test code
if __name__ == '__main__':
    mylist = [1, 11, 9, 4, 3, 6, 8, 2]
    alist = myMergeSort(mylist)
    print(f'Here you go 1: {alist}')
