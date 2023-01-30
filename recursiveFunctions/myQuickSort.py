'''
Code description: A (pure) recursive implementation of Quick Sort.
Author: gz
Date: 1/23/23
'''

from typing import List, Any

def myQuickSort(mylist: List[int]) -> List[int]:
    pivot = mylist[0]
    left: list[Any] = [x for x in mylist if x < pivot]
    right: list[Any] = [y for y in mylist if y > pivot]
    if len(left) > 1:
        left = myQuickSort(left)
    if len(right) > 1:
        right = myQuickSort(right)

    return left + [pivot] + right


# Test code
if __name__ == '__main__':
    mylist = [1, 11, 4, 6, 8, 2]
    alist = myQuickSort(mylist)
    print(f'Here you go: {alist}')


