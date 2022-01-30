# example 

# f(x) = x + 3 -> f(1) = 4 

def add(x):
    return x+3
    # return None if you do not put a return function 
# Call function // invoke a function 

result = add(1)

print(type(result)) #


# example


# f(x) = x + 3 -> f(1) = 4 

# def add(x):
#     r1 = x+3
#     r2 = x-100
#     return r1, r2
    # return None if you do not put a return function # function only take in one paramater, both pass 2 add(1,2), is going to break TypeError: add() missing 1 requried positional argument: 'x'
# Call function // invoke a function 

# result = add(1,2)

# print(result[0])
# print(result[1])

# print(result)

# example


# f(x) = x + 3 -> f(1) = 4 

def add(x):
    for i in range(0,10):
        print(i)
        if i == 4:
            # break -> stops the loop does NOT exit function
            return i # -> stops the Loops and DOES exit the function
    return x+3

int

# input -> string 

    # return None if you do not put a return function # function only take in one paramater, both pass 2 add(1,2), is going to break TypeError: add() missing 1 requried positional argument: 'x'
# Call function // invoke a function 

result = add(1)

print(type(result))

# example

def search(person):
    for student in ['serge', 'brain', 'paul', 'leo']:
        if student == person:
            # break -> stops the loop does NOT exit function
            return student

    return 'Student not found!'

# Call function // invoke a function 

result = search('asdf')

print(type(result))

# example

def search(person):
    for student in ['serge', 'brain', 'paul', 'leo']:
        if student == person:
            # break -> stops the loop does NOT exit function
            break # student

    return 'Student not found!'

# Call function // invoke a function 

result = search('asdf')

print(type(result))

# example

def search(person):
    age = int(input('How old are you?'))
    print(age)
    for student in ['serge', 'brain', 'paul', 'leo']:
        if student == person:
            # break -> stops the loop does NOT exit function
            break # student

    return 'Student not found!'

# Call function // invoke a function 

result = search('asdf')

print(type(result))

# example

def search(person):
    age = float(input('How old are you?'))
    print(age)
    for student in ['serge', 'brain', 'paul', 'leo']:
        if student == person:
            # break -> stops the loop does NOT exit function
            break # student

    return 'Student not found!'

# Call function // invoke a function 

result = search('asdf')

print(type(result))

# teacher example
def double(num):
    return num

def double_list_values():

    li = [5, 10, 11, 23, 81, 74]

    doubled = list(map(lambda x: x*2, li))
    print(doubled)

double_list_values()





