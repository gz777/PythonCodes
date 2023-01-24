'''
Code description: A recursive implementation of Selection Sort.
Author: gz
Date: 1/23/23
'''

def mySelectionSort(mylist: int, elemIdx: int, sorted: int) -> int:
    if elemIdx > 0: # We've already compared the first element of the list
        iPos = 0
        for idx, x in enumerate(sorted):
            if x >= mylist[elemIdx]:
                break
            iPos = idx+1
        sorted.insert(iPos, mylist[elemIdx])
        mySelectionSort(mylist, elemIdx-1, sorted)
        return sorted

if __name__ == '__main__':
    mylist = [1, 11, 4, 6, 8, 2]
    blist = mySelectionSort(mylist, len(mylist)-1, [mylist[0]]) #start recursion from the last elem in the list. sorted list contains the first elem in the list
    print(f'Here you go: {blist}')
