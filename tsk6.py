def print_result(func):
    def wrapper(arg):
        result = func(arg)
        print(result)
        return result
    return wrapper

@print_result
def square(x):
    return x * x

@print_result
def reverse_string(s):
    return s[::-1]

@print_result
def is_even(n):
    return n % 2 == 0

def main():
    """
    Main function to demonstrate decorator functionality.
    """
    a = int(input())
    square(a)
    
    b = input()
    reverse_string(b)
    
    c = int(input())
    is_even(c)

if __name__ == '__main__':
    main()
