# s={1,2,45,"abc"}
# print(type(s))

#to create empty set
# a=set()
# print(a)

#we can't find index position
# s={1,23,"err",8,7,9,"qwe"}
# print(s[3])

#set automatically remove duplicate values and it is unorderd
# a={3,4,"ef",4,545,"fg"}
# print(a)


#to remove duplicates values in list using set(imp)
# l=[12,3.4,12,3,4,3,4.1,4]
# l=set(l)
# l=list(l)
# print(l)


#set methods
#-------------

#1.add(to add a element to a list)
# s={2,4,7}
# s.add(5)
# print(s)

#2.clear(to fully clear the set)
# s={2,4,7}
# s.clear()
# print(s)

#3.copy(to copy the set)
# s={2,4,7}
# s.copy()
# print(s)

#4.difference(to find the difference from one set to another set)
# s={2,5,3,7,1,6}
# s1={5,8,3,6,32}
# s.difference(s1)
# print(s)

#5.dicard(to delete an element from a set)
# s={4,65,4,34,5}
# s.discard(4)
# print(s)

#6.remove(to remove an eleemt from set)
# s={2,6,8,43,5}
# s.remove(6)
# print(s)

#7.pop()to delete any one of element from set
# s={24,36,3,3,1}
# s.pop()
# print(s)
#8.update(to add a new set value to a set)
# s={1,5,3,36,2,6}
# s.update({4,6,3,2,622})
# print(s)
