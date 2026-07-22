

# #Square Pattern
# # n = 5
# # for i in range(n):
# #     for j in range(n):
# #         print("*", end=" ")
# #     print()     #empty print line will print in new line

# # Right angle triangle pattern
# # n = 5
# # for i in range(n):
# #     for j in range(i+1):
# #         print("*", end=" ")
# #     print() 

# #inverted right angle triangle pattern
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("*", end = " ")
#     print()

# Diamond Pattern
# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end = " ")
#     for k in range(2*i+1):
#         print("*", end = " ")
#     print()
# for i in range(n-2, -1, -1): 
#     for j in range(n-i-1):
#         print(" ", end = " ")
#     for k in range(2*i+1):
#         print("*", end = " ")
#     print()

# Armstrong number - sum of cube of digits is equal to the number itself
# Example - 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


#hollow square pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Pascal pattern with numbers - 
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1


