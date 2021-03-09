# FIles -----> txt,excelsheets, images, audio, pdf, gsheets, videos, png, gif
# By Default, text files only
# Modes --- 3 Modes
# Read --- r , read only , cursor is at the begin of file,  must be created before read
        # rb , read only in binary mode
        # r+ --- read and write both allowed
        # rb+ ---- both allowed in binary mode
# Write --- w , write only , cursor is at the begin of file , file is self created if doesnt exist
        # wb --- write in binary only
        # w+ --- write as well read allowed
        # wb+ ---- write and read in binary
# Append --- a , write only, cursor is at the end of file, file is created if doesnt exist
        # ab --- write in binary 
        # a+ --- write and read allowed
        # ab+ --- write and read in binanry only

#open('filename.ext' , 'mode of opening a file')
# file = open('testfile.txt' , 'w') # Current Working Dir
# file.write("****")# Only Strings allowed
# file.close()
# #read()
# #write()
# #close()

# file = open('testfile.txt' ,'rb+')
# #data = file.read() # till eof file
# #file.write("See this data...")
# file.write(b"Binary")
# print(file.read())
# file.close()


# file = open('newfile.txt' , 'w+')
# print(f"Cursor Before ANy Operation : {file.tell()}")
# file.write("Write is performed before read here...")
# print(f"Cursor After Write/Before Read Operation : {file.tell()}")
# #file.seek(no of chars to move from ref point,reference point == 0 beg, 1 current, 2 end)
# file.seek(0,0)
# print(f"Cursor After Seek/Before Read Operation : {file.tell()}")
# print(file.read())
# print(f"Cursor After Read Operation : {file.tell()}")
# file.close()



# file  = open('anewfile.txt' , 'ab+')
# file.write("hELLO, wORLD!")
# file.seek(0,0)
# print(file.read())
# file.close()
li = ['apple\n' , 'green\n' , 'blue\n' , 'orange\n' , 'black\n' , 'purple\n']
file = open('somenewfile.txt' , 'w+')
# for i in li:
#     file.write(i + '\n')
file.writelines(li)
file.seek(0,0)
#file.read(5)
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readlines())
for i in file:
    print(i)
file.close()


###################################################################
import os

print(os.getcwd())
#os.mkdir("MyDir")
os.chdir("MyDir")
print(os.getcwd())
file = open("Hey.txt" , 'w')
file.write("Hey, Files")
file.close()

os.chdir('../') #  A Folder Back
#os.rename('dictds.py' , 'newdictds.py')
#os.remove('somenewfile.txt')
#os.remove('MyDir')
import shutil

#shutil.rmtree('MyDir') for non empty folders





