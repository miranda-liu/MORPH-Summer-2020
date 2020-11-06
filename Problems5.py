from collections import deque
from queue import PriorityQueue
from queue import queue
from pqdict import PQDict

# BFS
def bfs1(graph, vertex): # BFS version 1
    queue = deque([vertex]) # double ended queue(deque), contains the nodes you need to visit
    level = {vertex: 0} # dictionary
    parent = {vertex: None} # dictionary
    while queue: # is not empty
        v = queue.popleft() # gets rid of first one and returns
        for n in graph[v]:
            if n not in level:            
                queue.append(n)
                level[n] = level[v] + 1
                parent[n] = v
    return level, parent

# BFS version 2, tells you if a path exists between two nodes
def path_exists(G, node1, node2): # G is a graph, node1 and node2 are two nocdes
    visited_nodes = set()
    queue = [node1] # implemented as a list, initialize queue with node1
    for node in queue: # iterate through queue
        neighbors = G.neighbors(node) # get neighbors of node1
        if node2 in neighbors:
            return True # returns True if path exists
            break
        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes]) # add the neighbors of the current node node that have not yet been visited to queue. 
                    # To do this, you'll need to use the .extend() method of queue together with a list comprehension. 
                    # The .extend() method appends all the items in a given list.
                    # The output expression and iterator variable of the list comprehension are both n. 
                    # The iterable is the list neighbors, and the conditional is if n is not in the visited nodes.
        if node == queue[-1]: # when queue is empty
             print('Path does not exist between nodes {0} and {1}'.format(node1, node2))
             return False # returns False if path does not exist




# Dijkstra's Algorithm

# returns shortest distance using Dijkstra's from every node to the start node s
# g is the adjacency list of weighted graph
# n is the number of nodes in the graph
# s is the index of the starting node (0<= s < n)
# goes through every single node's possible paths
def dijkstra_distance_lazy_no_skipping(g, n, s): # lazy implementation -> the things in pq aren't actively replaced, they're removed and new ones are added
    visited = [False] * n # none of the nodes have been visited yet
    distance = [float('inf')] * n # none of the distances have been confirmed
    distance[s] = 0 # distance to the starting node is 0
    pq = PriorityQueue() # making a priority queue to store what needs to be travelled
    pq.insert((s, 0)) # insert the starting node
    # heaps are a way to structure so the most important thing is always the highest (like the root of a tree)
    # priority queue: not necessarily in the order it's listed, ordered by "priority" by weighting
    while pq.size() != 0: # while the pq isn't empty -> still nodes to visit
        index, minValue = pq.poll() # poll returns a node represented by a index and minValue, returns the next most promising index with minValue
        visited[index] = True # the node is now visited at that specific index
        for edge in g[index]: # for each edge in the weighted graph/adjacency list g
            if visited[edge.to] == False: # edge.to gives the indexes of the adjacent edges -> if edge hasn't been visited yet
                newDistance = distance[index] + edge.cost # edge.cost gives the cost of going from g[index] to g[edge.to]
            if newDistance < distance[edge.to]: # if this new distance is less than the old recorded distance
                distance[edge.to] = newDistance # set distance to new distasnce
                pq.insert((edge.to, newDistance)) # add to priority queue to visit in the future
    return distance # return distance
# for one way vs two ways: change g -> g uses a 2x2 matrix to dictate that node's neighbors, inside the matrix
# to build the matrix: use bfs to find neighbors


# returns shortest distance using Dijkstra's from every node to the start node s
# g is the adjacency list of weighted graph
# n is the number of nodes in the graph
# s is the index of the starting node (0<= s < n)
# optimizes by skipping nodes where a better path through other nodes has already been found
def dijkstra_distance_lazy_with_skipping(g, n, s): # lazy implementation -> the things in pq aren't actively replaced, they're removed and new ones are added
    visited = [False] * n # none of the nodes have been visited yet
    distance = [float('inf')] * n # none of the distances have been confirmed
    distance[s] = 0 # distance to the starting node is 0
    pq = PriorityQueue() # making a priority queue to store what needs to be travelled
    pq.insert((s, 0)) # insert the starting node
    # heaps are a way to structure so the most important thing is always the highest (like the root of a tree)
    # priority queue: not necessarily in the order it's listed, ordered by "priority" by weighting
    while pq.size() != 0: # while the pq isn't empty -> still nodes to visit
        index, minValue = pq.poll() # poll returns a node represented by a index and minValue, returns the next most promising index with minValue
        visited[index] = True # the node is now visited at that specific index
        if distance[index] > minValue: # if the current distance is still larger than the minValue, continues -> otherwise skips
            for edge in g[index]: # for each edge in the weighted graph/adjacency list g
                if visited[edge.to] == False: # edge.to gives the indexes of the adjacent edges -> if edge hasn't been visited yet
                    newDistance = distance[index] + edge.cost # edge.cost gives the cost of going from g[index] to g[edge.to]
                if newDistance < distance[edge.to]: # if this new distance is less than the old recorded distance
                    distance[edge.to] = newDistance # set distance to new distasnce
                    pq.insert((edge.to, newDistance)) # add to priority queue to visit in the future
    return distance # return distance

