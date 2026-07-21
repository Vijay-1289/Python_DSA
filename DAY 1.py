# print("Vijay\nVijay\nVijay")
# print(r"\\tcurrent\\new\\folder")
# # \ is a escape character

# check if the number is even or odd using function
# def funce(a):
#     if a % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')

# a =  int(input())
# funce(a)

""" dictionary """  
# dict = {
#     "name": "Vijay",
#     "age": 20,
#     "gender": "Male",
#     "courses": ["Python", "Java", "C++"]
# }
# dict['age'] = 21
# dict.update({"name":"Vijay Rama Raju"})
# print(dict)
# print(dict.get("name"))
# print(dict.keys())
# print(dict.values())
# print(dict.items())

""" *args """
# def count(*args):
#     print(type(args))

# count(1,2,3,4,5)

# """ **kwargs """
# import pathlib
# import pathlib
# def count(**kwargs):
#     print(type(kwargs))

# count(name="Vijay", age=21, gender="Male", courses=["Python", "Java", "C++"])

# # default parameters should be last and unknown parameters should be first
# def default(a,b=10):
#     print(a,b)


# """OOPS"""

# """1. Polymorphism"""
# l = [1, 2, 3]
# s =  "Vijay"
# len(l)
# len(s)      

# Static typing will always require type declaration 
# Dynamic typing will not require type declaration


# x = "Vijay"
# print(x[-2:-5:-1])

# i= 1
# while i>0:
#     print("hi")

# print the sum of numbers from 1 to n using for loop
a  = int(input())
sum = 0
for i in range(1, a):
    sum+=i
print(sum)

#print the sum of numbers from 1 to n using while loop
sum=0
while a > 0:
    sum+=a
    a-=1
print(sum)

