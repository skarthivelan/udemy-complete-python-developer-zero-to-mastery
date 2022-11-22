my_list =[5,4,3]

print(list(map(lambda item: item*item, my_list)))

some_list=['a','b','c','d','b','m','n','n']

duplicates = [item for item in sorted(some_list) if (item)]

print(duplicates)