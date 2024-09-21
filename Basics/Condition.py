
# x = 0
# y = 89

# if x > y:
#     print('x is small')
# else:
#     print('y is small')



# Looping

arr = [12,23,34,21,23,12]
for i in arr:
    print(i, end=' ')

print()
# for DIC


d = {"name":"akash", "age":21, "salary":70}
for key in d:
    print(key, end=" ")
    
print()

# print(d['name']) # This willl print the value of presner at key

for key in d:
    print(d[key], end=" ")

print()

for val in d.values():
    print(val, end=" ")

print()

# packing and unpacking

data = [ (34,45), (56,67), (56,67)]
for i, j in data:
    print(i, j)

print()

# dict.items() method returns the array of key value pare as a tupal

print(d.items())

# Range function

for i in (0,1,2,3,4,5):
    print(i, end=' ')

for i in range(0, 10):
    print(i, end=' ')

print()

val = range(1, 10)
print(type(val))

print('\n', list(val))
print('\n', tuple(val))
print('\n', str(val))

print(list(range(10, 110, 10)))

print( tuple( range(-10, 11, 2)))


# break and continue statement

for i in range(0, 11):
    if i != 9:
        print(i, end=' ')
        continue
    print("Break is going to called!")
    break
print("End Code")


# for else block

for i in ['a', 'b', 'c', 'd']:
    if i=='e':
        break
    print(i, end=' ')
else:
    print("Complete loop runs sucessfully")





### iterables
# object that can return its elements one at a time

my_list = [12,"aks", '89', 78.98]
for i in my_list:
    print(i, end=' ')

print()
# we can create the iterable - list , tuple, dict, str

my_list1 = iter(my_list)

print(next(my_list1))
print(next(my_list1))
print(next(my_list1))
print(next(my_list1))



# Example making the itrable

num = [1,2,3,4,5]

print(type(num))

# my_itrable = iter(num)
# print(type(my_itrable))

# print(next(num))

print(len(num))

num = ["a","b","C","D","r"]

for i in range( len(num) ):
    print(num[i], end=' ')



