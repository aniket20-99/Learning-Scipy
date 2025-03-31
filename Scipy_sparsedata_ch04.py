# Sparse Data:- Data that has mostly unused elements.like the elements that dont carry any information.[1,2,3,4,0,6,8,0,2,3,6]
# Data which has the maximum number of zero into it is called sparse data. 
# Example (Sparse data):- [1,0,2,0,0,3,0,0,0,0,4]
# Dense Array: [2,5,6,8,9,1,2,3,5] having atleast some information. 
# while scientific calculation formula will only if there is a non zero number thats why data is taken in ML which doesnt have any sparse data. 

# How to work with Sparse Data. 
# Scipy has a module name scipy.sparse 
# There are two types of matrics in sparse data. 1 --> Compressed Sparse Column(CSC) 2 --> Compressed Sparse Row(CSR)

# CSR Matrics: Here we will create a CSR matrics from an array. 
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

#Sparse matrix Methods
import numpy as np
from scipy.sparse import csr_matrix
arr1 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr1).data)

# What if we want to count nonzeros, we can do this via count_nonzero() methods. 
import numpy as np
from scipy.sparse import csr_matrix
arr1 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr1).count_nonzero())

# For removing the zeros elements from the matrix we will use eliminate_zeros(). 
import numpy as np
from scipy.sparse import csr_matrix
arr1 = np.array([[0,0,0],[0,0,1],[1,0,2]])
arr_new = csr_matrix(arr1)
arr_new.eliminate_zeros()
print(arr_new)

# Eliminating duplicate entries with the sum_duplicates() method:

import numpy as numpy
from scipy.sparse import csr_matrix

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
arr_new = csr_matrix(arr)
arr_new.sum_duplicates()
print(arr_new)

# Conversion from CSR to CSC with the tocsc():
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
arr_new = csr_matrix(arr).tocsc()
print(arr_new)
