import sys
from itertools import combinations

def solution(numbers):
    numbers.sort()
    two_sum_list = list(combinations(numbers, 2))
    answer = []
    for two_sum in two_sum_list:
        if (two_sum[0] + two_sum[1]) not in answer:
            answer.append(two_sum[0] + two_sum[1])

    return sorted(answer)

print(solution([2,1,3,4,1]))