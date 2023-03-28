from EmployeeFactory import EmployeeFactory
from AnimalFactory import AnimalFactory

Manager1 = EmployeeFactory.createManager("Joko")
Manager2 = EmployeeFactory.createManager("Moro")
Staff1 = EmployeeFactory.createStaff("Agus")
Staff2 = EmployeeFactory.createStaff("Sanjaya")
Manager1.get_detail()

kucing1 =  AnimalFactory.create("cat")
