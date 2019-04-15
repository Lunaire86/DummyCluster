##
# Class: FileHandler
# @author: marispau


class FileHandler:
    """ This class handles the files and readies the data for usage.
        It returns a list that holds lists of nodes to be distributed in racks,
        and also the maximum nodes per rack.
    """

    def __init__(self, file_name):
        """
        This creates the file object and separates the different orders in lists.
        :param file_name: str
        """
        with open(f"./orders/{file_name}") as file:
            self._list_of_nodes = []
            self._max_nodes_per_rack = file.readline()

            for line in file.readlines():
                lst = [int(_.strip()) for _ in line.split(' ')]
                self._list_of_nodes.append(lst)

        file.close()

    def __repr__(self):
        """
        Object representation.
        :return: str
        """
        return f"FileHandler({self._list_of_nodes})"

    def get_orders(self):
        """
        Returns the number of nodes per order.
        :return: int
        """
        return self._list_of_nodes

    def get_max_nodes(self):
        """
        Returns maximum nodes per rack, as given in the first line of the file.
        :return: int
        """
        return self._max_nodes_per_rack

    def get_info(self):
        """
        Generator that yields a string representation of each nested list.
        :return: generator
        """
        for i in range(len(self._list_of_nodes)):
            yield f"{self._list_of_nodes[i][0]} nodes with {self._list_of_nodes[i][1]} GB memory and " \
                  f"{self._list_of_nodes[i][2]} CPU(s)."
