name = input("Enter your name: ")
sub1 = int(input("Enter Math marks: "))
sub2 = int(input("Enter English marks: "))
sub3 = int(input("Enter Python marks: "))


if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
    print("Invalid Marks!")
else:
    total_marks = sub1 + sub2 + sub3
    average_marks = total_marks / 3


    if average_marks >= 80:
        grade = "A+"
    elif average_marks >= 70:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "F"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")