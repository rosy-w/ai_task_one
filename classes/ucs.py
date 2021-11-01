import networkx as nx
from collections import defaultdict 
try:
    import queue
except ImportError:
    import Queue as queue

from queue import PriorityQueue

class UCSTraverser:
    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.explored = []
        self.frontier = PriorityQueue()
    
    def traverse(self, start, goal):
        self.frontier.put((0, start))

        while not self.frontier.empty():
            cost, node = self.frontier.get()
            if node == goal:
                return node
            
            if node not in self.explored:
                self.explored.append(node)
                print(f"Coming from {node}")
                for child in self.graph[node]:
                    if child not in self.frontier.queue:
                        weight = self.graph.get_edge_data(node, child)['weight']
                        self.frontier.put((cost + int(weight), child))
        return None
