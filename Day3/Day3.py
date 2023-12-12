import sys

INTS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"
]

def import_file():
    try:
        return open(sys.argv[1])
    except FileNotFoundError:
        print("Could not open file.")
        quit()
    except IndexError:
        print("Please provide an argument for the input file.")
        quit()

def get_line_lenght(lines):
    return len(lines[0])

def find_left(fileLines, i):
    while(fileLines[i-1] in INTS):
        i = i - 1
    return i

def get_int_from_left(fileLines, i):
    num = ""
    while(fileLines[i] in INTS):
        num += fileLines[i]
        i = i + 1
    return num

def get_int_from_right(fileLines, i):
    num = []
    while(fileLines[i] in INTS):
        num.append(fileLines[i])
        i = i - 1
    num.reverse()
    return "".join(num)
    

def check_adjacent(fileLines, i, length):
    if(fileLines[i-1] in INTS):
        print("L",end="")
        print(fileLines[i-1])
        num = get_int_from_right(fileLines, i-1)
        print(num)
    if(fileLines[i+1] in INTS):
        print("R",end="")
        print(fileLines[i+1])
        num = get_int_from_left(fileLines,i+1)
        print(num)
    if(fileLines[i-length-1] in INTS):
        print("TL",end="")
        print(fileLines[i-length-1])
        new_i = find_left(fileLines, i-length-1)
        num = get_int_from_left(fileLines, new_i)        
        print(num)
    elif(fileLines[i-length] in INTS):
        print("T",end="")
        print(fileLines[i-length])
        new_i = find_left(fileLines,i-length)
        num = get_int_from_left(fileLines, new_i)
        print(num)
    elif(fileLines[i-length+1] in INTS):
        print("TR",end="")
        print(fileLines[i-length+1])
        new_i = find_left(fileLines,i-length+1)
        num = get_int_from_left(fileLines, new_i)
        print(num)
    if(fileLines[i+length-1] in INTS):
        print("BL",end="")
        print(fileLines[i+length-1])
        new_i = find_left(fileLines, i+length-1)
        num = get_int_from_left(fileLines, new_i)        
        print(num)
    elif(fileLines[i+length] in INTS):
        print("B",end="")
        print(fileLines[i+length])
        new_i = find_left(fileLines,i+length)
        num = get_int_from_left(fileLines, new_i)
        print(num)
    elif(fileLines[i+length+1] in INTS):
        print("BR",end="")
        print(fileLines[i+length+1])
        new_i = find_left(fileLines,i+length+1)
        num = get_int_from_left(fileLines, new_i)
        print(num)
    print("Ret num: " + str(num))
    return int(num)

#TODO
#   Add a total counter
#   Clean up check_adjacent



if __name__ == "__main__":
    file = import_file()
    lines = file.readlines()
    # Could either convert the lines into one big string
    # Or could loop through all the lines.
    # String method would allow one to use a range to loop
    # through the string, subtracting the range by length to
    # go up a line and check for adjacent ints.
    # list would allow one to save the current index and move
    # up a level to check for adjacent ints.
    lines = [x[0:-1] for x in lines]
    length = get_line_lenght(lines)
    fileLines = "".join(lines)
    total = 0
    for i in range(0,len(fileLines)):
        #if index == a symbol
        if((not fileLines[i] in INTS) and (fileLines[i] != ".")):
            print(fileLines[i])
            total += check_adjacent(fileLines, i, length)
            #check all adjacent indicies
    print("Total: " + str(total))
