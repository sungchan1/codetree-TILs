braces = input().strip()

length = len(braces)

result = 0
for i in range(length-1):
    if braces[i] == "(":
        for j in range(i+1, length):
            if braces[j] == ")":
                result +=1 

print(result)