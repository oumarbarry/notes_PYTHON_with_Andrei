from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1=time()
        execution = fn(*args, **kwargs)
        t2=time()
        print(f'took {t2-t1} s')
        return execution
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()