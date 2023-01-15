from Member import Member


class Manager(Member):
    def __init__(self, name, age, pnum, address, salary, department):
        Member.__init__(self, name, age, pnum, address, salary)
        self.department = department

    def work(self):
        return print(self.name + " is working as a manager")

