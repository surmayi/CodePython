def isValid( s):
        if(len(s)%2==1):
            return False
        if(len(s)==0):
            return True
        l = list(s)
        one =[]
        one.append(l.pop(0))
        while(len(l)>0):
            if(l[0] in ['{','[','(']):
                one.append(l.pop(0))
            else:
                if(((l[0]==']') and (one[-1]=='['))
                   or ((l[0]=='}') and (one[-1]=='{'))
                   or ((l[0]==')') and (one[-1]=='('))):
                    l.pop(0)
                    one.pop()
                else:
                    return False
        if(len(one)!=0):
            return False
        else:
            return True 

isValid("()[]{}") #true