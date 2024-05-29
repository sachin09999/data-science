# while loop
# i=1
# while i<6:
#     print(i)
#     i+=1

# i=1
# while i<6:
#     print(i)
#     if i==3:
#      break
#     i+=1

# i=1
# while i<6:
#     print(i)
#     if i==3:
#      continue
#     i+=1

#function
# def my_function():
#     print("this is my function")

# my_function()   

# def my_function(name):
#     print(name)

# my_function("hello")  

# num1=200
# num2=500

# def add(a,g):
#     print(a+g)

# add(num1,num2)   

# def myfunction(*kids):    #->args parameter
#     print("the youngest child "+kids[2])

# myfunction("ram","shyam","jai")   

# def myfunction1(child1,child2,child3):
#     print("the youngest child is "+child3)

# myfunction1(child1="hello",child2="hi",child3="hey")

# lst=[1,2,3,4,5,6,8]
# def square(n):
#     for n in n:
#      print(n**2)
# square(lst)    

# def avgfn(c,d):
#     print((c+d)/2)
# a=int(input("enter the number a "))
# b=int(input("enter the number b "))
# avgfn(a,b)

# def agfn(inputlst):
#     return sum(inputlst)/len(inputlst)

# agfn([24,35,34,34])

# find minimum

# def mini(a):
#     for x in a:
#      if a>x:
#       x=a

# ls = [1,2,3,4,5,6,7,8]
# mini(ls)

# Python program to find smallest 
# number in a list

# l=[1,2,3,4,5,6,7,8]
# # Assign first element as a minimum.
# min(l)
# def min(a):
#  min1 = l[0]
# for i in range(len(l)):
# 	# If the other element is min than first element
# 	    if l[i] < min1: 
# 		    min1 = l[i] #It will change
# 			return min1:

#lambda
#lambda arg:expression
x = lambda a,b,c: a+b+c
print(x(10,20,30))

