# File: clients_list.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.identified_entities_list import IdentifiedEntitiesList


# Consts
# Globals


# Classes
class ClientsList(IdentifiedEntitiesList):
    """
    Container for Client class instances
    """

    def __init__(self):
        """
 -      Initialiser - instance variables:
            data: from base class
        """
        super().__init__()

    def __str__(self):
        """
        To string method

        :return: string representation of this client list instance
        """
        return "{0}:{1}".format(ClientsList.__name__, self.count())
