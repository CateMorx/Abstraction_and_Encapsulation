#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#design a program that creates a Car object then calls the accelerate method five times. After each call to the accelerate method, 
#get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, 
#get the current speed of the car and display it.

#imports necessary elements
from Car_Class import Car
from tkinter import Tk, Text

#Class for Car_Object
class Car_Object:
    #GUI constructor
    def __init__(self):
        #creates window for GUI
        self.root = Tk()
        self.root.title("Speed Display")

        #creates text widget for GUI
        self.text = Text(self.root)
        self.text.pack()

    #def that shows output in GUI
    def show_output(self, output):
        #Appends each item in output list to be shown in text widget
        for item in output:
            self.text.insert("end", str(item) + "\n")

    #def create car object
    def main(self):
         # Create a Car object
        car = Car(2023, "Tesla")

        #instantiates list for output
        output = []

        #accelerates and display speed 5 times
        for _ in range(5):
            #calls accelerate function
            car.accelerate()
            #appends lines of text output into output list
            output.append("Car accelerates \n"+"Current speed:"+ str(car.get_speed()))
            
        #decelerates and display speed 5 times
        for _ in range(5):
            #calls brake function
            car.brake()
            #appends lines of text output into output list
            output.append("Car decelerates using brakes \n"+"Current speed:"+ str(car.get_speed()))

        #calls function tha shows output
        self.show_output(output)
        #starts the event loop of the GUI application
        self.root.mainloop()

    #def that creates rainbow window background

#Executes code within main
if __name__ == '__main__':
    window = Car_Object()
    window.main()