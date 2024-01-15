import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # matrix = []
    N = int(input())
    max=0
    # for _ in range(N):
    row = list(map(int, input().split()))
    # matrix.append(row)
    score_dict = {}
    for i in range(0,101):
        score_dict[i] = 0 # i 점수의 사람 수
        
        for j in range(1,1001):
            if i == row[j-1]:
                score_dict[i] += 1
        
        if score_dict[i] >= max:
            max = score_dict[i]
    
    print(max)
        # print(score_dict)
    # print(f"#{tc} {mode_value}")
    # pass

    # print(f'#{tc}')
