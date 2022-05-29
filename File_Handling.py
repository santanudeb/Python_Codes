# File Handling

# text file
fileData = open('File.txt', 'r')          # read
newfileData = open('New_File.txt', 'w')   # write

print(fileData.read())

# reading 1 line
# print(fileData.readline(), end="")
# print(fileData.readline(), end="")

# adding 1 line
# newfileData.write("something")
# newfileData.write("new")

# copying other file
for i in fileData :
    newfileData.write(i)

# image file
imgfile = open('Cat.jpg', 'rb')          # reading image   rb = read binary  # 'name.imageformat'
newimgfile = open('Cat_New.jpg', 'wb')   # writing image   wb = write binary # 'name_new.imageformat'

# copying other image
for i in imgfile :
    newimgfile.write(i)