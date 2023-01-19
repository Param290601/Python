
# class car(): 
# 	def __init__(self, model, color): 
# 		self.model = model 
# 		self.color = color 
		
# 	def show(self): 
# 		print("Model is", self.model ) 
# 		print("color is", self.color ) 
		

# audi = car("audi a4", "blue") 
# ferrari = car("ferrari 488", "green") 

# audi.show()	  
# ferrari.show() 

# print("Model for audi is ",audi.model) 
# print("Colour for ferrari is ",ferrari.color) 



# class A(object):
# 	def __init__(self, something):
# 		print("A init called")
# 		self.something = something


# class B(A):
# 	def __init__(self, something):
		
# 		A.__init__(self, something)
# 		print("B init called")
# 		self.something = something


# obj = B("Something")

# class Dog:

	
# 	attr1 = "mammal"

# 	def __init__(self, name):
# 		self.name = name


# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")


# print("Rodger is a ",Rodger.__class__.attr1)
# print("Tommy is also a ",Tommy.__class__.attr1)


# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

class Person:
 
    
    # def __init__(name):
    #     print("My name is",name)
 
    def say_hi(self,surname):
        self.say()
        print('Hello, my name is', surname)
    def say(self):
        print('Hello, my name is')
 
 
p = Person()
p.say_hi("tilva")
# print("name is",p.name)

