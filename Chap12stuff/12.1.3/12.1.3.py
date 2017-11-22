"""Echo the contents of a file."""
f = open('myfile.txt')

for line in f:
    print(line)

f.close()
