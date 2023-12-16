def solution(s):
    answer = ''
    arr = [i.lower() for i in list(s.split(" "))]
    for word in arr:
        tmp_word = ""
        if len(word) > 0:
            tmp_word = word[0].upper()
            if len(word) > 1:
                tmp_word += word[1:]
        answer += tmp_word + " "
    return answer[:-1]