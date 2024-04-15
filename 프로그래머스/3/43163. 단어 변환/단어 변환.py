from collections import deque

def solution(begin, target, words):
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