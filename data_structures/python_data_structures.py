
# Liner Data Structures
# These are the data structures which store the data elements in a sequential manner.
#
# Array: It is a sequential arrangement of data elements paired with the index of the data element.
# Linked List: Each data element contains a link to another element along with the data present in it.
# Stack: It is a data structure which follows only to specific order of operation. LIFO(last in First Out) or FILO(First in Last Out).
# Queue: It is similar to Stack but the order of operation is only FIFO(First In First Out).
# Matrix: It is two dimensional data structure in which the data element is referred by a pair of indices.


# Non-Liner Data Structures
# These are the data structures in which there is no sequential linking of data elements. Any pair or group of data elements can be linked to each other and can be accessed without a strict sequence.
#
# Binary Tree: It is a data structure where each data element can be connected to maximum two other data elements and it starts with a root node.
# Heap: It is a special case of Tree data structure where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes.
# Hash Table: It is a data structure which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element.
# Graph: .It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.

# Python Specific Data Structures
# These data structures are specific to python language and they give greater flexibility in storing different types of data and faster processing in python environment.
#
# List: It is similar to array with the exception that the data elements can be of different data types. You can have both numeric and string data in a python list.
# Tuple: Tuples are similar to lists but they are immutable which means the values in a tuple cannot be modified they can only be read.
# Dictionary: The dictionary contains Key-value pairs as its data elements.




# ARRAYS

# typecode
# b	Represents signed integer of size 1 byte/td>
# B	Represents unsigned integer of size 1 byte
# c	Represents character of size 1 byte
# i	Represents signed integer of size 2 bytes
# I	Represents unsigned integer of size 2 bytes
# f	Represents floating point of size 4 bytes
# d	Represents floating point of size 8 bytes

from array import *
array1 = array('i', [10,20,30,40,50])

# access array elements
array1[0]

# insertion operation
array1.insert(1,60)

# deletion operation
array1.remove(40)

# search operation
array1.idex(40)

# update operation
array1[2] = 80

# Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

