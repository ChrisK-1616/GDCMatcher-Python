# File: client.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.identified_entity import IdentifiedEntity
from data_model.named_entity import NamedEntity


# Consts
# Globals


# Classes
class Client(IdentifiedEntity, NamedEntity):
    """
    Client entity class - class variables:
        __next_id: from base class
        __ID_PREFIX: two letter prefix for each unique identifier, as string, with private access
    """
    __ID_PREFIX = "CL"

    def __init__(self, name):
        """
        Initialiser - instance variables:
            id: from base class
            name: from base class

        :param name: to associate with this client instance
        """
        IdentifiedEntity.__init__(self, Client.__ID_PREFIX)
        NamedEntity.__init__(self, name)

    def __str__(self):
        """
        To string method

        :return: string representation of this client instance
        """
        s = "Id: {0}, ".format(self.id)
        s += "{0}".format(self.name)

        return s

    def make_displayable(self):
        """
        Provides a string version of a Client instance that can then be used as displayable data

        :return: Client instance as displayable string
        """
        s = "Id: {0}\n".format(self.id)
        s += "Name: {0}".format(self.name)

        return s
