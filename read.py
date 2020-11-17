from sys import argv

script, filename = argv

print(f"We're going to read {filename}:")

txt = open(filename)


print(txt.read())
