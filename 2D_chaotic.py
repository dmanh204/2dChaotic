class Henon:
    def __init__(self, x0, y0 , a, b) -> None:
        self.x = x0
        self.y = y0
        self.a = a
        self.b = b
    def cal(self):
        x = 1- self.a * self.x**2 + self.y # x(i+1) = 1 -a*(x(i)^2) + y(i) 
        y = self.b * self.x                 # y(i+1) = b * (i)
        # Update value
        self.x = x
        self.y = y

class Duffig:
    def __init__(self, x, y, a, b) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.b = b
    def cal(self):
        x = self.y
        y = (- self.b) * self.x + self.a *self.y +self.y**3

        #Update
        self.x = x
        self.y = y
import math
class Standard:
    def __init__(self, x, y, k) -> None:
        # x, y in [0,2pi]
        self.x = x
        self.y = y
        self.k = k

    def mod2pi(self, x):
        pi = math.pi
        thuong = math.floor(x/(2*pi))
        return x-(thuong*2*pi)
    def cal(self):
        self.x = self.mod2pi(self.x + self.y) # x(i+1) = mod(x(i)+y(i))
        self.y = self.mod2pi(self.y + self.k * math.sin(self.x)) # y(i+1) = y(i) + Ksin(x(i+1)) , self.x da update

class Lozi:
    def __init__(self, x, y, a, b) -> None:
        self.x = x
        self.y = y
        self.b = b
        self.a = a

    def cal(self):
        x = 1 - self.a * abs(self.x) + self.y # x(i+1) = 1 - a*|x| +y
        y = self.b * self.x # y(i+1) = b * x
        self.x = x
        self.y = y

class Cat:
    def __init__(self, x, y, a, b) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.b = b
    def mod1(self, input):
        temp = math.floor(input)
        return input - temp
    def cal(self):
        x = self.mod1(self.x + self.a * self.y) # x(i+1) = x + a*y
        y = self.mod1(self.b * self.x + self.a * self.b* self.y) # y(i+1) = b*x +a *b*y
        self.x = x
        self.y = y

class Baker:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def cal(self):
        if 0<= self.x <= 1/2:
            self.x = 2*self.x
            self.y = self.y /2
        if 1/2 < self.x <= 1:
            self.x = 2* self.x - 1
            self.y = self.y /2 + 1/2 