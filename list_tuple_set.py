grades_list = [77, 80, 90]  # ordered and mutable
grades_tuple = (77, 80, 90) # immutable
grades_set = {77, 80, 90}   # unique and unordered

# despite tuples being immutable, you can create a new tuple out of two individual tuples
extend_tuple = grades_tuple + (100,) # need comma for it to be a tuple, otherwise just an int
print(type(extend_tuple))
print(grades_tuple)
print(extend_tuple)

# can add to a set but duplicate values will be ignored
grades_set.add(60)
grades_set.add(60)
print(grades_set)

# advanced set operations
# we only care about the content of the set, not the order
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9, 11}

set_intersection = set1.intersection(set2)  # intersection will print only values that exist in both sets
print(set_intersection)

set_union = set1.union(set2)    # union will return only unique values
print(set_union)

set_difference = set1.difference(set2)  # difference is the values that are unique to each set 
print(set_difference)
