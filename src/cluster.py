##
# Class: Cluster
# @author: marispau


from rack import Rack


class Cluster:
    """
    Keeps track of a list of racks.
    Create new racks as needed and insert nodes.
    """

    def __init__(self, name, max_nodes_per_rack):
        """
        Constructor for the Cluster class initiates the objects with a name,
        a list of racks and maximum amount of nodes allowed per rack.
        :param name: str
        :param max_nodes_per_rack: int
        """
        self._name = name
        self._list_of_racks = []
        self._max_nodes_per_rack = int(max_nodes_per_rack)

    def __repr__(self):
        """
        Object representation.
        :return: str
        """
        return f"Cluster({self._name}, {self._max_nodes_per_rack})"

    def __str__(self):
        """
        String representation of the object.
        :return: str
        """
        return f"Cluster {self._name} contains racks that takes a maximum of {self._max_nodes_per_rack} node objects."

    def __iter__(self):
        """
        Adds the iter() method.
        :return: iterator
        """
        return iter(self._list_of_racks)

    def add_nodes_to_cluster(self, order_list):
        """
        Takes a list of lists with order data and adds nodes accordingly.
        Checks whether the last rack in the list is full or not.
        :param order_list: list
        """
        for order in order_list:

            nodes_to_add = order[0]
            memory = order[1]
            cpu = order[2]

            if len(self._list_of_racks) == 0:
                new_rack = Rack()
                self._list_of_racks.append(new_rack)

                if nodes_to_add >= self._max_nodes_per_rack:
                    [new_rack.insert_node(memory, cpu) for _ in range(self._max_nodes_per_rack)]
                    nodes_to_add -= self._max_nodes_per_rack

                elif nodes_to_add < self._max_nodes_per_rack:
                    [new_rack.insert_node(memory, cpu) for _ in range(nodes_to_add)]
                    nodes_to_add = 0

            for nodes in range(nodes_to_add):

                if self._list_of_racks[-1].is_full(self._max_nodes_per_rack):
                    new_rack = Rack()
                    self._list_of_racks.append(new_rack)
                    new_rack.insert_node(memory, cpu)
                else:
                    self._list_of_racks[-1].insert_node(memory, cpu)

    def count_racks(self):
        """
        Counts number of racks in Cluster object.
        :return: int
        """
        return len(self._list_of_racks)

    def count_cpus(self):
        """
        Counts number of CPUs in the Cluster object.
        :return: int
        """
        cpu_counter = 0
        for rack in self._list_of_racks:
            cpu_counter += rack.count_cpus()
        return cpu_counter

    def count_nodes(self):
        """
        Counts total amount of Node objects in the Cluster object.
        :return: int
        """
        counter = 0
        for rack in self._list_of_racks:
            nodes_found = rack.count_nodes()
            counter += nodes_found
        return counter

    def count_all_nodes_with_enough_memory(self, required_memory):
        """
        Counts all Node objects with enough memory as per the parameter value.
        :param required_memory: int
        :return: int
        """
        counter = 0
        for rack in self._list_of_racks:
            node_count = rack.count_nodes_with_enough_memory(required_memory)
            counter += node_count
        return counter

    def check_for_holes_in_racks(self):
        """
        Checks for Rack objects that are not filled up (except the last in the list)
        :return: str
        """
        counter = 0
        if self.count_racks() > 0:
            anticipated_full_racks = self.count_nodes() // self._max_nodes_per_rack
            for rack in self._list_of_racks:
                if rack.is_full(self._max_nodes_per_rack):
                    counter += 1
        else:
            return "A cluster has no racks."
        if counter == anticipated_full_racks:
            return f"Expected {anticipated_full_racks} full racks, got {counter}."

    def count_nodes_in_last_rack(self):
        """
        Counts Node objects in the last Rack object.
        :return: int
        """
        try:
            return self._list_of_racks[-1].count_nodes()
        except IndexError:
            return 0
