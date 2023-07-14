dic = {'ABC':2,'DEF':3,'GHI':4,"JKL":5,"MNO":6,"PQRS":7,"TUV":8,"WXYZ":9}
char = list(input())
time = 0
for i in dic:
    for x in char:
        if x in i:
            time += dic[i]+1
print(time)