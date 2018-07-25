# 6002 Lecture 3 - Graph Problems

## Exercise 1

2018-07-11 17:38

> We often use graphs to simplify optimization problems, as they are easy implement on a computer.

图可以简化最优化问题，因为图的关系容易被计算机实现。

> The following concepts can be illustrated with a graph. Determine which variables should be represented by edges and vertices in this graph.

> ### A school's course catalog

> Some classes must occur at least one semester before certain other classes (e.g., Calculus I must be taken before Calculus II), but not all classes have prerequisites.

> If we want to represent the catalog as a graph, which variables should be represented as edges and vertices?

> A) Each edge is a class, while different vertices indicate the semester the class is taken.

Class cannot connect two semesters.

> B) Each vertex is a class, while a directional edge indicates that one class must come before another. __correct__

Directional edges can show the prerequisite relationship.

> C) Each vertex is a class, while edges between two vertices indicate that the classes may be taken at the same time.

Too much edges, indicating that nearly every two vertices have an edges.

> Explanation:

> A) does not make sense in general. An edge connecting two vertices would indicate that a class is taken in two semesters.

> B) is correct. An edge pointing from one class to another implies that the source of the edge is a prerequisite.

> C) does not offer any indication of which class is required before another.



> ### Students in a line

> Second graders are lining up to go to their next class, but must be ordered alphabetically before they can leave. The teacher only swaps the positions of two students that are next to each other in line.

> If we want to represent this situation as a graph, which variables should be represented as edges and vertices?

> A) Vertices represent permutations of the students in line. Edges connect two permutations if one can be made into the other by swapping two adjacent students. __correct__

Permutation is unique. Swap between permutations fits one edge.

> B) Vertices represent students. Edges connect two students if they are next to each other in line.

直观，简单，但是不知道这关系对最优化算法什么用。

> C) Vertices represent permutations of the students, and each edge represents an individual student. An edge connects two vertices if that student is involved in swap between the two permutations.

两个节点之间就有两条边了，两条边还不容易定义方向（也可以：如果student_1在Permutation_A到Permutation_B是向后交换了一个位置，就定义student_1是Permutation_A到Permutation_B的directional edge。)

> Explanation:

> A) is correct. Travelling from one vertex to another through an edge represents a legal move.

> B) only offers information relevant to the current state of the line. There is no information regarding how the line can change.

说得好！

> C) does not make sense to implement. Multiple edges would have to connect every vertex, and many edges would be needed to fully represent a single child.

没懂。

---

## Exercise 2

> Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C). Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent students.

We construct our graph by first adding the following nodes:

```python
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
```

Add the appropriate edges to the graph.

Hint: How to get started?

Write your code in terms of the nodes list from the code above. For each node, think about what permutation is allowed. A permutation of a set is a rearrangement of the elements in that set. In this problem, you are only adding edges between nodes whose permutations are between elements in the set beside each other . For example, an acceptable permutation (edge) is between "ABC" and "ACB" but not between "ABC" and "CAB".

```python
for i in range(len(nodes)):
    src = nodes[i].getName()
    for j in range(i+1, len(nodes)):
        des = nodes[j].getName()
        for k in range(len(src)-1):
            if src[k] != des[k]:
                if src[k+1] == des[k] and src[k] == des[k+1]:
                    g.addEdge(Edge(nodes[i], nodes[j]))
                else:
                    break
```

```commandline
# ABC->ACB
# ABC->BAC
# ACB->ABC
# ACB->CAB
# BAC->ABC
# BAC->BCA
# BCA->BAC
# BCA->CBA
# CAB->ACB
# CAB->CBA
# CBA->BCA
# CBA->CAB
```

## Exercise 3

3/4 points (graded)

For questions 1 and 2, consider our previous problem (permutations of 3 students in a line).

### When represented as a tree, each node will have how many children?


2 correct  2
 
Explanation:

From each permutation, there are two possible swaps (Students 1st and 2nd in line, and Students 2nd and 3rd in line).

### Given two permutations, what is the maximum number of swaps it will take to reach one from the other?


3 correct  3
 
Explanation:

We can label the permutations a through f and construct a graph as such:

a <--> b <--> c <--> d <--> e <--> f <--> a

这是一个手拉手的环。

Clearly, it takes a maximum of 3 movements along edges to get from any node to another. 

The maximum number of permutations happens when we go from ABC to CBA. We have to go ABC -> BAC -> BCA -> CBA.

For questions 3 and 4, consider the general case of our previous problem (permutations of n students in a line). Give your answer in terms of n.

### When represented as a tree, each node will have how many children?

n-1 correct  n - 1
 
Explanation:

In any given permutation, n students are lined up. Since one may only swap the positions of two adjacent students, there are exactly  pairs we are able to swap. Each of these swaps will create a distinct ordering, so there are exactly n-1 children of each node.

### Given two permutations, what is the maximum number of swaps it will take to reach one from the other?

n **incorrect**  n * (n - 1)/2
 
Explanation:

