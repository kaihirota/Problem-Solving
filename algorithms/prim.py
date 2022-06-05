from collections import defaultdict, deque, OrderedDict
from itertools import combinations
from queue import PriorityQueue
from typing import List, Tuple

from mygraph import MyGraph

"""
ported to graph_weighted.py
"""

class WeightedMyGraph(MyGraph):
    def __init__(self, matrix: List[List], is_directed: bool):
        super().__init__(matrix, is_directed)

    @staticmethod
    def from_edges(edges: List[Tuple[int, int]], is_directed: bool):
        """assumption: nodes are from 0 to n - 1"""
        edges = [(src, dst) for src, dst, weight in edges]
        nodes = set(sorted([item for elem in edges for item in elem]))
        matrix = [[0] * len(nodes) for i in range(len(nodes))]

        for src, dest, weight in edges:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = weight

            if is_directed is False:
                matrix[dest][src] = weight

        return WeightedMyGraph(matrix, is_directed)

    def get_edges(self):
        edges = set()

        for i in range(len(self._adjacency_matrix)):
            if self.is_directed == False:
                start = i + 1
            else:
                start = 0
            for j in range(start, len(self._adjacency_matrix[0])):
                if self._adjacency_matrix[i][j] != 0:
                    edges.add((i, j, self._adjacency_matrix[i][j]))
                    if self.is_directed == False and self._adjacency_matrix[j][i] != 0:
                        edges.add((j, i, self._adjacency_matrix[j][i]))
        return list(edges)

    def BFS(self, s, t, parent):
        # augments a path with residual capacity of at least 1

        visited = [False] * len(self._adjacency_matrix)
        visited[s] = True
        queue = deque()
        queue.append(s)

        while queue:
            u = queue.popleft()

            # look at outgoing edges from node u, append edges
            for i, val in enumerate(self._adjacency_matrix[u]):
                if visited[i] == False and val > 0:
                    visited[i] = True
                    queue.append(i)
                    parent[i] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * len(self._adjacency_matrix)
        max_flow = 0

        while self.BFS(source, sink, parent):
            # updates parent list with augmenting paths
            path_flow = float("Inf")

            s = sink
            while(s != source):
                path_flow = min(path_flow, self._adjacency_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self._adjacency_matrix[u][v] -= path_flow
                self._adjacency_matrix[v][u] += path_flow
                v = parent[v]

        return max_flow

    def dijkstra_shortest_path(self, src, dest=None):
        """
        computes shortest distance from src to every other node

        input:
            src: index of source node between 0 and n-1
            dest: index of destination node between 0 and n-1
        returns:
            dist: integer distance to src node if dest != None. Else, entire distance array will be returned.
        """
        dists = [float('inf')] * len(self._adjacency_matrix)

        q = PriorityQueue()
        q.put([0, src]) # (distance, node)

        while not q.empty():
            # pop off nearest node (given the path taken so far) from src
            weight_u, u = q.get()

            if weight_u >= dists[u]:
                # if this line is reached, then a shorter path to node u has been found
                continue

            # update dists only if current path to node u is shortest path found so far
            dists[u] = weight_u

            if u == dest:
                # shortest path to destination found
                return dists[dest]

            # add neighbors of u to q
            neighbors = self._adjacency_matrix[u]
            for v, weight_v in enumerate(neighbors):
                if weight_v > 0:
                    q.put([weight_u + weight_v, v])

        return dists

    def prim_mst(self) -> List[Tuple]:
        """
        returns:
            mst: minimum spanning tree. List of tuples of form (source, destination, weight)
        """
        n_nodes = len(self._adjacency_matrix)
        n_edges = 0
        visited = [False] * n_nodes
        visited[0] = True
        mst = []

        while n_edges < n_nodes - 1:
            minimum = float('inf')
            src = None
            dest = None
            wt = None

            for u in range(n_nodes):
                if visited[u] == True:
                    for v in range(n_nodes):
                        weight = self._adjacency_matrix[u][v]

                        # next unvisited node
                        if visited[v] == False and weight != 0:
                            if minimum > weight:
                                minimum = weight
                                src, dest, wt = u, v, weight

            visited[dest] = True
            mst.append((src, dest, wt))
            n_edges += 1

        return mst


if __name__ == "__main__":
    adjacency_matrix = [
        [0, 9, 75, 0, 0],
        [9, 0, 95, 19, 42],
        [75, 95, 0, 51, 66],
        [0, 19, 51, 0, 31],
        [0, 42, 66, 31, 0]
    ]
    directed = False
    graph = WeightedMyGraph(adjacency_matrix, directed)
    print('directed:', directed)

    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('\nadjacency matrix')
    for row in graph._adjacency_matrix:
        print(row)

    print("\nPrim's Algorithm")
    mst = graph.prim_mst()
    for src, dest, weight in mst:
        print(f'{src} -> {dest}, {weight}')
