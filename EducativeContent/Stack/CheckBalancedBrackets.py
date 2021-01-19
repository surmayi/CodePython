from stack import Stack

def CheckBalancedBrackets(str):
    if not str:
        return 'Empty String'
    s = Stack()
    balanced =True
    ope=0
    for val in str:
        if val in '([{':
            s.appendToStack(val)
            ope+=1
        elif s.isEmptyStack():
            balanced=False
        elif not match(s.peekStack(),val):
            balanced =False
        else:
            s.deleteFromStack()
            ope-=1
    if ope>0 or balanced==False:
        return False
    else:
        return True

def match(ope,close):
    if ope == '(' and close == ')':
        return True
    elif ope=='{' and close =='}':
        return True
    elif ope=='[' and close ==']':
        return True
    else:
        return False


print(CheckBalancedBrackets("()"))

print(CheckBalancedBrackets("(((({}))))[]"))