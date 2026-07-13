'''
17.Create an undirected graph with the following edges:
* A– B
* A– C
* B– D
* C– D
Display the adjacency list of the graph.    
'''
graph = {
    "A": [],
    "B": [],
    "C": [],
    "D": []
}

graph["A"].append("B")
graph["B"].append("A")

graph["A"].append("C")
graph["C"].append("A")

graph["B"].append("D")
graph["D"].append("B")

graph["C"].append("D")
graph["D"].append("C")

for vertex in graph:
    print(vertex, "->", graph[vertex])