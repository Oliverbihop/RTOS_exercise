s = input("Nhập câu của bạn: ")
d={"UPPER CASE":0, "LOWER CASE":0}
space=0
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    elif c.isspace():
        space+=1
    else:
        pass
false_=(space+1)-d["UPPER CASE"]
print ("chữ viết Sai:", false_)
print ("chữ viết đúng",d["UPPER CASE"] )