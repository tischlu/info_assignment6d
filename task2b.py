#from vehicle import *
import random

class Customer(object):
    def __init__(self, name):
        self.__name = name
        self.__score = Customer.credit_score(self)

    ######## CODE MISSING HERE

    def __str__(self):
        return "Customer: " + str(self.__name)

    ######## CODE MISSING HERE

    def credit_score(self):
        x = random.randint(0, 100)
        if x > 60:
            return True
        else:
            return False

    ######## CODE MISSING HERE

    def get_score(self):
        return self.__score
        ######## CODE MISSING HERE


class VIP_Customer(Customer):
    def credit_score(self):
        return True
        ######## CODE MISSING HERE


### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

print(Wendy) # expected output: Customer: Wendy
print(Heidi) # expected output: Customer: Heidi

print(Wendy.get_score()) # expected output: True
print(Heidi.get_score()) # expected output: True
