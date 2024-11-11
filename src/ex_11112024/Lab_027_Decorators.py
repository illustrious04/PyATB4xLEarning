# Real tim example with Time decorator.
import time
from queue import PriorityQueue


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(f"Time Taken by function {end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui_1():
    print("Time Taken by this function")
    time.sleep(2)


print("Ui test 2 will start")
@time_decorator
def test_ui_2():
    print("This UI will take 5 sec")
    time.sleep(5)