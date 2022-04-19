def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD = gcd(a,b)
num1 = a/GCD
num2= b/GCD
print("LCM is:", GCD * num1 * num2)
print("GCD is:", gcd(a,b))