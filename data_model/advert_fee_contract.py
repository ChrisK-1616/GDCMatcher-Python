# File: advert_fee_contract.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.fixed_fee_contract import FixedFeeContract
from data_model.contract import Contract


# Consts
# Globals


# Classes
class AdvertFeeContract(FixedFeeContract):
    """
    Advert Fee Contract entity class - class variables:
        __next_id: from base class
        __ID_PREFIX: from base class
        base_commission: from base class
        fixed_fee: from base class
    """

    def __init__(self, owner, speciality, payment, contractor_allocated=None):
        """
        Initialiser - instance variables:
            id: from base class
            owner: from base class
            speciality: from base class
            contractor_allocated: from base class
            payment: from base class
            times_viewed: count of how many times this contract has been viewed, as integer, property with read-only
                          access
            completed: from base class

        :param owner: to associate with this contract instance
        :param speciality: to associated with this contract instance
        :param payment: to associated with this contract instance
        :param contractor_allocated: to associated with this contract instance {optional}
        """
        super().__init__(owner, speciality, payment, contractor_allocated)
        AdvertFeeContract.fixed_fee = 0.1  # Given value for the advert fee class instances, can be changed subsequently
        self.__times_viewed = 0

    @property
    def times_viewed(self):
        return self.__times_viewed

    def make_displayable(self):
        """
        Provides a string version of an AdvertFeeContract instance that can then be used as displayable data, note
        that this also increments the times viewed property

        :return: AdvertFeeContract instance as displayable string
        """
        # Each time an instance of this class is made displayable it also increments its times viewed property
        self.inc_times_viewed()

        s = "Id: {0}\n".format(self.id)
        s += "Owner: {0} ({1})\n".format(self.owner.id, self.owner.name)
        s += "Speciality: {0}\n".format(self.speciality)
        s += "Contractor Allocated: {0}{1}\n".format(self.contractor_allocated.id if self.contractor_allocated else
                                                     "None", " (" + self.contractor_allocated.name + ")" if
                                                     self.contractor_allocated else "")
        s += "Base Commission: {0}%\n".format(Contract.base_commission)
        s += "Fixed Fee Per View: £{0:.2f}\n".format(AdvertFeeContract.fixed_fee)
        s += "Times Viewed: {0}\n".format(self.times_viewed)
        s += "Payment: £{0:.2f}\n".format(self.payment)
        s += "Completed: {0}\n".format(self.completed)
        if self.completed:  # If the contract is completed, then show how much revenue it contributed
            s += "Revenue Contributed: £{0:.2f}\n".format(self.calculate_revenue())
        else:  # Show how much potential revenue will be contributed if contract is completed
            s += "Revenue Potential: £{0:.2f}".format(self.calculate_revenue())
        # In format placeholders, ":.2f" means always show two decimals, for instance 1.2 would show as 1.20

        return s

    def inc_times_viewed(self):
        if not self.completed:  # Only increment times viewed if contract is not completed
            self.__times_viewed += 1

    def calculate_revenue(self):
        """
        Uses the base commission property to calculate the revenue from the payment made on completion of the contract:

            revenue = (base_commission / 100.0) * payment

        :return: revenue as float
        """
        return Contract.calculate_revenue(self) + (self.__times_viewed * AdvertFeeContract.fixed_fee)
