from colorama import Fore,Back,Style,init
import csv
init()


students = {} #to store student record
users_login = {}  #to store user and password for teacher

#Functions

#For Admin Use
def admin():
    print(Fore.GREEN + '\n---Welcome Admin!---' + Style.RESET_ALL)
    #Create a loop
    while True: 
        print('\n1. View Registered Name \n2. Register Account \n3. delete Account \n4. File Management \n5. Back')
        try:
            choice = int(input('\nPlease Enter Choice 1/2/3/4/5: \n'))
        
            if choice == 1:
                if not users_login:
                    print(Fore.RED + 'No Record' + Style.RESET_ALL)
                else:
                    print('\n--Teachers Account--\n')
                    for user,password in users_login.items():
                            print(f'User: {user} \nPass: {password}\n')
            elif choice == 2:
                register()
                csv_adminrecord()
            elif choice == 3:
                remove_account()
            elif choice == 4:
                while True:
                    print('\nPlease select option:\n')
                    print('\n1. View Student Record \n2. View Registered Account \n3. Restore Registered Account \n4. Back')
                    choice = input('\nEnter your choice 1/2/3: ')
                    if choice == '1':
                        print(Fore.CYAN + '\n--Student Record--\n' + Style.RESET_ALL)
                        with open('Teacher.csv', 'r') as Read_record:
                            print(Read_record.read())  
                    elif choice == '2':
                        print(Fore.CYAN + '\n--Registered Account--\n' + Style.RESET_ALL)
                        with open('admin.csv', 'r') as registered_account:
                            print(registered_account.read())
                    elif choice == '3':
                        csv_Restoreadmin()
                        print('\nAccounts Succesfully Restored!')
                    elif choice == '4':
                        break
                    else:
                        print(Fore.RED + '\nInvalid Input Please select 1,2 or 3' + Style.RESET_ALL)
            elif choice == 5:
                return
            else:
                print(Fore.RED + 'Invalid Input Choices are 1-5' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.RED + 'INVALID NUMBER!' + Style.RESET_ALL)
#For Teachers
def Teacher():
    print(Fore.GREEN + "\n--- Welcome Teacher ---\n" + Style.RESET_ALL)
    username = input("Enter your username: ").strip().lower()
    if username not in users_login:
        print(f"Teacher username not found. Please register first.")
        return
    password = input("Enter your password: ").strip()
    if users_login[username] == password:
        print(Fore.GREEN + "\nLogin successful!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nIncorrect password. Please try again." + Style.RESET_ALL)
        return
    while True:
        try:           
            print(Fore.GREEN + f"\n---Welcome, Teacher {username}.---\n" + Style.RESET_ALL)
            print('Please Select Option:\n')
            print('1. View Student List \n2. Search a student \n3. Add Student \n4. Delete Student \n5. Manage File \n6. Back')
            choice = int(input('\nPlease Enter choice 1/2/3/4: \n'))
            if choice == 1:
                if not students:
                    print(Fore.RED + "No Record" + Style.RESET_ALL)
                else:
                    # Separate students into 'pass' and 'fail' categories based on their average
                    passed_students = {name: info for name, info in students.items() if info["average"] >= 75}
                    failed_students = {name: info for name, info in students.items() if info["average"] < 75}

                    # Display all students
                    print(Fore.CYAN + "\nAll the Students and their Grades:" + Style.RESET_ALL)
                    for student_id, info in students.items():
                        print(f"\nStudent No.: {student_id}")
                        print(f"Name: {info["name"]}")
                        print("Subjects and Grades:")
                        for subject, grade in info["subjects"].items():
                            print(f"{subject}: {grade}")
                        print(f"Average: {info['average']:.1f}")
                        print(f"Final Grade: {info['letter_grade']}")
                    total = len(students)
                    print(Fore.LIGHTYELLOW_EX + f'\nYour total no. of students are {total}' + Style.RESET_ALL)

                    # Display passed students
                    print(Fore.GREEN + "\nPassed Students:" + Style.RESET_ALL)
                    for student_id, info in passed_students.items():
                        print(f"\nStudent No.: {student_id}") 
                        print(f"Name: {info["name"]}")
                        print(f"Average: {info['average']:.1f}")
                        print(f"Final Grade: {info['letter_grade']}")
                    total = len(passed_students)
                    print(Fore.GREEN + f'\nTotal No. of Passing Students: {total}' + Style.RESET_ALL)

                    # Display failed students
                    print(Fore.RED + "\nFailed Students:" + Style.RESET_ALL)
                    for student_id, info in failed_students.items():
                        print(f"\nStudent No.: {student_id}")
                        print(f"\nName: {info["name"]}")
                        print(f"Average: {info['average']:.1f}")
                        print(f"Final Grade: {info['letter_grade']}")
                    total = len(failed_students)
                    print(Fore.RED + f'\nTotal No. of Failed Students: {total}' + Style.RESET_ALL)
            elif choice == 2:
                Search_student()
            elif choice == 3:
                Add_Student()
            elif choice == 4:
                student_delete = int(input('Please Enter the Student No. \n'))
                if student_delete in students:
                    students.pop(student_delete)
                    print(Fore.LIGHTGREEN_EX + 'Student Removed on the list' + Style.RESET_ALL)
                else:
                    print(Fore.RED + 'Name not in record' + Style.RESET_ALL)
            elif choice == 5:
                print('\nEnter Option\n')
                print('1. Save Data \n2. Load Data \n3. Add Student in File \n4. Back')
                choice = input('\nEnter your choice: ')
                if choice == '1':
                    csv_record()
                    print(Fore.GREEN + 'Saved Data Successful' + Style.RESET_ALL)
                elif choice == '2':
                    restorerecord()
                    print(Fore.GREEN + 'Load Data Successful' + Style.RESET_ALL)
                elif choice == '3':
                    csv_addrecord()
                    print(Fore.GREEN + 'Add Student Successful' + Style.RESET_ALL)
                elif choice == '4':
                    break
                else:
                    print('Invalid Input Please select 1,2 or 3')
            elif choice == 6:
                break
            else:
                print(Fore.RED + 'Invalid Input' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.RED + 'Invalid Input' + Style.RESET_ALL)
