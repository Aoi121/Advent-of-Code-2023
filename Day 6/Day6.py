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
                print(new_records)
                return (len(new_records) * 2) - 1
            else:
                print(new_records)
                return (len(new_records) - 1) * 2
        if(distance > record):
            new_records.append(distance)
        prev_distance = distance

def main():
    input_file = import_file() 
    lines = input_file.readlines()
    times = parse_file(lines[0])
    records = parse_file(lines[1])
    totals = 1
    for i in range(0,len(times)):
        num_records = calculate_times(times[i],records[i])
        totals = totals * num_records
    print(totals)

if __name__ == "__main__":
    main()