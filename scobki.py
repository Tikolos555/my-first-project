def scobki(s):
    a=[]
    for i in range (len(s)):
        if s[i]=="(":
            a.append(0)
        else:
            if len(a)==0:
                return False
            a.pop()
    if len(a)==0:
        return True
    
print(scobki(""))