Consider the case where the two permutations whose exchange would take the maximum number of swaps. Clearly these are two whose orders are opposite. 
(这个clearly我没看出来，囧。定理是要发现了才证明的，通往数学发现之路不容易啊。)

It takes n-1 swaps to move the last person in line to the first position. This leaves the rest of the line's old order intact.

Next it takes n-2 swaps to move the last person in line to the second position. We continue until only one more swap is needed (switching the last two people in line). This takes (n-1) + (n-2) + ... + 2 + 1 = n*(n-1)/2 swaps.

---

## Exercise 4

5/7 points (graded)

Consider our continuing problem of permutations of three students in a line. Use the enumeration we established when adding the nodes to our graph. That is,

```python
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]
```

so that ABC is Node 0, BCA is Node 3, etc.

Using Depth First Search, and beginning at the listed source nodes, give the first path found to the listed destination nodes. For the purpose of this exercise, assume DFS prioritizes lower numbered nodes. For example, if Node 2 is connected to Nodes 3 and 4, the first path checked will be 23. Additionally, DFS will never return to a node already in its path.

To denote a path, simply list the numbers of the nodes exactly as done in the lecture.

Hint: Visual representation

You can never go wrong with drawing a picture of the problem. Here is one possible visualization. The possible permutations are denoted in the graph below. From each node, you can choose to go in either direction. In this particular depth-first-search problem, you will choose the lower numbered node over the higher numbered one, even if it will lead to a longer path from the source to the destination.

![](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0cc1a7fc9161594df8ae57529a09849b/asset-v1:MITx+6.00.2x+3T2017+type@asset+block/l9p4.png)

Source: 0

Destination: 4

014 correct  014

Source: 4

Destination: 1

41 correct  41

Source: 1

Destination: 1

1 correct  1

Source: 2

Destination: 4

2014 correct  2014

** Source: 2

Destination: 3

23 **incorrect**  201453 **

Source: 3

Destination: 1

3201 correct  3201

We saw before that for permutations of 3 people in line, any two nodes are at most three edges, or four nodes, away. But DFS has yielded paths longer than three edges! In this graph, given a random source and a random destination, what is the probability of DFS finding a path of the shortest possible length?


6 **incorrect**  2/3
 
Explanation:

First, realize that the structure of this graph is a set of six nodes, all connected in a circle. Each node has two edges that connect it to adjacent nodes.

Given any node, we know that DFS will prioritize the lower-numbered neighbor. Thus, for any destination, we first check for paths along this side. If our destination is our source, we terminate the DFS, and return a path of length zero, which is clearly the shortest. Otherwise, we continue in a circle in one direction. We cannot change direction once we have begun to traverse the circle, as the path may not include any node more than once. It will have found the shortest path for the nodes that are 0, 1, 2, or 3 edges away, but will yield paths of length 4 and 5 for the last two nodes that are, in reality, 2 and 1 edges away, respectively. As it has found the shortest path for 4 nodes, but not for 2, the probability is 4 in 6, or 2/3.

---
## Exercise 5

4/5 points (graded)

Challenge Problem! This problem is difficult and may stump you, but we include it because it is very interesting, especially for those who are more mathematically inclined.

Don't worry if you can't get all the math behind it, and don't get discouraged. Remember that you do not lose points for trying a problem multiple times, nor do you lose points if you hit "Show Answer". If this problem has you stumped after you've tried it, feel free to reveal the solution and read our explanations.

In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with  nodes as KN. Answer the following questions in terms of .

1. How many edges are in KN?


n*(n-1)/2
  correct  n * (n - 1)/2
 
Explanation:

Answer: 
In a directed graph, each node would connect to all other nodes, yielding n*(n-1) edges. In our undirected graph, an edge from A to B and from B to A are the same edge, so there are, in fact, half as many.

Alternatively - if you are familiar with the binomial coefficient - see that for each edge, you must choose two nodes to connect. Thus there are 

(n 2) = n*(n-1)/2

edges.

2. Consider the new version of DFS. This traverses paths until all non-circular paths from the source to the destination have been found, and returns the shortest one.

Let A be the source node, and B be the destination in KN. How many paths of length 2 exist from A to B?


n-2
  correct  n - 2
 
Explanation:

Answer: 
We have a source A and a destination B. Paths of length 2 contain exactly three nodes. We must select one more node to place in the middle of our path. As we cannot select the A or B, we are left with N - 2 choices to construct a path.

3. How many paths of length 3 exist from A to B?


(n-2)*(n-3)
  correct  (n - 2) * (n - 3)
 
Explanation:

Answer: 
Use the same reasoning as used for the previous problem. After knowing our source and destination, we must travel through 2 additional nodes without touching any node twice. For the first node, we have n-2  choices, and for the second, we have n-3 choices.

Note that this is equivalent to 

(n-2)! / (n-4)!

4. Continuing the logic used above, calculate the number of paths of length  from A to B, where 
1 <= m <= (n-1), 
and write this number as a ratio of factorials.

To indicate a factorial, please enter fact(n) to mean n!; fact(n+2) to mean (n+2)!, etc.

The 'logic above' from the last part of the problem
Click to see the solution for the previous problem, if you want some guidence on how to think about this problem part

