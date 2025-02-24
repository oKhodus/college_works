class Vector:
    def __init__(self, x_val, y_val):
        """Initialize coordinates for vector x and y

        Args:
            x_val (int): coordinate x of vector
            y_val (int): coordinate y of vector
        """
        self.x = x_val
        self.y = y_val
        self.s = None

    def __add__(self, v2:tuple):
        """Summary of coordinates: (x1+x2, y1+y2)

        Args:
            v2 (tuple): second vector which will be summed with first

        Returns:
            tuple: summed vector
        """
        return Vector(self.x + v2.x, self.y + v2.y)

    def scalar(self, v2:tuple):
        """ Implementation of scalar multiplying

        Args:
            v2 (tuple): second vector - from which will be used coordinates (x, y) in formula

        Returns:
            int: final value of scalar multiplying
        """
        self.s = v1.x * v2.x + v1.y * v2.y
        return self.s

    def __str__(self):
        """Returning of string

        Returns:
            str: final result of calculation
        """
        if self.s is not None:
            return f"Output (scalar): {self.s}\n"
        else:
            return f"Output: ({self.x}, {self.y})\n"
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
print(v3)

v4 = Vector(-1, 7) + Vector(3, -2)
print(v4)

v5 = v1.scalar(v2)

print(v1)