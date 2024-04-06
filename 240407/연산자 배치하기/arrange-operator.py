from sys import stdin as s

def dfs(index: int, value: int, numbers: list, operands: list) -> list[int, int]:
    if sum(operands) == 0:
        return [value]
    result = []
    # 덧셈
    if operands[0] > 0:
        copy_operands = operands[:]
        copy_operands[0] -= 1
        result += dfs(index+1, value + numbers[index], numbers,copy_operands)
    # 뺄셈
    if operands[1] > 0:
        copy_operands = operands[:]
        copy_operands[1] -= 1
        result += dfs(index+1, value - numbers[index], numbers, copy_operands)
    # 곱셈
    if operands[2] > 0:
        copy_operands = operands[:]
        copy_operands[2] -= 1
        result += dfs(index+1, value * numbers[index], numbers,copy_operands )

    result.sort()    
    return result

n = int(s.readline())
numbers = list(map(int, s.readline().split()))
operands = list(map(int, s.readline().split()))
results = dfs(1, numbers[0], numbers, operands)
print(results[0], results[-1])