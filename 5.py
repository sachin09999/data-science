
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
class animal:
    name="elephant"
    weight=2000
    age=25

    def display(self):
      print(self.name)
      print(self.weight)
      print(self.age)


a=animal() 
print(a.age)