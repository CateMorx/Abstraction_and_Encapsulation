#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 9
#Write a class named Pet, which should have the following data attributes:_ _name, _ _animal_type, _ _age.
# The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
#set_name(), set_animal_type(), set_age(), get_name(), get_animal_type(), get_age()

#Class Pet
class Pet:
    # Constructor with name, animal_type, age
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = ""

    # def set_name()
    def set_name(self, name):
        self.__name = name

    # def set_animal_type()
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # def set_age()
    def set_age(self, age):
        self.__age = age

    # def get_name()
    def get_name(self):
        return self.__name
    
    # def get_animal_type()
    def get_animal_type(self):
        return self.__animal_type
    
    # def get_age()
    def get_age(self):
        return self.__age
