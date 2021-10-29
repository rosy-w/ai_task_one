from collections import defaultdict 
try:
    import queue
except ImportError:
    import Queue as queue

from queue import PriorityQueue

class GBfsTraverser: 
  # Constructor 
  def __init__(self): 
    self.visited = []
    self.end_search = False
    self.expanded=[]
  def GBFS(self,graph,heuristic,start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        current=node
        if current not in visited:
            visited.add(current)
            self.expanded.append(current)

            if current == goal:
                return node, self.expanded

            neighbours = graph[current]
            print ("Command; Walk to " ,current,end = "\n")
            for i in neighbours:
                if i not in visited:
                    total_cost = heuristic[i]
                    queue.put((total_cost, i))