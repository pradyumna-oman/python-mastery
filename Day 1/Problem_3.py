# Problem: Find the Greatest of Three Numbers

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    if num1 > num2:
        if num1 > num3:
            print(num1 ,"is the greatest number.")
        else:
            print(num3 ,"is the greatest number.")
    elif num2 > num3:
        print(num2 ,"is the greatest number.")
    elif num3 > num1:
        print(num3 ,"is the greatest number.")
    else:
        print("All three numbers are equal.")

if __name__ == "__main__":
    main()