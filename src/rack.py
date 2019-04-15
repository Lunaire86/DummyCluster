##
# Class: Rack
# @author: marispau


from node import Node


class Rack:
    """
    Saves node objects of a specified rack in a list.
    All racks operate with a the same amount of maximum nodes.
    """

    def __init__(self):
        """
        Rack objects only hold a list of nodes.
        """
        self._list_of_nodes = []

    def __repr__(self):
        """
        Object representation.
        :return: str
        """
        return f"Rack({self._list_of_nodes}"

    def __str__(self):
        """
        String representation of the object.
        :return: str
        """
        return f"Rack object containing {self._list_of_nodes}"

    def __len__(self):
        """
        Adds the len() method.
        :return: int
        """
        return len(self._list_of_nodes)

    def __iter__(self):
        """
        Adds the iter() method.
        :return: iterator
        """
        return iter(self._list_of_nodes)

    def is_full(self, maximum_nodes):
        """
        Checks if the rack is full.
        :param maximum_nodes: int
        :return: bool
        """
        if len(self._list_of_nodes) == maximum_nodes:
            return True
        return False

    def insert_node(self, memory, cpu):
        """
        Place node objects in the rack. Parameters sent to Node class.
        :param memory: int
        :param cpu: int
        """
        self._list_of_nodes.append(Node(memory, cpu))

    def count_nodes(self):
        """
        Counts number of nodes in the Rack object.
        :return: int
        """
        return len(self._list_of_nodes)

    def count_cpus(self):
        """
        Counts numbers of CPUs in the Rack object.
        :return: int
        """
        cpu_counter = 0
        for node in self._list_of_nodes:
            number_of_cpus = node.get_cpu()
            cpu_counter += number_of_cpus
        return cpu_counter

    def count_nodes_with_enough_memory(self, required_memory):
        """
        Count nodes with a minimum amount of memory given by the parameter.
        :param required_memory: int
        :return: int
        """
        enough_memory = 0
        for node in self._list_of_nodes:
            if node.has_enough_memory(required_memory):
                enough_memory += 1
        return enough_memory
