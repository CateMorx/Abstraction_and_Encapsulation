#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
# creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
# Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.

#Imports necessarry elements
from Class_Fan import Fan
from tkinter import Tk, Label, font

#Class TestFan
class Test_Fan:
#def for assigning values for fan 1 & 2
    def main(self):
        fan1 = Fan(speed=Fan.FAST, radius=10, color='yellow', on=True)

        #calls gui for fan1
        self.create_gui(fan1, "Fan 1 properties:")

        #duplicates fan 1
        fan2 = fan1

        #Calls setter for all attributes
        fan2.set_speed(Fan.MEDIUM)
        fan2.set_radius(5)
        fan2.set_color('blue')
        fan2.set_on(False)

        #calls gui for fan2
        self.create_gui(fan2, "Fan 2 properties:")

#def GUI
    def create_gui(self, fan, title):
        root = Tk()
        root.title(title)

        #Custom font
        custom_font = font.Font(family="Arial", size=24, weight="bold")

        #Label for speed
        speed_label = Label(root,text="Speed: " + str(fan.get_speed()),font=custom_font)
        speed_label.pack()

        #Label for radius
        radius_label = Label(root,text="Radius: " + str(fan.get_radius()),font=custom_font)
        radius_label.pack()

        #Label for color
        color_label = Label(root,text="Color: " + str(fan.get_color()),font=custom_font)
        color_label.pack()

        #Label for on
        on_label = Label(root,text="On: " + str(fan.is_on()),font=custom_font)
        on_label.pack()
        
        #Custom size for window
        root.geometry("400x600")

        #calls def for changing background color
        self.apply_rainbow_colors(root,[speed_label, radius_label, color_label, on_label])

        #starts the event loop of the GUI application
        root.mainloop()


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
    window = Test_Fan()
    window.main()