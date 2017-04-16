grades_list = [77, 80, 90]
grades_tuple = (77, 80, 90) #immutable
grades_set = {77, 80, 90}   #unique and unordered

# despite tuples being immutable, you can create a new tuple out of two individual tuples
extend_tuple = grades_tuple + (100,) #need comma for it to be a tuple, otherwise just an int
print(type(extend_tuple))
print(grades_tuple)
print(extend_tuple)
