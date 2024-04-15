# 알고리즘 : 최단거리, BFS 
# 시간복잡도 : 고려X
# 구현 과정
# 1. begin 각 index를 순회하며 bfs 수행
# 2. 현재 index의 문자를 변경할 수 있는 모든 단어를 queue에 추가
# 3. 추가된 단어가 있으면 현재 index visit True, cnt + 1, 
#    추가된 단어 없으면 index + 1 후 2번 수행
# 4. queue 빼며 visit False인 문자 변경 가능한 경우 queue에 추가, 2~3반복

from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))

    while queue:
        change_word, cnt = queue.popleft()
        
        if change_word == target:
            return cnt
        
        for i in range(len(change_word)):
            if target[i] != change_word[i]:
                for word in reversed(words):
                    tmp_words = list(word)
                    tmp_words[i] = change_word[i]
                    if "".join(tmp_words) == change_word:
                        queue.append((word, cnt+1))
                        words.remove(word)
    
    return 0
    

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer