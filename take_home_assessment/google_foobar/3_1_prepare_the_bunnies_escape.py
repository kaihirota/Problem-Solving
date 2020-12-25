"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
    11

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

import copy

def solution(map):
    m, n = (len(map), len(map[0]))
    
    if m == n == 1:
        return 1

    map = BFS(map)
    if map[-1][-1] != 0:
        min_path = -map[-1][-1]
    else:
        min_path = m * n

    for i in range(m):
        for j in range(n):
            if map[i][j] == 1:
                neighbors = 0
                if i + 1 < m and map[i+1][j] != 1:
                    neighbors += 1
                if i - 1 >= 0 and map[i-1][j] != 1:
                    neighbors += 1
                if j + 1 < n and map[i][j+1] != 1:
                    neighbors += 1
                if j - 1 >= 0 and map[i][j-1] != 1:
                    neighbors += 1
                
                if neighbors >= 2:
                    min_path = min(min_path, remove_wall(map, i, j))

    return min_path


def BFS(map):
    start = (0, 0, -1)
    m, n = (len(map), len(map[0]))
    stack = [start]
    while stack:
        i, j, steps = stack.pop(0)
        map[i][j] = steps
        if i + 1 < m and map[i+1][j] == 0:
            stack.append((i+1, j, steps-1))
        if i - 1 >= 0 and map[i-1][j] == 0:
            stack.append((i-1, j, steps-1))
        if j + 1 < n and map[i][j+1] == 0:
            stack.append((i, j+1, steps-1))
        if j - 1 >= 0 and map[i][j-1] == 0:
            stack.append((i, j-1, steps-1))
    return map


def remove_wall(map, i, j):
    new_map = copy.deepcopy(map)
    start = (0, 0, -1)
    m, n = (len(new_map), len(new_map[0]))
    stack = [start]
    seen = set()
    new_map[i][j] = 0

    while stack:
        i, j, steps = stack.pop(0)
        if (i, j) in seen:
            continue
        seen.add((i, j))
        
        new_map[i][j] = steps
        if i + 1 < m and new_map[i+1][j] != 1:
            stack.append((i+1, j, steps-1))
        if i - 1 >= 0 and new_map[i-1][j] != 1:
            stack.append((i-1, j, steps-1))
        if j + 1 < n and new_map[i][j+1] != 1:
            stack.append((i, j+1, steps-1))
        if j - 1 >= 0 and new_map[i][j-1] != 1:
            stack.append((i, j-1, steps-1))

    if -new_map[-1][-1] != 0:
        return -new_map[-1][-1]
    else:
        return m * n



assert solution([
    [0, 1, 1, 0], 
    [0, 0, 0, 1], 
    [1, 1, 0, 0], 
    [1, 1, 1, 0]]) == 7

assert solution([
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]]) == 11

assert solution([
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]]) == 11

assert solution([
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]]) == 11

assert solution([[0, 0, 0, 0, 0, 0]]) == 6
assert solution([[0, 0, 0, 1, 0, 0]]) == 6
assert solution([[0]]) == 1

assert solution([
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0], 
    [1, 1, 1, 1, 1, 1], 
    [0, 1, 1, 0, 1, 1], 
    [1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]]) == 11