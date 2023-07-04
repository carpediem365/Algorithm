#9번씩 입력받고 리스트에 저장해보자
all_list = []

max_num =0
col_index =0
row_index = 0
for i in range(9):
    num = list(map(int,input().split()))
    all_list.append(num)
    if max(num) >=max_num:
        max_num = max(num)
        row_index = i+1
        col_index = num.index(max_num)+1
   
#print(all_list)        
print(max_num) 
print(row_index,col_index)    