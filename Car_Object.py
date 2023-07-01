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
        self.apply_rainbow_colors()

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

        #calls function that shows output
        self.show_output(output)
        #starts the event loop of the GUI application
        self.root.mainloop()

    #def for changing background color
    def apply_rainbow_colors(self, root, labels):
        #creates list for color for rainbow
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        #define variable current color
        current_color_index = 0

        def change_background_color():
            #calls nonlocal variable
            nonlocal current_color_index

            #assigns value of current_color_index element from colors list to color.
            color = colors[current_color_index]

            #configures window background color
            root.configure(bg=color)

            #changes the color of the background of label text along with the window background
            for label in labels:
                label.configure(highlightbackground=color)
                label.config(bg=color)
            #update the current_color_index variable in a cyclic manner
            current_color_index = (current_color_index + 1) % len(colors)

            #scheduling the execution of the self.change_background_color function after delay
            root.after(1000, change_background_color)
        change_background_color()

#Executes code within main
if __name__ == '__main__':
    window = Car_Object()
    window.main()