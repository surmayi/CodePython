def arrayAdvanceGame(lis):
    furthest_reached =0
    currInd=0
    lastInd=len(lis)-1
    while currInd<=furthest_reached and furthest_reached<lastInd:
        furthest_reached = max(furthest_reached,lis[currInd]+currInd)
        currInd+=1
    return furthest_reached>=lastInd

print(arrayAdvanceGame([3,3,1,0,2,1]))
print(arrayAdvanceGame([3,2,0,0,2,1]))