# Register User Log-in
def register():
    while True:
        print("\n--- Register ---")
        username = input("Enter a username: ").strip().lower()
        if username in users_login:
            print("Username already exists. Try a different one.")
            return
        password = input("Enter a password: ").strip().lower()
        #storing account in dictionary
        users_login[username] = password 
        print(Fore.GREEN + f"\nRegistration for Teacher {username} is successful!.\n" + Style.RESET_ALL)
        break
# for Deleting User-log in Account
def remove_account():
    print("\n--- Remove Account ---")
    username = input("Enter the username: ").strip()
    if username not in users_login['teacher']:
        print(Fore.RED + f"{username.capitalize()} username not found." + Style.RESET_ALL)
        return
    password = input("Enter the password: ").strip()
    if users_login['teacher'][username] == password:
        del users_login['teacher'][username]
        print(f"Account of Teacher '{username}' has been removed.")
    else:
        print("Incorrect password. Account removal failed.")
# I created a grading Scale
def Grade_Letter(average):
        if average == 100:
            return 'A+'
        elif average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 75:
            return 'C'
        else:
            return 'Failed'
# Create a function to view the student grade by searching the student name
def Search_student():
    student_num = input("\nEnter the name of the student no. to view grades: ")
    found = False
    csv_file = 'Teacher.csv'
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader)
        
        print(f"\nGrades for {student_num}:")
        for row in reader:
            student_no, name, subject, grade, average, final_grade = row
            if student_no == student_num:
                print(f"Student No: {student_no} Name: {name} Subject: {subject}, Grade: {grade}, Average: {average}, Final Grade: {final_grade}")
                found = True
    
    if not found:
        print(f"No records found for student: {student_no}")
# Function for student to view their grade
def Student_View():
    while True:
        Search_student()
        choice = input("\nDo you want to view another student's grades? (yes/no): ").lower()
        if choice == 'yes':
            continue
        else:
            print("back.")
            break
