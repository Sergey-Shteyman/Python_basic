line_string = open("text.txt", "r").read().lower()
chars = {}
quantity = 0

for char in line_string:
   if ord('a') <= ord(char) <= ord('z'):
       x = chars.get(char, 0)
       chars[char] = x + 1
       quantity += 1

lout = [(k, "{:5.3f}".format(chars[k] / quantity)) for k in chars.keys()]
lout.sort(key=lambda x: x[0])
lout.sort(key=lambda x: x[1], reverse=True)
sout = "\n".join([i[0] + " " + i[1] for i in lout])
open("analysis.txt", "w").write(sout)
