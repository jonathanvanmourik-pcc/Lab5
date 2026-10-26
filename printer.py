

def print_options(promptlist):

    for i in range(len(promptlist)):
        print("{}: {}".format(i,promptlist[i]))

def print_dict(dictval):

    for i, g in dictval.items():
        print("{}: {}".format(i,g))