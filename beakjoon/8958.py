#8958
n = int(input())
for i in range(n):
    Num = input()
    score = 0
    count = 0
    for j in range(len(Num)):
        if Num[j] == 'O':
            count += 1
            score += count
        elif Num[j] == 'X':
            score += 0
            count = 0
        print(score)