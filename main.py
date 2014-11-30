__author__ = 'hali'


from staff import Staff


choices = """You have three choices
1 >> add new employee
2 >> print employee record by name
3 >> print all employees
Type CRTL+C to exit program"""


def add_new(mystaff):
    name = input("Name: ")
    number = int(input("Number: "))
    years = int(input("Years Worked: "))
    salary = float(input("Salary: "))
    mystaff.add_employee(name, number, years, salary)


def print_emp_details(e_name, mystaff):
    for emp in mystaff.employee_list:
        if emp.get_name() == e_name:
            print(emp)


def print_staff():
    for emp in mystaff.employee_list:
        print(emp)


if __name__ == '__main__':
    mystaff = Staff()
    print("Welcome to my Staff Management Program")
    print(choices)
    while True:
        choice = input("Enter Choice\n")
        if choice == "1":
            add_new(mystaff)
        elif choice == "2":
            e_name = input("Name: ")
            print_emp_details(e_name, mystaff)
        elif choice == "3":
            print_staff()
        else:
            print("Invalid Input")
            print(choices)
