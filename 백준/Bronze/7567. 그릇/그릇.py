bowl = list(input())
num=10
#print(bowl)
for i in range(1,len(bowl)):
    if bowl[0] =="(":
        if bowl[i] == "(":
            num +=5
        elif bowl[i] == ")":
                num +=10
                bowl[0] =")"
    elif bowl[0] ==")":
        if bowl[i] ==")":
            num += 5
        elif bowl[i] =='(':
            num += 10
            bowl[0] ="("
print(num)       