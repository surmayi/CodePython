class Solution(object):
    def numberOfBoomerangs(self, points):
        count =0
        for i in range(len(points)):
            d={}
            for j in range(len(points)):
                if i!=j:
                    dt = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                    count+= d.get(dt,0)
                    d[dt] = d.get(dt,0) +1
        return count*2
        