import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","STC","Phase2","J1","Phase3","Mada","ParkingLot"]
node_sizes=[2000,1000,1000,1000,1000,1000,1000,1000,1000,2000]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes

#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase2","STC",weight="50")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Mada","ParkingLot",weight="700")
G.add_edge("Phase3","ParkingLot",weight="350")

#position the nodes to resemble Nairobis map
G.nodes["SportsComplex"]['pos']=(-4,2)
G.nodes["Siwaka"]['pos']=(-2,2)
G.nodes["Ph.1A"]['pos']=(0,2)
G.nodes["Ph.1B"]['pos']=(0,0)
G.nodes["Phase2"]['pos']=(2,0)
G.nodes["J1"]['pos']=(4,0)
G.nodes["Mada"]['pos']=(6,0)
G.nodes["STC"]['pos']=(0,-2)
G.nodes["Phase3"]['pos']=(4,-2)
G.nodes["ParkingLot"]['pos']=(4,-4)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

#color the nodes in the route_bfs
node_col = 'darkturquoise'
edge_col = 'peru'

arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col,font_size=8, node_size=node_sizes)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()

