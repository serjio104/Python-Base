import math


class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x,self.y)

    def __str__(self):
        return '({}, {})'.format(self.x,self.y)

    def __add__(self,other):
        return Vector2D(self.x + other.x,self.y + other.y)

    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self,other):
        return Vector2D(self.x - other.x,self.y - other.y)

    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x,-self.y)


x = Vector2D(3,4)
print(x)
print(abs(x))


class MyClass:
   def __init__(self, param_1, param_2):
       self.param_1 = param_1
       self.param_2 = param_2
   def __str__(self):
       return f"Объект с параметрами ({self.param_1}, {self.param_2})"

mc = MyClass("text_1", "text_2")
print(mc)

