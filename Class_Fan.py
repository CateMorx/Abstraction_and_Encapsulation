#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#The Fan class represents a fan and has constants SLOW, MEDIUM, and FAST for speed values. It has private data fields for speed, on/off status, radius, and color. 
#The class provides accessor and mutator methods for all data fields and a constructor to create a fan object with default values.

#Class
class Fan():
    #Puts label on fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3
# A constructor that creates a fan with the speed (default SLOW), radius (default 5), color (default blue), and on (default False)
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
#accessor and mutator for speed
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed
#accessor and mutator for on
#accessor and mutator for radius
#accessor and mutator for color