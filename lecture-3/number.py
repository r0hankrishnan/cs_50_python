# try:
#     x = int(input("What's x? "))
#     print("x is ", x)    
# except ValueError:
#     print("x is not an integer")

# try:
#     x = int(input("what's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# while True:
#     try:
#         x = int(input("what's x? "))
#     except ValueError:
#         print("x isn't an integer")
#     else:
#         break

# print(f"x is {x}")

# while True:
#     try:
#         x = int(input("what's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")

# print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("what's x? "))
#         except ValueError:
#             print("x isn't an integer")
#         else:
#             break
#     return x

# main()

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             print("x isn't an integer")

# main()

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             pass

# main()

def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()