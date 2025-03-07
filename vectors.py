import math

class Vector:
    def __init__(self, x, y, z=0):

        """Initialize a 2D or 3D vector."""
        self.x = x
        self.y = y
        self.z = z  # Defaults to 0 for 2D vectors

    def __add__(self, other):
        """Vector addition: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Vector subtraction: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, scalar):
        """Scalar multiplication: v * k"""
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        """Scalar division: v / k"""

        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)


    def dot(self, other):
        """Dot product: v1 · v2"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):

        """Cross product (only meaningful for 3D vectors)"""
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):

        """Returns the vector magnitude (length)"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):

        """Returns a unit vector (same direction, magnitude = 1)"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)  # Return a zero vector
        return self / mag

    def angle_between(self, other):
        """Returns the angle (in radians) between two vectors"""
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        if magnitudes == 0:
            return 0
        return math.acos(dot_product / magnitudes)

    def rotate_2D(self, angle):
        """Rotates a 2D vector by an angle in degrees"""

        rad = math.radians(angle)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)

    def __repr__(self):

        return f"Vector({self.x}, {self.y}, {self.z})"
