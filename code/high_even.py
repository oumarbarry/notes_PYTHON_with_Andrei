def highest_even(is_even_list):
    even_list = []
    for item in is_even_list:
        if item % 2 == 0:
            even_list.append(item)
    return max(even_list)


total = 0

def count():
    global total
    total += 1
    return total
