class Student:

    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def __str__(self):
        return "Name: {}, Roll No: {}, Marks: {}".format(self.name,self.roll_no,self.marks)
    
students = []

def add_student():
    name = input("Enter Student Name : ")
    roll_no = input("Enter Student Roll Number : ")
    marks = int(input("Enter Student Marks : "))
    student = Student(name,roll_no,marks)
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records.")
    else:
        for s in students:
            print(s)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            print("GoodBye!!")
            break
        else:
            print("Invalid choice. Try again.")
    
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")

