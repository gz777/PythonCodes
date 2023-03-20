'''
Write a recursive descend parser for the following toy grammar:
<assignmentstmt>-> <id>=<num> | <id>=<num>+<num>
<num>->1|2|3
<id>-> a|b</id></num></num></id></num></num></id></assignmentstmt>
'''
# gz 3/16/23 - imperitive approach

SUCCESS = True
FAILED = False

def assignmentstmt(a):
    index = 0
    size = len(a)
    
    if id(a[index]) and check(index,size):
        index = index + 1
    else:
        return FAILED
    
    if check(index,size) and a[index] == '=':
        index = index + 1
    else:
        return FAILED
    
    if check(index,size) and num(a[index]):
        index = index + 1
    else:
        return FAILED
        
    if index == size:
        return SUCCESS # case <id>=<num>
    elif check(index,size) and a[index] == '+':
        index = index + 1
        if check(index,size) and num(a[index]):
            index = index + 1
        else:
            return FAILED
            
        if index == size:
            return SUCCESS # case <id>=<num>+<num>
        else:
            return FAILED

#utility functio
def check(index, size):
    if (index >= size ):
        return FAILED
    return SUCCESS
        
def id(s):
    if s in ['a', 'b']:
        return SUCCESS
    return FAILED


def num(s):
    return bool( s in ['1', '2', '3'])



        
# unit test
while True:
    a = input('Enter an assignment statement in the format of id=num or id=num+num: ')
    print(f'{a} is {assignmentstmt(a)}')
    b = input('Enter 0 to stop; any key to continue: ')
    if b == '0':
        break
 

