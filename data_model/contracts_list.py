# File: contracts_list.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.identified_entities_list import IdentifiedEntitiesList


# Consts
# Globals


# Classes
class ContractsList(IdentifiedEntitiesList):
    """
    Container for Contract class instances, adds methods that return a list of all Contract instances held in
    this container that have a supplied speciality, return a list of all Contract instances held in this container that
    have a supplied owner, return a list of all Contract instances held in this container that have not yet been
    allocated a Contractor instance and return a list of all Contract instances held in this container that are
    allocated to a supplied Contractor instance
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

        :return: string representation of this contract list instance
        """
        return "{0}:{1}".format(ContractsList.__name__, self.count())

    def get_with_owner(self, owner):
        """
        Provides a list of all the contained Contract instances that have the supplied owner, note this will be an empty
        list if no Contracts have the supplied owner

        :param owner: this is the owner to match with Contract instances as Client instance
        :return: All Contract instances with supplied owner identifier as list
        """
        contracts = []
        for contract in self.data:
            if contract.owner.id == owner.id:
                contracts.append(contract)

        return contracts

    def get_with_speciality(self, speciality):
        """
        Provides a list of all the contained Contract instances that have the supplied speciality, note this will be
        an empty list if no Contracts have the supplied speciality

        :param speciality: this is the speciality to match with Contract instances as string
        :return: All Contract instances with supplied speciality as list
        """
        contracts = []
        for contract in self.data:
            if contract.speciality == speciality:
                contracts.append(contract)

        return contracts

    def get_all_unallocated(self):
        """
        Provides a list of all the contained Contract instances that have not as yet been allocated to a Contractor
        instance

        :return: All Contract instances not as yet allocated as list
        """
        contracts = []
        for contract in self.data:
            if not contract.contractor_allocated:
                contracts.append(contract)

        return contracts

    def get_with_contractor(self, contractor):
        """
        Provides a list of all the contained Contract instances that have been allocated to the supplied Contractor
        instance, note will be an empty list if no Contracts have been allocated to the supplied Contractor instance

        :param contractor: this is the contractor to match with Contract instances as Contractor instance
        :return: All Contract instances with supplied speciality as list
        """
        contracts = []
        for contract in self.data:
            # Must check that Contractor instance is not None, if it is then cannot be a match
            if contract.contractor_allocated and contract.contractor_allocated.id == contractor.id:
                contracts.append(contract)

        return contracts
