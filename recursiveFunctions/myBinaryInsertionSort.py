# binary insertion sort gz 2/3/23
'''
    when inserting next element to the sorted list, using binary search.
    Better performance in insertion operation. O(log n) instead of O(n).

    sorted: initial list contains first element in mylist
'''
from typing import List

def myBinaryInsertionSort(mylist: List[int], elemIdx: int, sorted: List[int]) -> List[int]:
    if elemIdx > 0:  # We've already compared the first element of the list
        myBinarySearchInsertion(sorted, 0, len(sorted)-1, mylist[elemIdx])
        myBinaryInsertionSort(mylist, elemIdx - 1, sorted)
        return sorted


# elem: the element to be inserted into the sorted list
def myBinarySearchInsertion(mylist: List[int], firstElemIndex: int, lastElemIndex: int, elem: int) -> List[int]:
    if firstElemIndex > lastElemIndex:
        mylist.insert(lastElemIndex + 1, elem)
        return mylist

    mid = (firstElemIndex + lastElemIndex) // 2
    if mylist[mid] > elem:
        lastElemIndex = mid - 1
    else:
        firstElemIndex = mid + 1
    return myBinarySearchInsertion(mylist, firstElemIndex, lastElemIndex, elem)

# Test code
if __name__ == '__main__':
    mylist = [38, 1, 36, 11, 5, 9, 4, 3, 6]
    mysorted = [1, 3, 5, 7, 11]
    alist = myBinarySearchInsertion(mysorted, 0, len(mysorted)-1, 2)
    print(f'Here you go 1: {alist}')

    blist = myBinaryInsertionSort(mylist, len(mylist) - 1, [mylist[0]])  # start recursion from the last elem in the list. sorted list contains the first elem in the list
    print(f'Here you go 2: {blist}')
