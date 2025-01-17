# lambdas
sample = lambda x : x*3/2

print(sample(2))

# lambdas with map

numbers = [1, 2, 3, 4, 5]

fractions = lambda x : x*3/2

sample = list(map(fractions,numbers))

print(sample)


# lamdas with sorted

# imagine list of tuples
students = [
    ('Alice', 25, 90),
    ('Bob', 21, 85),
    ('Charlie', 24, 92),
    ('David', 22, 88)
]
sorted_list = sorted(students, key=lambda x:x[1])

print(sorted_list)

#### list comprehensions
squares = [x*x for x in range(10)]

even_squares = [x*x for x in range(10) if x%2==0]

print(even_squares)

#Nested list comprehensions
my_list = [(x,y) for x in range(10) for y in range(x+1,10)]
print(my_list)

# with function call
strings = ['apple', 'banana', 'cherry']
sizes = [ len(item) for item in strings]
print(sizes)

# slicing

l1 = [2, 3, 4, 5, 6, 3, 1]

# by last element index
print(l1[:-1])
# output
[2, 3, 4, 5, 6, 3]

# by first element and last element index
print(l1[4:-1])
# output
[6, 3]

# by first element, end element open and start element open and end element

print(l1[3::-1])
#[5, 4, 3, 2]

print(l1[3:2:-1])
#[5]
