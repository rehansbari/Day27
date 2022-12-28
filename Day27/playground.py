#This function tells Python that it can accept any number of arguments due to the *args
#This demonstrates unlimited positional arguements
# *args acts as a tuple where we can refer to objects by index like an array
def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum
#kwargs acts more like a dictionary where we can access objects by index
def calculate(n, **kwargs):
    print(kwargs)

#Can pass any number of values and function will add them all up
print(add(1, 2, 3, 4))

calculate(2, add=3, multiply=5)