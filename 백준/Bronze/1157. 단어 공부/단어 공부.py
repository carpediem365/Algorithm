#set으로 풀기
alphabet = input().upper()
set_alphabet = set(alphabet)

max_count =0
largest_alphabet=""
for char in set_alphabet:
    if alphabet.count(char) >max_count:
        max_count = alphabet.count(char)
        largest_alphabet = char
    elif alphabet.count(char)  == max_count:
        if largest_alphabet != char:
            largest_alphabet ="?"
print(largest_alphabet)