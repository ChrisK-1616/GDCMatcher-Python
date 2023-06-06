# File: main_app.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
from data_model.client import Client
from data_model.contractor import Contractor
from data_model.contract import Contract
from data_model.fixed_fee_contract import FixedFeeContract
from data_model.advert_fee_contract import AdvertFeeContract
from data_model.clients_list import ClientsList
from data_model.contractors_list import ContractorsList
from data_model.contracts_list import ContractsList


# Consts
# Globals


# Classes
class MainApp:
    """
    This class is used to encapsulate the application as a whole, here the required dependent class instances will be
    created, managed and operated, these are the clients, contractors and contracts lists and the UI, there are also
    all the necessary methods for operating the application, note - the clients, contractors and contracts lists are
    at class scope as there is only one of each required

    Main application class - class variables
        __clients: clients list, as ClientsList, with private access
        __contractors: contractors list, as ContractorsList, with private access
        __contracts: contracts list, as ContractsList, with private access
    """
    __clients = ClientsList()
    __contractors = ContractorsList()
    __contracts = ContractsList()

    def __init__(self, name, ui):
        """
 -      Initialiser - instance variables:
            name: the name given to the main application, as string, property with read/write access
            ui: the instance of the UI currently operating the application, as UI, property with read-only access
            revenue: money made as contracts are completed, as float, property with read/write access
        """

        self.__name = str(name)
        self.__ui = ui
        self.__revenue = 0.0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = str(name)

    @property
    def ui(self):
        return self.__ui

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        self.__revenue = revenue

    def __str__(self):
        """
        To string method

        :return: string representation of this main application instance
        """

        return "{0} - Current Revenue £{1}".format(self.name, self.revenue)

    def preload(self, file_path):
        """
        This method is purely available to preload a known set of data to aid in testing the application and can be
        removed before distributing the final production version of the application

        :param file_path: path to the file from which to preload data as string
        :return: None
        """
        # We will use part of the os module to check for file existance
        import os.path

        # If the file does not exist (or it is a directory rather than a file), then display an error message and abort
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            print("\nError: preload data file on path '{0}' not found".format(file_path))
            return

        # Open data file
        data_file = open(file_path, "r")

        # Read all lines from data file into an array
        entries = data_file.readlines()

        # Process each entry
        for entry in entries:
            # First check to see if the entry is a comment, if so then ignore this and check next entry
            if entry[0] == "#":
                continue

            # Process each entry by converting the string to a dictionary representation using eval()
            entry_as_dict = eval(entry)

            # If the entry does not evaluate to a dictionary then assign cls None else assign cls the name of the class
            # to be instantiated assuming the preload data is correctly formed
            cls = None
            if type(entry_as_dict) is dict and "class" in entry_as_dict:
                # Find the class this entry is using the "class" key from entry as dictionary
                cls = entry_as_dict["class"]

            # Do class specific instantiation and adding to the correct container by using the relevant add_XXXXXX()
            # method, note special care needs to be made when setting up the preload data to ensure that the correct
            # client identifiers are associated with the correct client owners of the contract data
            if cls == "Client":
                self.add_client(entry_as_dict["name"])  # Add a new client

            elif cls == "Contractor":
                self.add_contractor(entry_as_dict["name"], entry_as_dict["speciality"])  # Add a new contractor

            elif cls == "Contract":
                # Add new contract of type "base"
                success, contract = self.add_contract("base", self.get_client(entry_as_dict["owner_id"]),
                                                      entry_as_dict["speciality"], entry_as_dict["payment"])

                # Check if this contract has a contractor allocated
                if entry_as_dict["contractor_allocated_id"]:
                    # Yes so allocate to this contractor
                    self.allocate_contractor(contract, self.get_contractor(entry_as_dict["contractor_allocated_id"]))

                # Check if this contract is completed
                if entry_as_dict["completed"]:
                    # Yes so complete this contract
                    self.complete_contract(contract)

            elif cls == "FixedFeeContract":
                # Add new contract of type fixed fee
                success, contract = self.add_contract("fixed", self.get_client(entry_as_dict["owner_id"]),
                                                      entry_as_dict["speciality"], entry_as_dict["payment"])

                # Check if this contract has a contractor allocated
                if entry_as_dict["contractor_allocated_id"]:
                    # Yes so allocate to this contractor
                    self.allocate_contractor(contract, self.get_contractor(entry_as_dict["contractor_allocated_id"]))

                # Check if this contract is completed
                if entry_as_dict["completed"]:
                    # Yes so complete this contract
                    self.complete_contract(contract)

            elif cls == "AdvertFeeContract":
                # Add new contract of type advert fee
                success, contract = self.add_contract("advert", self.get_client(entry_as_dict["owner_id"]),
                                                      entry_as_dict["speciality"], entry_as_dict["payment"])

                # Check if this contract has a contractor allocated
                if entry_as_dict["contractor_allocated_id"]:
                    # Yes so allocate to this contractor
                    self.allocate_contractor(contract, self.get_contractor(entry_as_dict["contractor_allocated_id"]))

                # Check if this contract is completed
                if entry_as_dict["completed"]:
                    # Yes so complete this contract
                    self.complete_contract(contract)

            # Note - if the class key is any other value than those in the if .. elif then it is ignored

        print("\nData from file on path '{0}' successfully loaded".format(file_path))

    def execute(self):
        """
        Executes the main application

        :return: None
        """
        # Preload the main application with data from the "data/preload.dat" file, we will use this to help with testing
        # so a set of known data is always available when the application starts, we can remove this once ready to
        # distribute the production version of the application
        self.preload("data/preload.dat")

        # Inject this main application instance into the UI as a dependency, this allows the UI to navigate to the main
        # application instance and call the necessary methods to operate the application functionality
        self.__ui.main_app = self

        # Run the UI
        self.ui.run()

    def add_client(self, name):
        """
        Add new client instance with the supplied name

        :param name: name of the new client as string
        :return: tuple with first entry a success indicator as boolean and the second entry either the newly added
                 client (if successful) or an error message (if unsuccessful)
        """
        client = Client(name)

        if not MainApp.__clients.add(client):  # Unsuccessful so return error message
            return False, "Error: new client was not added, reason not known"

        return True, client  # Successful so return newly added client instance

    def remove_client(self, ident):
        """
        Remove client instance by supplied identifier

        :param ident: identifier of the client instance to remove
        :return: tuple with first entry a success indicator as boolean and the second entry either the details of the
                 removed client (if successful) or an error message (if unsuccessful)
        """
        # Find client instance
        client = MainApp.__clients.find_by_id(ident)

        # Check if client instance exists, if not return unsuccessful flag and error message
        if not client:
            return False, "Error: cannot remove client with Id: {0}, it does not exist".format(ident)

        # Check if any contracts owned by this client, if so then return unsuccessful flag and error message
        if MainApp.__contracts.get_with_owner(client):
            return False, "Error: cannot remove client with Id: {0}, it is a contract owner".format(ident)

        # Store client details as string
        details = client

        # Now able to remove client instance
        MainApp.__clients.remove(client)

        return True, details  # Successful so return True and the removed client details

    def get_client(self, ident):
        """
        Return the client instance with the supplied identifier

        :param ident: identifier of client as string
        :return: client instance or None if it does not exist
        """
        return MainApp.__clients.find_by_id(ident)

    def get_all_clients(self):
        """
        Return all the client instances as a list

        :return: all client instances
        """
        return MainApp.__clients.data

    def add_contractor(self, name, speciality):
        """
        Add new contractor instance with the supplied name and speciality

        :param name: name of the new contractor as string
        :param speciality: speciality of the new contractor as string
        :return: tuple with first entry a success indicator as boolean and the second entry either the newly added
                 contractor (if successful) or an error message (if unsuccessful)
        """
        contractor = Contractor(name, speciality)

        if not MainApp.__contractors.add(contractor):  # Unsuccessful so return error message
            return False, "Error: new contractor was not added, reason not known"

        return True, contractor  # Successful so return newly added contractor instance

    def remove_contractor(self, ident):
        """
        Remove contractor instance by supplied identifier

        :param ident: identifier of the contractor instance to remove
        :return: tuple with first entry a success indicator as boolean and the second entry either the details of the
                 removed contractor (if successful) or an error message (if unsuccessful)
        """
        # Find contractor instance
        contractor = MainApp.__contractors.find_by_id(ident)

        # Check if contractor instance exists, if not return unsuccessful flag and error message
        if not contractor:
            return False, "Error: cannot remove contractor with Id: {0}, it does not exist".format(ident)

        # Check if any contracts are allocated to this contractor, if so then return unsuccessful flag and error message
        if MainApp.__contracts.get_with_contractor(contractor):
            return False, "Error: cannot remove contractor with Id: {0}, it is allocated to a contract".format(ident)

        # Store contractor details as string
        details = contractor

        # Now able to remove contractor instance
        MainApp.__contractors.remove(contractor)

        return True, details  # Successful so return True and the removed contractor details

    def get_contractor(self, ident):
        """
        Return the contractor instance with the supplied identifier

        :param ident: identifier of contractor as string
        :return: contractor instance or None if it does not exist
        """
        return MainApp.__contractors.find_by_id(ident)

    def get_contractors_with_speciality(self, speciality):
        """
        Return all the contractor instances that match the supplied speciality as a list

        :param speciality: speciality to match with contractors as string
        :return: all matching contractor instances
        """
        return MainApp.__contractors.get_with_speciality(speciality)

    def get_all_contractors(self):
        """
        Return all the contractor instances as a list

        :return: all contractor instances
        """
        return MainApp.__contractors.data

    def add_contract(self, contract_type, owner, speciality, payment):
        """
        Add new contract instance with the supplied contract type, owner, speciality and payment

        :param contract_type: type (base, fixed or advert) of the new contract as string
        :param owner: owner of the new contract as Client instance
        :param speciality: speciality of the new contractor as string
        :param payment: payment amount of the new contract as float
        :return: tuple with first entry a success indicator as boolean and the second entry either the newly added
                 contract (if successful) or an error message (if unsuccessful)
        """
        # Instantiate the correct contract class depending on the supplied contract type
        if contract_type == "b" or contract_type == "base":
            contract = Contract(owner, speciality, payment)
        elif contract_type == "f" or contract_type == "fixed":
            contract = FixedFeeContract(owner, speciality, payment)
        elif contract_type == "a" or contract_type == "advert":
            contract = AdvertFeeContract(owner, speciality, payment)
        else:  # Not a valid contract type so return as unsuccessful with an error message
            return False, "Error: new contract was not added, invalid contract type"

        if not MainApp.__contracts.add(contract):  # Unsuccessful so return error message
            return False, "Error: new contract was not added, reason not known"

        return True, contract  # Successful so return newly added contract instance

    def remove_contract(self, ident):
        """
        Remove contract instance by supplied identifier

        :param ident: identifier of the contract instance to remove
        :return: tuple with first entry a success indicator as boolean and the second entry either the details of the
                 removed contract (if successful) or an error message (if unsuccessful)
        """
        # Find contract instance
        contract = MainApp.__contracts.find_by_id(ident)

        # Check if contract instance exists, if not return unsuccessful flag and error message
        if not contract:
            return False, "Error: cannot remove contract with Id: {0}, it does not exist".format(ident)

        # Check if this contract is completed, if not then check if it has an allocated contractor, if a contractor is
        # allocated then return unsuccessful flag and error message
        if not contract.completed and contract.contractor_allocated:
            return False, "Error: cannot remove contract with Id: {0}, " \
                          "it is not completed and has an allocated contractor".format(ident)

        # Store contract details as string
        details = contract

        # Now able to remove contract instance
        MainApp.__contracts.remove(contract)

        return True, details  # Successful so return True and the removed contract details

    def allocate_contractor(self, contract, contractor):
        """
        Change the allocated contractor on the supplied contract instance to the supplied contractor instance

        :param contract: contract as Contract instance
        :param contractor: contractor as Contractor instance
        :return: None
        """
        contract.contractor_allocated = contractor

    def complete_contract(self, contract):
        """
        Change the completed flag on the supplied contract instance to True and record the revenue from the contract

        :param contract: contract as Contract instance
        :return: None
        """
        contract.completed = True
        self.__revenue += contract.calculate_revenue()

    def get_contract(self, ident):
        """
        Return the contract instance with the supplied identifier

        :param ident: identifier of contract as string
        :return: contractor instance or None if it does not exist
        """
        return MainApp.__contracts.find_by_id(ident)

    def get_contracts_for_owner(self, owner):
        """
        Return all the contract instances that match the supplied owner as a list

        :param owner: owner to match with contracts as string
        :return: all matching contract instances
        """
        return MainApp.__contracts.get_with_owner(owner)

    def get_contracts_for_speciality(self, speciality):
        """
        Return all the contract instances that match the supplied speciality as a list

        :param speciality: speciality to match with contracts as string
        :return: all matching contract instances
        """
        return MainApp.__contracts.get_with_speciality(speciality)

    def get_all_unallocated_contracts(self):
        """
        Return all the contract instances that have no contractor allocated as a list

        :return: all matching contract instances
        """
        return MainApp.__contracts.get_all_unallocated()

    def get_contracts_allocated_to_contractor(self, contractor):
        """
        Return all the contract instances that are allocated to the supplied contractor as a list

        :param contractor: contractor to match with allocated contracts as string
        :return: all matching contract instances
        """
        return MainApp.__contracts.get_with_contractor(contractor)

    def get_all_contracts(self):
        """
        Return all the contract instances as a list

        :return: all contract instances
        """
        return MainApp.__contracts.data
