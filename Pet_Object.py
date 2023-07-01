#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. 
#This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

#imports necessary elements
from Pet_Class import Pet
import tkinter as tkinter

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

        #Label, Text Box, and Button for name Input
        self.pet.name_label = tkinter.Label(GUI, text="Please Enter the Name of Your Pet:")
        self.pet.name_label.pack(pady=5)
        self.pet.name_entry = tkinter.Entry(GUI)
        self.pet.name_entry.pack(pady=5)
        self.pet.name_button= tkinter.Button(GUI, text="Enter", command=self.name_enter)
        self.pet.name_button.pack(pady=10)

        #Label, Text Box, and Button for name Input
        self.pet.name_label = tkinter.Label(GUI, text="Please Enter the Name of Your Pet:")
        self.pet.name_label.pack(pady=5)
        self.pet.name_entry = tkinter.Entry(GUI)
        self.pet.name_entry.pack(pady=5)
        self.pet.name_button= tkinter.Button(GUI, text="Enter", command=self.name_enter)
        self.pet.name_button.pack(pady=10)
    # def for set_name()
    # def for set_animal_type()
    # def for set_age()
    # def for get_name(), get_animal_type(), get_age()