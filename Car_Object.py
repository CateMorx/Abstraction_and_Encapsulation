#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#design a program that creates a Car object then calls the accelerate method five times. After each call to the accelerate method, 
#get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, 
#get the current speed of the car and display it.

#imports necessary elements
from Car_Class import Car
from tkinter import Tk, Label

#Class for Car_Object
class Car_Object:
    #GUI constructor
    def __init__(self):
        self.root = Tk()
        self.root.title("Output Window")

    #def create car object
    def main(self):
         # Create a Car object
        car = Car(2023, "Tesla")

        #accelerates and display speed 5 times
        for _ in range(5):
            car.accelerate()
            accelerate_label=Label("Car accelerates \n"+"Current speed:"+ str(car.get_speed()))
            accelerate_label.pack()
            
        #decelerates and display speed 5 times
        for _ in range(5):
            car.brake()
            decelerate_label=Label("Car decelerates using brakes \n"+"Current speed:"+ str(car.get_speed()))
            decelerate_label.pack()
        self.root.mainloop()
    #def that creates rainbow window background

#Executes code within main
if __name__ == '__main__':
    window = Car_Object()
    window.main()