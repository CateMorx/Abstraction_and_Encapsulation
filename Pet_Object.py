#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. 
#This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

#imports necessary elements
from Pet_Class import Pet
import tkinter as tkinter
from tkinter import messagebox

pet=Pet()
#Class Pet
class Pet_GUI:
    #GUI constructor
    def __init__(self, pet, GUI):
        self.GUI = GUI
        self.pet= pet

        #Label, Text Box, and Button for name Input
        self.pet.name_label = tkinter.Label(GUI, text="Please Enter the Name of Your Pet:")
        self.pet.name_label.pack(pady=5)
        self.pet.name_entry = tkinter.Entry(GUI)
        self.pet.name_entry.pack(pady=5)
        self.pet.name_button= tkinter.Button(GUI, text="Enter", command=self.name_enter)
        self.pet.name_button.pack(pady=10)

        #Label, Text Box, and Button for Animal Type Input
        self.pet.animal_type_label = tkinter.Label(GUI, text="Please Enter the Type of Animal Your Pet Is:")
        self.pet.animal_type_label.pack(pady=5)
        self.pet.animal_type_entry = tkinter.Entry(GUI)
        self.pet.animal_type_entry.pack(pady=5)
        self.pet.animal_type_button= tkinter.Button(GUI, text="Enter", command=self.animal_type_enter)
        self.pet.animal_type_button.pack(pady=10)

        #Label, Text Box, and Button for Age Input
        self.pet.age_label = tkinter.Label(GUI, text="Please Enter the Age of Your Pet:")
        self.pet.age_label.pack(pady=5)
        self.pet.age_entry = tkinter.Entry(GUI)
        self.pet.age_entry.pack(pady=5)
        self.pet.age_button= tkinter.Button(GUI, text="Enter", command=self.age_enter)
        self.pet.age_button.pack(pady=10)

        #Button to print and display results
        self.pet.print = tkinter.Button(GUI, text="Print", command=self.print)
        self.pet.print.pack(pady=10)


        #Label and textbox for name
        self.pet.name_results_label = tkinter.Label(GUI, text="Name:")
        self.pet.name_results_label.pack(pady=5)
        self.pet.name_results_entry = tkinter.Entry(GUI)
        self.pet.name_results_entry.pack(pady=5)

        #Label and textbox for animal
        self.pet.animal_type_results_label = tkinter.Label(GUI, text="Animal Type:")
        self.pet.animal_type_results_label.pack(pady=5)
        self.pet.animal_type_results_entry = tkinter.Entry(GUI)
        self.pet.animal_type_results_entry.pack(pady=5)

        #Label and textbox for age
        self.pet.age_results_label = tkinter.Label(GUI, text="Age:")
        self.pet.age_results_label.pack(pady=5)
        self.pet.age_results_entry = tkinter.Entry(GUI)
        self.pet.age_results_entry.pack(pady=5)

    # def for set_name()
    def name_enter(self):
        name = self.pet.name_entry.get()
        if not name:
            messagebox.showinfo("Error", "Please enter a Name")
            return
        else:
            self.pet.set_name(str(name))

    # def for set_animal_type()
    def animal_type_enter(self):
        try:
            animal_type = self.pet.animal_type_entry.get()
            if not animal_type:
                messagebox.showinfo("Error", "Please enter an Animal Type")
                return
            if not animal_type.isalpha():
                raise ValueError
                return
            else:
                self.pet.set_animal_type(str(animal_type))
        except ValueError:
            messagebox.showerror("ValueError", "Animal Type should only contain alphabetic characters")

    # def for set_age()
    def age_enter(self):
        try:
            age = self.pet.age_entry.get()
            if not age:
                messagebox.showinfo("Error", "Please enter the Age")
                return
            if not age.isdigit():
                raise ValueError
                return
            if int(age)<1:
                raise ValueError
                return
            else:
                self.pet.set_age(str(age))
        except ValueError:
            messagebox.showerror("ValueError", "Age must be an integer")

    # def for get_name(), get_animal_type(), get_age()
    def print(self):
        name= self.pet.get_name()
        animal_type=self.pet.get_animal_type()
        age=self.pet.get_age()
        self.pet.name_results_entry.insert(0, str(name))
        self.pet.animal_type_results_entry .insert(0, str(animal_type))
        self.pet.age_results_entry.insert(0, str(age))


#starts the event loop of the GUI application
root = tkinter.Tk()
root.title("Pet Class")
pet_gui = Pet_GUI(pet, root)
root.mainloop()