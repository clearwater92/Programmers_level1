from collections import Counter

def solution(N, stages):

    # 해당 스테이지를 플레이하고 있는 사람 수
    stage = Counter(stages)

    # 실패율
    failure = [0]*N
    num = len(stages)
    for i in range(1, N+1) :
        if stage[i] != 0 :
            failure[i-1] = stage[i]/num
            num -= stage[i]

    answer = []
    num = len(failure)
    for i, item in enumerate(failure):
        m = item
        idx = i
        for j, _item in enumerate(failure[::-1]):
            if _item >= m:
                m = _item
                idx = num -1-j
        answer.append(idx+1)
        failure[idx] = -1

    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))
print(solution(4,[4,4,4,4,4]))