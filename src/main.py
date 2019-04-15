##
# Main program
# @author: marispau


from test import Test


def run_tests(test_unit, file_name):
    """
    Runs various tests to make sure the program works as intended.
    :param test_unit: str
    :param file_name: str
    """
    program = test_unit
    if program == "Abel":
        print("\nYOU ARE RUNNING THE MAIN PROGRAM\n")
    elif program == "Test 1":
        print("\nYOU ARE RUNNING TEST PROGRAM 1\n")
    elif program == "Test 2":
        print("\nYOU ARE RUNNING TEST PROGRAM 2\n")
    else:
        return "Error"

    run = Test(test_unit, file_name)

    run.print_orders()
    run.print_cluster_info()
    run.print_cluster_numbers(32)
    run.print_check_for_holes()


def main():
    """
    The main program sets the values for the tests and initiates the testing.
    User input driven.
    """
    abel = "Abel", "data.txt"
    test_1 = "Test 1", "zero_nodes.txt"
    test_2 = "Test 2", "zero_orders.txt"

    start_msg = "\n<<PROGRAM STARTED>>"
    choices = "\nPress [A] for Abel\nPress [1] for test 1\nPress [2] for test 2\nPress [X] to exit\n"
    print(start_msg, choices)

    user_input = input().strip().upper()
    valid_input = ("A", "1", "2", "X")

    while user_input not in valid_input:
        print("Invalid input.\n", choices)
        user_input = input().strip().upper()

    while user_input != "X":
        if user_input not in valid_input:
            print("Invalid input.\n", choices)
            user_input = input().strip().upper()

        if user_input == "A":
            run_tests(*abel)
            print(choices)
            user_input = input().strip().upper()

        elif user_input == "1":
            run_tests(*test_1)
            print(choices)
            user_input = input().strip().upper()

        elif user_input == "2":
            run_tests(*test_2)
            print(choices)
            user_input = input().strip().upper()

    print("TERMINATED")


if __name__ == '__main__':
    main()
