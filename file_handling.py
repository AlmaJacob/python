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

f=open("python/demo2.txt",'a')
f.write('\nheyy')

