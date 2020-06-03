from collections import defaultdict, deque, OrderedDict
from itertools import combinations
from queue import PriorityQueue
from typing import List, Tuple

from graph import Graph

class WeightedGraph(Graph):
    def __init__(self, matrix: List[List], directed: bool):
        super().__init__(matrix, directed)

    @staticmethod
    def from_edges(e: List[Tuple[int, int]], directed: bool):
        """assumption: nodes are from 0 to n - 1"""
        edges = [(src, dst) for src, dst, weight in e]
        nodes = set(sorted([item for elem in edges for item in elem]))
        matrix = [[0] * len(nodes) for i in range(len(nodes))]

        for src, dest, weight in e:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = weight

            if directed is False:
                matrix[dest][src] = weight

        return WeightedGraph(matrix, directed)

    def get_edges(self):
        edges = set()

        for i in range(len(self.adjacency_matrix)):
            if self.directed == False:
                start = i + 1
            else:
                start = 0
            for j in range(start, len(self.adjacency_matrix[0])):
                if self.adjacency_matrix[i][j] != 0:
                    edges.add((i, j, self.adjacency_matrix[i][j]))
                    if self.directed == False and self.adjacency_matrix[j][i] != 0:
                        edges.add((j, i, self.adjacency_matrix[j][i]))
        return list(edges)

    def BFS(self, s, t, parent):
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
        parent = [-1] * len(self.adjacency_matrix)
        max_flow = 0

        while self.BFS(source, sink, parent):
            # updates parent list with augmenting paths
            path_flow = float("Inf")

            s = sink
            while(s != source):
                path_flow = min(path_flow, self.adjacency_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.adjacency_matrix[u][v] -= path_flow
                self.adjacency_matrix[v][u] += path_flow
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
        dists = [float('inf')] * len(self.adjacency_matrix)

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
            neighbors = self.adjacency_matrix[u]
            for v, weight_v in enumerate(neighbors):
                if weight_v > 0:
                    q.put([weight_u + weight_v, v])

        return dists


if __name__ == "__main__":
    # src, dest, weight
    edges = [(0, 1, 3), (0, 2, 2), (0, 3, 8), (1, 4, 2), (2, 3, 5),
             (2, 4, 4), (4, 5, 1), (5, 1, 2), (5, 2, 6)]
    directed = True
    graph = WeightedGraph.from_edges(edges, directed)

    print('directed:', directed)
    print('adjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    print('\nadjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')


    print('\nNetwork flow / Ford Fulkerson')
    # ford fulkerson demo
    adjacency_matrix = [
        [0, 5, 14, 0, 0, 0, 0, 0, 0], # s
        [0, 0, 4, 0, 3, 0, 0, 0, 0], # a
        [0, 0, 0, 0, 0, 7, 0, 0, 0], # b
        [0, 0, 0, 0, 0, 0, 6, 6, 0], # c
        [0, 0, 0, 8, 0, 0, 0, 4, 0], # d
        [0, 6, 0, 0, 3, 0, 0, 6, 0], # e
        [0, 0, 0, 0, 0, 0, 0, 0, 10], # f
        [0, 0, 0, 0, 0, 0, 0, 0, 8], # g
        [0, 0, 0, 0, 0, 0, 0, 0, 0] # t
    ]
    directed = True
    graph = WeightedGraph(adjacency_matrix, directed)
    print('directed:', directed)

    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('adjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')

    print('\nadjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    source = 0 # s
    sink = 8 # t
    maxflow = graph.ford_fulkerson(source, sink)
    print("\nMax Flow:", str(maxflow))

    print('\nresidual graph')
    for row in graph.adjacency_matrix:
        print(row)

    print("\nWeighted Graph / Dijkstra's Shortest Path")
    edges = [
        (0, 2, 9), (0, 6, 14), (0, 7, 15),
        (2, 3, 24), (3, 1, 19), (3, 5, 2),
        (4, 3, 6), (4, 1, 6), (5, 1, 16),
        (5, 4, 11), (6, 5, 30), (6, 7, 5),
        (6, 3, 18), (7, 5, 20), (7, 1, 44)
    ]
    directed = True
    graph = WeightedGraph.from_edges(edges, directed)
    print('directed:', directed)

    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('adjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')

    print('\nadjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    print('Shortest distance:')
    src = 0
    dest = 1
    print(graph.dijkstra_shortest_path(src, dest))
