import time


def calc_time(func):
    def wrapper(*args):
        print("xargs:", *args)
        t1 = time.time()
        func(*args)
        t2 = time.time()
        print(t2 - t1)
        return t2 - t1
    return wrapper


@calc_time
def test_demo(num):
    print(num)


test_demo(123)