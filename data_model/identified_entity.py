# File: identified_entity.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
# Consts
# Globals


# Classes
class IdentifiedEntity:
    """
    Identified entity base class - class variables:
        __next_id: number element of unique identifier to use for the next id, as integer, with private access
    """
    __next_id = 1000

    def __init__(self, id_prefix):
        """
        Initialiser - instance variables:
            id: unique identifier of this entity instance, as string, property with read-only access

        :param id_prefix: used to build the unique identifier of this entity
        """
        self.__id = str(id_prefix) + str(IdentifiedEntity.__next_id)  # Build unique id
        IdentifiedEntity.__next_id += 1  # Increment the next id class variable

    @property
    def id(self):
        return self.__id

    def __str__(self):
        """
        To string method

        :return: string representation of this entity instance
        """
        s = IdentifiedEntity.__name__ + ","
        s += "id:{0}".format(self.id)

        return s
