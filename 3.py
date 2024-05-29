# #dictonary
# d={1:"sachin","age":18,"branch":["cs","ai","Ai ml"],"age":(18,19,20),"address":{"alwar","chikani"}}
# print(d)
# print(type(d))
# print(len(d))
# d={}
# print(type(d))

# #dictionary constructor
# v = dict(name="sachin",clas="4thsem",age="18")
# print(v)

# t={
#   "brand":"ford",
#   "year":"1991"  
# }
# # print(dt["brand"])
# # print(dt.keys())
# # print(dt.values())
# # print(dt.items())
# # print(dt.get("brand"))
# # print(dt.pop("brand"))
# x= t.update({"brand":"Tesla"})
# print(x)

#dictionary inside dictionary

# dt={'dt1':{"name":"sachin"},'dt2':{"age":"18"}}
# print(dt)
# print(dt['dt1']["name"])

#if else

# a=5
# b=5

# # if b>a:
# #     print("b is greater than a")
# # else:
# #     print("not greater")
# if a>b:print("hello")
# else:print("hi")

# print("a") if a>b else print("b")

# print("a") if a>b else print("b") if a==b else print("not equal")

# a=4 
# c=4
# b=3

# if a>b and c>b:
#     print("both are greater")

# a=2
# b=1
# if not a>b:
#     print("hello")

# #pass

# x=41
# if x>32:
#     print("hello")
#     pass
#     if x>32:
#         print("hi")
#     else
#         print("hu")

#input from user in python

# x=int(input("enter the value of x "))
# y=int(input("enter the value of y "))
# z=x+y
# print(z)

#vovel

# x=input("enter the character :")
# if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
#     print("it is a vovel")
# else:
#     print("not a vovel")    

# for x in "hello":
#     print(x)

# for x in range(1,10):
#     print(x)

# x=int(input("enter the numnber :"))
# for i in range(1,11):
#     print(x,"x",i,"=",x*i)

fruit =["apple","mango","guava"]
for index,fruit in enumerate(fruit):
    print(index,fruit)