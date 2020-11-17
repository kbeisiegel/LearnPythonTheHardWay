i = 0
numbers = []

for printnum in range(0, 6):
    while i < 6:
        print(f"At the top is {i}")
        numbers.append(i)



        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom is {i}")



for num in numbers:
    print(num)
