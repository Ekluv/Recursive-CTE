import networkx as nx

from company.models import Employee


G=nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(1, 4)
G.add_edge(4, 5)
G.add_edge(3, 5)


nx.shortest_path(G, source=1, target=3)
# [1,2,3]
nx.shortest_path(G, source=1, target=4)
# [1,4]
nx.shortest_path(G, source=1, target=5)
# [1,4,5]
nx.shortest_path(G, source=3, target=5)
# [3,5]
nx.shortest_path(G, source=2, target=3)
# [2,3,5]
# 

employees = Employee.objects.all()

G=nx.Graph()
