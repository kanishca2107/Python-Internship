students = []
roll_numbers = set()
while True:

    print("===STUDENT MANAGEMENT SYSTEM===")
    print("1.add students")
    print("2.update students")
    print("3.delete students")
    print("4.search students")
    print("5.view students")
    print("6.rank list")
    print("7.exit")
    choice = int(input("entrt your choice: "))
    if choice == "1":
        roll = int(input("enter your roll: "))
        if roll in roll_numbers:
            print("roll number alreday exist❌")
        name = input("enter the name: ")
        marks = int(input("enter your marks: "))
        dept = input("enter your department: ")
        student = {"name":name,
                "roll":roll,
                "marks":marks,
                "dept":dept}
        student.append(students)
        roll_numbers.add(roll)
        if marks >= 95:
            badge = "🔥topper"
        elif marks >= 85:
            badge = "😉excellent"
        elif marks >= 75:
            badge = "👍good"
        else:
            badge = "📕📖need improvement"
        print(f"students were added succesfully{badge}")
    elif choice == "2":
        if not students:
            print("student not found try again later")
            continue
        

        

    

            
            