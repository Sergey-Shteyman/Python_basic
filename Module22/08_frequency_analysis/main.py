line_string = open("text.txt", "r").read().lower()
chars = {}
quantity = 0

for char in line_string:
   if ord('a') <= ord(char) <= ord('z'):
       value = chars.get(char, 0)
       chars[char] = value + 1
       quantity += 1

lout = [(index, "{:5.3f}".format(chars[index] / quantity)) for index in chars.keys()]
lout.sort(key=lambda argument: argument[0])
lout.sort(key=lambda argument: argument[1], reverse=True)
sout = "\n".join([i_elem[0] + " " + i_elem[1] for i_elem in lout])
open("analysis.txt", "w").write(sout)
