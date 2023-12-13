import sys

def import_file():
    try:
        return open(sys.argv[1])
    except FileNotFoundError:
        print("Could not open file.")
        quit()
    except IndexError:
        print("Please provide an input file as an argument of this program.")
        quit()

def find_points(line):
    start = line.find("|") + 1
    line = "".join(line)
    line = line[start:]
    nums = line.split()
    return nums

def compile_winning_nums(line):
    #change to a split
    start = line.find(":") + 1
    end = line.find("|") - 1
    line = "".join(line)
    line = line[start:end]
    winning = line.split()
    return winning
    

def main():
    inputFile = import_file()
    file = inputFile.readlines()
    #For each line in file
    #1. Compile the winning numbers into a list
    #2. Loop through the achieved numbers
    #3. For each num, check if in the winning nums
    #4. If true: check if points == 0
    #              points += 1
    #            else:
    #               points *= 2
    total = 0
    for line in file:
        score = 0
        nums = find_points(line)
        print(nums)
        winning = compile_winning_nums(line)
        for i in nums:
            if i in winning:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
        total = total + score
    print(total)


if __name__ == "__main__":
    main()