#### Graph Introduction 
#       Relation are initi and nodes 
#       1. no self-loops   
#       2. Muliedge - 
#
####   Where do the graph come from?  - social network/computer network/ecologial relationwork/electricl circuite
#            traversal problems /find the spinning trees/flow ....etc.
#       1. Adjacency  matrix   
#       2. Adjacency list representation  -!!!!!!!!!!!!!!!!!!!!! - Adjacency List Representation 
#       3. Incidcence representation 


#  Vertic/node  -------- the connection between the node  ''' edge''''
#  graph []e.g. the sereve is the node, the link is the edge
#               google map  ------ street, ----- edge  



#### How to represent the graph on the computer
#       1. adjacency matrix  --- graph is define by the matrix, vertices is from the rows and column [n_ij] is representh the edge
#           k nodes will have the k(k-1) edge, e.g., many of the matrix store the (0,0) 
#       2. adjacency list representive --------every node points  to list of the neighbors  ---- adjacency node  ( thus there is not storage the 0.0)
#           |k| + |m|  is the size of the adjacency list representative
#       3. incidence matrix representive
#

####    Traversals -- Operation ofhe the graph
#       operation of the graph  - traversal will visit all the node in the graph in some order, CAN ONLY visit a node once!
#       A. visit node only once 
#       B. violate a new node, ist must be along the edge starting from the nodes already visited

#       Google ----  crawing the web  ---- html is graph --- link take the link the new edge
#              

####    Breadth First Search ---BFS
#       FIFO --- staring the 1 node, visiting the each node, if visited, queue data structure, define the behaivor of the data structure; 
#       ----BFS --- define the seraching queue --- pi parent, d is the depth of hte node; ----visited true/false

#   def bfs(G,s)
#    Q  {s} -  {contain the starting node}
#    s.d  = 0 (depth is 0 initial)
#    s.seen = True
#    s.parent = pi
#    Q != 0
#    u = dequeue(Q)
#    for all u <= adj(u, G) 
#       if (!v.seen): 
#           v.d = u.d + 1
#           v.pi = u
#           v.seen = true
#           dequeue(u,Q)

####    DFS  - Depth First search 

#   def(dfs) Graph G, node u, 
#       Global time =1 
#       v {pi: parent;   d:= discovery time; f:= finish time}
#       seen := false 
#       book keeping 
#       if (v.seen) :  RETURN
#       for all v <= adj(u) 
#           if (no v.seen)
#               v.pi := u
#               v.d := time 
#               time = time +1
#               dfsvisit(G,v)
#               v.seen = TURE
#
##  dfs its creat a DFS tree after the serach

##      Property of DFS - outer loop: for i = 1 to n, n is the number of the nodes dfsvisit (G,i)

#  Back edge / forward edge / craoss edge 
#  no direction of the graph, is a forest, technical is no connected
#   Back edge is ancentad in a tree
#   if there is a back edge there will be a circle
#   

####     Topological Sort -----Directed Acyclic Graph
##       1. running the DFS firstly, 
#        2. sort the nodes in descending order according to the finishing time
#        
#   
#    