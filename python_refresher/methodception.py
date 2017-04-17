def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print(methodception(add_two_numbers))

print(methodception(lambda: 35 + 77))

print((lambda x: x * 3)(5))

my_list = [13, 56, 77, 485]
print(list(filter(lambda x: x != 13, my_list)))

print([x for x in my_list if x != 13])
