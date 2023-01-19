
# class Person(object):

	
# 	def __init__(self, name, idnumber):
# 		self.name = name
# 		self.idnumber = idnumber

# 	def display(self):
# 		print(self.name)
# 		print(self.idnumber)




# class Employee(Person):
# 	def __init__(self, name, idnumber, salary, post):
# 		self.salary = salary
# 		self.post = post

		
# 		Person.__init__(self, name, idnumber)



# a = Employee('Rahul', 886012, 200000, "Intern")

# a.display()

class A(object):
    department = "computer"
    a = 50
    __b = 60
    # def __init__(self,name,id):
    #     self.name = name
    #     self.id = id
    def display(self):
        # print("Name: ",self.name, "ID no:",self.id)
        print("protected in parent",self._a)
class B:
    # def __init__(self,surname,native,name,id):
    #     self.surname = surname
    #     self.native = native
    #     self.name = name
    #     self.id = id

    def display(self):
        # print("Name: ",self.name, "ID no:",self.id)
        print("protected in child",self.A.a)


b = B()
# b.display()
# print(b.department)
b.display()

# a = A("param",56)
# a.display()
# print(b.a)
 