words = input() #단어입력받기
word_index = {} #단어 위치를 딕셔너리로 저장
alphabet ="abcdefghijklmnopqrstuvwxyz" #알파벳리스트
#wrods에서 글자 하나씩 뽑아와서 해당 글자가 words에 있는지 확인
#마지막에 a,b,c 순서로 위치출력
for i in words: #입력받은 단어를 하나씩 확인
    word_index[i]=words.find(i) #딕셔너리로 해당 알파벳 처음위치 저장
for i in alphabet:#word_index에 해당 알파벳이 있는지 확인하는 과정
    if i in word_index:#i가 word_index에 있으면 true이기 때문에 아래 구문 실행
        print(word_index[i],end=" ")
    else: #i word_index에 없으면 -1 출력
        print(-1,end=" ")

