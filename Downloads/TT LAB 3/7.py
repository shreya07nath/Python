def sum(n):
    if n == 0:
        return 0
    else:
        return (n % 10 + sum(int(n / 10)))
num = int(input("Enter the number: "))
print("Sum of digits in",num,"is", sum(num))