#Make a program to print "meow" three times using while
i = 3

while i != 0:
    print("meow")
    i = i-1

#Print "meow" three times with lists and for loop -- 
for _ in range(3):
    print("meow")

#Print "meow" without loops
print("meow\n" * 3, end = "")

#Ask user how many times to meow and make sure to filter out negative values
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#Create meow function
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()