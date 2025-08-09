print("Enter a number : ")
num = int(input())

result = True

for i in range(2, int(num**0.5)+1) :
    if num % i == 0 : 
        result = False
        break

if result : 
    print("Prime number")
else : 
    print("Not prime number")