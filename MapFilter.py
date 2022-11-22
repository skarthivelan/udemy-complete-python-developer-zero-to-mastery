from functools import reduce

def cap(item):
    return item.capitalize()

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(cap,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, my_numbers[::-1])))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def cutoff(item):
    return item>50

print(list(filter(cutoff,scores)))

def acc(a, item):
    return a+item
#4 Comine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print((reduce(acc,my_numbers+scores,0)))

print(sorted(my_numbers+scores))