print("Welcome to Eagle Academy.")
print("What is your name ?")
yourname = input()

print("How are you?")
print("Choose from good,great,fine,or something else:")
greeting = input()

if "good" in greeting.lower() or "great" in greeting.lower() or fine in greeting.lower():
    print("Sweet!")
else:
    print("its all good")

print("Enter student's name:")
myname = input()
import time

current_grade = int(input("Enter your current grade" + myname + "(1-12):"))
current_year = int(input("Enter the year you went into that grade" + myname + ":"))

for grade in range (current_grade,13):
    years_left =grade - current_grade
    num_letters="st" if grade == 1 else "nd" if grade == 2 else "rd" if grade == 3 else "th"
    years_until_grad=12 - grade
    years_until=current_year+years_left+1
    print(f"{years_until},you will graduate the {grade}{num_letters} grade and will have{years_until_grad} years left unti the 12th Grade.")
    time.sleep(.5)
    if grade == 12:
        break
print(myname + "will graduate in" + str(years__until)+".")

