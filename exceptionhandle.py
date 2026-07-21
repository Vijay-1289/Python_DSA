# Exception Handling


# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("Done")


# for i in range(5):
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Done")


# try:
#     a = int(input("Enter a number: "))
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("Done")

# a = int(input("Enter a number: "))
# if a < 0:
#     raise ValueError("Number is negative")
# else:
#     print(a)


# keep asking valid input until user enters a valid input

while True:
    try:
        a = int(input("Enter a number: "))
        print(a)
        break
    except ValueError as e:
        print(e)

#handling index error while acccessing list until valid 
l = [1,2,3,4,5]
while True:
    try:
        a = int(input("Enter a index: "))
        print(l[a])
        break
    except IndexError as e:
        print(e)

