import sys, math

def import_file():
    try:
        return open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File could not be opened.")
        quit()
    except IndexError:
        print("This program requires an input file to run.")
        quit()

def parse_file(input_file):
    input_file = "".join(input_file)
    start = input_file.find(":") + 1
    return input_file[start:].split()

def parse_file_no_space(input_file):
    input_file = input_file.replace(" ", "")
    input_file = input_file[:-1]
    start = input_file.find(":") + 1
    return input_file[start:]

def calculate_times(time, record):
    #22 v 21
    #Short circuit for speed:
    #check if distance < prev_distance
    #true: check if time is even
    #   true: len((new_records - 1) * 2)
    #   false: len(new_records * 2) 
    #0 always == 0.
    time = int(time)
    record = int(record)
    prev_distance = -1
    new_records = []
    for i in range(1, time):
        #i == ms held for and i == speed
        remaning_time = time - i
        distance = i * remaning_time
        if(distance < prev_distance):
            if(time % 2 == 0):
                #print(new_records)
                return (len(new_records) * 2) - 1
            else:
                #print(new_records)
                return (len(new_records) - 1) * 2
        if(distance > record):
            new_records.append(distance)
        prev_distance = distance

def main():
    input_file = import_file() 
    lines = input_file.readlines()

    # 1 Star solution
    times = parse_file(lines[0])
    records = parse_file(lines[1])
    totals = 1
    for i in range(0,len(times)):
        num_records = calculate_times(times[i],records[i])
        totals = totals * num_records
    print("1 Star: " + str(totals))

    #2 Star solution
    time = parse_file_no_space(lines[0])
    records = parse_file_no_space(lines[1])
    print("Calculating...")
    num_records = calculate_times(time,records)
    print("2 Star: " + str(num_records))

if __name__ == "__main__":
    main()