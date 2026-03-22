class Point:
    """
    A class representing a point on a plane.

    Attributes:
        x (int/float): The x-coordinate of the point.
        y (int/float): The y-coordinate of the point.
    """
    
    def __init__(self, coordinates=(0, 0)):
        """Initialize a new Point object."""
        self.x = coordinates[0]
        self.y = coordinates[1]  
    
    def get_x(self):
        """Return the x-coordinate of the point."""
        return self.x
    
    def get_y(self):
        """Return the y-coordinate of the point."""
        return self.y
    
    def distance(self, other):
        """Calculate the Euclidean distance between this point and another point."""
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx**2 + dy**2) ** 0.5
        
        return distance
    
    def sum(self, other):
        """Create a new point that is the sum of this point and another point."""
        new_x = self.x + other.x
        new_y = self.y + other.y
        
        return Point((new_x, new_y))
    
    def __str__(self):
        """
        Return a string representation of the Point object. The format is "(x; y)".
        
        Returns:
            str: A formatted string with the point coordinates.
        """
        return "({}; {})".format(self.x, self.y)
    
    def __repr__(self):
        """
        Return a string representation for debugging.

        Returns:
            str: A formatted string with the point coordinates.
        """
        return "({}; {})".format(self.x, self.y)


def main():
    """The main function of the program."""

    p = Point((3, -7))
    print(p)  
    
    a = Point()
    print(a)         
    print(a.get_x()) 
    print(p.get_y())  
    c = Point((-2, 4))
    print(p.distance(c)) 
    d = c.sum(p)
    print(d)  

if __name__ == "__main__":
    main()
