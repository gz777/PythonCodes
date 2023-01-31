'''
Code description: A recursive implementation of Heap Sort,
Author: gz
Date: 1/30/23
'''
from typing import Any, List


def myHeapSort(mylist: List[int]) -> List[int]:
    return myHSort(myMinHeapify(mylist, len(mylist)), len(mylist), [])


def myMinHeapify(mylist: List[int], i: int) -> List[int]:
    if i == 0:
        return mylist
    leftIndex = 2 * i - 1
    rightIndex = 2 * i
    min = i - 1
    if leftIndex < len(mylist) and mylist[leftIndex] < mylist[min]:
        min = leftIndex
    if rightIndex < len(mylist) and mylist[rightIndex] < mylist[min]:
        min = rightIndex
    if min != i - 1:
        mylist[i - 1], mylist[min] = mylist[min], mylist[i - 1]
        myMinHeapify(mylist, min + 1)
    return myMinHeapify(mylist, i - 1)


def myHSort(mylist: List[int], i: int, mysorted: List[int]) -> List[int]:
    if i == 0:
        return mysorted

    mysorted.append(mylist[0])
    mylist[0], mylist[i - 1] = mylist[i - 1], mylist[0]
    mylist.pop()
    myMinHeapify(mylist, 1)
    return myHSort(mylist, i - 1, mysorted)

# Test code
if __name__ == '__main__':
    mylist = [38, 1, 36, 11, 5, 9, 4, 3, 6]
    alist = myHeapSort(mylist)
    print(f'Here you go: {alist}')
