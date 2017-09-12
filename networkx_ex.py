import matplotlib.pyplot as plt
import networkx as nx


pos = {0: (50, 50), 1: (40, 60), 2: (60, 60)} 
X=nx.Graph()
nx.draw_networkx_nodes(X, pos, node_size=3000, nodelist=[0,1,2], node_color='r')
# X.add_edge(0, 1)
# X.add_edge(0, 2)

# G=nx.Graph()
# G.add_node("a")
# G.add_nodes_from(["b","c"])

# edge = ("d", "e")
# G.add_edge(*edge)
# edge = ("a", "b")
# G.add_edge(*edge)

# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())

# ['a', 1, 'c', 'b', 'e', 'd', 2]

# [('a', 'b'), (1, 2), ('e', 'd')]

# # adding a list of edges:
# G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

nx.draw(X)

plt.savefig("simple_path.png") # save as png
plt.show() # display