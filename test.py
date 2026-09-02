# THIS IS FOR THE IF,ELIF,ELSE AND MATCH CASE STATEMENT BASIC QUESTION FOR PRACTICE PURPOSE



#Question: Write a program to check whether a number is greater than 20 or not using if else statement.
num = int(input(""))

if(num>20):
    print("Hello world")
else:
    print("No")

#Question: Write a program to check whether a person is eligible to vote or not based on age using if else statement.
age=int(input("Enter your age:"))
if age>21:
    print("Bro ofcourse you can vote")
elif age>=18 and age<21:
    print("Hello new voter")
elif age>=16 and age<18:
    print("you need to wait for 2 years to vote")
elif age<16:
    print("you are too young to vote")
else:
    print("Not eligible")



#Question: Write a program to check whether a number is positive, negative or zero using if else statement.
num = int(input("Enter a number: "))
if num >= 1:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
elif num < 0:
    print("The number is negative.")

#Question: Write a program to check the grade of a student based on marks using if else statement.
marks=int(input("Enter your marks: "))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("F")


#Question: Write a program to check whether a student is pass or fail based on marks in three subjects using nested if else statement.
eng = int(input("Enter your marks: "))#30
maths=int(input("Enter a number: "))#50
sci=int(input("Enter a count: "))#70
if eng>=30:
    if maths>=50:
        if sci>=70:
            print("You are pass")
        else:
            print("You are fail in science")
    else:
        print("you are fail in maths")
else:
    print("you are fail in all the subjects")

#Question: Write a program to check whether a letter is a vowel or consonant using match case statement.
letter = input("Enter a letter: ")
match letter:
    case "a":
        print(f"{letter} is a vowel")
    case "e":
        print(f"{letter} is a vowel")
    case "i":
        print(f"{letter} is a vowel")
    case "o":
        print(f"{letter} is a vowel")
    case "u":
        print(f"{letter} is a vowel")
    case _:
        print(f"{letter} is a consonant")


#question: Write a program to check whether a student is pass or fail based on marks using if else statement.
marks=int(input("enter your marks "))
if marks<=50 and marks<=27:
    print("Relatives are very happy")
elif marks>50 and marks<=100:
    print("Relatives are very sad")
else:
    print("Relatives are not happy")


#question: Write a program to check whether a student is pass or fail based on marks using if else statement.
marks=int(input("enter your marks "))
if marks>=33:
    print("Pass")
else:
    print("Fail")   


#question: Write a program to check whether a student is pass or fail based on marks using if else statement.
marks=int(input("Enter your marks "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=65:
    print("C")
elif marks>=33:
    print("Fail")
elif marks<33:
    print("Fail and need to repeat the same class")
