# generators

def counter(ticks):
    for i in range(ticks):
        yield i*2
        i=i+1

sample_gen = counter(5)

for i in sample_gen:
    result = i*5
    print(result)


# another way of creating generator is

my_squares = (x*x for x in range(10))

for num in my_squares:
    print(num)

some = (1,2,4,5)

for num in some:
    print(num)


# decorators

def sample(func):
    def wrapper(*args,**kwargs):
        param1 = args[0]
        if isinstance(param1, int):
            print("arg is a valid integer")
            result = func(*args,**kwargs)
            return result
        else:
            print(f"arg must be a valid integer, you have provided : {args[0]}")
    return wrapper
@sample    
def get_customer_details(id):
    print(f"id of customer is :{id}")
    

get_customer_details(6)