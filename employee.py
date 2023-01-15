from Member import Member


class Employee(Member):
    def __init__(self, name, age, pnum, address, salary, specialization):
        Member.__init__(self, name, age, pnum, address, salary)
        self.specialization = specialization

    def work(self):
        print(self.name + " is working as an employee")

    def getsalary(self):
        print(self.name + "'s salary is " + str(self.salary))
