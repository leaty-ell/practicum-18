import json

def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False)
    return wrapper

@to_json
def get_person(name, age, city):
    return {"name": name, "age": age, "city": city}

@to_json
def get_numbers_list(a, b, c):
    return [a, b, c]

@to_json
def get_tuple_data(x, y):
    return (x, y, x + y)

def main():
    """
    Main function to demonstrate to_json decorator.
    """
    name = input()
    age = int(input())
    city = input()
    print(get_person(name, age, city))
    
    a = int(input())
    b = int(input())
    c = int(input())
    print(get_numbers_list(a, b, c))
    
    x = int(input())
    y = int(input())
    print(get_tuple_data(x, y))

if __name__ == '__main__':
    main()
