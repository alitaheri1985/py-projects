# definition of sets in python:
# A set is an unordered collection of unique elements. It is defined using curly braces {} or the built-in set() function. Sets are mutable,
# meaning you can add or remove elements from them. They support various operations such as union, intersection, difference, and symmetric difference.
# Sets are commonly used for membership testing, eliminating duplicate entries, and performing mathematical set operations.
# This code demonstrates the usage of sets in Python, including creation, modification, and various set operations such as union, intersection, difference,
# and symmetric difference. It also checks for membership and subset/superset relationships between two sets.

set1 = {1,2,3,4,4,10,3,55,1,5,6,7,8,9,10}
print ("======================= create set1 ============================")
print (set1)

set1.add(11)
print ("======================= add 11 to set1 ============================")
print (set1)

set2 = set(["sd","sdff","sdf",11,3,"sdytuyf","trf","sdj"])
print ("======================= create set2 ============================")
print (set2)

print ("======================= union of set1 and set2 ============================")  
print (set2 | set1)

print ("======================= intersection of set1 and set2 ============================")
print (set2 & set1)

print ("======================= difference of set1 and set2 ============================")
print (set1 - set2)

print ("======================= symmetric difference of set1 and set2 ============================")
print (set2 ^ set1)

print ("======================= check if 3 in set1 and set2 ============================")
print ("3 in set1: ", 55 in set1)
print ("3 in set2: ", 55 in set2)

print ("======================= check if set1 is subset of set2 ============================")
print (set1.issubset(set2))

print ("======================= check if set1 is superset of set2 ============================")
print (set1.issuperset(set2))

print ("======================= check if set1 and set2 are disjoint ============================")
joined_set = set1 | set2
print (joined_set)
print (set1.isdisjoint(set2))

print ("======================= remove 3 from set1 ============================")
set1.remove(3)
print (set1)

print ("======================= remove sdff from set2 ============================")
set2.remove("sdff")
print (set2)