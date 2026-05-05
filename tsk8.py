from datetime import datetime

def log_exceptions(log_file="errors.log"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} - {type(e).__name__}: {str(e)}\n")
                raise
        return wrapper
    return decorator

@log_exceptions()
def divide(a, b):
    return a / b

@log_exceptions()
def get_element(lst, idx):
    return lst[idx]

def main():
    print(divide(8, 0))

if __name__ == '__main__':
    main()
