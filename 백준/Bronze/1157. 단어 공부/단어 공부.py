alphabet = input().upper()
count_dict = {}

for char in alphabet:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

max_count = max(count_dict.values())
largest_alphabets = [char for char, count in count_dict.items() if count == max_count]

if len(largest_alphabets) == 1:
    largest_alphabet = largest_alphabets[0]
else:
    largest_alphabet = "?"

print(largest_alphabet)