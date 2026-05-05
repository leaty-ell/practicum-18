import time
import functools

class TimeLimitExceeded(Exception):
    pass

class CallLimitExceeded(Exception):
    pass


def limit(max_time=6, max_calls=4, period=11):
    def decorator(function):
        calls = []
        
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            calls[:] = [t for t in calls if current_time - t < period]
            
            if len(calls) >= max_calls:
                raise CallLimitExceeded(f"Превышен лимит вызовов: {max_calls} за {period}с")
            
            start = time.time()
            result = function(*args, **kwargs)
            elapsed = time.time() - start
            
            if elapsed > max_time:
                raise TimeLimitExceeded(f"Превышено время выполнения: {elapsed:.2f}с > {max_time}с")
            
            calls.append(current_time)
            return result
        return wrapper
    return decorator


@limit(max_time=3, max_calls=3, period=6)
def slow_function(n):
    time.sleep(n)
    return n * 2


def main():
    try:
        print(slow_function(1))
        print(slow_function(1))
        print(slow_function(1))
    except CallLimitExceeded as e:
        print(f"Ошибка: {e}")
    except TimeLimitExceeded as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()
