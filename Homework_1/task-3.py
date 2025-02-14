import time
import random

def decorator_1(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        elapsed_time = finish - begin
        print(f"{func.__name__} call executed in {elapsed_time:.4f} sec")
        return result
    return wrapper


@decorator_1
def task_one():
    print("Starting task one...")
    output = 0
    limit = random.randint(20, 500)
    for i in range(limit):
        output += (i ** 2)

@decorator_1
def task_two(x=3, y=8):
    print("Executing complex operation...")
    highest = float('-inf')
    count = random.randint(50, 900)
    calculations = [i ** 2 for i in range(count)]
    for num in calculations:
        if num > highest:
            highest = num

task_one()
task_two()
task_one()
task_two()
task_one()