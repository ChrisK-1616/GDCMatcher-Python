# File: fixed_fee_contract.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.contract import Contract


# Consts
# Globals


# Classes
class FixedFeeContract(Contract):
    """
    Fixed Fee Contract entity class - class variables:
        __next_id: from base class
        __ID_PREFIX: from base class
        base_commission: from base class
        fixed_fee: fixed fee added to the final base commission element of revenue, as float, with public access
    """
    fixed_fee = 50.0  # Initial value for fixed fee of all contracts, this can be changed subsequently

    def __init__(self, owner, speciality, payment, contractor_allocated=None):
        """
        Initialiser - instance variables:
            id: from base class
            owner: from base class
            speciality: from base class
            contractor_allocated: from base class
            payment: from base class
            completed: from base class

        :param owner: to associate with this contract instance
        :param speciality: to associated with this contract instance
        :param payment: to associated with this contract instance
        :param contractor_allocated: to associated with this contract instance {optional}
        """
        super().__init__(owner, speciality, payment, contractor_allocated)

    def make_displayable(self):
        """
        Provides a string version of a FixedFeeContract instance that can then be used as displayable data

        :return: FixedFeeContract instance as displayable string
        """
        s = "Id: {0}\n".format(self.id)
        s += "Owner: {0} ({1})\n".format(self.owner.id, self.owner.name)
        s += "Speciality: {0}\n".format(self.speciality)
        s += "Contractor Allocated: {0}{1}\n".format(self.contractor_allocated.id if self.contractor_allocated else
                                                     "None", " (" + self.contractor_allocated.name + ")" if
                                                     self.contractor_allocated else "")
        s += "Base Commission: {0}%\n".format(Contract.base_commission)
        s += "Fixed Fee: £{0:.2f}\n".format(FixedFeeContract.fixed_fee)
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
        Uses the base commission property to calculate the revenue from the payment made on completion of the contract
        plus the fixed fee:

            revenue = ((base_commission / 100.0) * payment) + fixed_fee

        :return: revenue as float
        """
        return super().calculate_revenue() + FixedFeeContract.fixed_fee
