sample_set={1,3,2,4,6,6,8,9}
print(sample_set)
if 10 in sample_set:
    print("yes 10 is in the set")
else:
    print("no 10 is not in the set")
sample_set.add(11)
#add is used to add things obvsiouly
sample_set.add(True)
print(sample_set)
sample_set.discard(50)
#discard wont throw any error unless the element is there
print(sample_set)
sample_set.remove(2)
print(sample_set)

#union
set1={1,3,5,6,7,5}
set2={2,5,2,5,6,7,8,10}
#join the elements
print(set1|set2)
#| is used to get the union
print(set1.union(set2))
#either way

#intersection
print(set1.intersection(set2))
print(set1&set2)
#any way

#difference
print(set1.difference(set2))
print(set1-set2)

#symetric difference
print(set1.symmetric_difference(set2))
print(set1^set2)

set1.intersection_update(set2)
print(set1)