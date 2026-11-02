# Problem: Find the Greatest of Two Numbers

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 > num2:
        print(num1 ,"is the greatest number.")
    elif num1 == num2:
        print("Both numbers are equal.")
    else:
        print(num2 ,"is the greatest number.")

if __name__ == "__main__":
    main()