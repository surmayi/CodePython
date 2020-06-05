def plusOne( digits):
        val =0 
        for d in digits:
            val=val*10+d
        print(val)
        return list(map(int, str(val+1))) 
plusOne([4,3,2,1])