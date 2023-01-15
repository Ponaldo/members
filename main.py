import employee
import manager


def main():
    purab = employee.Employee("Purab", 17, 9046163132, "Avenue Royale", 50, "Janitor")
    pawan = manager.Manager("Pawan", 38, 9047199845, "Lakeside", 9999999, "Technology")
    purab.work()
    pawan.work()
    purab.getsalary()
    purab.prtaddress()


main()
