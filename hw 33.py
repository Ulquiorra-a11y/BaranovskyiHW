import time
from functools import wraps

def measure_time(repits):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None
            for _ in range(repits):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total_time += (end - start)
            avg_time = total_time / repits
            print(f"Среднее время выполнения для {repits} вызовов: {avg_time} секунд")
            print(f"Результат: {result}")
            return result
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()