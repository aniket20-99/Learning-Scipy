# Working with graphs:we have a module names scipy.sparse.csgraph
# adjacency matrix: nxn matrix where n is the number of element in the graph. 
# Connected Components:
 
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
arr = np.array([[0,1,2],[1,0,0],[2,0,0]])
arr_new = csr_matrix(arr)
print(connected_components(arr_new))

# Dijkstra method: Its uses to show the shortest path in a graph from one element to another element. 
# I takes 3 arguments: 1--> return_predecessors(It return value in boolean), 2--> indices(Shows the path between the elements), 3 --> limit(max weight of path)
# FInding Shortest path from element 1 to 2

import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
arr = np.array([[0,1,2],[1,0,0],[2,0,0]])
arr_new = csr_matrix(arr)
print(dijkstra(arr_new,return_predecessors=True,indices=0))

# Floyd Warshall() Method: It is use for finding shortest path between all the pairs of elements. 

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
arr = np.array([[0,1,2],[1,0,0],[2,0,0]])
arr_new = csr_matrix(arr)
print(floyd_warshall(arr_new,return_predecessors=True))

# Bellman_ford() method: Its also used to find the shortest path between the pairs of element but it can also handle negative weight as well. 
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
arr = np.array([[0,-1,-2],[1,0,0],[2,0,0]])
arr_new = csr_matrix(arr)
print(bellman_ford(arr_new,return_predecessors=True,indices= 0))

# depth_first_order() method: It returns depth first traversal from a node:It has two arguments 1--> graphs, 2--> starting element

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
arr  = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
arr_new = csr_matrix(arr)
print(depth_first_order(arr_new,1))

# breadth_first_order() Method: It returns breadth first  from a node:It has two arguments 1--> graphs, 2--> starting element
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
arr  = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
arr_new = csr_matrix(arr)
print(breadth_first_order(arr_new,1)) 
