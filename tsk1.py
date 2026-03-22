class Dog:
    def __init__(self, name):
        """Initialize the dog with a name"""
        self.name = name
    
    def __str__(self):
        """Return the dog's name when printed"""
        return self.name
    
    def say(self):
        """Make the dog bark"""
        print("Гав!")


def main():
    """The main fuction of the programm"""
    dog_name = input("Введите кличку собаки: ")
    small_dog = Dog(dog_name)
    small_dog.say()
    print('Кличка собаки', small_dog.name)


if __name__ == "__main__":
    main()
