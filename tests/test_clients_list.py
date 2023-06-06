# File: test_clients_list.py
# Description: Automated tests for elements of Game Developer Contract Matcher (GDCMatcher) case study prototype
# Author: Chris Knowles


# Imports
import unittest
from data_model.clients_list import ClientsList
from data_model.identified_entity import IdentifiedEntity
from data_model.client import Client


# Consts
# Globals


# Classes
class TestClientsList(unittest.TestCase):
    """
    Test fixture to exercise the methods from the clients list class
    """
    def setUp(self):
        """
        Set up run before every test case

        :return:
        """
        # Create a new clients list before every test case and add some sample clients to it
        self.clients_list = ClientsList()

        # Force the reset of the Client class next identifier counter to 1000, needs to be done through the
        # IdentifiedEntity class since this counter is in the base class
        IdentifiedEntity._IdentifiedEntity__next_id = 1000

        # Add 4 instances of clients (with ids of CL1000, CL1001, CL1002, CL1003), note - this is done using the data
        # list accessed directly in clients list instance as we cannot be sure the add() method works yet
        self.clients_list.data.append(Client("Ubisoft Entertainment"))
        self.clients_list.data.append(Client("Electronic Arts Inc"))
        self.clients_list.data.append(Client("Bethesda Softworks LLC"))
        self.clients_list.data.append(Client("Blizzard Entertainment Inc"))

    def test_add_new_id(self):
        """
        Test case to check a new client can be added to the clients list using the add() method

        :return: None
        """
        # Arrange
        in_client_name = "New Client"
        ex_clients_count = 5

        # Act, note - use count of clients in the clients list to check new client has been added (is this the best
        # approach? if not why? and what alternative approach to use?)
        self.clients_list.add(Client(in_client_name))
        ac_clients_count = len(self.clients_list.data)

        # Assert
        self.assertEqual(ex_clients_count, ac_clients_count,
                         "Test failed, expected client count: {0} got clients count: {1}".
                         format(ex_clients_count, ac_clients_count))

    def test_add_existing_id(self):
        """
        Test case to check a new client can be added to the clients list using the add() method if this will cause a
        clash with an existing client unique identifier

        :return: None
        """
        # Arrange, note - we have to artificially reset the next id counter in the Client class so when using add() it
        # tries to use an existing identifier
        IdentifiedEntity._IdentifiedEntity__next_id = 1000  # Force update of private __next_id class property
        in_client_name = "New Client"
        ex_clients_count = 4  # Should not add a new client with existing identifier

        # Act, note - use count of clients in the clients list to check new client has been added (is this the best
        # approach? if not why? and what alternative approach to use?)
        self.clients_list.add(Client(in_client_name))
        ac_clients_count = len(self.clients_list.data)

        # Assert
        self.assertEqual(ex_clients_count, ac_clients_count,
                         "Test failed, expected client count: {0} got clients count: {1}".
                         format(ex_clients_count, ac_clients_count))

    def test_has_client_CL1001(self):
        """
        Test case to check if the has() method returns True if an identifier for an existing client is passed to it

        :return: None
        """
        # Arrange
        in_client_id = "CL1001"

        # Act
        ac_result = self.clients_list.has(in_client_id)

        # Assert
        self.assertTrue(ac_result,
                        "Test failed, expected result of True")

    def test_has_client_CL9999(self):
        """
        Test case to check if the has() method returns False if an identifier for a non-existing client is passed to it

        :return: None
        """
        # Arrange
        in_client_id = "CL9999"

        # Act
        ac_result = self.clients_list.has(in_client_id)

        # Assert
        self.assertFalse(ac_result,
                        "Test failed, expected result of False")


if __name__ == "__main__":
    unittest.main()
