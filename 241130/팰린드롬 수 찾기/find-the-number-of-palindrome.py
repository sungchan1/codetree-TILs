start, end = map(int,  input().split())

count = 0
for number in range(start, end+1):
    str_number = str(number)
    if str_number == str_number[::-1]:
        count +=1

print(count)