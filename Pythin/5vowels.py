a = 0
e = 0
i2 = 0
i = 0
o = 0
u = 0
letterlist = ["a"]
words = input("What do you want to count: ")
letterlist = list(words)
letterlist.append("z")
letterlist.append("z")
letterlist.append("z")
letterlist.append("z")
letterlist.append("z")
while i < letterlist.__len__():
    if letterlist[i] == "a":
        a += 1 
        i = 1 + i
    if letterlist[i] == "e":
        e += 1     
        i = 1 + i
    if letterlist[i] == 'i':
        i2 += 1 
        i = 1 + i
    if letterlist[i] == "o":
        o += 1
        i = 1 + i
    if letterlist[i] == "u":
        u += 1 
        i = 1 + i
    else:
        i = 1 + i
print("a = " + str(a))
print("e = " + str(e))
print("i = " + str(i2))
print("o = " + str(o))
print("u = " + str(u))