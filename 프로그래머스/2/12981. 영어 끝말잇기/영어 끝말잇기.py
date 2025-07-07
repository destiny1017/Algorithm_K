def solution(n, words):
    answer = [0, 0]
    word_set = set()
    i = 0
    before_word = words[0][0]
    while len(word_set) < len(words):
        word = words[i]
        if word in word_set or before_word[-1] != word[0]:
            return [i % n + 1, i // n + 1]
        before_word = word
        word_set.add(word)
        i += 1
    return answer