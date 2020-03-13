"""
Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
"""
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.h = height
        self.r = radius

    def volume(self):
        return Cylinder.pi*(self.r**2)*self.h

    def surface_area(self):
        return 2*Cylinder.pi*self.r*(self.h + self.r)


class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print("Deposit accepted!")

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            print("Withdrawal Accepted!")
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f"{self.owner}, {self.balance}"
