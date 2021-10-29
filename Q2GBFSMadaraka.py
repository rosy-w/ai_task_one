import os
import networkx as nx
import matplotlib.pyplot as plt
from classes.greedybfs import GBfsTraverser

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","STC","Phase2","J1","Phase3","Mada","ParkingLot"]
node_sizes=[000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
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

#getting heuristics from txt file
def getHeuristics(G):
    heuristics = {}
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, 'heuristics.txt'))
    for i in G.nodes():
        node_heuristic_val = f.readline().split()
        heuristics[node_heuristic_val[0]] = node_heuristic_val[1]
    return heuristics

heuristics = getHeuristics(G)
node_pos = nx.get_node_attributes(G,'pos')

#call BFS
route_bfs = GBfsTraverser()
routes = route_bfs.GBFS(G,heuristics,"SportsComplex","ParkingLot")

route_list = route_bfs.expanded
#color the nodes and edges in the route_bfs
node_col = ['#c3b3ff' if not node in route_list else '#69f591' for node in G.nodes()]
green_colored_edges = list(zip(route_list,route_list[1:]))
edge_col = ['#000000' if not edge in green_colored_edges else '#2dc458' for edge in G.edges()]
arc_label=nx.get_edge_attributes(G,'label')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_label)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels={('SportsComplex','Siwaka'):'UnkRoad(450m)',
   ('Siwaka','Ph.1A'):'SangaleRd(10m)',('Siwaka','Ph.1B'):'SangaleLink(230m)',('Ph.1A','Ph.1B'):'ParkingWalkWay(100m)',('Ph.1B','Phase2'):'KeriRd(112m)',
   ('Phase2','J1'):'KeriRd(600m)',('J1','Mada'):'SangaleRd(200m)',('Ph.1A','Mada'):'SangaleRoad(850m)',('Ph.1B','STC'):'KeriRd(50m)',
   ('STC','Phase2'):'STCwalkway(50m)',('Phase2','Phase3'):'KeriRd(500m)',('Phase3','ParkingLot'):'HimaGRd(350m)',('STC','ParkingLot'):'LibraryWalkWay(250m)',
   ('ParkingLot','Mada'):'LangataRd(700m)'},font_color='#000000',font_size='x-small')
plt.axis('off')
plt.show()
