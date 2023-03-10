from enum import Enum

# class Discount:
#     def __init__(self,name, discountAppliedFunction:function):
#         self.name = '\'A\' name discount'
#         self.dicsountApplied = discountAppliedFunction
    

class Dependent:
    def __init__(self, name:str, employee:object):
        self.name = name
        self.dependentOf = employee
    

class Employee:
    def __init__(self, name, salary = 2000, optedForBenefits = True):
        self.name = name
        self.salary = salary
        self.dependents = []
        self.optedForBenefits = optedForBenefits
        
    
    def addDependent(self, dependent:object) -> None:
        for dep in self.dependents:
            if dep.name == dependent.name:
                print(f"Dependent already exist")
                return
        self.dependents.append(dependent)
        print(f"Dependent added successfully")
        return
        
class PayCheckCalculator:
    def __init__(self,):
        self.__BENEFITS_COST_PER_YEAR = 1000
        self.__DEPENDENT_COST_PER_YEAR = 500
        self.__DISCOUNT_RATE_FOR_A_NAME = 0.1
        self.__NO_OF_PAYCHECKS = 26
        self.availableDiscounts = []
    
    def addDiscount(discount:object):
        self.availableDiscounts.append(discount)
        return 
    
    def checkNameDiscountApplied(self, person) -> bool:
        if person.name.startswith('A') or person.name.startswith('a'):
            return True
        return False
    
    def calculateBenefitCost(self, person: object, isDependent = False) -> float:
        benefitCost = self.__BENEFITS_COST_PER_YEAR if not isDependent else self.__DEPENDENT_COST_PER_YEAR
        if person.name.startswith('A') or person.name.startswith('a'):
            benefitCost *= (1 - self.__DISCOUNT_RATE_FOR_A_NAME)
        return benefitCost

    def calculateTotalCost(self, employee: object) -> tuple:
        dependentDiscountApplied = 0
        employeeDiscountApplied = 1 if self.checkNameDiscountApplied(employee) else 0
        dependentBenefitCost = 0
        employeeBenefitCost = 0
        if employee.optedForBenefits:
            employeeBenefitCost = self.calculateBenefitCost(employee)
            for dependent in employee.dependents:
                dependentBenefitCost += self.calculateBenefitCost(dependent, True)
                if self.checkNameDiscountApplied(dependent):
                    dependentDiscountApplied +=1
        totalCost = employeeBenefitCost + dependentBenefitCost
        return (employeeBenefitCost, employeeDiscountApplied, dependentBenefitCost, dependentDiscountApplied, totalCost)
    
    def calculatePayCheck(self, employee: object) -> None:
        empSalaryBeforeDeductions = employee.salary
        employeeBenefitCost, employeeWithDiscount, dependentBenefitCost, dependentWithDiscount, totalBenefitCost = self.calculateTotalCost(employee1)
        empSalaryAfterDeductions = empSalaryBeforeDeductions - (totalBenefitCost/ self.__NO_OF_PAYCHECKS)
        monthlyEmployeeBenefitCost = employeeBenefitCost/self.__NO_OF_PAYCHECKS
        monthlyDependentBenefitCost = dependentBenefitCost/self.__NO_OF_PAYCHECKS
        monthlyTotalCost = empSalaryBeforeDeductions - (monthlyEmployeeBenefitCost + monthlyDependentBenefitCost)
        assert(monthlyTotalCost, empSalaryAfterDeductions)
        
        print(f"\t\t\tPaycheck breakdown for {employee.name}")
        print(f"Gross Employee Salary:\t\t ${empSalaryBeforeDeductions}")
        print(f"Employee Benefit Cost: \t\t -${monthlyEmployeeBenefitCost} ({employeeWithDiscount} with A name discount)")
        print(f"Dependent Benefit Cost:\t\t -${monthlyDependentBenefitCost} ({len(employee.dependents)} dependents x {self.__DEPENDENT_COST_PER_YEAR/self.__NO_OF_PAYCHECKS}) ({dependentWithDiscount} with A name discount)")
        print("-------------------------------------------------------------------------------")
        print(f"Paycheck value after deductions: \t\t {monthlyTotalCost}")
        

        
# Example usage
employee1 = Employee("Nisarg")

dependent1 = Dependent("Jay", employee1)
dependent2 = Dependent("Aakash", employee1)

employee1.addDependent(dependent1)
employee1.addDependent(dependent2)

# def aNameDiscountApplied(person):
#     if person.name.startswith('A') or person.name.startswith('a'):
#         return True
#     return False
# aNameDiscount = Discount('\'A\' name discount', aNameDiscountApplied)

paycheckCalc = PayCheckCalculator()
# paylocityBenefits.addDiscount(aNameDiscount)
paycheckCalc.calculatePayCheck(employee1)



