
#11. CALCULATING PERCENTAGE AND MARKS.
print("CALCULATING PERCENTAGE AND Grading accordingly.")
m1 = int(input("Enter marks of Physics:"))
m2 = int(input("Enter marks of Maths:"))
m3 = int(input("Enter marks of Chemistry:"))
m4 = int(input("Enter marks of English:"))
m5 = int(input("Enter marks of Biology:"))
sum_total = (m1+m2+m3+m4+m5)
percentage = (sum_total/500)*100
print(percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage > 40:
    print("Grade E")
else:
    print("Grade F")