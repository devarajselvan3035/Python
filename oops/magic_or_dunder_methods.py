# Vector procemsll


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, object):
        self._check_instance(object)
        return Vector(self.x + object.x, self.y + object.y)

    def __eq__(self, object):
        self._check_instance(object)
        return (self.x == object.x) and (self.y == object.y)

    def __ne__(self, object):
        self._check_instance(object)
        return not (self == object)

    def _check_instance(self, object):
        if not isinstance(object, Vector):
            raise ValueError("Given object is not a vector")


v1 = Vector(1, 2)
v2 = Vector(1, 2)
v3 = v1 + v2
print(v1 != 10)
