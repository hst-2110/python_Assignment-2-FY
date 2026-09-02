#6.PROGRAM TO CHECK BIGGEST OF THE TWO NUMBERS FROM THE KEYBOARD.
print("PROGRAM TO CHECK BIGGEST OF THE TWO NUMBERS FROM THE KEYBOARD.")
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
if num1 > num2:
    print(f" {num1} is biggest of the two numbers.")
elif num2 > num1:
    print(f" {num2} is biggest of the two numbers.")
elif num1 == num2 :
    print(" both are equal.")
else:
    print("Enter a vaild input.")
