from collections import deque
import sys

sys.setrecursionlimit(10**6)

class Block:
    def __init__(self):
        self.cnt = 0

    def plus_and_copy(self):
        self.cnt += 1
        return self
    
def dfs(x, y, land, blocks, block):

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    # dfs에 해당되는 모든 블럭에 동일한 석유블럭 삽입
    blocks[x][y] = block.plus_and_copy()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
            continue
        if land[nx][ny] == 0 or blocks[nx][ny] is not None:
            continue
        dfs(nx, ny, land, blocks, block)
        
    return block

def solution(land):
    x, y = len(land), len(land[0])
    blocks = [[None for _ in range(y)] for _ in range(x)]
    answer = 0
    
    # 석유 존재하는 블럭 영역에 동일한 블럭 객체 삽입
    for i in range(x):
        for j in range(y):
            if land[i][j] == 1 and blocks[i][j] is None:
                dfs(i, j, land, blocks, Block())
    
    # 각 열에 존재하는 모든 석유존의 cnt 합산하여 더 큰 값 대입
    for j in range(y):
        cnt = 0
        contain_blocks = []
        for i in range(x):
            if land[i][j] == 1 and blocks[i][j] is not None:
                if blocks[i][j] in contain_blocks:
                    continue
                contain_blocks.append(blocks[i][j])
                cnt += blocks[i][j].cnt
        answer = max(answer, cnt)
                    
    return answer