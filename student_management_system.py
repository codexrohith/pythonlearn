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
    marks = float(input("Enter Student Marks : "))
    student = Student(name,roll_no,marks)
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records.")
    else:
        for s in students:
            print(s)
def search_student():
    rollno=input("enter the students roll number you have to search")
    for s in students:
        if s.roll_no == rollno:
            print(s)
            break
    else:
        print("Student not found.")

def update_marks():
    rollno = input("Enter student roll number to update marks: ")
    for s in students:
        if s.roll_no == rollno:
            s.marks=float(input("Enter New Marks of {} : ".format(s.name)))
            print("Marks updated successfully!")
            break
    else:
        print("Student not found.")

def delete_student():
    rollno = input("Enter roll number to delete: ")
    for s in students:
        if s.roll_no == rollno:
            students.remove(s)
            print(f"Student with Roll No {rollno} deleted successfully.")
            break
    else:
        print("Student not found!!")

def show_topper():
    if not students:
        print("No student records.")
        return
    else:
        max_marks = max(s.marks for s in students)
        print(f"Topper(s) with {max_marks} marks:")
        for s in students:
            if s.marks == max_marks:
                print(s)


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice (1 to 7): "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice==3:
            search_student()
        elif choice==4:
            update_marks()
        elif choice==5:
            delete_student()
        elif choice==6:
            show_topper()
        elif choice==7:
            print("GoodBye!!")
            break
        else:
            print("Invalid choice. Try again.")
    
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")

