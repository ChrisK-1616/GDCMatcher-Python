# File: menu_ui.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
# Consts
# Globals


# Classes
class MenuUI:
    """
    This is a console-based UI for the main application, utilising the menu system previously implemented in the earlier
    version of the case study system, it is loosely coupled to the main application through a dependency on the main
    application instance, calling back on this instance to action the required functionality for the system

    MenuUI class - class variables
        __MAIN_MENU_ID: constant representing the main menu, as integer, with private access
        __CLIENTS_MENU_ID: constant representing the clients menu, as integer, with private access
        __CONTRACTORS_MENU_ID: constant representing the contractors menu, as integer, with private access
        __CONTRACTS_MENU_ID: constant representing the contracts menu, as integer, with private access

        __current_menu: indicates which is the currently active menu, as integer, with private access
        __finished: flag used to indicate if the run() method of this UI should continue to execute, as boolean, with
                    private access
    """
    __MAIN_MENU_ID = 0
    __CLIENTS_MENU_ID = 1
    __CONTRACTORS_MENU_ID = 2
    __CONTRACTS_MENU_ID = 3

    __current_menu = __MAIN_MENU_ID  # Initially set to main menu as current menu
    __finished = False  # Initially False to ensure UI runs its main menu at least once

    def __init__(self):
        """
 -      Initialiser - instance variables:
            main_app: the instance of the main application this UI is operating, as MainApp, property with read/write
            access
        """
        self.__main_app = None  # Initially not set, injected into the main application as part of its initialisation

    @property
    def main_app(self):
        return self.__main_app

    @main_app.setter
    def main_app(self, main_app):
        self.__main_app = main_app

    def run(self):
        """
        This method runs the menu system and is invoked at the very start of the application operation, it continue to
        execute until the __finished flag is set to True

        :return: None
        """

        # Main menu loop
        while not MenuUI.__finished:
            if MenuUI.__current_menu == MenuUI.__MAIN_MENU_ID:  # Display and process main menu
                MenuUI.display_main_menu()

                # Get user menu choice
                choice = MenuUI.get_menu_choice(1, 5)

                # Process user menu choice
                self.process_main_menu_choice(choice)

            elif MenuUI.__current_menu == MenuUI.__CLIENTS_MENU_ID:  # Display and process clients
                MenuUI.display_clients_menu()

                # Get user menu choice
                choice = MenuUI.get_menu_choice(1, 5)

                # Process user menu choice
                self.process_clients_menu_choice(choice)

            elif MenuUI.__current_menu == MenuUI.__CONTRACTORS_MENU_ID:  # Display and process contractors
                MenuUI.display_contractors_menu()

                # Get user menu choice
                choice = MenuUI.get_menu_choice(1, 6)

                # Process user menu choice
                self.process_contractors_menu_choice(choice)

            else:  # Must be contracts menu so display and process this menu
                MenuUI.display_contracts_menu()

                # Get user menu choice
                choice = MenuUI.get_menu_choice(1, 10)

                # Process user menu choice
                self.process_contracts_menu_choice(choice)

    @staticmethod
    def display_main_menu():
        """
        Displays the main menu

        :return: None
        """
        print("\nMain Menu")
        print("-------------------")
        print("1. Clients Menu")
        print("2. Contractors Menu")
        print("3. Contracts Menu")
        print("4. Display Revenue")
        print("5. Exit")
        print("Please enter your choice (1 - 5): ", end="", flush=True)
        # Note: , end="", flush=True prevents newline after print()

    @staticmethod
    def display_clients_menu():
        """
        Displays clients menu

        :return: None
        """
        print("\nClients Menu")
        print("----------------------")
        print("1. Add Client")
        print("2. Remove Client")
        print("3. Display Client")
        print("4. Display All Clients")
        print("5. Return")
        print("Please enter your choice (1 - 5): ", end="", flush=True)
        # Note: , end="", flush=True prevents newline after print()

    @staticmethod
    def display_contractors_menu():
        """
        Displays contractors menu

        :return: None
        """
        print("\nContractors Menu")
        print("--------------------------------------")
        print("1. Add Contractor")
        print("2. Remove Contractor")
        print("3. Display Contractor")
        print("4. Display Contractors With Speciality")
        print("5. Display All Contractors")
        print("6. Return")
        print("Please enter your choice (1 - 6): ", end="", flush=True)
        # Note: , end="", flush=True prevents newline after print()

    @staticmethod
    def display_contracts_menu():
        """
        Displays contracts menu

        :return: None
        """
        print("\nContracts Menu")
        print("---------------------------------------------")
        print(" 1. Add Contract")
        print(" 2. Remove Contract")
        print(" 3. Allocate Contract")
        print(" 4. Complete Contract")
        print(" 5. Display Contract")
        print(" 6. Display Contracts For Owner")
        print(" 7. Display Contracts For Speciality")
        print(" 8. Display All Unallocated Contracts")
        print(" 9. Display Contracts Allocated To Contractor")
        print("10. Return")
        print("Please enter your choice (1 - 10): ", end="", flush=True)
        # Note: , end="", flush=True prevents newline after print()

    def process_main_menu_choice(self, choice):
        """
        Process the user choice made when main menu is current menu

        :param: choice: user choice to process as integer
        :return: None
        """
        if choice < 0:  # If choice is not valid do nothing
            pass

        elif choice == 1:  # Switch to clients menu
            MenuUI.switch_to_menu(MenuUI.__CLIENTS_MENU_ID)

        elif choice == 2:  # Switch to contractors menu
            MenuUI.switch_to_menu(MenuUI.__CONTRACTORS_MENU_ID)

        elif choice == 3:  # Switch to contracts menu
            MenuUI.switch_to_menu(MenuUI.__CONTRACTS_MENU_ID)

        elif choice == 4:  # Switch to contracts menu
            self.display_revenue()

        else:  # Must be choice 5 so action exit function
            self.action_exit_function()

    def process_clients_menu_choice(self, choice):
        """
        Process the user choice made when clients menu is current menu

        :param: choice: user choice to process as integer
        :return: None
        """
        if choice < 0:  # If choice is not valid do nothing
            pass

        elif choice == 1:  # Action Add Client function
            self.add_client()

        elif choice == 2:  # Action Remove Client function
            self.remove_client()

        elif choice == 3:  # Action Display Client function
            self.display_client()

        elif choice == 4:  # Action Display All Clients function
            self.display_all_clients()

        else:  # Must be choice 5 so switch to main menu
            MenuUI.switch_to_menu(MenuUI.__MAIN_MENU_ID)

    def process_contractors_menu_choice(self, choice):
        """
        Process the user choice made when contractors menu is current menu

        :param: choice: user choice to process as integer
        :return: None
        """
        if choice < 0:  # If choice is not valid do nothing
            pass

        elif choice == 1:  # Action Add Contractor function
            self.add_contractor()

        elif choice == 2:  # Action Remove Contractor function
            self.remove_contractor()

        elif choice == 3:  # Action Display Contractor function
            self.display_contractor()

        elif choice == 4:  # Action Display Contractors With Speciality function
            self.display_contractors_with_speciality()

        elif choice == 5:  # Action Display All Contractors function
            self.display_all_contractors()

        else:  # Must be choice 6 so switch to main menu
            MenuUI.switch_to_menu(MenuUI.__MAIN_MENU_ID)

    def process_contracts_menu_choice(self, choice):
        """
        Process the user choice made when contracts menu is current menu

        :param: choice: user choice to process as integer
        :return: None
        """
        if choice < 0:  # If choice is not valid do nothing
            pass

        elif choice == 1:  # Action Add Contract function
            self.add_contract()

        elif choice == 2:  # Action Remove Contract function
            self.remove_contract()

        elif choice == 3:  # Action Allocate Contract function
            self.allocate_contractor()

        elif choice == 4:  # Action Complete Contract function
            self.complete_contract()

        elif choice == 5:  # Action Display Contract function
            self.display_contract()

        elif choice == 6:  # Action Display Contracts For Owner function
            self.display_contracts_for_owner()

        elif choice == 7:  # Action Display Contracts For Speciality function
            self.display_contracts_for_speciality()

        elif choice == 8:  # Action Display All Unallocated Contracts function
            self.display_all_unallocated_contracts()

        elif choice == 9:  # Action Display Contracts Allocated To Contractor function
            self.display_contracts_allocated_to_contractor()

        else:  # Must be choice 10 so action switch to main menu
            MenuUI.switch_to_menu(MenuUI.__MAIN_MENU_ID)

    @staticmethod
    def switch_to_menu(menu_id):
        """
        Sets the current menu to menu_id parameter

        :param: menu_id: identifier of the menu to switch to as integer
        :return: None
        """
        MenuUI.__current_menu = menu_id

    @staticmethod
    def get_menu_choice(start, end):
        """
        Returns a user menu choice as an integer, this returns the entered menu choice if it is valid and returns -1 if
        not valid, a valid option must be between start and end parameters

        :param: start: first valid choice number as integer
        :param: end: last valid choice number as integer
        :return: user entered menu choice or -1 if entered choice is invalid
        """
        choice = MenuUI.get_int_input()

        if (choice >= start) and (choice <= end):
            return choice  # valid option choice

        return -1  # Invalid option choice entered

    @staticmethod
    def get_string_input():
        """
        Returns a user input as a string

        :return: user entered string
        """
        return input()

    @staticmethod
    def get_int_input():
        """
        Returns a user input as an int number

        :return: user entered integer number
        """
        return int(input())

    @staticmethod
    def get_float_input():
        """
        Returns a user input as a float number

        :return: user entered floating point number
        """
        return float(input())

    @staticmethod
    def get_bool_input():
        """
        Returns a user input as a boolean

        :return: user entered boolean
        """
        return bool(input())

    def display_revenue(self):
        """
         Display revenue accrued so far by main application by accessing its revenue property

        :return: None
        """
        print("\nCurrently accrued revenue is: £{0:.2f}".format(self.main_app.revenue))
        # In the format placeholder, ":.2f" means always show two decimals, for instance 1.2 would show as 1.20

    def add_client(self):
        """
        Delegate to the main application by calling its add client method, passing the name provided by the user

        :return: None
        """
        # Ask user for client name
        print("\nEnter client name: ", end="", flush=True)
        name = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a tuple with the first entry as
        # a boolean indicator if the operation completed successfully and the second entry as the newly added client
        success, client = self.main_app.add_client(name)

        # Output confirmation of new client added
        if success:
            print("\nAdded new:")
            print(client)
        else:
            print("\nError: new client could not be added")

    def remove_client(self):
        """
        Delegate to the main application by calling its remove client method, passing the identifier of the client to
        remove as provided by the user

        :return: None
        """
        # Ask user for client identifier to remove
        print("\nEnter identifier of client to remove: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a tuple with the first entry as
        # a boolean indicator if the operation completed successfully and the second entry as either the details of the
        # removed client if successfully remove or an error message if not successfully removed
        success, details = self.main_app.remove_client(ident)

        if success:
            print("\nRemoved:")
            print(details)
        else:
            print("\n" + details)

    def display_client(self):
        """
         Display client instance from main application by calling its get client method, passing the identifier of the
         client to display as provided by the user

        :return: None
        """
        # Ask user for client identifier to display
        print("\nEnter identifier of client to display: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return either the client instance
        # associated with the supplied identifier or None if not found
        client = self.main_app.get_client(ident)

        if not client:
            print("\nNo client with Id: {0}".format(ident))
        else:
            print("")
            print(client.make_displayable())  # Print found client

    def display_all_clients(self):
        """
         Display list of all client instances from main application by calling its get all clients method

        :return: None
        """
        # Delegate operation to the main application, the main application will return a list of all client instances,
        # note this could be the empty list if there are no client instances
        clients = self.main_app.get_all_clients()

        if not clients:
            print("\nNo clients to display")
        else:
            for client in clients:  # Print each client in turn
                print("")
                print(client.make_displayable())

    def add_contractor(self):
        """
        Delegate to the main application by calling its add contractor method, passing the name and speciality provided
        by the user

        :return: None
        """
        # Ask user for contractor name
        print("\nEnter contractor name: ", end="", flush=True)
        name = MenuUI.get_string_input()

        # Ask user for contractor speciality
        print("Enter contractor speciality: ", end="", flush=True)
        speciality = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a tuple with the first entry as
        # a boolean indicator if the operation completed successfully and the second entry as the newly added contractor
        success, contractor = self.main_app.add_contractor(name, speciality)

        # Output confirmation of new contractor added
        if success:
            print("\nAdded new:")
            print(contractor)
        else:
            print("\nError: new contractor could not be added")

    def remove_contractor(self):
        """
        Delegate to the main application by calling its remove contractor method, passing the identifier of the
        contractor to remove as provided by the user

        :return: None
        """
        # Ask user for contractor identifier to remove
        print("\nEnter identifier of contractor to remove: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a tuple with the first entry as
        # a boolean indicator if the operation completed successfully and the second entry as either the details of the
        # removed contractor if successfully remove or an error message if not successfully removed
        success, details = self.main_app.remove_contractor(ident)

        if success:
            print("\nRemoved:")
            print(details)
        else:
            print("\n" + details)

    def display_contractor(self):
        """
         Display contractor instance from main application by calling its get contractor method, passing the identifier
         of the contractor to display as provided by the user

        :return: None
        """
        # Ask user for contractor identifier to display
        print("\nEnter identifier of contractor to display: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return either the contractor instance
        # associated with the supplied identifier or None if not found
        contractor = self.main_app.get_contractor(ident)

        if not contractor:
            print("\nNo contractor with Id: {0}".format(ident))
        else:
            print("")
            print(contractor.make_displayable())  # Print found contractor

    def display_contractors_with_speciality(self):
        """
         Display list of all contractor instances from main application that match the speciality provided by the user
         by calling its get contractors with speciality method

        :return: None
        """
        # Ask user for speciality to match with contractor instances
        print("\nEnter speciality to match with contractors: ", end="", flush=True)
        speciality = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a list of all contractor
        # instances that match the user provided speciality, note this could be the empty list if there are no
        # contractor instances
        contractors = self.main_app.get_contractors_with_speciality(speciality)

        if not contractors:
            print("\nThere are no contractors with Speciality: {0}".format(speciality))
        else:
            for contractor in contractors:  # Print each contractor in turn
                print("")
                print(contractor.make_displayable())

    def display_all_contractors(self):
        """
         Display list of all contractor instances from main application by calling its get all contractors method

        :return: None
        """
        # Delegate operation to the main application, the main application will return a list of all contractor
        # instances, note this could be the empty list if there are no client instances
        contractors = self.main_app.get_all_contractors()

        if not contractors:
            print("\nNo contractors to display")
        else:
            for contractor in contractors:  # Print each contractor in turn
                print("")
                print(contractor.make_displayable())

    def add_contract(self):
        """
        Delegate to the main application by calling its add contract method, passing the contract type, owner,
        speciality and payment provided by the user

        :return: None
        """
        # Ask user for contract type, must be either "base", "fixed" or "advert"
        valid = False
        contract_types = ["b", "base", "f", "fixed", "a", "advert"]
        contract_type = "base"
        print("")
        while not valid:
            print("Enter contract type [(b)ase, (f)ixed or (a)dvert]: ", end="", flush=True)
            contract_type = MenuUI.get_string_input().lower()

            if contract_type in contract_types:  # Valid contract type so break from loop
                break

        # Ask user for contract owner identifier
        print("Enter contract owner: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Check if this owner exists as a client instance, the owner of a contract must be a valid client instance
        owner = self.main_app.get_client(ident)

        # If this owner does not exist then display an error message and abort
        if not owner:
            print("\nError: no client with Id: {0}, so this cannot be the contract owner".format(ident))
            return

        # Ask user for contract speciality
        print("Enter contract speciality: ", end="", flush=True)
        speciality = MenuUI.get_string_input()

        # Ask user for contract payment
        print("Enter contract payment: ", end="", flush=True)
        payment = MenuUI.get_float_input()

        # Delegate operation to the main application, the main application will return a tuple with the first entry as
        # a boolean indicator if the operation completed successfully and the second entry as the newly added contract
        success, contract = self.main_app.add_contract(contract_type, owner, speciality, payment)

        # Output confirmation of new contract added
        if success:
            print("\nAdded new:")
            print(contract)
        else:
            print("\nError: new contract could not be added")

    def remove_contract(self):
        """
        Delegate to the main application by calling its remove contract method, passing the identifier of the contract
        to remove as provided by the user

        :return: None
        """
        # Ask user for contract identifier to remove
        print("\nEnter identifier of contract to remove: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a tuple with the first entry as
        # a boolean indicator if the operation completed successfully and the second entry as either the details of the
        # removed contract if successfully remove or an error message if not successfully removed
        success, details = self.main_app.remove_contract(ident)

        if success:
            print("\nRemoved:")
            print(details)
        else:
            print("\n" + details)

    def allocate_contractor(self):
        """
        Delegate to the main application by calling its allocate contractor method, passing the contract being allocated
        and the contractor to allocate both as provided by the user

        :return: None
        """
        # Ask user for contract identifier to allocate contractor to
        print("\nEnter identifier of contract to allocate: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Get the contract with the user provided identifier, if this does not exist then display an error message and
        # abort
        contract = self.main_app.get_contract(ident)
        if not contract:
            print("\nError: no contract with Id: {0} so cannot allocate contractor to it".format(ident))
            return

        # If the contract is completed it cannot be allocated to a different contractor, so display an error message
        # and abort
        if contract.completed:
            print("\nError: contract with Id: {0} is completed so cannot allocate different contractor".format(ident))
            return

        # Ask user for contractor identifier to allocate this contract to
        print("Enter identifier of contractor to allocate to the contract: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Get the contractor with the user provided identifier, if this does not exist then display an error message and
        # abort
        contractor = self.main_app.get_contractor(ident)
        if not contractor:
            print("\nError: no contractor with Id: {0} so cannot allocate it to the contract".format(ident))
            return

        # If the contractor does not have the same speciality as the contract then display an error message and abort
        if not contractor.speciality == contract.speciality:
            print("\nError: contractor speciality and contract speciality differ so cannot allocate".format(ident))
            return

        # Allocate user provided contractor to user provided contract and display a confirmation of the change
        self.main_app.allocate_contractor(contract, contractor)
        print("\nContractor with Id: {0} allocated to contract with Id: {1}".format(contractor.id, contract.id))

    def complete_contract(self):
        """
        Delegate to the main application by calling its complete contract method, passing the contract being completed
        as provided by the user

        :return: None
        """
        # Ask user for contract identifier to complete
        print("\nEnter identifier of contract to complete: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Get the contract with the user provided identifier, if this does not exist then display an error message and
        # abort
        contract = self.main_app.get_contract(ident)
        if not contract:
            print("\nError: no contract with Id: {0} so cannot complete it".format(ident))
            return

        # If the user provided contract is already completed then display an error message and abort
        if contract.completed:
            print("\nError: contract with Id: {0} already completed".format(ident))
            return

        # If the user provided contract has no allocated contractor then display an error message and abort
        if not contract.contractor_allocated:
            print("\nError: contract with Id: {0} is not allocated to contractor so cannot be completed".format(ident))
            return

        # Flag user provided contract as completed and display a confirmation of the change
        self.main_app.complete_contract(contract)
        print("\nContract with Id: {0} is now completed".format(contract.id))

    def display_contract(self):
        """
          Display contract instance from main application by calling its get contract method, passing the identifier of
          the contract to display as provided by the user

         :return: None
         """
        # Ask user for contract identifier to display
        print("\nEnter identifier of contract to display: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return either the contract instance
        # associated with the supplied identifier or None if not found
        contract = self.main_app.get_contract(ident)

        if not contract:
            print("\nNo contract with Id: {0}".format(ident))
        else:
            print("")
            print(contract.make_displayable())  # Print found contract

    def display_contracts_for_owner(self):
        """
         Display list of all contract instances from main application that match the owner provided by the user by
         calling its get contracts for owner method

        :return: None
        """
        # Ask user for owner identifier to match with contracts
        print("\nEnter identifier of owner to match with contracts: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Get the owner with the user provided identifier, if this does not exist then display an error message and
        # abort
        owner = self.main_app.get_client(ident)
        if not owner:
            print("\nError: no owner with Id: {0} so no contracts to display".format(ident))
            return

        # Delegate operation to the main application, the main application will return a list of all contract instances
        # that match the user provided owner, note this could be the empty list if there are no contract instances
        contracts = self.main_app.get_contracts_for_owner(owner)

        if not contracts:
            print("\nNo contracts are owned by owner with Id: {0}".format(ident))
        else:
            for contract in contracts:  # Print each contract in turn
                print("")
                print(contract.make_displayable())

    def display_contracts_for_speciality(self):
        """
         Display list of all contract instances from main application that match the speciality provided by the user by
         calling its get contracts with speciality method

        :return: None
        """
        # Ask user for speciality to match with contract instances
        print("\nEnter speciality to match with contracts: ", end="", flush=True)
        speciality = MenuUI.get_string_input()

        # Delegate operation to the main application, the main application will return a list of all contract instances
        # that match the user provided speciality, note this could be the empty list if there are no contract instances
        contracts = self.main_app.get_contracts_for_speciality(speciality)

        if not contracts:
            print("\nThere are no contracts for Speciality: {0}".format(speciality))
        else:
            for contract in contracts:  # Print each contract in turn
                print("")
                print(contract.make_displayable())

    def display_all_unallocated_contracts(self):
        """
         Display list of all unallocated contract instances from main application by calling its get all unallocated
         contracts method

        :return: None
        """
        # Delegate operation to the main application, the main application will return a list of all contract instances
        # that do not have a contractor allocated to them
        contracts = self.main_app.get_all_unallocated_contracts()

        if not contracts:
            print("\nThere are no unallocated contracts")
        else:
            for contract in contracts:  # Print each contract in turn
                print("")
                print(contract.make_displayable())

    def display_contracts_allocated_to_contractor(self):
        """
         Display list of all contract instances from main application that are allocated to the contractor provided by
         the user by calling its get contracts allocated to contractor method

        :return: None
        """
        # Ask user for contractor identifier to match with contracts
        print("\nEnter identifier of contractor to match with contracts: ", end="", flush=True)
        ident = MenuUI.get_string_input()

        # Get the contractor with the user provided identifier, if this does not exist then display an error message and
        # abort
        contractor = self.main_app.get_contractor(ident)
        if not contractor:
            print("\nError: no contractor with Id: {0} so no contracts to display".format(ident))
            return

        # Delegate operation to the main application, the main application will return a list of all contract instances
        # that are allocated to the user provided contractor, note this could be the empty list if there are no contract
        # instances
        contracts = self.main_app.get_contracts_allocated_to_contractor(contractor)

        if not contracts:
            print("\nContractor with Id: {0} is not allocated to any contracts".format(ident))
        else:
            for contract in contracts:  # Print each contract in turn
                print("")
                print(contract.make_displayable())

    def action_exit_function(self):
        """
        Sets the finished flag to True

        :return: None
        """

        MenuUI.__finished = True

        print("\nThank you for using {0}, bye".format(self.main_app.name))
