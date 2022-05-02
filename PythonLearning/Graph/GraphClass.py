class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_routes = {}
        for start,end in self.edges:
            self.graph_routes[start] = self.graph_routes.get(start,[]) + [end]
        print(self.graph_routes)


    def get_paths(self,start,end,path=[]):
        path = path+[start]
        if start==end:
            return [path]
        if start not in self.graph_routes:
            return []
        allPaths =[]
        for node in self.graph_routes[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    allPaths.append(p)
        return allPaths


    def get_min_path(self,start,end,path=[]):
        path =path + [start]
        if start==end:
            return path
        if start not in self.graph_routes:
            return None
        shortest_path =None
        for node in self.graph_routes[start]:
            if node not in path:
                new_path = self.get_min_path(node,end,path)
                if new_path and (not shortest_path or len(shortest_path)>len(new_path)):
                    shortest_path= new_path
        return shortest_path




routes = [
    ("Mumbai","Pune"),
    ("Mumbai", "Surat"),
    ("Surat", "Bangaluru"),
    ("Pune","Hyderabad"),
    ("Pune","Mysuru"),
    ("Hyderabad","Bangaluru"),
    ("Hyderabad", "Chennai"),
    ("Mysuru", "Bangaluru"),
    ("Chennai", "Bangaluru")
]

graph = Graph(routes)
start = 'Mumbai'
end = 'Bangaluru'
print(graph.get_paths(start,end))

print(graph.get_min_path(start,end))