class Employee:
    def __init__(self, emp_id, emp_name, basic_salary, qualification):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.qualification = qualification

    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False

    def validate_qualification(self):
        if self.qualification.lower() == "bachelors" or self.qualification.lower() == "masters":
            return True
        else:
            return False


class Graduate(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, qualification, job_band, cgpa):
        super().__init__(emp_id, emp_name, basic_salary, qualification)
        self.job_band = job_band
        self.cgpa = cgpa

    def validate_job_band(self):
        if self.job_band.upper() in ["A", "B", "C"]:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            incentive = 0
            if self.job_band.upper() == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job_band.upper() == "B":
                incentive = 0.06 * self.basic_salary
            elif self.job_band.upper() == "C":
                incentive = 0.1 * self.basic_salary

            if self.cgpa >= 4 and self.cgpa <= 4.25:
                tpi = 1000
            elif self.cgpa > 4.25 and self.cgpa <= 4.5:
                tpi = 1700
            elif self.cgpa > 4.5 and self.cgpa <= 4.75:
                tpi = 3200
            elif self.cgpa > 4.75 and self.cgpa <= 5:
                tpi = 5000

            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1

    def display(self):
        print("Employee Name: ",self.emp_name)
        print("Employee Id: ",self.emp_id)
        print("Employee Qualification: ",self.qualification)
        print("Employee Job_band: ",self.job_band)
        print("Employee CGPA: ",self.cgpa)
        print("Employee gross_Salary: ",self.calculate_gross_salary())


class Lateral(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, qualification, job_band, skill_set):
        super().__init__(emp_id, emp_name, basic_salary, qualification)
        self.job_band = job_band
        self.skill_set = skill_set

    def validate_job_band(self):
        if self.job_band.upper() in ["D", "E", "F"]:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            incentive = 0
            if self.job_band.upper() == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job_band.upper() == "E":
                incentive = 0.16 * self.basic_salary
            elif self.job_band.upper() == "F":
                incentive = 0.2 * self.basic_salary

            sme_bonus = 0
            if self.skill_set.lower() == "agp":
                sme_bonus = 6500
            elif self.skill_set.lower() == "agpt":
                sme_bonus = 8200
            elif self.skill_set.lower() == "agdev":
                sme_bonus = 11500

            gross_salary = self.basic_salary + pf + sme_bonus+ incentive
            return gross_salary
        else:
            return -1

    def display(self):
        print("Employee Name: ",self.emp_name)
        print("Employee Id: ",self.emp_id)
        print("Employee Qualification: ",self.qualification)
        print("Employee Job_band: ",self.job_band)
        print("Employee Skill: ",self.skill_set)
        print("Employee gross_Salary: ",self.calculate_gross_salary())

e = Employee(101,"Sapneswar",10000,"bachelors")
g = Graduate(101,"Sapneswar",10000,"bachelors","A",5)
l = Lateral(102,"Ashirbad",15000,"bachelors","D","agp")
g.calculate_gross_salary()
g.display()
print("\nLateral Employee")
l.calculate_gross_salary()
l.display()
