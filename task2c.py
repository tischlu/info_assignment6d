#from vehicle import *
#from customer import *


class Employee(object):
    emp_id = 0

    def __init__(self, name):
        self.__name = name
        self.__id = Employee.emp_id
        Employee.emp_id += 1


    ######## CODE MISSING HERE

    def __str__(self):
        return "Employee: " + self.__name + " is of type " + Employee.get_title(self)

    ######## CODE MISSING HERE

    def get_name(self):
        return self.__name

    ######## CODE MISSING HERE

    def get_title(self):
        return "Subordinate"
        ######## CODE MISSING HERE


class Manager(Employee):
    def get_title(self):
        return "Manager"


    def get_sales_report(self, salesman):
        try:
            sum(Salesman.sales[salesman])
        except KeyError as err:
            print(salesman + " does not have any sales yet!")


class Salesman(Employee):
    sales = {}

    def sale(self, vehicle, sales_price, customer):
        if customer.credit_score():
            if Salesman.sales[Salesman()]:
                Salesman.sales[Salesman].append(sales_price)
            else:
                Salesman.sales[Salesman()] = sales_price
        else:
            print(customer + " does not have a high enough credit score.")
        ######## CODE MISSING HERE


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

# print(Eric) # expected output: Employee: Eric is of type Manager
# print(Kyle) # expected output: Employee: Kyle is of type Subordinate
# print(Stan) # expected output: Employee: Stan is of type Subordinate
# print(Kenny) # expected output: Employee: Kenny is of type Subordinate
# print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2, 6000, Heidi)

# Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000
