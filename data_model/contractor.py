# File: contractor.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.identified_entity import IdentifiedEntity
from data_model.named_entity import NamedEntity


# Consts
# Globals


# Classes
class Contractor(IdentifiedEntity, NamedEntity):
    """
    Contractor entity class - class variables:
        __next_id: from base class
        __ID_PREFIX: two letter prefix for each unique identifier, as string, with private access
    """
    __ID_PREFIX = "CR"

    def __init__(self, name, speciality):
        """
        Initialiser - instance variables:
            id: from base class
            name: from base class
            speciality: speciality associated with this contractor instance, as string, property with read/write access

        :param name: to associate with this contractor instance
        :param speciality: to associated with this contractor instance
        """
        IdentifiedEntity.__init__(self, Contractor.__ID_PREFIX)
        NamedEntity.__init__(self, name)
        self.__speciality = str(speciality)

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, speciality):
        self.__speciality = str(speciality)

    def __str__(self):
        """
        To string method

        :return: string representation of this contractor instance
        """
        s = "Id: {0}, ".format(self.id)
        s += "{0}".format(self.name)

        return s

    def make_displayable(self):
        """
        Provides a string version of a Contractor instance that can then be used as displayable data

        :return: Contractor instance as displayable string
        """
        s = "Id: {0}\n".format(self.id)
        s += "Name: {0}\n".format(self.name)
        s += "Speciality: {0}".format(self.speciality)

        return s
