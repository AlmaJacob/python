# import re
# a="mrng"
# print(re.search("m",a))
# print(re.search("mrng",a))
# print(re.search("j",a))
# if re.search("j",a):
#     print("match")
# else:
#     print("not match")

# if re.search("n",a):
#     print("match")
# else:
#     print("not match")

# print(re.search("m.",a))
# print(re.search("m..",a))
# print(re.search("m...",a))
# print(re.search("r.",a))
# print(re.search("r..",a))
# print(re.search("n.",a))
# print(re.search("m.*",a))
# print(re.search("n.*",a))
# print(re.search("r.*",a))
# print(re.search("g.*",a))
# print(re.search("m.+",a))
# print(re.search("r.+",a))
# print(re.search("n.+",a))
# print(re.search("g.+",a))
# print(re.search("m.?",a))
# print(re.search("r.?",a))
# print(re.search("n.?",a))
# print(re.search("g.",a))
# a="JAKE"
# print(re.search("[A-Z]",a))
# print(re.search("[A-z]",a))
# print(re.search("[a-z]",a))

# a="aRjOy"
# print(re.search("[a-z]",a))
# print(re.search("[A-Z]",a))
# print(re.search("[a-m]",a))
# print(re.search("[A-M]",a))

# a="1234"
# print(re.search("[0-9]",a))
# print(re.search("[6-9]",a))

# a="abc123"
# print(re.search("[a-z][0-9]",a))
# a="123"
# print(re.search("[a-z][0-9]",a))
# a="abc"
# print(re.search("[a-z][0-9]",a))

# a="abc"
# print(re.search("[a-z0-9]",a))
# a="asd348"
# print(re.search("[a-z].[0-9]",a))
# print(re.search("[a-z].*[0-9]",a))
# print(re.search("[a-z].?[0-9]",a))
# print(re.search("[a-z].+[0-9]",a))
# print(re.search("[a-z].?[0-9].*",a))
# print(re.search("[a-z].?[0-9].+",a))
# print(re.search("[a-z].?[0-9].?",a))

#moblie no validation
# import re
# a="8281380509"
# if len(a)==10 and re.search("[6-9].{9}",a) and a.isdigit():
#     print("valid")
# else:
#     print("not")    

#email validation
# import re
# a="almajacob7@gmail.com" 
# print(re.search("^[a-z].*@gmail.com$",a))

#password validation
# import re
# a="alm22$ac"
# if len(a)>=8 and re.search("^[A-z0-9].*[$%#@0-9]",a) and not(a.isdigit()): 
#     print("valid")
# else:
#     print("not valid")    