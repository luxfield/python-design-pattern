from Employee import Employee

class EmployeeFactory:
    def createManager(name: str) -> Employee:
        return Employee(name, "Manager", "10000000")

    def createStaff(name: str) -> Employee:
        return Employee(name, "Staff", "5000000")
