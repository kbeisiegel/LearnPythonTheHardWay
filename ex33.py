
numbers = []

def printnum(x, n):
    i = 0
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)


        i = i + n
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
printnum(23, 7)
print("The numbers:")

for num in numbers:
    print(num)
