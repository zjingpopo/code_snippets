from functools import wraps
import traceback

# function decorators

def dec_example(func):

	@wraps(func) # let wrapper function have func's metadata
	def wrapper(*args, **kwargs): # let wrapper function take func's arguments
		print('I am the wrapper function')

		return func(*args, **kwargs)

	return wrapper

def another_dec(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		print('I am another wrapper')

		return func(*args, **kwargs)

	return wrapper

@dec_example
@another_dec
def multiply(a, b):
	print('I am the function to be decorated')
	return a * b
'''
print(multiply(1,2))
print('----------')
print(multiply(3,2))
'''

def dec_with_args(*dec_args, **dec_kwargs):

	print('pre')
	def decorator(func):
		print('*dec_arg:', dec_args)
		print('**dec_kwargs:', dec_kwargs)

		def wrapper(*args, **kwargs):
			print("inner")
			return func(*args, **kwargs)
		return wrapper


	print('post')
	return decorator

@dec_with_args(1, 2, mad = 2, bad = 3)
def add(a, b):
	print('In add')
	return a + b

'''
print(add(2,3))
print(add(3,5))
'''

def get_args(func):

	def decorator(*args, **kwargs):
		print('in decorator')

		def inner_wrap():
			print('in inner_wrap')
			return func(*args, **kwargs)

		return inner_wrap

	return decorator

@get_args
def plus(a, b):
	print('in plus', plus.__name__)
	return a + b

# using decorator to pass a function that takes arguments to a function
# only takes one function name as argument
def run_func(func):
	return func()

'''
print(run_func(plus(1, 2)))
'''

# class decorators
class class_dec_example():
	pass

class another_class_dec():
	pass