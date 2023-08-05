'''
Leetcode- https://leetcode.com/problems/clone-graph/
'''

'''
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        node_map = {}
        
        def clone(node):
            if node in node_map:
                return node_map[node]
            
            clone_node = Node(node.val)
            node_map[node] = clone_node
        

            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            
            return clone_node
        
        return clone(node) if node else None
    
# T: O(V + E), where V is the number of nodes and E is the number of edges in the input graph.
    
'''
Explaination of nodes:

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

adjList = [node1, node2, node3, node4]
'''

'''
Exlanation(solution):

Example Graph---

   1
  / \
 2   3

1. The cloneGraph method is called with the node 1.
2. node is not None, so we proceed.
3. node_map is initialized as an empty dictionary.
4. The clone function is defined.
5. We enter the clone function with node as 1.
6. node is not in node_map, so we create a clone clone_node with value 1.
7. node_map now contains {1: clone_node}.
8. We iterate through node.neighbors, which are 2 and 3.
9. We recursively call clone on 2.
10. node is not in node_map, so we create a clone clone_node with value 2.
11. node_map now contains {1: clone_node_1, 2: clone_node_2}.
12. We recursively call clone on 3.
13. node is not in node_map, so we create a clone clone_node with value 3.
14. node_map now contains {1: clone_node_1, 2: clone_node_2, 3: clone_node_3}.
15. We finish cloning 1 and its neighbors, so we return clone_node_1 to the initial call.
16. The cloneGraph method returns clone_node_1.

'''