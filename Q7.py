#7.PROGRAM TO CHECK BIGGEST OF THE THREE NUMBERS FROM THE KEYBOARD.
print("PROGRAM TO CHECK BIGGEST OF THE THREE NUMBERS FROM THE KEYBOARD.")
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
if num1 > num2 and num1 > num3:
    print(f" {num1} is biggest of the three numbers.")
elif num2 > num1 and num2 > num3:
    print(f" {num2} is biggest of the three numbers.")
elif num3 > num1 and num3 > num1:
    print(f" {num3} is biggest of the three numbers.")    

elif num1 == num2 and num1 == num3 :
    print("all are equal.")
else:
    print("Enter a vaild input.")

