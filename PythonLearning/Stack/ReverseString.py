from stack import Stack

def reverseString(str):
    if not str:
        return 'Empty String'
    s=Stack()
    for val in str:
        s.appendToStack(val)
    rev_str=''
    while s.peekStack():
        rev_str+=s.deleteFromStack()
    return rev_str


print(reverseString('abcdabcd'))