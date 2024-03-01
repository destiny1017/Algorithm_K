def solution(phone_book):
    phone_set = set(phone_book)
    for item in phone_set:
        phone_set.remove(item)
        for i in range(len(item)):
            split_str = item[0:len(item) - i]
            if split_str in phone_set:
                return False
        phone_set.add(item)
        
    return True