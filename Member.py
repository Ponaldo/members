

class Member:
    def __init__(self, name, age, pnum, address, salary):
        self.name = name
        self.age = age
        self.pnum = pnum
        self.address = address
        self.salary = salary

    def work(self):
        print(self.name + " is working as a member")

    def prtaddress(self):
        print(self.address)
