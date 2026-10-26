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
    optionval = 0

    print("\n Welcome to the CIS-133Y grading system.")
    printer.print_options(PROMPTLIST)
    optionval = valid.get_integer("\nPlease enter the option you would like to use: ")
    return optionval

def create_new_student(gradesdict):
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
    nameval = ""
    namecheckval = ""
    gradeval = 0

    printer.print_dict(gradesdict)
    nameval = valid.get_string("Please enter the student's name whose grade you would like to change: ")
    namecheckval = gradesdict.get(nameval)
    if namecheckval in gradesdict:
        print("\nStudent doesn't exist.")
    else:
        gradeval = valid.get_integer_positive("Please enter the student's grade: ")
        gradesdict[nameval] = gradeval
        return gradesdict





if __name__ == "__main__":
    main()