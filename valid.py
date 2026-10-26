def get_integer(prompt):
    #gets_int
    val = 0
    while True:
        try:
            val = int(input(prompt))
            return val
        except:
            print("Invalid integer.")

def get_float(prompt):
    #gets_int
    val = 0.0
    while True:
        try:
            val = float(input(prompt))
            return val
        except:
            print("Please enter a real number.")

def get_string(prompt):

    val = ""
    while True:
        val = input(prompt)
        if val != "":
            return val
        else:
            print("Invalid string.")

def get_integer_positive(prompt):
    #gets_int
    val = 0
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
        except:
            print("Please enter a positive whole number.")