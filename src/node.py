##
# Class: Node
# @author: marispau


class Node:
    """
    Lets the user create node objects and request information.
    """

    def __init__(self, memory, cpu):
        """
        Initialises node objects with a given amount of memory and CPUs
        :param memory: int
        :param cpu: int
        """
        if cpu < 1 or cpu > 2:
            raise ValueError("Invalid number. Node can only have 1 or 2 CPUs.")
        self._memory = int(memory)
        self._cpu = cpu

    def __repr__(self):
        """
        Object representation.
        :return: str
        """
        return f"Node({self._memory}, {self._cpu})"

    def __str__(self):
        """
        String representation of the object.
        :return: str
        """
        return f"Node with {self._memory} GB memory and {self._cpu} CPUs."

    def has_enough_memory(self, required_memory):
        """
        Checks if the node has got the requested amount of memory or not.
        :param required_memory: int
        :return: bool
        """
        if self._memory >= required_memory:
            return True
        return False

    def get_cpu(self):
        """
        Counts number of CPUs in the Node object.
        :return: int
        """
        return self._cpu
