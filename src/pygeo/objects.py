import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            return np.dot(self._vector, other._vector)
        elif isinstance(other, float) or isinstance(other, int):
            return Vector(self._vector* other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""
    def __init__(self,origin,direction):
        if origin != direction:
            self.origin = origin
            self.direction = direction
            self.difference = self.origin-self.direction
    def __repr__(self):
        return f"Ray{self.origin,self.direction}"
    def __eq__(self,other):
        if isinstance(other,Ray):
            return (np.array_equal(other.origin,self.origin) and np.array_equal(other.direction,self.direction))
        return False

#pt = Ray(Point((0,1,2)), Point((1,2,1)))
#print(pt)

    


class Sphere(Point):
    """A sphere."""
    def __init__(self,center,radius):
        if radius > 0:
            self.center=center
            self.radius=radius
    def __repr__(self):
        return f"Sphere{self.center,self.radius}"
    def __eq__(self,other):
        if isinstance(other,Sphere):
            return np.array_equal(other.center,self.center) and (other.radius==self.radius)
        return False

#rt = Sphere(Point((0,1,2)), 25)
#print(rt)


class Triangle:
    """A triangle."""

    ...
