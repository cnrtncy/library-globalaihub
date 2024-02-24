from time import perf_counter

""" Created this method before I started the project in case I need to monitor the performance of the application. (Not all perf metrics.)"""


def perf_monitor(func):

    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} executed in {end - start:.5f} seconds")
        return result

    return wrapper
