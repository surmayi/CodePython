class Solution(object):
    def findRestaurant(self, list1, list2):
        l = len(list1) if len(list1)<=len(list2) else len(list2)
        prev =0
        fin=set()
        for i in range(len(list1)):
            if list1[i] in list2:
                prev = i + list2.index(list1[i])
                fin.add(list1[i])
                break;
        for j in range(i+1,len(list1)):
            if list1[j] in list2:
                s=j+ list2.index(list1[j])
                if s<=prev:
                    prev = s 
                    fin.add(list1[j])
                    
                else:
                    pass
        return fin
        