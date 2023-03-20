
'''
Write a recursive descend parser for the following toy grammar:
<assignmentstmt>-> <id>=<num> | <id>=<num>+<num>
<num>->1|2|3
<id>-> a|b</id></num></num></id></num></num></id></assignmentstmt>
'''
# gz 3/16/23 - functional approach with lambda

SUCCESS = True
FAILED = False

def assignmentstmt(a):
    index = 0
    funcs2 = [id, lambda x: x=='=', num, lambda x: x=='+', num] # <id>=<num>+<num>
    funcs1 = funcs2[:3] # <id>=<num>
    
    for i in range(len(a)):
        if not funcs2[i](a[i]): # since funcs1 is a proper subset of funcs2, and in the same order, we can simply use funcs2
            return FAILED
        index = i+1
        
    if index == len(funcs1) or index == len(funcs2):
        print(f'index {index} {len(funcs1)} {len(funcs2)}')
        return SUCCESS
    else:
        return FAILED
 
    
def id(s):
    return ( s in ['a', 'b'])


def num(s):
    return ( s in ['1', '2', '3'])


        
# unit test
while True:
    a = input('Enter an assignment statement in the format of id=num or id=num+num: ')
    print(f'{a} is {assignmentstmt(a)}')
    b = input('Enter 0 to stop; any key to continue: ')
    if b == '0':
        break
 


