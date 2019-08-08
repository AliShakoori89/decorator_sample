# def say_hello(name):
#     return f"Hello {name}"


# def say_bye(name):
#     return f"bye {name}"


# def speak (func):
#     return func('hesam')

# print()
# print(speak(say_bye))

############################

# def parent():
#     print('do something in parent')

#     def first_child():
#         print('do someting in first child')

#     def seconf_child():
#         print('do someting in seconf child')

#     first_child()
#     seconf_child()

# parent()


###########################

# def my_decratore(func):
#     def wrapper():
#         print('do someting one')
#         func()
#         print('do someting tow')

#     return wrapper

# @my_decratore
# def say_hello():
#     print('helooooooooooooooo')

# say_hello()

###################################

# def do_twice(func):
#     def wrapper(*args , **kwargs):
#         func(*args , **kwargs)
#         func(*args , **kwargs)
#     return wrapper

# @do_twice
# def say_hello(name):
#     print(f"heloooooo{name}")

# say_hello('hesam')

############################################

# def percent (func):
#     def inner(*args,**kwargs):
#         print('%' * 30)
#         func(*args,**kwargs)
#         print('%' * 30)
#     return inner

# def star(func):
#     def inner(*args,**kwargs):
#         print('*' * 30)
#         func(*args,**kwargs)
#         print('*' * 30)
#     return inner



# @star
# @percent
# def printer(msg):
#     print(msg)

# printer('Ali shakoori')

############################
def repeat(num_times):
    def decrator_repeat(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                value=func(*args,**kwargs)
            return value              
        return wrapper
    return decrator_repeat

@repeat(3)
def printer(msg):
    print(msg)

printer('hello ali')
