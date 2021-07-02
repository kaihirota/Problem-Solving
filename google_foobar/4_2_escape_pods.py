"""
Escape Pods
===========

You've blown up the LAMBCHOP doomsday device and broken the bunnies out of Lambda's prison - and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time. 

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function solution(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

Then in each time step, the following might happen:
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final solution remains the same.)

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({0, 1}, {4, 5}, {{0, 0, 4, 6, 0, 0}, {0, 0, 5, 2, 0, 0}, {0, 0, 0, 0, 4, 4}, {0, 0, 0, 0, 6, 6}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    16

Input:
Solution.solution({0}, {3}, {{0, 7, 0, 0}, {0, 0, 6, 0}, {0, 0, 0, 8}, {9, 0, 0, 0}})
Output:
    6

-- Python cases --
Input:
solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
Output:
    6

Input:
solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    16

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

from collections import deque
class WeightedGraph:
    def __init__(self, matrix):
        """
        input:
            matrix: List[List[int]]
        """
        self.adjacency_matrix = matrix

    def __len__(self):
        return len(self.adjacency_matrix)

    def _BFS(self, s, t, parent):
        """
        input:
        s: int
            source (not to be mistaken with parent, source refers to the root or the origin)
        t: int
            target / sink
        parent: List 
            maps nodes to a parent
        """

        # augments a path with residual capacity of at least 1
        visited = [False] * len(self.adjacency_matrix)
        visited[s] = True
        queue = deque()
        queue.append(s)

        while queue:
            u = queue.popleft()

            # look at outgoing edges from node u, append edges
            for i, val in enumerate(self.adjacency_matrix[u]):
                if visited[i] == False and val > 0:
                    visited[i] = True
                    queue.append(i)
                    parent[i] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        """
        returns:
            max_flow: int
        """
        parent = [-1] * len(self.adjacency_matrix)
        max_flow = 0

        # updates parent list with augmenting paths
        while self._BFS(source, sink, parent):
            path_flow = float("Inf")

            s = v = sink

            # find minimum capacity of an augmenting path
            while(s != source):
                path_flow = min(path_flow, self.adjacency_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            # update flow / capacity of residual graph
            while(v != source):
                u = parent[v]
                self.adjacency_matrix[u][v] -= path_flow
                self.adjacency_matrix[v][u] += path_flow
                v = parent[v]

        return max_flow

def transform(graph, sources, sinks):
    """
    Given a graph with multiple sources and sinks, 
    insert a super source and super sink with infinite capacity 
    in order to transform it into single-source single-sink flow network.
    Edges from super source have infinite capacity, 
    and so do incoming edges of the super sunk.

    input:
        graph: List[List[int]]

    returns:
        WeightedGraph
    """
    graph = [[0] + row + [0] for row in graph]
    super_source = [0] * (len(graph) + 2)
    super_sink = [0] * len(super_source)

    for source in sources:
        super_source[1+source] = float("Inf")

    for sink in sinks:
        graph[sink][-1] = float("Inf")

    graph.insert(0, super_source)
    graph.append(super_sink)

    return WeightedGraph(graph)


def solution(entrances, exits, path):
    """
    input:
        entrances: List[int]
        exits: List[int]
        path: List[List[int]]
    """
    graph = transform(path, entrances, exits)
    max_flow = graph.ford_fulkerson(0, len(graph)-1)
    return max_flow



assert solution(
    [0], 
    [3], 
    [
        [0, 7, 0, 0], 
        [0, 0, 6, 0], 
        [0, 0, 0, 8], 
        [9, 0, 0, 0]
    ]) == 6

assert solution(
    [0, 1], 
    [4, 5], 
    [
        [0, 0, 4, 6, 0, 0], 
        [0, 0, 5, 2, 0, 0], 
        [0, 0, 0, 0, 4, 4], 
        [0, 0, 0, 0, 6, 6], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0]
    ]) == 16