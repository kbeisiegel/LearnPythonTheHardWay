from sys import argv

script, input_file = argv

def print_all(f):           # this is the first function/mini-script
    print(f.read())         # read action

def rewind(f):          # 2nd function/mini-script being set
    f.seek(0)           # seeking action back to beginning

def print_a_line(line_count, f):        # 3rd function set
    print(line_count, f.readline())     # readline action (reads 1 line)

current_file = open(input_file)         # setting current_file's value with open function

print("First, let's print the whole file:\n")       #print text with spacer

print_all(current_file)          # running print all function with current file

print("Now let's rewind, kind of like a tape.")  # print text

rewind(current_file)            # running rewind function with current file

print("Let's print three lines:") # print text

current_line = 1        # setting a value for current_line variable
print_a_line(current_line, current_file) # running print a line function

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
