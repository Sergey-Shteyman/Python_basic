zen_python = open("zen.txt", "r")

data = zen_python.read().split("\n")
for i_line in data[::-1]:
    print(i_line)

zen_python.close()
