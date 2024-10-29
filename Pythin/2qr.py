import qrcode

info = input("Input the website or info: ")
img = qrcode.make(info)
name = input("What do you want the file name to be: ")
type(img)  
img.save(name + ".png")
