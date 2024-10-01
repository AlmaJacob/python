
# counting numbers in a text file
# f=open('python/demo2.txt','r')
# c=f.readlines()
# f.seek(0)
# letter=0
# for i in c:
#     e=f.readline().strip()
#     for i in e:
#         if i!= " ":
#             letter+=1
# print(letter)

#counting capital and small letter in text file
# f=open('python/demo2.txt','r')
# l=f.readlines()
# f.seek(0)
# cap=0
# letters=0
# words=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     s=a.split()
#     for i in s:
#         if i!='':
#             words+=1
#     for i in a:
#         if i!=' ':
#             if i.isupper():
#                 cap+=1
#             letters+=1
# print(letters)
# print('capital',cap)
# print('small',letters-cap)
# print('words',words)
