def solution(phone_book):
    phone_set = set(phone_book)
    tmp_set = phone_set.copy()
    for item in phone_set:
        tmp_set.remove(item)
        for i in range(len(item)):
            split_str = item[0:len(item) - i]
            if split_str in tmp_set:
                return False
        tmp_set.add(item)
    
    return True