# Function for Input the students, subjects, and grades
def Add_Student():
    num_students = int(input("Enter the number of students: "))         
    for hm_students in range(num_students):
        while True:
            try:
                student_ID = int(input('\nPlease Enter Student number: '))
                if student_ID in students:
                    raise ValueError ('Student Number Already Exist. Please Try again')
                break
            except ValueError as error:
                print(Fore.RED + f'{error}' + Style.RESET_ALL)
        name = input("\nEnter the student's name: ").lower()
        
        while True:
            try:
                num_subjects = int(input(f"How many subjects does {name} have? "))
                break
            except ValueError:
                print('Value Error')

        subjects = {}        
        for hm_subjects in range(num_subjects):
            subject = input("Enter the subject name: ")
                    
            # using loop to enter valid input
            while True:
                try:
                    grade = int(input(f"Enter the grade for {subject}: "))
                    if grade < 1 or grade > 100:
                        raise ValueError("Grade must be between 0 and 100.") #if the value not between 1-100
                    subjects[subject] = grade
                    break  # Exit the loop if the input is valid
                except ValueError as error: #for the value error it will print default error message
                    print(Fore.RED + f"\n{error},\n Please Enter Correct Number\n" + Style.RESET_ALL) #it will print if the input is not an integer
                
        average = sum(subjects.values()) / len(subjects) #compute the average grade
        letter_grade = Grade_Letter(average) #for pass or fail
                    
        students[student_ID] = {'name': name,"subjects": subjects, "average": average, "letter_grade": letter_grade} #nested dictionary
        print(Fore.GREEN + '\nAdd Student Successful!' + Style.RESET_ALL) 
# To Save the input Record in the csv
def csv_record():
    csv_file = "Teacher.csv"
    with open(csv_file, 'w', newline='') as Teacher_file: #new line para walang spacing
        writer = csv.writer(Teacher_file)
        
        header = ["Student no.","Name", "Subject", "Grade", "Average", "Final Grade"]# Write the header
        writer.writerow(header)
        
        for Student_num, info in students.items(): # Write student data
            for subject, grade in info['subjects'].items():
                writer.writerow([Student_num,info["name"], subject, grade, f"{info['average']:.1f}", info['letter_grade']]) #i used :.1f to round off the float
#Add student in File management
def csv_addrecord():
    csv_file = "Teacher.csv"
    with open(csv_file, 'a', newline='') as Teacher_file: #new line para walang spacing
        writer = csv.writer(Teacher_file)
        
        for Student_num, info in students.items(): # Write student data
            for subject, grade in info['subjects'].items():
                writer.writerow([Student_num,info["name"], subject, grade, f"{info['average']:.1f}", info['letter_grade']]) #I used :.1f to round off the float
#to save the user and password in csv
def csv_adminrecord():
    csv_adminfile = "admin.csv"
    with open(csv_adminfile, 'w', newline='') as admin_file: #new line para walang spacing
        writer = csv.writer(admin_file)
        
        header = ["User", "Password"]# Write the header
        writer.writerow(header)
        
        for userlogin, pass_code in users_login.items(): # for admin list
                writer.writerow([userlogin,pass_code]) #showed user and password
# to restore the registered account
def csv_Restoreadmin():
    admin_restore = 'admin.csv'
    with open(admin_restore,'r') as restore_adminfile: # Open the CSV file
        admin_restorefile = csv.reader(restore_adminfile)
        next(admin_restorefile) #skip the header
        for row in admin_restorefile:
            user = row[0]
            passcode = row[1]

            users_login[user] = passcode
#to restore the record
def restorerecord():
    csv_restore = 'Teacher.csv'
    with open(csv_restore,'r') as restore_file: # Open the CSV file
        csv_restorefile = csv.reader(restore_file)
        next(csv_restorefile) #skip the header
        for row in csv_restorefile: #extract the data in row
            student_ID = row[0]
            name = row[1]
            subject = row[2]
            grade = int(row[3])
            average = float(row[4])
            final_grade = row[5]
            
            # Add the data to the dictionary
            students[name] = {
                'student_ID': student_ID,
                'subjects': {subject : grade},
                'average': average,
                'letter_grade': final_grade
            }


def main():
    while True:
        print(Fore.GREEN + "\n--- Welcome to TAGS ---\n" + Style.RESET_ALL)
        print("1. Teacher  \n2. Student \n3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")
        if choice == '1':
            Teacher()
        elif choice == '2':
            print(Fore.GREEN + '\n--Welcome Student--\n' + Style.RESET_ALL)
            print('Select Option: \n1. View Student Record \n2. Back')
            choice = int(input('\nEnter Choice 1/2: '))
            if choice == 1:
                Student_View()
            elif choice == 2:
                continue
            else:
                print(Fore.RED + '\nInvalid Input choose 1 or 2\n' + Style.RESET_ALL)
        elif choice == '2468':
            admin()
        elif choice == '3':
            print(Fore.CYAN + "\nGoodbye!\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please enter 1, 2, or 3.\n" + Style.RESET_ALL)

main() 
