# File: contract.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.identified_entity import IdentifiedEntity


# Consts
# Globals


# Classes
class Contract(IdentifiedEntity):
    """
    Contract entity class - class variables:
        __next_id: from base class
        __ID_PREFIX: two letter prefix for each unique identifier, as string, with private access
        base_commission: percentage of payment paid as commission on completion of contract, as float, with public
                         access
    """
    __ID_PREFIX = "CT"
    base_commission = 10.0  # Initial value for base commission of all contracts, this can be changed subsequently

    def __init__(self, owner, speciality, payment, contractor_allocated=None):
        """
        Initialiser - instance variables:
            id: from base class
            owner: instance of the owner of this contract, as Client instance, property with read-only access
            speciality: speciality associated with this contract instance, as string, property with read-only access
            contractor_allocated: instance of the contractor allocated to this contract, as Contractor instance,
                                  property with read/write access
            payment: payment t0 be made on completion of this contract, as float, property with read-only access
            completed: flag to indicate if the contract is completed or not, as boolean, property with read/write access

        :param owner: to associate with this contract instance
        :param speciality: to associated with this contract instance
        :param payment: to associated with this contract instance
        :param contractor_allocated: to associated with this contract instance {optional}
        """
        IdentifiedEntity.__init__(self, Contract.__ID_PREFIX)
        self.__owner = owner
        self.__speciality = str(speciality)
        self.__contractor_allocated = contractor_allocated
        self.__payment = float(payment)
        self.__completed = False

    @property
    def owner(self):
        return self.__owner

    @property
    def speciality(self):
        return self.__speciality

    @property
    def contractor_allocated(self):
        return self.__contractor_allocated

    @contractor_allocated.setter
    def contractor_allocated(self, contractor_allocated):
        self.__contractor_allocated = contractor_allocated

    @property
    def payment(self):
        return self.__payment

    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, completed):
        self.__completed = completed

    def __str__(self):
        """
        To string method

        :return: string representation of this contract instance
        """
        s = "Id: {0}, ".format(self.id)
        s += "Owner: {0} : {1}".format(self.owner.id, self.owner.name)

        return s

    def make_displayable(self):
        """
        Provides a string version of a Contract instance that can then be used as displayable data

        :return: Contract instance as displayable string
        """
        s = "Id: {0}\n".format(self.id)
        s += "Owner: {0} ({1})\n".format(self.owner.id, self.owner.name)
        s += "Speciality: {0}\n".format(self.speciality)
        s += "Contractor Allocated: {0}{1}\n".format(self.contractor_allocated.id if self.contractor_allocated else
                                                     "None", " (" + self.contractor_allocated.name + ")" if
                                                     self.contractor_allocated else "")
        s += "Base Commission: {0}%\n".format(Contract.base_commission)
        s += "Payment: £{0:.2f}\n".format(self.payment)
        s += "Completed: {0}\n".format(self.completed)
        if self.completed:  # If the contract is completed, then show how much revenue it contributed
            s += "Revenue Contributed: £{0:.2f}\n".format(self.calculate_revenue())
        else:  # Show how much potential revenue will be contributed if contract is completed
            s += "Revenue Potential: £{0:.2f}".format(self.calculate_revenue())
        # In format placeholders, ":.2f" means always show two decimals, for instance 1.2 would show as 1.20

        return s

    def calculate_revenue(self):
        """
        Uses the base commission property to calculate the revenue from the payment made on completion of the contract:

            revenue = (base_commission / 100.0) * payment

        :return: revenue as float
        """
        return (Contract.base_commission / 100.0) * self.__payment
