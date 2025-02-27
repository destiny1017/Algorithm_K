def solution(book_time):
    answer = 0
    use_times = [0] * 1451
    for b in book_time:
        st = b[0].split(":")
        ed = b[1].split(":")
        st_time = int(st[0]) * 60 + int(st[1])
        ed_time = int(ed[0]) * 60 + int(ed[1]) + 10
        for i in range(st_time, ed_time):
            use_times[i] += 1
    # print(use_times[:60])
    return max(use_times)