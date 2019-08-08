import time

def timing_function(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + " seconds"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10**7)):
        num_list.append(num)

@timing_function
def my_function_1():
	num_list = [num for num in range(0, 10**7)]

print(my_function())
print(my_function_1())