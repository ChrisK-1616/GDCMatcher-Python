# File: contractors_list.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.identified_entities_list import IdentifiedEntitiesList


# Consts
# Globals


# Classes
class ContractorsList(IdentifiedEntitiesList):
    """
    Container for Contractor class instances, adds a method that returns a list of all Contractor instances held in
    this container that have a supplied speciality
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

        :return: string representation of this contractor list instance
        """
        return "{0}:{1}".format(ContractorsList.__name__, self.count())

    def get_with_speciality(self, speciality):
        """
        Provides a list of all the contained Contractor instances that have the supplied speciality, note this will be
        an empty list if no Contractors have the supplied speciality

        :param speciality: this is the speciality to match with Contractor instances as string
        :return: All Contractor instances with supplied speciality as list
        """
        contractors = []
        for contractor in self.data:
            if contractor.speciality == speciality:
                contractors.append(contractor)

        return contractors
