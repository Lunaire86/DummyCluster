##
# Class: TEST
# @author: marispau


from cluster import Cluster
from fileHandler import FileHandler


class Test:
    """
    This class handles all the testing, and calls various methods on the chosen Cluster objects.
    """

    def __init__(self, name, file_name):
        """
        Test class constructor takes name of cluster to be tested, and its respective file.
        :param name: str
        :param file_name: str
        """
        self._file_handler = FileHandler(file_name)
        self._node_orders = self._file_handler.get_orders()
        self._max_nodes_per_rack = self._file_handler.get_max_nodes()
        self._cluster = Cluster(name, self._max_nodes_per_rack)
        self._cluster.add_nodes_to_cluster(self._node_orders)

    def print_orders(self):
        """
        Prints to terminal: orders read from file.
        """
        print("ORDERS READ FROM FILE:")
        counter = 0
        for i in self._node_orders:
            counter += 1
            print(f"Order {counter}: {i}")
        if counter == 0:
            print("No orders found.\n")
        else:
            print("End of order list.\n")

    def print_cluster_info(self):
        """
        Prints to terminal: information about the Cluster object.
        """
        print("ABOUT CLUSTER:")
        print(f"{repr(self._cluster)}\n{self._cluster}\n")

    def print_cluster_numbers(self, req_mem):
        """
        Prints to terminal: numbers of interest tied to the Cluster object.
        :param req_mem: int
        """
        print("PRINT VARIOUS COUNTERS:")
        print(f"Total number of racks: {self._cluster.count_racks()}\nTotal number of nodes: "
              f"{self._cluster.count_nodes()}\nTotal number of CPUs: {self._cluster.count_cpus()}\n"
              f"Number of nodes with more than {req_mem} GB memory: "
              f"{self._cluster.count_all_nodes_with_enough_memory(req_mem)}\n")

    def print_check_for_holes(self):
        """
        Prints to terminal: whether or not there are holes in the Rack objects.
        """
        print("CHECK FOR HOLES IN RACKS:")
        print(self._cluster.check_for_holes_in_racks())
        if self._cluster.count_racks() != 0:
            print(f"Nodes in last rack: {self._cluster.count_nodes_in_last_rack()}")
        else:
            print()
