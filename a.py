def prime(n):
    if n <= 1:
        print("not  ax prime")
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            print("not prime number")
    return "prime "
        
n = int(input("enter the number you want"))
print(prime(n))
