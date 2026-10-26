#******************************************************************************
# Author:           Jonathan van Mourik
# Lab:              Lab 5
# Date:             10/25/26
# Description:      Basic Grade System
# Input:            int: options selection, str: student name
# Output:           Str: student name, Int: student grade
# Sources:          Lab 5
#******************************************************************************
# intentionaly only whole numbers for grades
# Password is pyth0nrul3s
"""
Welcome to the CIS-133Y grading system.
Please enter the Super Secret Password: pyth0nrul3s

 Welcome to the CIS-133Y grading system.
0: View Grades
1: Add Student
2: Change Grade
3: Exit

Please enter the option you would like to use: 1

Adding a New Student:
Please enter the student's name: Jeff
Please enter the student's grade: 54

 Welcome to the CIS-133Y grading system.
0: View Grades
1: Add Student
2: Change Grade
3: Exit

Please enter the option you would like to use: 0

Student Grades:
Jonathan: 100
Tim: 50
Frank: 0
Jeff: 54

 Welcome to the CIS-133Y grading system.
0: View Grades
1: Add Student
2: Change Grade
3: Exit

Please enter the option you would like to use: 3
"""
import valid
import printer

def main():

    gradesdict = {"Jonathan": 100,
                  "Tim": 50,
                  "Frank": 0}
    SUPERSECRETPASSWORD = "pyth0nrul3s"
    PROMPTLIST = ["View Grades", "Add Student", "Change Grade", "Exit"]
    optionval = 0
    passwordval = False

    passwordval = print_intro(SUPERSECRETPASSWORD)
    while passwordval == True:
        optionval = get_optionval(PROMPTLIST)
        if optionval == 0:
            print("\nStudent Grades:")
            printer.print_dict(gradesdict)
        elif optionval == 1:
            print("\nAdding a New Student:")
            gradesdict = create_new_student(gradesdict)
        elif optionval == 2:
            print("\nChange Student Grades:")
            gradesdict = change_student_grades(gradesdict)
        else:
            break


def print_intro(SUPERSECRETPASSWORD):
    #prints the intro and checks password
    passcode = ""
    optionval = 0
    repeatval = False

    print("\nWelcome to the CIS-133Y grading system.")
    passcode = valid.get_string("Please enter the Super Secret Password: ")
    if passcode == SUPERSECRETPASSWORD:
        repeatval = True
        return repeatval
    else:
        print("It appears you are not allowed into the system.")
        print("Goodbye")


def get_optionval(PROMPTLIST):
    #gets options for the menu
    optionval = 0

    print("\n Welcome to the CIS-133Y grading system.")
    printer.print_options(PROMPTLIST)
    optionval = valid.get_integer("\nPlease enter the option you would like to use: ")
    return optionval

def create_new_student(gradesdict):
    #adds a student and coresponding grade into the dictionary
    #intentionaly only whole numbers for grades
    nameval = ""
    gradeval = 0
    namecheckval = ""

    nameval = valid.get_string("Please enter the student's name: ")
    namecheckval = gradesdict.get(nameval)
    if namecheckval == nameval:
        print("\nStudent already exists.")
    else:
        gradeval = valid.get_integer_positive("Please enter the student's grade: ")
        gradesdict[nameval] = gradeval
        return gradesdict

def change_student_grades(gradesdict):
    #intentionaly only whole numbers for grades
    #Changes the value of a students grade
    nameval = ""
    gradeval = 0

    printer.print_dict(gradesdict)
    nameval = valid.get_string("Please enter the student's name whose grade you would like to change: ")
    if nameval in gradesdict:
        gradeval = valid.get_integer_positive("Please enter the student's grade: ")
        gradesdict[nameval] = gradeval
        return gradesdict
    else:
        print("\nStudent doesn't exist.")
        return gradesdict



if __name__ == "__main__":
    main()