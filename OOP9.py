class Employee:
    def __init__(self,name,base_pay,bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
    
    def getPay(self):
        return self.base_pay + self.bonus

class SalesEmployee(Employee):
    def __init__(self,name,base_pay,bonus,incentive):
        super().__init__(name,base_pay,bonus)
        # self.name = name
        # self.base_pay = base_pay
        # self.bonus = bonus
        self.incentive = incentive
    
    def getPay(self):
        return super().getPay() + self.incentive

dude1 = Employee("John", 23000,3000)
dude2 = SalesEmployee("Johnny", 24000,4000,1500)

#Access method from Parent class
print(dude1.getPay())
print(dude2.getPay())
