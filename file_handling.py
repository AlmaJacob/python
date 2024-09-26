# f=open("python/demo.txt","x")
# f.write("these is a text file")

#read modes

# f=open("python/demo.txt",'r')
# print(f.read())
# a=f.read(4)
# f.seek(0)

# b=f.read()
# print(f.tell())
# print(a)
# print('-'*20)
# print(b)
# c=f.readlines()
# f.seek(0)
# for i in range(len(c)):
#     e=f.readline().strip()
#     print(e[::-1])

#write modes

# f=open("python/demo2.txt",'a')
# f.write('\nheyy')

#to remove text file
# import os
# os.remove('python/heyy.txt')

#to check a file is exist or not
# import os
# if os.path.exists("python/demo2.txt"):
#     print("file found")
# else:
#     print("not found")

#to create a folder
#--------------------
#syntax
#--------
# import os
# os.mkdir("folder_name")

# import os
# os.mkdir("sample")

#to remove or delete a folder
#--------------------
#syntax
#--------
# import os
# os.rmdir("folder_name")

# import os
# os.rmdir("sample")
