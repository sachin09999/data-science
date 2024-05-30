
# #exception handling
# a=int(input("enter the number "))
# b=int(input("enter the number "))
# try:
#     print("program is runnnig")
#     result=a/b
#     print("program ins executed")
#     print("result of division is ",result)

# except Exception as e:
#     print("as get an error")
#     print(e)    

# else:
#     print("no exception found")
# finally:
#     print("the code will run")        


# try:
#     a=1
#     if a>0:   
#      print("program is running")

# except SyntaxError as e:
#     print(e)

# else:
#     print("there is no error")

# finally:
#     print("the code will run")            

#oops
# class animal:
#     name="elephant"
#     weight=2000
#     age=25

#     def display(self):
#       print(self.name)
#       print(self.weight)
#       print(self.age)

# a=animal() 
# print(a.age)

# a.age="999"
# print(a.age)

# constructor
    # __init__()

# class animal:
#     name="Lion"
#     weight=85
#     age=100
    
#     def __init__(self,name,weight,age):
#         self.name=name
#         self.weight=weight
#         self.age=age
#         print(self.name,self.weight,self.age)
#         # print(self.name,self.weight,self.age)

#     # def __init__(self):
#     #     print(self.name)
#     #     print(self.weight)
#     #     print(self.age)

# # a=animal()   
# b=animal(name="Tiger",weight=400,age=32)     

# class bank:
#     name
#     # age=111
#     # address="alwar"
#     # bank="swiss bank"
#     # accno=111222333

#     def show_info(self):
#         print(self.name)
#         # print(self.age)
#         # print(self.address)
#         # print(self.bank)
#         # print(self.accno)

#     def get_info(self,name):
#         self.name=name=input("enter the name")   

# # b=bank()
# # b.show_info()
# c=bank()
# c.get_info()
# c.show_info()

#inheritance
class first:
    sirname="singh"
    def a(self,n):
     self.n=sirname
     
    # def __init__(self,sirname):
    #     self.sirname=sirname

class second(first):
    name="sachin"  

s=second()     
print(s.name,s.sirname)