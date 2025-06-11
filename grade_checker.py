#This will hold students data
students = {}

#loading students name from file
try:
    with open("student.txt", "r") as file:
        for line in file:
            name = line.strip().title()
            if name not in students:
                students[name] = {}

except FileNotFoundError: #(if file does not exist yet, this function will make it ignore)
    pass

#option menu
while True:  
    print("\n_Program Menu List_")
    print("1.Add New Student")
    print("2. Add Grade for a Student")
    print("3. View all Students and Grade")
    print("4. Calculate student average")
    print("5 . Exit")

#collecting user choice   
    choice = input("\nEnter your choice(1-5): ")

#adding new student
    if choice == "1":
        name = input("Enter student's full name: ").strip() .title()
        if name in students:
            print("\nName of Student exists already")
        else:
            students[name] = {}
            print(f"{name}'s name has been added to database")

             #save the names to a file
            with open("student.txt","a") as file:
                file.write(name + "\n")
    
#adding grade for students
    elif choice == "2":
        name = input("\nEnter student's name: ").strip() .title()
        if name not in students:
            print(f"{name} does not exist in database")
        else:
            subject = input("Enter subject: ").title()
            try:
                score = float(input("Enter subject grade(score): "))
                students[name][subject] = score

            except ValueError:
                print("Enter Valid Score")

#viewing all students
    elif choice == "3":
        print("\nEnter Student Name")
        name = input(" ").strip().title()
        if not students:
            print("No Students found")
        else:
            for name, grades in students.items():
                print(f"{name} Grades:")
                if not grades:
                    print("Student has no grade yet")
                else:
                    for subject, score in grades.items():
                        print(f"{subject}:{score}")


#calculate a student average grade
    elif choice == "4":
        print("\nWhose average do you wish to calculate")
        name = input(" ").strip().title() #ak for name 
        if name not in students:
            print("Student not found")
        elif not students[name]:
            print("Student has no Grade record")
        else:
            scores = list(students[name].values())
            average = sum(scores)/len(scores)
            print(f"{name}'s average is {average:.2f}")


#exiting program
    elif choice == "5":
        print("\nThank You for using this Program")
        break