fact(n-2)/fact(n-m-1)
  correct  fact(n - 2)/fact(n - m - 1)
 
Explanation:

Answer: 
Following the previous problems, it is clear that in choosing our first node between A and B, we have  (n-2) choices. Similarly, in choosing the second, we have (n-3) choices.

In fact, in choosing the jth node, we have (n-j-1) choices. Taking the product from j = 1 to m - 1 (since m - 1 nodes exist between A and B in a path of length m), we get (n-2)! / (n-m-1)!

5. Using the fact that for any n, , where  is some constant, determine the asymptotic bound on the number of paths explored by DFS. For simplicity, write  as just n,  as n^2, etc.


n^n
  **incorrect**  fact(n - 2)
 
我懂了这个，只是没有敢这么写。
 
Explanation:

Answer: 
Note that DFS will traverse every path from A to B. To calculate the number of paths, we must sum the paths of every length (from 1 to ). This sum can be written as:

This is equal to .

Since , which is a constant, the number of paths is .

---
## Exercise 6
3/5 points (graded)

In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with  nodes as KN. Answer the following questions in terms of .

1. What is the asymptotic worst-case runtime of a Breadth First Search on KN? For simplicity, write  as just n,  as n^2, etc.


n
  correct  n
 
Explanation:

Answer: 
BFS begins by checking all the paths of length 1. In its worst case, it must check the paths to every node from the source to find the destination. This is at most, n checks.

2. BFS will always run faster than DFS.


True
False correct
Explanation:

Consider a graph of two nodes, A and B, connected by an edge. You wish to search for a path from A to B. As there is exactly one edge in the graph, and exactly one path from A to B, both run in an equal number of steps.

3. If a BFS and DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as DFS when run on two nodes in KN.


True correct
False
Explanation:

As seen in our previous problems in this lecture sequence, BFS checks at most n paths in KN, and DFS always checks O((n-2)!) paths. If given the same node prioritization, both will first find the desired node in the same number of steps.

同样的步数？对KN来说的？

非最短路径的DFS是在找什么？找到那里的路径！

4. If a BFS and Shortest Path DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as Shortest Path DFS when run on two nodes in any connected unweighted graph.


True correct
False **incorrect**
Explanation:

While Shortest Path DFS may find the desired node first in this case, it still must explore all other paths before it has determined which path is the fastest. BFS will explore only a fraction of the paths.

5. Regardless of node priority, BFS will always run at least as fast as Shortest Path DFS on two nodes in any connected unweighted graph.


True correct
False **incorrect**
Explanation:

Shortest Path DFS must always explore every path from the source to the destination to ensure that it has found the shortest path. Once BFS has found a path, it knows that it is the shortest, and does not have to explore any other paths.

---
## Exercise 7
10/10 points (graded)

1. Consider once again our permutations of students in a line. Recall the nodes in the graph represent permutations, and that the edges represent swaps of adjacent students. We want to design a weighted graph, weighting edges higher for moves that are harder to make. Which of these could be easily implemented by simply assigning weights to the edges already in the graph?


A) A large student who is difficult to move around in line. correct
B) A sticky spot on the floor which is difficult to move onto and off of. correct
C) A student who resists movement to the back of the line, but accepts movement toward the front.
correct
Explanation:

Answer: A, B

A) is easily implemented by weighting heavily all edges that involve moving the particular student.

B) is implemented by increasing the weight of all edges that involve a swap with that spot in line.

> C) cannot be done without weighting two directions of an edge differently. In this case, putting one student behind another is not the same as putting the first student in front of the other, but in our undirected graph, it is.

2. Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, as well as the parameters from Edge. You should additionally include a getWeight method. The string value of a WeightedEdge from node A to B with a weight of 3 should be "A->B (3)".

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        pass
    def getWeight(self):
        # Your code here
        pass
    def __str__(self):
        # Your code here
        pass
Code Editor


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.getSource().getName() + "->" + self.getDestination().getName() + " (" + str(self.getWeight()) + ")"
        
---

## Lab: Graphs

Info
In this lab, we will be visualizing distances in a graph.

Dijkstra's algorithm is a general method to find the shortest distances from a node to all other nodes in a graph. We provide a Javascript implementation of the algorithm below. Initially we set the connection probability to 0.67; that is, any possible connection in the graph has a 2/3 chance of appearing. The graph is interactive; you can add new edges by clicking and dragging from one node to another (note that you can only add edges between neighbors). You can also remove connections by clicking on them. If you click on a node, the distance will be color-coded into all the nodes; an "infinite" distance (i.e. nodes that are impossible to reach) will be shown as bright blue, and the source node itself (distance 0) will be bright red.

Try to play around with the graph. What kind of an edge would make the highest impact on distances? Try to create interesting scenarios by setting the connection probability to 0, and creating a graph from scratch.

[Lab: Graphs](https://courses.edx.org/courses/course-v1:MITx+6.00.2x+3T2017/courseware/8d9a47872ed641a1ace050f1c1ba7ac7/67dad053e2b74dd1825aaeb6c8476a34/7)



