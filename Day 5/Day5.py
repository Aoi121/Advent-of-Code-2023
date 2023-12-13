import sys

def import_file():
    try:
        return open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File could not be opened.")
        quit()
    except IndexError:
        print("This program requires an input file to run.")
        quit()

def parse_seeds(input_file):
    input_file = input_file.readlines()[0]
    start = input_file.find(":") + 1
    return input_file[start:].split()

def init():
    # calculate the maps, add to a tuple
    # call sorted on the tuple.
    # later, if the seed value is less than or greater than
    # the tuple's max and min, use the original value rather 
    # than converting.
    map(3333452986, 2926455387, 455063168)

def map(destination, source, length):
    pass

def main():
    #make an init func that creates maps for all the funtions in the almanac
    #for each seed, use another func that converts it's value to another
    #based on the contents of the tuples.
    input_file = import_file()
    seeds = parse_seeds(input_file)
    init()




if __name__ == "__main__":
    main()
