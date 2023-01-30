'''
Code description: A pure recursive implementation of Bubble Sort.
Author: gz
Date: 1/30/23

Bubble sort, it is more convenient to implement it in an iterative function, nested loop. But for fun, implement it in a pure recursive way
'''
from typing import List

def myBubbleSort(mylist: List[int], size: int) -> List[int]:
    if size <= 1:
        return mylist
    myCompSwap(mylist, 0, size)  # inner loop
    return myBubbleSort(mylist, size - 1)  # outer loop


def myCompSwap(mylist: List[int], index: int, size: int):
    if index < size - 1:
        if mylist[index] > mylist[index + 1]:
            mylist[index], mylist[index + 1] = mylist[index + 1], mylist[index]  # python's convenient way to swap
        myCompSwap(mylist, index + 1, size)


# Test code
if __name__ == '__main__':
    mylist = [1, 11, 9, 4, 3, 6, 8, 2]
    alist = myBubbleSort(mylist, len(mylist))
    print(f'Here you go: {alist}')


