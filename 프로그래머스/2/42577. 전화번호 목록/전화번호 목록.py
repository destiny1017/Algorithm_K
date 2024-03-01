def solution(phone_book):
    phone_set = set(phone_book)
    tmp_set = phone_set.copy()
    for item in phone_set:
        tmp_set.remove(item)
        fix_len = len(tmp_set)
        for i in range(len(item)):
            split_str = item[0:len(item) - i]
            tmp_set.add(split_str)
            if len(tmp_set) == fix_len:
                return False
            tmp_set.remove(split_str)
        tmp_set.add(item)
    
    return True