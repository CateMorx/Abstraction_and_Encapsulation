#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
# creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
# Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.

#Imports necessarry elements
from Class_Fan import Fan
from tkinter import Tk, Label

#Class TestFan
class Test_Fan:
#def for assigning values for fan 1 & 2
    def main(self):
        fan1 = Fan(speed=Fan.FAST, radius=10, color='yellow', on=True)

        fan2 = fan1
        fan2.set_speed(Fan.MEDIUM)
        fan2.set_radius(5)
        fan2.set_color('blue')
        fan2.set_on(False)
        self.create_gui(fan2, "Fan 2 properties:")
#def GUI
    def create_gui(self, title):
        root = Tk()
        root.title(title)
        speed_label = Label(root,text="Speed: " + str(self.get_speed()))
        speed_label.pack()

        radius_label = Label(root,text="Radius: " + str(self.get_radius()))
        radius_label.pack()

        color_label = Label(root,text="Color: " + str(self.get_color()))
        color_label.pack()

        on_label = Label(root,text="On: " + str(self.is_on()))
        on_label.pack()
        
        #starts the event loop of the GUI application
        root.mainloop()

#Executes code within main
if __name__ == '__main__':
    window = Test_Fan()
    window.main()