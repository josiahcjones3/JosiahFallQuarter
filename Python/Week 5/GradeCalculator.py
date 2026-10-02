NumberGrade=int (input("Enter Your Grade"))

if(NumberGrade >90):
    print("GOOD JOB!YOU GOT AN A")
elif(80<=NumberGrade<=79):
    print("You Got A B! Pretty Decent")
number_grade = int(input("Enter your number grade (1-100): "))

if number_grade >= 90:
    letter_grade = "A"
if number_grade >= 80:
    letter_grade = "B"
if number_grade >= 70:
    letter_grade = "C"
if number_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"