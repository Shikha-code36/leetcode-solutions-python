'''
Leetcode - https://leetcode.com/problems/course-schedule/
'''
'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def is_cycle(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False

            visited[node] = 1

            if node in graph:
                for neigh in graph[node]:
                    if is_cycle(neigh):
                        return True
                        
            visited[node] = 2
            return False
            
        graph = {}
        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
            
        visited = [0]*numCourses

        for course in range(numCourses):
            if is_cycle(course):
                return False

        return True

# T:O(V + E) 

'''
Explaination -
 
for example---

numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]

Step 1: Initialize Variables and Graph

-- numCourses is 4, meaning there are 4 courses labeled from 0 to 3.
-- prerequisites is a list of prerequisite pairs: [1, 0], [2, 1], [3, 2], and [0, 3].

Step 2: Build the Graph
We create an adjacency list to represent the directed graph based on the prerequisite pairs:

Graph:
0 -> [3]
1 -> [0]
2 -> [1]
3 -> [2]

Step 3: Perform DFS to Detect Cycles
We'll perform Depth-First Search (DFS) to traverse the graph and detect cycles. The DFS function will mark nodes as visiting and visited while exploring the graph.

Starting DFS from each node:

    - Node 0:
        - Marked as visiting (visited[0] = 1)
        - Visit its neighbor 3
            - Node 3:
                - Marked as visiting (visited[3] = 1)
                - Visit its neighbor 2
                    - Node 2:
                        - Marked as visiting (visited[2] = 1)
                        - Visit its neighbor 1
                            - Node 1:
                                - Marked as visiting (visited[1] = 1)
                                - Visit its neighbor 0
                                    - Node 0:
                                        - Already visiting (visited[0] = 1)
                                        - Cycle detected, return True

Result: A cycle was detected during the DFS traversal, indicating that it's not possible to finish all courses due to the cyclic dependency.

Final Output: False

In this example, the code correctly identified that there is a cycle in the graph, which means 
it's not possible to finish all courses with the given prerequisites. The function returns False. 
The cycle [0, 1, 2, 3, 0] was detected during the traversal.

'''