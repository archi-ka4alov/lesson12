def result_number(n):
    result_list = []
    for i in range(1, ((n + 1) // 2)):
        for j in range((i + 1), 21):
            if n % (i + j) == 0:
                result_list. append(i)
                result_list.append(j)
    return result_list

number1 = int(input())
print(*result_number(number1), sep='')