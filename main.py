students=[]

def addstudent(name, marks):
    students.append({"Name": name, "Marks":marks})

while True:
    print("Menu\n1. Add Student\n2. View Students\n3. Find Topper\n4. Average Marks\n5. Delete Student\n6. Search Student\n7. Edit Marks\n8. Save & Exit\n")
   
    choice = int(input("Enter choice: "))

    if choice==1:
        name= input("Enter name: ")
        marks= int(input("Enter Marks: "))
        addstudent(name,marks)
       
    elif choice==2:
        for student in students:
            print(f"{student['Name']} {student['Marks']}")
        print("\n")
    elif choice==3:
        maxi=0
        for student in students:
            a= student["Marks"]
            n= student["Name"]
            if a>maxi:
                maxi=a
                maxiname=n
        print (f"{maxiname}\n")
    elif choice==4:
        num=0
        total=0
        for student in students:
            num+=1
            total+=student["Marks"]
        avg= total/num
        print(avg)
        print("\n")
    elif choice==5:
        delete= input("Enter name of student you want to delete: ")
        for student in students:
            if student['Name']==delete:
                students.remove(student)
    elif choice==6:
        delete= input("Enter name of student to search: ")
        for student in students:
            if student['Name']==delete:
                print(f"found: {student['Name']} {student['Marks']}")
    elif choice==7:
        delete= input("Enter name of student to edit marks: ")
        newmarks= int(input("Enter new marks: "))
        for student in students:
            if student['Name']==delete:
                student['Marks']= newmarks
    elif choice==8:
        with open(r"C:\Users\GichiRichi Laptop\OneDrive\Desktop\Python\File Handling\file.txt", "w") as f:
            for student in students:
                f.write(f'{student["Name"]} {student["Marks"]}\n')
        break

    