# returns a possible shortest path and distance using Dijkstra's from every node to the start node s
# g is the adjacency list of weighted graph
# n is the number of nodes in the graph
# s is the index of the starting node (0<= s < n)
# optimizes by skipping nodes where a better path through other nodes has already been found
def dijkstra_distance_lazy_with_skipping(g, n, s): # lazy implementation -> the things in pq aren't actively replaced, they're removed and new ones are added
    visited = [False] * n # none of the nodes have been visited yet
    distance = [float('inf')] * n # none of the distances have been confirmed
    previous = [null] * n # the shortest path is not known yet, will be updated to track the path you took to get to node n
    distance[s] = 0 # distance to the starting node is 0
    pq = PriorityQueue() # making a priority queue to store what needs to be travelled
    pq.insert((s, 0)) # insert the starting node
    # heaps are a way to structure so the most important thing is always the highest (like the root of a tree)
    # priority queue: not necessarily in the order it's listed, ordered by "priority" by weighting
    while pq.size() != 0: # while the pq isn't empty -> still nodes to visit
        index, minValue = pq.poll() # poll returns a node represented by a index and minValue, returns the next most promising index with minValue
        visited[index] = True # the node is now visited at that specific index
        if distance[index] > minValue: # if the current distance is still larger than the minValue, continues -> otherwise skips
            for edge in g[index]: # for each edge in the weighted graph/adjacency list g
                if visited[edge.to] == False: # edge.to gives the indexes of the adjacent edges -> if edge hasn't been visited yet
                    newDistance = distance[index] + edge.cost # edge.cost gives the cost of going from g[index] to g[edge.to]
                if newDistance < distance[edge.to]: # if this new distance is less than the old recorded distance
                    distance[edge.to] = newDistance # set distance to new distasnce
                    pq.insert((edge.to, newDistance)) # add to priority queue to visit in the future
    return distance, previous # return distance and the previous list of nodes visited

# finds the shortest path between two nodes
# g is the adjacency list of weighted graph
# n is the number of nodes in the graph
# s is the index of the starting node (0 <= s <= n)
# e is the index of the end node (0 <= e <= n)
def findShortestPath(g, n, s, e):
    distance, previous = dijkstra_distance_lazy_with_skipping(g, n, s) # get distance and previous by running the method
    path = [] # path is empty at first
    if distance[e] == float('inf'): # if the distance is infinity to e from s, this means a path doesn't exist
        return path # returns empty path
    for node in previous: # for each node in previous
        path.add(node) # add to path
        if node == null: # when it reaches node, stop because the node s doesn't have a parent so it is null
            break
    path = path.reverse() # reverse path because you looped through an already reversed list
    return path # return the path

# when looking for just one node's (e) distance from s using Dijkstra's algorithm
# g is the adjacency list of weighted graph
# n is the number of nodes in the graph
# s is the index of the starting node (0 <= s <= n)
# e is the index of the end node (0 <= e <= n)
def dijkstra_distance_lazy_with_skipping_optimized(g, n, s, e): # lazy implementation -> the things in pq aren't actively replaced, they're removed and new ones are added
    visited = [False] * n # none of the nodes have been visited yet
    distance = [float('inf')] * n # none of the distances have been confirmed
    distance[s] = 0 # distance to the starting node is 0
    pq = PriorityQueue() # making a priority queue to store what needs to be travelled
    pq.insert((s, 0)) # insert the starting node
    # heaps are a way to structure so the most important thing is always the highest (like the root of a tree)
    # priority queue: not necessarily in the order it's listed, ordered by "priority" by weighting
    while pq.size() != 0: # while the pq isn't empty -> still nodes to visit
        index, minValue = pq.poll() # poll returns a node represented by a index and minValue, returns the next most promising index with minValue
        visited[index] = True # the node is now visited at that specific index
        if distance[index] > minValue: # if the current distance is still larger than the minValue, continues -> otherwise skips
            for edge in g[index]: # for each edge in the weighted graph/adjacency list g
                if visited[edge.to] == False: # edge.to gives the indexes of the adjacent edges -> if edge hasn't been visited yet
                    newDistance = distance[index] + edge.cost # edge.cost gives the cost of going from g[index] to g[edge.to]
                if newDistance < distance[edge.to]: # if this new distance is less than the old recorded distance
                    distance[edge.to] = newDistance # set distance to new distasnce
                    pq.insert((edge.to, newDistance)) # add to priority queue to visit in the future
        if index == e: # if e is already reached
            return distance[e] # end early by returning distance
    return float('inf') # return infinity because e is never reached from node s



# using Dijkstra's to return a list that contains the shortest distance to every node from the start node s
# g is the adjacency list of weighted graph
# n is the number of nodes in the graph
# s is the index of the starting node (0 <= s <= n)
def dijkstra_distance_eager(g, n, s): # eager implementation because by using an index priority queue, you can access values in the queue directly and change them -> no duplicates
    visited = [False] * n # none of the nodes have been visited yet
    distance = [float('inf')] * n # none of the distances have been confirmed
    distance[s] = 0 # distance to the starting node is 0
    ipq = PQDict() # making an indexed priority queue to store what needs to be travelled
    ipq.insert(s, 0) # insert the starting node
    while ipq.size() != 0: # while the ipq isn't empty -> still nodes to visit
        index, minValue = ipq.poll() # poll returns a node represented by a index and minValue, returns the next most promising index with minValue
        visited[index] = True # the node is now visited at that specific index
        if distance[index] > minValue: # if the current distance is still larger than the minValue, continues -> otherwise skips
            for edge in g[index]: # for each edge in the weighted graph/adjacency list g
                if visited[edge.to] == False: # edge.to gives the indexes of the adjacent edges -> if edge hasn't been visited yet
                    newDistance = distance[index] + edge.cost # edge.cost gives the cost of going from g[index] to g[edge.to]
                if newDistance < distance[edge.to]: # if this new distance is less than the old recorded distance
                    if ipq.contains(edge.to) == False: # if that node hasn't already been travelled that way
                        ipq.insert(edge.to, newDistance) # add in distance
                    else:
                        ipq.decreaseKey(edge.to, newDistance) # decreasekey updates the best distance for that node, instead of just adding in a new one
    return distance # return distance


