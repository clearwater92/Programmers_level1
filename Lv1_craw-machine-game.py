def solution (board, moves):
    moves = list(map(lambda mv: mv-1, moves))
    stack = [0]
    answer = 0
    for move in moves:
        for line in board:
            if line[move] != 0:
                stack.append(line[move])
                line[move] = 0
                if stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    answer+=2
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))