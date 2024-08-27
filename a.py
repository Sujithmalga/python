def prime(n):
    if n <= 1:
        print("it is not  prime")
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            print("it not prime number")
    return "prime number"
        
n = int(input("enter the number"))
print(prime(n))
