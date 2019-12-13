def translate(str):
    str = str.split("[")
    l = []
    for i in range(len(str)):
        if "]" in str[i]:
            l.append(str[i].split("]")[1])
            str[i] = str[i].split("]")[0]
            
    str.reverse()
    return "".join(str + l)
   
print(translate(input()))