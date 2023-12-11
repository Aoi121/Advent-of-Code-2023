import sys

nums = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

word_nums = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

word_to_int = {
    "one":1,
    "two":2,
    "three":3,
    "four":4, 
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

def open_file():
    try:
        return open(sys.argv[1])
    except Exception:
        print("Unable to open file.")

def find_word(line):
    left_num = -1
    right_num = -1
    smallest = 0
    largest = 0
    firstGo = True
    for i in range(0,9):
        temp = line.find(word_nums[i], largest)
        if(temp >= largest):
            if firstGo:
                smallest = temp
                firstGo = False
                left_num = word_to_int[word_nums[i]]
            largest = temp
            right_num = word_to_int[word_nums[i]]
    return [left_num, smallest, right_num, largest]

if __name__ == "__main__":
    file = open_file()

    left_num = -1
    right_num = -1
    total = 0
    word = ""

    largest = -1
    smallest = -1

    running = True
    lines = file.readlines()
    for line_num in lines:
        #print(line_num)
        first_iteration = True
        i = 0
        for x in line_num:
            if(first_iteration):
                num_list = find_word(line_num)
                first_iteration = False
            
            word = word + x
            if(x in nums):
                if(i > num_list[3]):
                    right_num = int(x)
                elif(i > num_list[1]):
                    if(left_num == -1):
                        left_num = int(x)
            i = i + 1
            
        total = total + ((left_num * 10) + right_num)
        #print(str(left_num) + "," + str(right_num))
        #print("t: " + str(total))
        left_num = -1
        right_num = -1
    print("Total: " + str(total))
