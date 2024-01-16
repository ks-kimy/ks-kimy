import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # matrix = []
    N = int(input())
    max=0
    max_key = 0
    dict_score ={}
    row = list(map(int, input().split())) # 
    for i in range(0,101):
        dict_score[i]= 0
        for j in range(0,1000):
            if i == row[j]:
                dict_score[i] += 1
        if dict_score[i]>= max:
            max = dict_score[i]
            max_key = i
    print(f"#{tc}", max_key)
    
    