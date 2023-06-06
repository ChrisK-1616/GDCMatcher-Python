# File: named_entity.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
# Consts
# Globals


# Classes
class NamedEntity:
    """
    Named entity base class
    """

    def __init__(self, name):
        """
        Initialiser - instance variables:
            name: name associated with this entity instance, as string, property with read/write access

        :param name: to associate with this entity instance
        """
        self.__name = str(name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = str(name)

    def __str__(self):
        """
        To string method

        :return: string representation of this entity instance
        """
        s = NamedEntity.__name__ + ","
        s += "name:{0}".format(self.name)

        return s
