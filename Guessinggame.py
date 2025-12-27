import random
n = random.randrange(1,100)
print(n)
num = int(input("Enter your number : "))
#print(num)
while num != n:
    if num < n:
        print("The number is low")
        num = int(input("Enter your number again : "))
    elif num > n :
        print("The number is high")
        num = int(input("Enter your number again : "))
    else:
        break
print("That is correct")