class NotSleeping:
    """
     A class representing a person who cannot sleep and counts sheep.
    This class keeps track of a person's name and the number of sheep they have counted
    while trying to fall asleep. The person can lose count and start over.
    
    Attributes:
        name (str): The name of the person.
        count_sheeps (int): The number of sheep counted.
    """
    
    def __init__(self, name, count_sheeps=0):
        """Initialize a new NotSleeping object."""
        self.name = name
        self.count_sheeps = count_sheeps
    
    def add_sheep(self):
        """Add one sheep to the count."""
        self.count_sheeps += 1
    
    def lost(self):
        """Reset the sheep counter."""
        self.count_sheeps = 0
    
    def get_count_sheeps(self):
        """Return the current number of counted sheep."""
        return self.count_sheeps


def main():
    """The main function of the program."""
    human = NotSleeping('Мистер Смит')
    
    human.add_sheep()  
    human.add_sheep() 
    human.add_sheep()  
    human.add_sheep() 
    human.add_sheep()  
    
    print(human.name, 'насчитал', human.count_sheeps, 'овец')
    
    human.lost()
   
    human.add_sheep()  
    human.add_sheep() 
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep() 
    
    print(human.name, 'насчитал', human.get_count_sheeps(), 'овец')


if __name__ == "__main__":
    main()
