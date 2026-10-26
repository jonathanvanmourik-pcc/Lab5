

def print_options(promptlist):
    #Creates a list of options based on a inputed list
    for i in range(len(promptlist)):
        print("{}: {}".format(i,promptlist[i]))

def print_dict(dictval):
    #prints boths sides of an entire dictionary
    for i, g in dictval.items():
        print("{}: {}".format(i,g))