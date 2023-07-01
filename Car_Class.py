#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#Write a class named Car that has the following data attributes: _ _year_model, _ _make, _ _speed. 
#The class should also have the following methods: accelerate(), brake(), get_speed()

#Class Car
class Car:
    #Constructor with year model, make, and speed
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0   

    #def for accelerate
    def accelerate(self):
        self.__speed += 5

    #def for brake
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    #def for get speed
    def get_speed(self):
        return self.__speed
