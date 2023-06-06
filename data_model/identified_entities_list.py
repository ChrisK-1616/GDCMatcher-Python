# File: identified_entities_list.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
# Consts
# Globals


# Classes
class IdentifiedEntitiesList:
    """
    Base class for all identified entity list classes, it contains an encapsulated list as the data container and
    provides methods to add entity instances to the container, remove entity instances from the container, return a
    an entity instance that is searched for by its identifier, return the number of entities held in the container and
    return whether an entity exists in the container or not (using the entity identifier)
    """

    def __init__(self):
        """
 -      Initialiser - instance variables:
            data: container for the added identified entities, as list, property with read-only access
        """
        self.__data = []  # The data property is a list of the contained identified entities

    @property
    def data(self):
        return self.__data

    def __str__(self):
        """
        To string method

        :return: string representation of this identified entity list instance
        """
        return "{0}:{1}".format(IdentifiedEntitiesList.__name__, self.count())

    def count(self):
        """
        Return the number of entities contained in this container

        :return: number of entities contained as integer
        """
        return len(self.data)

    def add(self, entity):
        """
        Add supplied entity to the container, but only if an entity with the a given identifier does not already
        exist in the container, return True if added successfully and False if not

        :param entity: entity to add to the container as IdentifiedEntity
        :return: True if added successfully, False if not
        """
        # Check if entity with same identifier as supplied entity exists in container
        if self.has(entity.id):
            return False  # Exists so abort and return False

        # Append entity to container
        self.data.append(entity)

        return True  # Successful

    def remove(self, entity):
        """
        Remove supplied entity from the container, but only if an entity with the a given identifier does exist in the
        container, return True if removed successfully and False if not

        :param entity: entity to remove from the container as IdentifiedEntity
        :return: True if added successfully, False if not
        """
        return self.remove_by_id(entity.id)

    def remove_by_id(self, ident):
        """
        Remove entity with supplied identifier from the container, but only if an entity with the given identifier
        exists in the container, return True if removed successfully and False if not

        :param ident: identifier of the entity to be removed as string
        :return: True if added successfully, False if not
        """
        # Check if entity exists in the container by finding its index, index returned of -1 means it does not exist in
        # the container
        entity_index = self.index_by_id(ident)

        if entity_index < 0:  # Does not exist so abort and return False
            return False

        # Found so remove entity from container
        del self.data[entity_index]

        return True  # Successful

    def find_by_id(self, ident):
        """
        Return the entity with the supplied identifier or None if no entity with supplied identifier exists in container

        :param ident: identifier of the entity to be found as string
        :return: entity instance if it exists or None if not
        """
        # Find entity with supplied identifier in the container
        for entity in self.data:
            if entity.id == ident:
                return entity  # Found so return this entity

        return None  # Not found so return None

    def index_by_id(self, ident):
        """
        Return the index in the container of the entity with the supplied identifier or -1 if no entity with supplied
        identifier exists in container

        :param ident: identifier of the entity for which index is to be found as string
        :return: index in container of entity instance if it exists or -1 if not as integer
        """
        # Find entity with supplied identifier in the container, recording index as this progresses
        index = 0
        for entity in self.data:
            if entity.id == ident:
                return index  # Found so return the index
            index += 1  # increment the index counter

        return -1  # Not found so return -1

    def index_of(self, entity):
        """
        Return the index in the container of the supplied entity or -1 if no such entity with exists in container

        :param entity: entity for which index is to be found as IdentifiedEntity
        :return: index in container of entity instance if it exists or -1 if not as integer
        """
        # Find supplied entity using its identifier
        return self.index_by_id(entity.id)

    def has(self, ident):
        """
        Check for the entity with the supplied identifier in the container, if it exists then return True, if not then
        return False

        :param ident: identifier of the entity to check for in the container
        :return: True if entity exists, False if not
        """
        # Find entity with supplied identifier in the container
        for entity in self.data:
            if entity.id == ident:
                return True  # Found so return True

        return False  # Not found so return False
