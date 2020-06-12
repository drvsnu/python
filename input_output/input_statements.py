def sum_of_two_numbers():
    # Read 2 numbers and print sum
    x = int(input("Enter int value:"))
    y = int(input("Enter int value:"))
    print("The sum of 2 numbers:", x + y)
    # In other way
    print("The sum of 2 numbers:", int(input("Enter int value:")) + int(input("Enter int value:")))


def read_employee_data():
    # Read employee data from input keyboard eno, ename, esal, eaddr and married
    eno = int(input("Enter employee no.:"))
    ename = input("Enter employee name:")
    esal = float(input("Enter employee salary:"))
    eaddr = input("Enter employee address:")
    emarried = bool(input("Enter employee is married?:"))
    print("Please confirm information .....!")
    print("Employee No:", eno)
    print("Employee Name:", ename)
    print("Employee Salary:", esal)
    print("Employee Address:", eaddr)
    print("Employee Married:", emarried)


def read_multiple_values_from_input_in_single_line():
    a, b = [int(i) for i in input("Enter 2 int values separated by space:").split()]
    print("The Product :", a * b)


def read_different_data_at_a_time():
    a, b, c = [eval(i) for i in input("Enter different data values separated by space:").split()]
    print("Type of a:", type(a))
    print("Type of b:", type(b))
    print("Type of c:", type(c))


def read_group_of_int_values_from_command_line_arguments():
    from sys import argv
    print("Length of args:", len(argv))
    print("List of argv:", argv)


if __name__ == "__main__":
    # sum_of_two_numbers()
    # read_employee_data()
    # read_multiple_values_from_input_in_single_line()
    # read_different_data_at_a_time()
    read_group_of_int_values_from_command_line_arguments()
